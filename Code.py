'''Restro Code '''
#Menu
Menu ={
  'Burger': 100,
  'Pizza': 200,
  'French Fries': 50,
  'Sandwich': 150,
  'Coke': 50,
  'Pepsi': 50,
  'Sprite': 50
}

#Greeting
print("Welcom to the Restro What do you want to order")
print( "Burger:Rs100\n Pizza:Rs200\n French Fries:Rs50\n Sandwich:Rs150\n Coke:Rs50 Pepsi:Rs50\n Sprite:Rs50")
#Order
order_total = 0

item_1 =input("Enter you first order : ")
order_total = order_total+Menu[item_1] #0+iteam from menue will be added
if item_1 in Menu:
  print(f'Your order is {item_1} and the price is {Menu[item_1]}')


else:
  print("Sorry we dont have this item")

another_item=input("Do you want to order something else? (Yes/No) : ")
if another_item == "Yes":
  item_2=input("Enter you Second order : ")
  order_total = order_total+Menu[item_2]
  if item_2 in Menu:
    print(f'Your order is {item_2} and the price is {Menu[item_2]}')


  else:
    print("Sorry we dont have this item")

print(f'Total amount you have to pay is {order_total}')
