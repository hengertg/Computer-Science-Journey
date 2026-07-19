## 6.100A PSet 1: Part A
## Name: henger
## Time Spent:
## Collaborators: Henger

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your year salary: "))
portion_saved = float(input("Enter your portion saved: "))
cost_of_dream_home = float(input("Enter the cost of your dream house: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
amount_saved = 0
down_payment = 0.25
r = 0.05


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

# Down Payment Calcultion of the Dream House
if cost_of_dream_home > 0:
    down_payment_total = cost_of_dream_home * down_payment
    print(f"Your down payment is {down_payment_total}")

else:
    print("Please enter a valid amount")


# Annual rate at end of each month calculation

annual_rate = r/12

month = amount_saved * annual_rate
print(f"your month rate is  {month}%")

# Saving increase by 1% of monthly salary algorithm

savings = annual_rate * portion_saved
print(f"your savings are {savings}%")
