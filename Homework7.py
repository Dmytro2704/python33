import random


#1
try:
    def time(s, v):
        t = s / v
        print("Time= ", t)


    def distance(v, t):
        s = v * t
        print("Distance = ", s)


    time(10, 2)
    distance(2, 5)
except ZeroDivisionError:
    print("Can not devide by zero")
except Exception:
    print("Wrong incoming data")

#2
def task2(num):
    if num >0: res=True
    elif num<0: res=False
    else: res="Number is equal zero"
    print(res)
task2(-2)

#3
def print_numbers(num):
    i=1
    while i<num:
        print(i)
        i+=1
print_numbers(5)

#4
def min_max(*nums):
    print("Min number = ",min(nums), "Index of the min number = ", nums.index(min(nums)))
    print("Max number = ",max(nums), "Index of the max number = ", nums.index(max(nums)))
min_max(1,2,3,4,5,6,7)

#5
def average(*nums):
    print("Average of numbers = ", sum(nums)/len(nums))
average(1,2,3,4,5,6,7,8,9,10)

#4
def rev(*nums):
    array=[*nums]
    array.reverse()
    print(array)
rev(1,2,3,4,5)

#5
def sum_range(a,b):
    if a<b:
        print("Sum of the numbers between arguments =", sum(range(a+1,b)))
    elif a>b:
        print("Sum of the numbers between arguments =", sum(range(b+1, a)))
    else:
        print("There is no any number between arguments")
sum_range(5,1)

#6
def sign_counter(*nums):
    pos=0
    neg=0
    zer=0
    for number in nums:
        if number>0:
            pos+=1
        elif number<0:
            neg+=1
        elif number==0:
            zer+=1
        else: print("Incoming element is not a number")
    print("Quantity of positive numbers =", pos, "Quantity of negative numbers =", neg, "Quantity of zeroes = ", zer)
sign_counter(-1,0,1,-2,2,-3,3,-4,6,5)

#7
try:
    def lucky(*nums):

        if len(nums) == 6:
            nums1 = nums[:3]
            nums2 = nums[3:]
            if sum(nums1) == sum(nums2):
                print("Your numbers are lucky!")
            else:
                print("Your numbers are unlucky")
        else:
            print("You must enter 6 numbers to check")

    lucky(1,2,3,3,2,1)
except NameError:
    print("Wrong data! Need six integers, to check lucky")

#8
def generate_random_numbers(quantity, first, last, filter):
    numbers=[]
    for i in range(quantity):
        number=random.randint(first,last)
        if number!=filter:
            numbers.append(number)
    print(numbers, "The function created an array of", quantity, "random elements starting with", first, "ending with ", last,"elements equal to the filter",filter,"were excluded")
generate_random_numbers(10,1,5,2)


