stock = { "AAPL" : 180, "TSLA" : 250}
total_investment = 0

n = int(input("Enter number of stock: "))
for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if name in stock :
        value = stock[name] * quantity
        total_investment += value
        print(f"{name} investment = {value} ")

    else:
        print("Stoch unavailable")
        break        
print("Total investment = ",total_investment)