# GenAI-workstation
A repo for learning and experimenting with GenAI frameworks and tools

# Interview Questions

## GEN AI - hashedIn
1. What are some chunking techniques for long documents?
    - Sliding window
    - Fixed size
    - Recursive
2. What is RAG?
    - RAG (Retrieval Augmented Generation) is a technique that combines the power of retrieval and generation to create more accurate and contextually relevant responses.
    - It works by first retrieving relevant information from a knowledge base (e.g. a database or a set of documents) and then using that information to generate a response to a user's query.
    - 
3. What is vectorDB?
    - A vector database is a database that stores and retrieves data in the form of vectors (i.e. arrays of numbers) instead of traditional key-value pairs.
    - It is used to store and retrieve embeddings of text data, which can be used for tasks such as similarity search and clustering.
4. Leetcode question - https://leetcode.com/problems/alternating-groups-ii/description/

## Numpy, Pandas, Json Handling - Genysys
Q1. given csv of employee table with employee_id, dept, salary, employee name
- read data from csv
- find total no. of employees
- find average salary of each department
- write the data to csv with dept, and average salary

Q2. Given api url (user and their post)
- fetch all the data of api
- find the user with maximum posts
- output the data in dictionary form into a json file, 

Q3. given a list comprising of a dictionary with student name and marks
- write a func that takes in list of data of student info and compares who clears the cuttoff for this (list and cutoff are i/p parameters)
- return a list with student name, marks obtained if cleared the cuttoff

## FastAPI and LLM (Langchain and Langraph)
Q1. Diff between Rule Based Chatbot and LLM Chatbot?
Q2. Diff between Langraph and ADK
Q3. Getting rule violation when API hit? What could be the reason?
Q4. How to improve performance for api?
Q5. How to fine tune an LLM Model
Q5. Sort int array, print 5 numbers in recursion.

## OTO Capital and C2C Adnaved System AI Engineer
Q1. How do you validate the response of an LLM and make sure it does not hallucinate?


## Some reference from JD
Experience with cloud platforms (AWS, Azure, or GCP).
Knowledge of Docker and Kubernetes.
Experience with FastAPI or Flask.
Familiarity with Hugging Face Transformers.
Experience with model deployment and MLOps.
Exposure to fine-tuning open-source LLMs.

## c2c Advanced System AI Engineer
1. Whats an MCP?
2. What are some frameworks for embeddings?
3. Frameworks for multiagent
4. Whats a knowledge graph
5. Whats inference Engine
6. p-99, p80
7. top-k, top-b
8. Explain Tranformer archtiecture
9. Langraph, and Langsmith
10. How Vector DB perform efficient searching for embedding values
11. How and whats ranking of chunks (for better output of RAG)
12. How can we optimize repeated queries given by user to avoid token waste?