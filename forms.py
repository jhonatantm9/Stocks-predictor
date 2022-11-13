from wtforms import Form
from wtforms import DecimalField
from wtforms import validators

# def isZero(form, field):
#     if field.data == 0:
#         field.data = 1e-10
#         print('zero')

class FormularioEntrada(Form):
    input1 = DecimalField(label='Op. In./(NWC+PP&E)', validators=[
        validators.input_required()
    ])
    input2 = DecimalField('Op. In./Interest Expense', validators=[
        validators.input_required()
    ])
    input3 = DecimalField('Working Capital Ratio', validators=[
        validators.input_required()
    ])
    input4 = DecimalField('RoE', validators=[
        validators.input_required()
    ])
    input5 = DecimalField('Asset Turnover', validators=[
        validators.input_required()
    ])
    input6 = DecimalField('Gross Profit Margin', validators=[
        validators.input_required()
    ])