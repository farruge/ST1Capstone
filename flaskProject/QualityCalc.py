# importing Flask and other modules
from flask import Flask, request, render_template
import pickle

# Establish Flask
quality = Flask(__name__)


# Defining the URL and functions
@quality.route('/', methods=["GET", "POST"])
def components():
    if request.method == "POST":
        # getting input in HTML form
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
