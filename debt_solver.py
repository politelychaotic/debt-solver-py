#!/bin/python


#debt_solver.py

'''
This is a Python program that takes in:
1) lines of credit/loans/any debt 
    a) principal (the amount you took out for a line for credit or a loan)
    b) remainder (the amount left to pay off)
2) the annual interest rate (as a number e.g. 3.5% -> 3.5)
3) an overall monthly budget that can be spent towards paying off the debt
4) minimum monthly payments
5) maximum monthly payments (if applicable, otherwise default is set at $500)

Using these inputs for each debt-line, the program will find the fastest way 
to pay off your debt within the monthly debt budget

-politelychaotic
August 2024
'''
