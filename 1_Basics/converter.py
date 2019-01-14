print("How many kilometers have you walked today ?")
km = float(input())
miles = km/1.60934
miles = round(miles,2)
print(f"Your {km} km ride equals to {miles} mi")