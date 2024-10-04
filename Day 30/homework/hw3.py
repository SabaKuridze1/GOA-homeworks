# 3) შექმენით თავდაპირველად ცარიელი სია მომხმარებელს შემოატანინეთ რიცხვი შემდეგ
# კი 1-დან ამ რიცხვამდე დაამატეთ ყველა რიცხვი სიაში გამოიყენეთ for loop და append

num=[]

inp=int(input('Enter any number: '))

for i in range(inp):
    num.append(i)

print(num)