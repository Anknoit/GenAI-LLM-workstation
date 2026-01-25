# GenAI-workstation
A repo for learning and experimenting with GenAI frameworks and tools

# Interview Questions

## GEN AI
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

## Numpy, Pandas, Json Handling
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