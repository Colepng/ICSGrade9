cheq_acc = int(input("How much money do you have in your chequing account "))
sav_acc = int(input("How much money do you have in your saving account "))

if cheq_acc > 1000 or sav_acc > 1500:
    serv_charge = 0
else:
    serv_charge = 0.15
print(f"${serv_charge}")