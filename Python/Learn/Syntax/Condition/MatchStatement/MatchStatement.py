Service = input("Choose service number(1-3): ")

match Service:
    case "1":print("Withdraw") #if answer is 1
    case "2":print("Composit") #if answer is 2
    case "3":print("Your current money") #if answer is 3
    case "":print("Invalid , Please try again") #if not input
