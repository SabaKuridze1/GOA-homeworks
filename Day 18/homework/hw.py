balance = 1000

while True:
    print("1. ბალანსის შემოწმება")
    print("2. ბანკში შეტანა")
    print("3. ამოღება")
    print("4. გამოსვლა")

    choice = int(input("ჩაწერე შენი არჩევანი: "))

    if choice == 1:
        print("შენი ბალანსია:", balance)
    elif choice == 3:
        amount = int(input("ჩაწერე რამდენი გინდა რომ ამოიღო ბანკის ანგარიშიდან: "))
        if amount > balance:
            print("ამოღება ვერ შესრულდა. ცადეთ თავიდან.")
        else:
            balance -= amount
            print("ამოღება წარმატებით შესრულდა. შენი ახალი ბალანსი არის:", balance)
    elif choice == 2:
        amount = int(input("ჩაწერე რამდენი გინდა რომ შეიტანო ბანკში: "))
        balance += amount
        print("შეტანა მოხერხდა წარმატებით. შენი აცალი ბალანსი არის:", balance)
    elif choice == 4:
        print("მადლობა რომ გამოიყენე ჩვენი ბანკის სისტემა!")
    else:
        print("არჩევანი ვერ შესრულდა. ცადე თავიდან.")