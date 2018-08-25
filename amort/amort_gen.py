# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 23:52:54 2018

@author: Joseph Aviles
@date: 07/20/18
@description: purpose is to make an amort schedule dataframe.
"""

import pandas as pd
import datetime as dt

def incrementMonth(date):
    if(date.month == 12):
       return dt.date(date.year+1,1,date.day)
    return dt.date(date.year,date.month+1,date.day)

def makeAmortDF(startDate,rate,loanAmt,loanPeriod,extraPayment=0):
    rate = rate / (12*100)
    payment = round(loanAmt * rate * (1.0+rate)**loanPeriod / ((1.0+rate)**loanPeriod-1),1)

    preDF = {'Pay Date':[startDate],
             'Beginning Balance':[loanAmt],
             'Payment':[payment],
             'Principal':[],
             'Interest':[],
             'Extra Payment':[extraPayment],
             'Cumulative Principal':[],
             'Cumulative Interest':[],
             'Ending Balance':[]}

    preDF['Interest'].append(round(preDF['Beginning Balance'][0]*rate,2))
    preDF['Principal'].append(round(payment - preDF['Interest'][0],2))
    preDF['Ending Balance'].append(preDF['Beginning Balance'][0]-preDF['Principal'][0])
    preDF['Cumulative Interest'].append(preDF['Interest'][0])
    preDF['Cumulative Principal'].append(preDF['Principal'][0])

    while preDF['Ending Balance'][-1] > 0:
        preDF['Extra Payment'].append(extraPayment)
        preDF['Beginning Balance'].append(preDF['Ending Balance'][-1])
        preDF['Payment'].append(payment)
        preDF['Pay Date'].append(incrementMonth(preDF['Pay Date'][-1]))
        preDF['Interest'].append(round(preDF['Beginning Balance'][-1]*rate,2))
        preDF['Principal'].append(round(payment - preDF['Interest'][-1],2))
        preDF['Ending Balance'].append(preDF['Beginning Balance'][-1]-preDF['Principal'][-1])
        preDF['Cumulative Interest'].append(preDF['Interest'][-1]+preDF['Cumulative Interest'][-1])
        preDF['Cumulative Principal'].append(preDF['Principal'][-1]+preDF['Cumulative Principal'][-1])

    return preDF #pd.DataFrame(preDF)
