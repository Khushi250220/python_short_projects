# Input we need from the user
# Total rent 
# Total food ordered for snacking
# electricity Charge 
# Person living in room

# ouput 
# total amount  you have to pay  



rent = int(input("enter the total rent = "))
food = int(input("Enter the amount of food ordered = "))
Electricity_reading = int(input("enter The total Electricity Reading = "))
charge_per_unit = int(input("Enter the charge per unit"))
persons = int(input("Enter the number of person living in the room = "))

Electricity_total = Electricity_reading*charge_per_unit
sum = rent+food + Electricity_total 
print(f"Total amount you have to pay : {sum /persons}")