m=[]
for i in range(5):
    item = input("enter the product")
    quantity = int(input("enter the quantity"))
    f = open("data.txt", "r")
    for i in f:
        if i.split(" ")[0] == item and int(i.split(" ")[2]) >= quantity:
            a = int(i.split(" ")[1])
            price = (quantity * a)
            m.append(price)
            print(price)
total=sum(m)
print("the total price is:",total)








