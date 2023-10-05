#Task1
# start=int(input('Start'))
# end=int(input('Finish'))
# while start != end:
#     start += 1
#     if start%7:
#         continue
#     print( start)

#Task2
# start=int(input('Start'))
# end=int(input('Finish'))
# #1
# while start != end:
#     start += 1
#     print(start)
# #2
# while end != start:
#     end -= 1
#     print(end)
# #3
# while start != end:
#     start += 1
#     if start%7:
#         continue
#     print( start)
#4
# i=0
# while start != end:
#     start += 1
#     if start%5:
#         continue
#     i+=1
# print(i)

#Task3
# sumOdd=0
# iE=0
# sumEven=0
# iO=0
# sumNine=0
# iN=0
# start=int(input('Start'))
# end=int(input('Finish'))
# while start != end:
#     start += 1
#     if start%2:
#         sumOdd=sumOdd+start
#         iO+=1
#     else:
#         sumEven=sumEven+start
#         iE+=1
#     if start%9:
#         continue
#     sumNine=sumNine+start
#     iN+=1
# print('SumEven= ', sumEven,'SumOdd= ', sumOdd, 'SumNine =', sumNine)
# AveO=sumOdd/iO
# AveE=sumEven/iE
# if iN!=0: AveN=sumNine/iN
# else: AveN=0
# print('Average odd= ', AveO,'Average even= ', AveE, 'Average nine =', AveN)

#Task4
# lenght=int(input('Enter lendht of the line'))
# sign=input('Enter the sign')
# i=0
# while i<lenght:
#     i+=1
#     print(sign, end='\n')

#Task5
# while True:
#     num=float(input("Enter a number"))
#     if num>0:
#         print("Number is positive")
#     elif num==0:
#         print("Number is equal to zero")
#     else:
#         print("Number is negative")
#     if num==7:
#         print('Good Bye!')
#         break

# Task6
# sum=0
# max=0
# min=1000000000
# while True:
#     num=float(input("Enter a number"))
#     sum=sum+num
#     print('Summ = ', sum )
#     if max<num: max=num
#     print('Max = ', max)
#     if min>num: min=num
#     print('Min = ', min)
#     if num==7:
#         print('Good Bye!')
#         break

#Task7
number = input("Enter a number: ")
i=0
sum=0
zer= 0
for digit in number:
    if digit != "0":
        i+=1
        sum+=int(digit)
    else:
        zer+= 1
print("Number of digits in a number:", (i+zer))
print("Summ of digits in a number:", sum)
print("Average of digits in a number:", sum/(i+zer))
print("Number of zeroes in a number:", zer)