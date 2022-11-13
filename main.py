#TIP CALCULATOR 

# 1. Take input for total bill 
# 2. Take input for how much tip customer would like to give 
# 3. Take input for how many people have to pay the bill 
# 4. Result of how many have every body to pay

print("!!! TIP CALCULATOR !!!") 

total_bill = float(input("How much is bill? \n"))
tip_bill = int(input("How much tip would you like to give? (15% or 20%) \n")) 
people_on_bill = int(input("How many people have to pay the bill? \n"))
                     
percentage = 1 + tip_bill / 100 
per_pers = total_bill / people_on_bill 
final = per_pers * percentage 
print(round(final))
