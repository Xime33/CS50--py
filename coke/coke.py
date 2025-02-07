def main():
    amount = 50
    while amount > 0:
        print(f"Amount Due: {amount}")
        insert = int(input("Insert Coin: "))

        if insert in [5,10,25]:
            amount -= insert
        else:
          print("Invalid coin")

    change = abs(amount)
    print(f"Change Owed: {change}")






main()
