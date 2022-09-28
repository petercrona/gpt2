from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

res = generator("I eat data for breakfast", max_length=100, num_return_sequences=5)

print(res)
