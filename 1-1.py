n = int(input("Введите количество монет"))
moneta_orel = 0
moneta_reshka = 0
for i in range(n):
    m = int(input("Укажите значение если монета орел то 1 если решка то 0"))
    if m == 0:
        moneta_reshka += 1
    else:
        moneta_orel += 1
if moneta_orel == moneta_reshka:
    print("Количество монет одинаковое переверните либо орлов либо решки")
elif moneta_reshka > moneta_orel:
    print ("Монет орел меньше переверните их")
else:
    print("Монет решек меньше переверните их")
    