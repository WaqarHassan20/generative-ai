import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o")
text = "Hello, world! How are you today?"
tokens = encoding.encode(text)

print("Tokens : ", tokens)
# Tokens: [13225, 11, 2375, 0, 3253, 553, 481, 4044, 30]

print("-----------------------")

decoded_text = encoding.decode([13225, 11, 2375, 0, 3253, 553, 481, 4044, 30])
print("Text : ", decoded_text)