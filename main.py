menu = {
    "Pasta" : 80,
    "Hakka_Noodles" : 90,
    "Dosa" : 150,
    "Waffle" : 135,
    "Burger" : 60,
    "Idli" : 50,
    "Chola_Bhatura" : 100,
    "Spicy_Corn" : 100,
    "Chola_Kulcha" : 120
}

print("Welcome to the Cafe !")
print("Pasta : Rs80\n Hakka_Noodles : Rs90\n Dosa : Rs150\n Waffle : Rs135\n Momos : Rs100\n Burger : Rs 60\n Idli : Rs50\n Chola_Bhatura : Rs100\n Spicy_Corn : Rs100\n Chola_Kulcha : Rs120")

order_total = 0 
item_1 = input("enter the name of the item you want to order : ")
if item_1 in menu :
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order ! ")
else:
    print(f"Your item {item_1} is not in the menu . Sorry you can try anything else !! ")

another_order = input("Do you want to order anything else ?")
if another_order == "Yes":
    item_2 = input("Enter the name of the second item : ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order !")
    else:
        print(f"Your item {item_2} is not in the menu . Sorry you can try anything else !! ")

print(f"The total amount to be paid by you is {order_total}")