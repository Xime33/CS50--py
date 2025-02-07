def main():
    #ask for the item
    item = input("Item: ").title()
    calories = matcher(item)

    if calories:
        print(f"Calories: {calories}")

def matcher (item):
    match item:
        case "Apple":
            return "130"
        case "Avocado":
            return "50"
        case "Banana":
            return "110"
        case "Cantaloupe":
            return "50"
        case "Grapes":
            return "90"
        case "Honeydew Melon":
            return "50"
        case "Kiwifruit":
            return "90"
        case "Lemon":
            return "15"
        case "Lime":
            return "20"
        case "Nectarine":
            return "60"
        case "Orange":
            return "80"
        case "Peach":
            return "60"
        case "Pear":
            return "100"
        case "Pineapple":
            return "50"
        case "Plums":
            return "70"
        case "Strawberries":
            return "50"
        case "Sweet Cherries":
            return "100"
        case "Tangerine":
            return "50"
        case "Watermelon":
            return "80"
        case _:
            return None


main()
