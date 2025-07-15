# Summarization 

## Overview

This folder contains code to run summarization tasks using OpenAI's GPT. <br>

## Usage

# We focus on experience and symptoms both since it has the best results in the original paper.
# In our case, we did not extract stressors (experience), therefore we give the estimated sections (experience) and estimated symptoms (symptoms) as input. 

### Sections and Symptom Both

Summarize the estimated traumatic experiences and symptoms using OpenAI's GPT-4 (and measure BERTScore F1 against the true summary).

Meaning of each arguments:<br>
```exp``` Extracted Section Data file with Excel format <br>
```symp``` Extracted Symptom Data file with Excel format <br>
```apikey``` Your openai api key <br>
```gpt4summary``` Filename of GPT4 Summary <br>
(```summary``` True Summary file <br>)
```
python3 summarization_exp_symp.py --exp=exp --symp=symp --apikey=apikey --gpt4summary=gpt4summary --summary=summary
```
