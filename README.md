# Custom Trained & OpenAI API Chatbots

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [OpenAI API Chatbot](#openai-api-chatbot)
  - [Description](#description-open)
  - [Usage](#usage-open)
- [NYT Chatbot](#nyt-chatbot)
  - [Description](#description-nyt)
  - [Usage](#usage-nyt)
- [Credits](#credits)
- [License](#license)

## Overview

This project explores building two different chatbots used to practice Chinese-language conversations about politics, technology, and business for non-native Mandarin speakers. The first chatbot is a GPT-2 chatbot custom trained on text from three decades of New York Times reporting on China. The second chatbot is build using OpenAI's GPT-3.5 Turbo API and is accessed through a web interface.

## Installation

1. Clone the repository: `git clone https://github.com/sam-braun/chinese-chat-pal.git`
2. Install dependencies: `pip install requirements.txt`

## OpenAI API Chatbot

### Description

This chatbot utilizes OpenAI's GPT-3.5 Turbo LLM via OpenAI's API and translates text into either simplified or traditional Mandarin Chinese (with the option of an added English transliteration in pinyin). User can also  This Chatbot is accessed via a web interface.

### Usage

- Create your own OpenAI API key by making an [OpenAI](https://platform.openai.com/docs/api-reference/introduction) developer account.
- Run the following command in the **gpt3.5-chatbot** directory to start the OpenAI chatbot: `python chinese_chat_pal.py`



## NYT Chatbot

### Description

This chatbot is powered by text data retrived from the New York Times Archive API. Text data preprocessing (removing punctuation and stopwards, tokenization, lemmatization) is handled by the exploratory Jupyter Notebooks. **chinese_gpt2_train.py** is based on code written by [Dinne Bosman](https://dwjbosman.github.io/chatbot-using-open-ai-gpt-2-transformer-model/) and [Keisuke Sato](https://dev.to/ksk0629/my-own-chatbot-by-fine-tuning-gpt-2-m0n). This chatbot is access through the command line.

### Usage

- Create your own New York Times API key by making a [New York Times Dev Portal](https://developer.nytimes.com) account.
- Text data can only be accessed in batches, so adjustments should be made to the first cell of **ProjectA1i_NYT.ipynb**.
- Run the following command in the **chatbot-training** directory to start training the NYT GPT-2 model: `python chinese_gpt2_train.py`. Once complete, an executable **./nyt_gpt2_model** will be produced.
- Run the following command in the **chatbot-training** directory to start your NYT chatbot: `python nyt_chatbot.py`
