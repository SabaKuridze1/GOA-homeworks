#   2) 1 დან 100 მდე დაბეჭდეთ ყოველი ლუწი რიცხვი და მიუწერეთ მათ რომ ლუწია, შემდეგ 1 და 100 მდე დაბეჭდეთ ყოველი კენტი რიცხვი და მიუწერეთ რომ კენტია, გამოიყენეთ მხოლოდ ლუპი
for i in range (1, 101):
    if i % 2 == 0:
        print(i + 'luwia')
    else:
        print(i + 'kentia')