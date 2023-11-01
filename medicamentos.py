medicines = {
    "name1": [],
    "price1": [],
    "name2": [],
    "price2": [],
    "name3": [],
    "price3": [],
    "name4": [],
    "price4": [],
    "name5": [],
    "price5": []
}

#name = input(f"name of the medicine: ")
#medicines["name1"] = name
#price = int(input("price of the medicine: "))
#medicines["price1"] = price
#name = input(f"name of the medicine: ")
#medicines["name2"] = name
#price = int(input("price of the medicine: "))
#medicines["price2"] = price
#name = input(f"name of the medicine: ")
#medicines["name3"] = name
#price = int(input("price of the medicine: "))
#medicines["price3"] = price
#name = input(f"name of the medicine: ")
#medicines["name4"] = name
#price = int(input("price of the medicine: "))
#medicines["price4"] = price
#name = input(f"name of the medicine: ")
#medicines["name5"] = name
#price = int(input("price of the medicine: "))
#medicines["price5"] = price

for c in range(1,6):
    name = input(f"name of the medicine: ")
    medicines[f"name{c}"] = name
    price = int(input("price of the medicine: "))
    medicines[f"price{c}"] = price

print(medicines)