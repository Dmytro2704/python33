#1
nums=[-5.1,-4,-3.2,-2,-1.3,0,1,2.4,3,4.5,5]
polNums=list(filter(lambda num:num>0,nums))
print(polNums)

#2
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
if num1<num2:
    newNums = list(filter(lambda num: num > num1 and num < num2, nums))
    print(newNums)
else:
    print("First number must be < then second to filter numbers")
#
# #3
intNums = list(filter(lambda num: isinstance(num, int), nums))
print(intNums)

#4
logs = ['Paolo', "George", "Peter","Pepa","Jim"]
def add(log):
    return log + "$"
newLogs=list(map(add, logs))
print(newLogs)

#5
products=["Phone", "Tablet", "TV", "PC", "Headphone", "Watch"]
prices=[500,800,1000,1500,200,400]
discount=[0.05, 0.1, 0.15,0.08,0.00,0.05]

mainList=list(zip(products,prices,discount))
print(mainList)

#6
strList=list(map(lambda num: str(num),intNums))
print(strList)

