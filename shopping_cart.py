foodslist=[]#1 food ki list bnai
priceslist=[]#1 prices ki list bnai
total=0

while True:# loop tbh tk chahiya jab tk user quit na kry is liya true rkha
    food=input("enter the food name for quit press(q/Q):")# quite condition bnai ha yha pr (if) ma
    if food.lower()=="q":# .lower is liya use kiya agar user capital q likhy ya small loop quite ho jay
        break# end krny ky liya loop
    else:# end ni kiya user ny to agy ka kam yha pr
        price=float(input("enter the price of food:$"))
        foodslist.append(food)#jo bh food user inter kry ga osy append mtln add krdo foodslist jo list bnai ha osma
        priceslist.append(price)# same logic append ki
print("----- YOUR CART LIST -----")


for food,price in zip(foodslist,priceslist):#zip use kiya 2 list ko combine krny ky liya taky on ka result columns ma show kr sko/ aur 1 loop ma dono list ky items ka result nikal diya 
    print(f"{food},${price}")
    
    
#ya alag line ma result dy ga for loop nichy wala
for price in priceslist:#forloop use kiya taky output [] esy list ma na close ay line a output ay har item
    total+=price
print(f"the total bill is ${round(total,2)}")
