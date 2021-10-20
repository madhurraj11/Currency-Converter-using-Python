# import sys
# sys.path.append('D:\college')
with open("currencyData.txt") as f:
    lines = f.readlines()
print(lines)
currencyDict = {}
for line in lines:
    a = line.split("\t")
    currencyDict[a[0]] = a[1]
print(currencyDict)
while True:
    amount = int(input("Enter amount:\n"))
    print("Enter the name of currency you wanna convert this amount to? Available Options:\n")
    for item in currencyDict.keys():
        print(item)
    currency = input("Please enter one of these values: \n")
    print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")
    chyn = input("Do You Want to Continue, Y|N:")
    if chyn == "Y" or chyn == "n":
        print("Thanks for using our Currency Converter....")
        break