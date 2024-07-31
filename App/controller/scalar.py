import pickle

def LoadScalar():

    with open('model/scaler.pkl', 'rb') as file:
        loaded_scalar = pickle.load(file)

    return loaded_scalar

