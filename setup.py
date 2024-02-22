from src.data_storage import store_data, data_processing

def set_up():
    '''
    This function sets up the data and the pinecone index
    '''
    data_processing()
    database = store_data()
    print("Data and Pinecone index set up")

    return database
