import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling, TrainingArguments, Trainer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

train_path = "/Users/samuelbraun/Desktop/ProjectA1_NYT/chatbot-development/train1.txt"
test_path = "/Users/samuelbraun/Desktop/ProjectA1_NYT/chatbot-development/test1.txt"

def load_dataset(train_path, test_path, tokenizer):
    train_dataset = TextDataset(tokenizer=tokenizer, file_path=train_path, block_size=128)
    test_dataset = TextDataset(tokenizer=tokenizer, file_path=test_path, block_size=128)
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
    
    return train_dataset, test_dataset, data_collator

train_dataset, test_dataset, data_collator = load_dataset('train.txt', 'test.txt', tokenizer)

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=1,
    per_device_train_batch_size=32,
    per_device_eval_batch_size=64,
    eval_steps = 400,
    save_steps=800,
    warmup_steps=500,
    logging_dir='./logs',
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

trainer.train()

# Save the trained model
model.save_pretrained('./nyt_gpt2_model')
tokenizer.save_pretrained('./nyt_gpt2_model')
