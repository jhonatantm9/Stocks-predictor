from flask import Flask, request, render_template
import pandas as pd
import joblib
import forms
import json

# Declare a Flask app
app = Flask(__name__)

# Main function here

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def main():
    formulario_input = forms.FormularioEntrada(request.form)

    #If a form is submitted
    if request.method == "POST" and formulario_input.validate():

        # Unpickle classifier
        model = joblib.load("model.pkl")
        print('Se presiono el boton')
        # Get values through input bars
        OpIn_Over_NWC_PPE = request.form['input1']
        print(OpIn_Over_NWC_PPE)
        OpIn_Over_InterestExpense = request.form['input2']
        WorkingCapitalRatio = request.form['input3']
        RoE = request.form['input4']
        Asset_Turnover = request.form['input5']
        Gross_Profit_Margin = request.form['input6']
        
        # Put inputs to dataframe
        X = pd.DataFrame([[OpIn_Over_NWC_PPE, OpIn_Over_InterestExpense,WorkingCapitalRatio,RoE,Asset_Turnover,Gross_Profit_Margin]],
                         columns=["Op. In./(NWC+FA)", "Op. In./Interest Expense",'Working Capital Ratio','RoE',
                                  'Asset Turnover','Gross Profit Margin'])
        X.replace(0, 1e-10)

        # Get prediction
        prediction = model.predict(X)[0]
        prediction = "El resultado de la predicción es: " "{:.4f}".format(prediction)

    else:
        prediction = ""

    print(prediction)
    return render_template("index.html", form=formulario_input, output=prediction, Titulo='App principal')

@app.route('/respuesta', methods=['POST'])
def respuesta():
    print(request.form)
    input1 = request.form['input1']
    response = {'status': 200, 'input': input1}
    return json.dumps(response)

@app.route('/about')
def about():
    return render_template("about.html", Titulo="Acerca de")


# Running the app
if __name__ == '__main__':
    app.run(debug = True)
