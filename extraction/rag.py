import pandas as pd
import argparse
import time
import os

from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import CacheBackedEmbeddings
from langchain.vectorstores import FAISS
from langchain.storage import LocalFileStore
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.callbacks import StdOutCallbackHandler


def build_qa_chain(DSM_5_trauma):
    trauma_loader = PyMuPDFLoader(f"{DSM_5_trauma}.pdf")
    trauma_documents = trauma_loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50, length_function=len
    )
    documnet_chunks = text_splitter.transform_documents(trauma_documents)

    store = LocalFileStore("./DSM5_cache/")

    # create an embedder
    core_embeddings_model = OpenAIEmbeddings(
        openai_api_key=api_key
    )  # text-embedding-ada

    embedder = CacheBackedEmbeddings.from_bytes_store(
        core_embeddings_model, store, namespace=core_embeddings_model.model
    )
    # store embeddings in vector store
    vectorstore = FAISS.from_documents(documnet_chunks, embedder)

    # instantiate a retriever
    retriever = vectorstore.as_retriever()

    # template for zero-shot with RAG
    open_ai_model = "gpt-4"
    llm = ChatOpenAI(api_key=api_key, model_name=open_ai_model)
    handler = StdOutCallbackHandler()

    template = """Answer the questions based on the following:
    {context}

    Q: I want to know the symptoms of a mental illness associated with Depression and Bipolarity in the form of a label (symptom), such as:
    For Major depression episode: depress(Depressed mood), dinter(Decreased interest),  dapp(Decreased appetite), iapp(Increased appetite), insom(Insomnia), hsom(Hypersomnia), agit(Psychomotor agitation), retard(Psychomotor retardation), fati(Fatigue), worth(Worthlesness), guilty(Excessive guilt), dcon(Decreased concentration), ddeci(Decreased decision), suii(Suicidal ideation), suip(Suicide plan), suia(Suicide attempt), distr(Signficant distress), isoc(Social-occupational impairment), nmed(No medication), npsycho(No pychotic disorder), nbipo(No manic or hypomanic episode).\
    For Bipolar disorder: mood(Expansive mood), iener(increased energy), iself(Increased self-esteem), dsleep(Decreased need for sleep), italk(Increased talk), iidea(Increased ideas), dcon(Decreased concentration), iacti(Increase in goal-directed activity), agit(Psychomotor agitation), irisk(Increased activities with high potential for painful consequences), nmed(No medication) \
    Manic: isoc(Social-occupational impairment), hosp(Hospitalization), psycho(Psychotic features) \
    Hypomanic: change(Change in functioning), obser(Mood disturbance and change in functioning observable by others), nisoc(No social-occupational impairment), nhosp(No hospitalization), npsycho(No psychotic features) for a total of 40 symptoms.
    Read the following interview transcript to extract the mental illness symptoms associated with Depression and Bipolarity and the sections that represent them. When extracting a symptom from the interview transcript, be sure to use only labels in the form label(symptom) minus (symptom), and when extracting a section from the interview transcript, be sure to use only the interview transcript.
    Also, when extracting a section from an interview multiple times, be sure to answer in the form of “...”, “...”, “...”, “...” .
    If there are no symptoms of mental illness associated with Depression and Bipolarity in a given interview, answer “none”.
    - Interview content: {question}

    Answer:
    - Symptom : 
    - Section :
    """
    prompt = ChatPromptTemplate.from_template(template)

    chain_type_kwargs = {"prompt": prompt}

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        callbacks=[handler],
        return_source_documents=True,
        chain_type_kwargs=chain_type_kwargs,
    )


def zeroshot_rag(df, DSM_5_trauma, gpt_result_filename):
    qa_chain = build_qa_chain(DSM_5_trauma)

    df["Estimation"] = ""
    ignore = 0
    for idx, row in df.iterrows():

        question = row["Statement"]

        try:
            response = qa_chain({"query": question})

            df.loc[idx, "Estimation"] = response["result"]

            time.sleep(20)

        except Exception as e:
            print(e)
            if "Limit" in str(e):
                time.sleep(10)

            else:
                ignore += 1
                print("ignored", ignore)

    # Save the dataframe to a new excel file
    df.to_excel(f"{gpt_result_filename}.xlsx", index=False)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Estimate Symptom and Section with Zero-shot Inference with RAG"
    )
    parser.add_argument(
        "--trauma",
        help="Trauma and Stressor-Related Disorders chapter of the DSM-5 with PDF Format",
        required=True,
    )
    parser.add_argument(
        "--data",
        help="Data File After Label Extraction with Excel Format",
        required=True,
    )
    parser.add_argument("--apikey", help="Your openai api key", required=True)
    parser.add_argument(
        "--result", help="Filename of the output generated by GPT", required=True
    )

    args = parser.parse_args()
    data_filename = args.data
    api_key = args.apikey
    gpt_result_filename = args.result
    DSM_5_trauma = args.trauma

    api_key = os.environ.get(api_key)
    api_key = api_key

    # zero-shot with RAG
    data = pd.read_excel(f"{data_filename}.xlsx")
    zeroshot_rag(data, DSM_5_trauma)
