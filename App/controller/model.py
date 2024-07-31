import pickle

def LoadModel():

    with open('model/diabetes.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    return loaded_model