#premise /business name
print("Asanka Hotel")   

Food_charge = float(input("Please enter the charge for the food: "))

#calculating for the tip at 18%
Tip_percent = 0.18
Tip_amount = Food_charge * Tip_percent

#calculating for tax at 7%
Tax_percent = 0.07
Tax_amount = Food_charge * Tax_percent

#total cost
Total_amount = Food_charge + Tip_amount + Tax_amount

#the print out
print(f"Food_charge: {Food_charge:.2f}")
print(f"Tip_percent (18%): {Tip_amount:.2f}")
print(f"Tax_percent (7%): {Tax_amount:.2f}")
print(f"Total_amount: {Total_amount:.2f}")
print("Thank you for shopping with us! ")