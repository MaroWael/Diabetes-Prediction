def GetPrediction(model, inputs: list):
    result = {
    0: "You are in good well",
    1: "Unfortunately, You are a diabetic"}
    predction = model.predict(inputs)[0]
    return result[predction]