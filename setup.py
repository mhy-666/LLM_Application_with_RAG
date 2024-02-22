from src.data_storage import store_data, data_processing, get_index
import os

def set_up():
    '''
    This function sets up the data and the pinecone index
    '''
    # print(os.path.dirname(__file__))
    # database = store_data()
    # print("Data and Pinecone index set up")
    database = get_index()

    return database
