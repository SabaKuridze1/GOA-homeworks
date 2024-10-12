# 2) შექმენით სია სადაც იქნება 10 სახელი შემდეგ ამ სიიდან ამოშლით ყველა იმ სახელს რომელიც იწყება ა ასოზე და დაბეჭდეთ გაფილტრული სია

datooooooo=['aveji','asmati','kavasaki','str','mee','bekeka','suii','ananasi','messi','barca']

for i in range(len(datooooooo)-2):
    if datooooooo[i][1]=='a':
        datooooooo.remove(datooooooo[i])
        i=i-1


print(datooooooo)
