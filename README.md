# LLM_Application_with_RAG (League of Legends Q&A System)


## Overview

This project aims to create a Q&A system focused on the gaming domain, specifically for the game League of Legends (LoL), developed by Riot Games. As the game continuously updates and introduces new champions, some are not recognized by ChatGPT. To address this, the project involves scraping hero introductions from the official LoL website, using Retrieval-Augmented Generation (RAG) to create a corresponding vector database, and ultimately compiling an encyclopedia knowledgeable about new champions.

## Implementation

### Data Collection

- **Champion Background Stories:** Using a web crawler, I scraped the background stories of all champions and saved them into a CSV file. **--web_scrapy.py**
- **Data Processing:** Utilized pandas to read the data from the CSV file.-**data_extraction.py**
- **Chunk Function:** Implemented a function that supports an overlap option, dividing each hero's story into chunks of no more than 1000 characters while ensuring sentences are not truncated. If an overlap size is specified, adjacent sentences can overlap by the specified number of characters. **--data_chunk.py**

### Vector Database and Embeddings

- **Embedding Conversion:** Called OpenAI's embedding API to convert the story chunks into embeddings and processed the data into a suitable DataFrame format. **--embedding.py**
- **Vector Database Storage:** Stored the processed data in the cloud vector database Pinecone, using it purely as a storage tool and not for its built-in similarity comparison API. Instead, I employed NumPy's cosine similarity to calculate the similarity between each piece of data and the query, ultimately retrieving the 5 most similar chunks as auxiliary context.**--data_storage.py,  retrieval.py**

### Model Integration and Deployment

- **ChatGPT Model API:** Utilized the ChatGPT 3.5 model API, with and without the context parameter, to generate responses. The first response utilizes the RAG method, and the second provides a regular GPT answer. **--LLMs.py**
- **Streamlit Deployment:** Deployed the model to the cloud using Streamlit, making the League of Legends encyclopedia accessible online. **--setup.py, streamlit_app.py**

## To use

need a OpenAI key

```
OPENAI_API_KEY='insertkeyhere'
```

then install python package and start in cloud or in local machine

```
pip install -r requirements.txt

streamlit run your_script.py
```

## Access

You can explore the League of Legends encyclopedia by visiting the deployed web application. [https://llmapplicationwithrag-hzrennqwpr7cht62fjzipk.streamlit.app/]