numero = int(input("Entre com um número para ver sua tabuada: "))

for num in range(10):
    print("{} x {:2} = {}".format(numero, num+1, (num+1)*numero))