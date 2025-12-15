# This script is custom made tokenizer script by me
# to understand the concept and flow of what happens during tokenization
import random

def tokenizer(data: str):
    """
    Docstring for custom_tokenizer.tokenizer
    1. Split the words or contents of dataset
    2. assign memory maps to the individual words - for lookup purpose
        - oftent stored in  embedding table, used by vectorizer to convert to vector
    """
    split_data = data.split()
    print(split_data)

    # for i in split_data:
    #     embedding_table = {
    #     split_data[i]: random.randint(1,5000)
    #    }
    print(map(random.randint(1, 5000), split_data))
    # print(embedding_table)


tokenizer("My name is Ankit Jha")