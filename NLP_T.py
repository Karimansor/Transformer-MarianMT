from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

def load_model_and_translate(model_path, tokenizer_path, input_text):
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        generated_ids = model.generate(inputs['input_ids'], max_length=512, num_beams=4, early_stopping=True)
    translated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return translated_text

model_path = r"C:\Users\XOX\Downloads\NLP_T"
tokenizer_path = model_path
input_text = "Hello, how are you?"
translated_text = load_model_and_translate(model_path, tokenizer_path, input_text)
print(f"Translated text: {translated_text}")
