for x in range(0,151):  # Básico
    print(x)

for q in range(5,1001,5): # Múltiplos de 5
    print(q)

for w in range(1,101):
    if w % 10 == 0:
        print("Coding Dojo")    # Contar, a la manera del Dojo
    elif w % 5 == 0:
        print("Coding")

total_impares = 0
for e in range(0,500001):
    if e % 2 != 0:              # Whoa. Es un gran idiota
        total_impares += e
print(total_impares)

for r in range(2018, 0, -4):    # Cuenta regresiva de a 4
    print(r)


lowNum = 2 
highNum = 9
mult = 3

for t in range(lowNum,highNum+1):           # Contador flexible
    if t % 3 == 0:
        print(t)
        
