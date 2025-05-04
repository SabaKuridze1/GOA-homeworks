shemotana = input("shemoitanet sityva: ")
listn = []
while shemotana != "sakmarisia":
    shemotana = input("kidev: ")
    listn.append(shemotana)
print(sorted(listn, key = len))
