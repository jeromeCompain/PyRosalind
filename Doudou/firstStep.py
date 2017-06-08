from builtins import int
a = 5 
b = 2
c = a / b
#types de variables : chaines de caracteres (str), listes (tuple), nombres (int pour entiers, float pour decimales) dictionnaires (dict)...
#===============================================================================
l = "hello word!"
# print(l)
# print(type(a))
# print(type(l))
# print(a+b)
# print(a-b)
# print(a*b)
#===============================================================================
print(c)
print(type(c))
print (55 % 25) # modulo, peut etre utile lors d'operation longues pour faire un suivi

t = "3"
print (type(t))
t = float(t)
print (t + a)
var = 6.5

print (round(var))

def round2(var):
    var = int(var + 0.5)
    return var

def round3(var):
    var2 = var * 10 
    if var2 % 10 == 5 :
        return int(var) + 1
    else : 
        return round(var)
    
print (round2(var))
print (round3(var))

a = 2527

if a % 2 == 0 : 
    print("a est pair")
elif a % 3 == 0 :
    print("a est multiple de trois mais pas pair")
elif a % 5 == 0 :
    print("a est multiple de 5")
else :
    print("ton nombre est pas fun")
    
i = 0
while i < 10 : 
    print("i = {0}".format(i))
    i += 1 
    
for i in range(1,4) :
    print("for i = {0}".format(i))
    
for i in l : 
    print("for i = {0}".format(i))


l = (1,2,3,4, "patate", 22, 46.54, "chausson aux pommes")
print(type(l))
print(l[4])
print(len(l))
# attention : list commence a 0 ; len donne la taille de la liste
for i in range(0,len(l)):
    print(l[i])

dic = {}
print(type(dic))

