from transformers import BertForQuestionAnswering, BertTokenizer, TrainingArguments, Trainer
from transformers.data.processors.squad import SquadV2Processor

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

processor = SquadV2Processor()
train_examples = processor.get_train_examples(data_dir='data/squad_v2')

# Initialize the BERT model for question answering
model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')

# Set up the training arguments
training_args = TrainingArguments(
    output_dir='./results',
    learning_rate=2e-5,
    num_train_epochs=2,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    gradient_accumulation_steps=2,
    evaluation_strategy='epoch',
    save_total_limit=2,
)

# Set up the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
)

# Train the model
trainer.train()