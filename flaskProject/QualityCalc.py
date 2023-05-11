# importing Flask and other modules
from flask import Flask, request, render_template
import pickle

# Establish Flask
quality = Flask(__name__)


# Defining the URL and functions
@quality.route('/', methods=["GET", "POST"])
def components():
    if request.method == "POST":
        #define variables
        fixed_acidity = 0.0
        volatile_acidity = 0.0
        citric_acid = 0.0
        residual_sugar = 0.0
        chlorides = 0.0
        free_sulphides = 0.0
        total_sulphides = 0.0
        density = 0.0
        pH = 0.0
        sulphates = 0.0
        alcohol = 0.0
        # getting input in HTML form
        while True:
            try:
                fixed_acidity = float(request.form.get("FA"))
                volatile_acidity = float(request.form.get("VA"))
                citric_acid = float(request.form.get("CA"))
                residual_sugar = float(request.form.get("RS"))
                chlorides = float(request.form.get("CH"))
                free_sulphides = float(request.form.get("FS"))
                total_sulphides = float(request.form.get("TS"))
                density = float(request.form.get("De"))
                pH = float(request.form.get("pH"))
                sulphates = float(request.form.get("SO4"))
                alcohol = float(request.form.get("Al"))
                break
            except ValueError:
                return "Please press the back button on your browser and enter a number for each component."
        # load model
        with open("winequality_predictor.h5", 'rb') as file:
            loaded_model = pickle.load(file)
        input_array = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                       chlorides, free_sulphides, total_sulphides, density, pH, sulphates, alcohol]
        prediction = loaded_model.predict([input_array])
        return "The predicted wine quality is " + str(prediction)
    return render_template("ComponentInputform.html")


if __name__ == '__main__':
    quality.run()
