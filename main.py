from flask import Flask, request, render_template
import pandas as pd
import joblib
import forms
import json

X_sin_escalar = pd.read_csv("./Tables/Ratios_sin_escalar.csv", index_col = 0)
X_sin_escalar = X_sin_escalar.drop(['Cash Ratio'], axis=1)
X_sin_escalar.reset_index(inplace=True, drop=True)

X_min = X_sin_escalar.min()
X_max = X_sin_escalar.max()
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
        # Get values through input bars
        OpIn_Over_NWC_PPE = float(request.form['input1'])
        OpIn_Over_NWC_PPE = (OpIn_Over_NWC_PPE - X_min[0]) / (X_max[0] - X_min[0])

        OpIn_Over_InterestExpense = float(request.form['input2'])
        OpIn_Over_InterestExpense = (OpIn_Over_InterestExpense - X_min[1]) / (X_max[1] - X_min[1])

        WorkingCapitalRatio = float(request.form['input3'])
        WorkingCapitalRatio = (WorkingCapitalRatio - X_min[2]) / (X_max[2] - X_min[2])

        RoE = float(request.form['input4'])
        RoE = (RoE - X_min[3]) / (X_max[3] - X_min[3])

        Asset_Turnover = float(request.form['input5'])
        Asset_Turnover = (Asset_Turnover - X_min[4]) / (X_max[4] - X_min[4])

        Gross_Profit_Margin = float(request.form['input6'])
        Gross_Profit_Margin = (Gross_Profit_Margin - X_min[5]) / (X_max[5] - X_min[5])
        
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
