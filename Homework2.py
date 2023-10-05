#Task1

num1=float(input('Enter num1'))
num2=float(input('Enter num2'))
num3=float(input('Enter num3'))
sel=(input("Choose the action + or *"))
if sel=="+":
    print("+ =", num1+num2+num3)
elif sel=="*":
    print("* =", num1*num2*num3)

else:
    print("Wrong action")

#Task2

num1=float(input('Enter num1'))
num2=float(input('Enter num2'))
num3=float(input('Enter num3'))
sel=(input("Choose the action max, min or average"))
if sel=="max":
    if num1>=num2:
        if num1>=num3:
            print("max =", num1)
        else:
            print("max =", num3)
    else:
        if num2>=num3:
            print("max =", num2)
        else:
            print("max =", num3)

elif sel=="min":
    if num1<=num2:
        if num1<=num3:
            print("min =", num1)
        else:
            print("min =", num3)
    else:
        if num2<=num3:
            print("min =", num2)
        else:
            print("min =", num3)
elif sel=="average":
    print('Average = ', (num1+num2+num3)/3)


else:
    print("Wrong action")

#Task3
d=float(input('Enter distance in meters'))
t=input('What unit of measure do you want to convert to? (miles, inches or yards.)')
if t=='miles': print('Distance in miles will be = ', d*0.000621371)
elif t=='inches': print('Distance in inches will be = ', d*39.3701)
elif t=='yards': print('Distance in yards will be = ', d*1.09361)
else: print("Wrong action")

#Task4
day=int(input('Enter day of the week number'))
if day==1:
    print('Monday')
elif day==2:
    print('Tuesday')
elif day==3:
    print('Wednesday')
elif day==4:
    print('Thursday')
elif day==5:
    print('Friday')
elif day==6:
    print('Saturday')
elif day==7:
    print('Sunday')
else: print('Wrong day of the week number')

#Task5

mon=int(input('Enter month of the year number'))
if mon==1:
    print('January')
elif mon==2:
    print('February')
elif mon==3:
    print('March')
elif mon==4:
    print('April')
elif mon==5:
    print('May')
elif mon==6:
    print('June')
elif mon==7:
    print('July')
elif mon==8:
    print('August')
elif mon==9:
    print('September')
elif mon==10:
    print('October')
elif mon==11:
    print('November')
elif mon==12:
    print('December')
else: print('Wrong month of the year number')

# Task6
sign=float(input('Enter a number'))
if sign>0:
    print('Number is positive')
elif sign<0:
    print('Number is negative')
else:
    print('Number is equal to zero')

# Task7
num1=float(input('Enter num1'))
num2=float(input('Enter num2'))
if num1!=num2:
    if num1>num2:
        print(num2, num1)
    else:
        print(num1, num2)
else: print('Numbers are equal')

# Task8
dur=int(input('Enter the call duration in minutes'))
mine=input('Choose your operator (Vodafone, Kyivstar or Lifecell)')
out=input('Choose subscriber`s operator (Vodafone, Kyivstar or Lifecell)')
if mine=='Vodafone':
    if out=='Vodafone': print('You call will be free of charge!')
    elif out=='Kyivstar': print('You call will cost : ', dur*0.4, '$, paying 40 cents for minute')
    elif out=='Lifecell': print('You call will cost : ', dur*0.5, '$, paying 50 cents for minute')
    else: print('Wrong subscriber`s operator')
elif mine=='Kyivstar':
    if out=='Kyivstar': print('You call will be free of charge!')
    elif out=='Vodafone': print('You call will cost : ', dur*0.45, '$, paying 45 cents for minute')
    elif out=='Lifecell': print('You call will cost : ', dur*0.55, '$, paying 55 cents for minute')
    else: print('Wrong subscriber`s operator')
elif mine=='Lifecell':
    if out == 'Lifecell': print('You call will be free of charge!')
    elif out=='Vodafone': print('You call will cost : ', dur*0.43, '$, paying 43 cents for minute')
    elif out=='Kyivstar': print('You call will cost : ', dur*0.53, '$, paying 53 cents for minute')
    else: print('Wrong subscriber`s operator')
else:
    print('Wrong own operator')


# Task9
man1Sales=float(input('How much did the first product manager sell for?'))
man2Sales=float(input('How much did the second product manager sell for?'))
man3Sales=float(input('How much did the third product manager sell for?'))
if man1Sales>=0 and man1Sales<500: zp1=200+man1Sales*0.03
elif man1Sales>=500 and man1Sales<=1000: zp1=200+man1Sales*0.05
elif man1Sales>1000: zp1=200+man1Sales*0.08
else: print('Wrong first manager`s sales')

if man2Sales>=0 and man2Sales<500: zp2=200+man2Sales*0.03
elif man2Sales>=500 and man2Sales<=1000: zp2=200+man2Sales*0.05
elif man2Sales>1000: zp2=200+man2Sales*0.08
else: print('Wrong second manager`s sales')

if man3Sales>=0 and man3Sales<500: zp3=200+man3Sales*0.03
elif man3Sales>=500 and man3Sales<=1000: zp3=200+man3Sales*0.05
elif man3Sales>1000: zp3=200+man3Sales*0.08
else: print('Wrong third manager`s sales')

print('First manager earned -',zp1,'\n','Second manager earned -',zp2,'\n','Third manager earned -',zp3,'\n')
if zp1==zp2 and zp2==zp3:
    print('Everybody were equal, each bonus salary will be', zp1+200)
else:
      if zp1>zp2:
        if zp1>zp3:
            print("First manager was best, his bonus salary will be  ", zp1+200)
        elif zp1<zp3:
            print("Third manager was best, his bonus salary will be  ", zp3+200)
        else:print("First and third managers were bests), their bonus salary will be  ", zp1+200)
      elif zp1<zp2:
        if zp2>zp3:
            print("Second manager was best, his bonus salary will be ", zp2+200)
        elif zp2<zp3:
            print("Third manager was best, his bonus salary will be  ", zp3+200)
        else:print("Third and second managers were bests), their bonus salary will be  ", zp2+200)
      else:print("First and second managers were bests), their bonus salary will be  ", zp1+200)



