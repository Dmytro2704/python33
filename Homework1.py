x=int(2.99)
print(x)

kol=int(input("Enter number"))
print(kol)

radius=float(input("Enter number"))
print (radius)

s=3.14*radius**2
print ("r = ", radius, "S = ", s)

hour=float(input("Сколько часов Вася спит ночью?"))
min=float(input("Сколько минут Вася спит днем"))
son=hour*60+min
print("Вася спит ", son, " минут в сутки")

sec=float(input("Введите значение в секундах"))
h=sec//3600
m=(sec-h*3600)//60
news=(sec-h*3600)%60
print("То же время в часах",h, " минутах",m, "секундах",news)






