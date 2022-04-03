# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 15:19:32 2021

@author: Preethi Abraham
"""
#Amortization Code-Preethi and Alvin

#We ask the user to enter a principal value
while True:
    try:
        Principal=float(input('Enter the principal amount'))
        break
    except ValueError:
         print("That was not a valid number. Please try again")


#We ask the user to enter the interest rate
while True:
    try:
        interest_rate=float(input('Enter the interest rate (between 0 to 1)'))
        break
    except ValueError:
         print("That was not a valid number. Please try again")


#We ask the user to input the expected payment amount
while True:
    try:
        expected_payment=float(input('Enter minimum expected payment'))
        break
    except ValueError:
         print("That was not a valid number. Please try again")

#We ask the user to input the extra payment amount
while True:
    try:
        extra_payment=float(input('Enter extra payment amount'))
        break
    except ValueError:
         print("That was not a valid number. Please try again")

#Here, we have set the first beginning principal to the value which the user has given for Principal
begin_P=Principal
begin_P

#We have computed the first interest amount
interest=round(((interest_rate*Principal)/12),2)
interest

#We have computed the first p_applied value
p_applied=expected_payment+extra_payment-interest
p_applied

#Finally, we have computed the first end principal value
end_P=begin_P-p_applied
end_P

#In order to calculate the total values such as total payment, total interest, total p applied and number of payments, we have initialized them to 0
total_payment=0
total_interest=0
total_P_applied=0
no_of_payments=0

#This is the heading of our table
print("Begin P  ","   Payment   ","   Interest  ", "  Extra Payment ", " P Applied  " ," End P ")

#The while condition is used here to print out each of the values until the end_P becomes 0
while(end_P>0):
        print(begin_P,"    ",expected_payment,"    ",interest,"   ",extra_payment,"           ",p_applied,"      ",end_P)
        begin_P=end_P
        expected_payment=expected_payment
        interest=round(((interest_rate*begin_P)/12),2)
        extra_payment=extra_payment
        p_applied=round((expected_payment+extra_payment-interest),2)
        end_P=round((begin_P-p_applied),2)
        total_payment=total_payment+ expected_payment
        total_interest=total_interest+interest
        total_P_applied=total_P_applied+p_applied
        no_of_payments=no_of_payments+1
        
    


    
#Finally, we print out the total of some of the columns and also the number of years that it takes to complete the payment
print('Total Payment= $',round(total_payment,2))
print('Total Interest= $',round(total_interest,2))
print('Total Principal Applied= $', round(total_P_applied,2))
print('No of payments to be made= ', no_of_payments)
print('No of years to make the payment=', int(no_of_payments/12))