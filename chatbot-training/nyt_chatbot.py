import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling, TrainingArguments, Trainer

# Save trained model
path_to_model = '/Users/samuelbraun/Desktop/ProjectA1_NYT/nyt_gpt2_model'
tokenizer = GPT2Tokenizer.from_pretrained(path_to_model)
model = GPT2LMHeadModel.from_pretrained(path_to_model)

# Interaction with trained model
model = GPT2LMHeadModel.from_pretrained('./nyt_gpt2_model')
tokenizer = GPT2Tokenizer.from_pretrained('./nyt_gpt2_model')

while True:  # This will keep the chatbot running and allow for continuous interaction
    input_text = input("You: ")  # Get input from the user
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # Adjust the temperature parameter
    temperature = 0.8
    sample_outputs = model.generate(input_ids, pad_token_id=50256, max_length=100, num_return_sequences=1, temperature=temperature)

    print("Chatbot:", tokenizer.decode(sample_outputs[0], skip_special_tokens=True))
