
import transformers

model = transformers.DistilBERTModel.from_pretrained("distilbert-base-uncased-emotion")

inputs = transformers.InputExample(text="I am happy today", label="happiness")

outputs = model(**inputs)

print(outputs.logits)
