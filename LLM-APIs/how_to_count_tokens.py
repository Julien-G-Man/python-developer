import tiktoken

def count_tokens(text):
    enc = tiktoken.encoding_for_model("gpt-4.1-mini")
    tokens = enc.encode(text)
    print(f"Number of tokens: {len(tokens)}")
    

text = "Julien is building AI systems in Africa."    
count_tokens(text)
