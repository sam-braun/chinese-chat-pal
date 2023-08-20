# Custom Trained & OpenAI API Chatbots

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [NYT Chatbot](#nyt-chatbot)
  - [Description](#description)
  - [Usage](#usage)
- [OpenAI API Chatbot](#openai-api-chatbot)
  - [Description](#description-1)
  - [Usage](#usage-1)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project explores building two different chatbots used to practice Chinese-language conversations about politics, technology, and business for non-native Mandarin speakers. The first chatbot is a GPT-2 chatbot custom trained on text from three decades of New York Times reporting on China. The second chatbot is build using OpenAI's GPT-3.5 Turbo API and is accessed through a web interface.

## Installation

1. Clone the repository: `git clone https://github.com/sam-braun/chinese-chat-pal.git`
2. Install dependencies: `pip install requirements.txt`

## NYT Chatbot

### Description

This chatbot is powered by text data from the New York Times. By leveraging article content, headlines, and other available data, it provides users with information and summaries about various topics. Text data preprocessing (removing punctuation and stopwards, tokenization, lemmatization) is handled by the exploratory Jupyter Notebooks. chinese_gpt2_train.py is based on code written by [Dinne Bosman](https://dwjbosman.github.io/chatbot-using-open-ai-gpt-2-transformer-model/) and [Keisuke Sato](https://dev.to/ksk0629/my-own-chatbot-by-fine-tuning-gpt-2-m0n).

### Usage

- Create your own New York Times API key. To find more information about the New York Times's API, please visit [New York Times Dev Portal](https://developer.nytimes.com).
- Run the following command in the chatbot-training directory to start the NYT chatbot: `python chinese_gpt2_train.py`

