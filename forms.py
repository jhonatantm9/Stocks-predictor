from wtforms import Form
from wtforms import DecimalField

class FormularioEntrada(Form):
    input1 = DecimalField('Op. In./(NWC+FA)')
    input2 = DecimalField('Op. In./Interest Expense')
    input3 = DecimalField('Working Capital Ratio')
    input4 = DecimalField('RoE')
    input5 = DecimalField('Asset Turnover')
    input6 = DecimalField('Gross Profit Margin')