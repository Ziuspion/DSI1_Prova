pt = 0.0
p = 0.0
fat = 0.0
tdp = 0.0
tcp = 0.0
peso = 0.0
leve = 0.0
medio = 0.0
pesado = 0.0
capital = 20 * 5
montante = 100 * 1 + float(20) / 100
tktm = 0.0
while tcp < 10:
    print("qual o peso do pacote?: ")
    peso = int(input())
    if peso <= 2:
        c = 10
        print("é menor ou igual à 2kg o preço fixo de " + str(c))
        p = c * tcp
        leve = leve + 1
    else:
        if peso > 2 or peso <= 10:
            c = 20
            print("está entre 2 à 10kg o preço fixo é de " + str(c))
            p = c * tcp
            medio = medio + 1
        else:
            if peso > 10:
                c = 30
                print("é maior que 10kg o preço fixo é de " + str(c))
                p = c * tcp
                pesado = pesado + 1
    print("1 se for internacional e 0 se não for")
    inter = int(input())
    if inter == 1:
        c = c * 1.2
        print("acrecimo de 20% " + str(c))
    pt = pt + peso
    fat = fat + c
    tdp = float(peso) / 10
    tcp = tcp + 1
if tcp > 0:
    tktm = float(fat) / 10
else:
    tktm = 0
print("Carga total de: " + str(pt) + " kg")
print("leves: " + str(leve) + "padroes: " + str(medio) + "pesados: " + str(pesado))
print("total de pacotes: " + str(tcp))
print("faturamento total: " + "R$" + str(fat))
print("média de faturamento por produto " + "R$" + str(tktm))
