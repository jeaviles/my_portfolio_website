from django import forms
from decimal import Decimal

class AmortForm(forms.Form):
    loan_amt = forms.DecimalField(label="Loan Amount",min_value=Decimal("0.01"))
    rate = forms.FloatField(label="Interest Rate",min_value=0,max_value=50)
    loan_period = forms.IntegerField(label="Loan Period (# of Months)",min_value=0)
    orig_date_year = forms.IntegerField(label="First Payment Year",
                                        min_value=1,
                                        max_value=3000)
    orig_date_month = forms.IntegerField(label="First Payment Month",
                                        min_value=1,
                                        max_value=12)
