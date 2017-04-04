#Sean Fitzhenry
#2/16/17
#Units 1&2 quiz

print("\t\tHello and welcome to my car value generator!")
print("\t\t\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/")

print("\n\t\t\t\t By Sean Fitzhenry")

name=input("What is your name?\n")
baseprice=int(input("\nWhat is the price of your vehicle?\n"))
sunroof=input("Do you want a sunroof?\n")
paintjob=input("Do you want a new paintjob?\n")
leatherseats=input("Do you want leatherseats?\n")

if sunroof=="yes" or "Yes" or "y" or "Y":
    price1=1500
else:
    price1=0
    
if paintjob=="yes"or "Yes" or "y" or "Y":
    price2=2000
else:
        price2=0
        
if leatherseats=="yes" or "Yes" or "y" or "Y":
    price3=800
else:
    price3=0

oneyear=(baseprice+price1+price2+price3)*.9
fiveyear=(baseprice+price1+price2+price3)*.5
tenyear=(baseprice+price1+price2+price3)*.1

print("The total stock price of your vehicle is", baseprice+price1+price2+price3, name+".\n")

print("\nDepreciation of your vehicle:")
print("After 1 year, your cars' value is estimated to be around","%.2f" %oneyear+"$.")
print("After 5 years, your cars' value is estimated to be around","%.2f" %fiveyear+"$.")
print("After 10 years, your cars' value is estimated to be around","%.2f" %tenyear+"$.")

print("\n\n\t\t \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/")
print("\t\t Thank you for using our car value generator", name+"!")
print("\t\t   We hope you found this useful! Come again!")

input("\n\npress enter to exit your car value generator")










