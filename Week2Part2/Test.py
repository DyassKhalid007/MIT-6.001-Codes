# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 01:45:14 2018

@author: Dyass
"""
balance = 320000; annualInterestRate = 0.2
monthly_interest_rate=annualInterestRate/12.0
minimum_monthly_payment=0
low_minimum_monthly_payment=balance/12.0
high_minimum_monthly_payment=(balance*(1+monthly_interest_rate)**12)/12.0
minimum_monthly_payment=(low_minimum_monthly_payment+high_minimum_monthly_payment)/2.0
print(minimum_monthly_payment)
c=False
epsilon=0.2
d=0
while True:
    a=0
    b=balance
    while a!=12:
        a+=1
        b=b-minimum_monthly_payment
        b+=(b*monthly_interest_rate)
        #print("b is:",round(b,2))
#        if b<=0:
#            break
    
    if round(b,2)==0:
        break
    elif b<0:
        high_minimum_monthly_payment=minimum_monthly_payment
    elif b>0:  
        low_minimum_monthly_payment=minimum_monthly_payment
    minimum_monthly_payment=(low_minimum_monthly_payment+high_minimum_monthly_payment)/2.0
    #print(minimum_monthly_payment)

    
        
        
    
        
print("Lowest Payment:",round(minimum_monthly_payment,2))