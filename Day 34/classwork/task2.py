#      2) შექმენით ფუნქცია რომელიც მომხმარებელს ეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი 

def luw_kenti():
    num=int(input('sheiyvanet ricxvi: '))
    if num%2==0:
        print('luwia')
    else:
        print('kentia')

luw_kenti()