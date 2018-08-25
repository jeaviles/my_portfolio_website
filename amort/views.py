from django.shortcuts import render
from .forms import AmortForm
from .amort_gen import makeAmortDF
from .plot_html import plot_html
import datetime as dt

def amort_view(request):
    form = AmortForm()

    if request.method == "POST":
        form = AmortForm(request.POST)

        if form.is_valid():
            loan_amt = float(request.POST.get("loan_amt"))
            rate = float(request.POST.get("rate"))
            loan_period = float(request.POST.get("loan_period"))
            orig_date_year = int(request.POST.get("orig_date_year"))
            orig_date_month = int(request.POST.get("orig_date_month"))

            date = dt.date(orig_date_year,orig_date_month,15)

            #print('loan_amt {} ,rate {} ,loan_period {} ,date {}'.format(loan_amt,rate,loan_period,date))

            df = makeAmortDF(startDate=date,
                             loanAmt=loan_amt,
                             rate=rate,
                             loanPeriod=loan_period)

            table_list = []

            for i in range(len(df['Payment'])):
                temp_list = []
                for key,value in df.items():
                    if(i == 0 and 'Cumulative' in key):
                        temp_list.append(0)
                    elif('Cumulative' in key):
                        temp_list.append(value[i-1])
                    elif('Extra' not in key):
                        temp_list.append(value[i])
                table_list.append(temp_list)

            html_plot = str(plot_html(df))

            return render(request,'amort/amort.html',{'form':form,
                                                        'df':df,
                                                        'table_list':table_list,
                                                        'html_plot':html_plot})

    return render(request,'amort/amort.html',{'form':form})
