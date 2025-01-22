# save this as app.py
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('C:/Users/ACER/Desktop/ManjuProject/ml_model.pkl', 'rb'))

crop_dict = {
    0: "Rice",
    1: "Wheat",
    2: "Mungbean",
    3: "Tea",
    4: "Coffee",
    5: "Jute",
    6: "Cotton",
    7: "Groundnut",
    8: "Sunflower",
    9: "Sugarcane",
    10: "Tobacco",
    11: "Paddy",
    12: "Maize",
    13: "Millet",
    14: "Barley",
    15: "Mustard",
    16: "Safflower",
    17: "Soyabean",
    18: "Oilseed",
    19: "Gram",
    20: "Lentil",
    21: "Peas",
    22: "Bean",
    23: "Chickpea",
    24: "Pea",
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['rainfall'])

        prediction = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])

        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
        else:
            crop = "Unknown Crop"

        return render_template("prediction.html", prediction_text="Predicted Crop: {}".format(crop))
    else:
        return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)
