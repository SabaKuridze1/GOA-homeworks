#  1) შექმენით მენტორების სახელების სია და ჩვეულებრივი სახელებისთვის განკუთვნილი სია შემდეგ
# მომხმარებელს შემოატანინეთ სახელი თუ ეს სახელი იქნება რომელიმე
# მენტორის სახელი ამ შემთხვევაში ეს სახელი დაემატოს მენტორებისთვის განკუთვნილ სიაში სხვა შემთხვევაში თუარიქნება ეს სახელი მენტორის
# სახელი დაემატოს ჩვეულებრივი სახელების სიაში შემდეგ კი ორივე დაბეჭდეთ


mentor=['luka cxvaradze', 'gabriel molodini', 'data tezelashvili','dato janezashvili', 'davit narimanidze','zuka abashidze']
names=['saba','luka','gio','jemali','aslani','aleqsandre']


VIP=[]
normal=[]


ur_name=input('Enter Your Name: ')
for i in range(len(mentor)):
    if ur_name==mentor[i]:
        VIP.append(ur_name)

for i in range (len(names)):
    if ur_name==names[i]:
        normal.append(ur_name)

print(VIP)
print(normal)