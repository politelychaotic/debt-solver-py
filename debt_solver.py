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

import random

class Debt:
    def __init__(self, principal, remainder, apr, budget, min=10, max=500, time):
        self.principal = principal
        self.remainder remainder
        self.apr = apr
        self.budget = budget
        self.min = min
        self.max = max
        self.time = time
        self.payopts = []

    def annual_increase(self):
        annual = self.principal * self.apr
        return annual

    def monthly_increase(self):
        mpr = self.apr / 12
        monthly = annual_increase() / 12
        return monthly_accrual

    def pay_schedule(self):
        annual_budget = self.budget * 12
        schedule = (self.time * self.apr + self.remainder) / annual_budget
        return schedule
    
    def find_optimal_schedule(self, schedule):
        for i in range(50):
            monthly_payment = random.randint(self.min, self.max)
            if monthly_payment not in self.payopts:
                self.payopts.append(monthly_payment)
        for i in range(len(self.payopts)):
            return
        
