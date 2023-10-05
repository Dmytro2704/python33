#1
str=input("Enter string")
rts=str[::-1]
if len(str)==1: print('One symbol  always is a palindrom :-)')
elif len(str)==2: print('Two symbols  could not be a palindrom :-)')
elif len(str)==0: print('You entered nothing')
else:
    if str == rts:
        print("Palindrom")
    else:
        print("Not a palindrom")

#2
text = input("Enter text")
words = input("Enter words to change").split()
for word in words:
    text = text.replace(word, word.upper())
print("Changed text : \n", text)

#3
text = input("Enter text")
count = 0
for i in range(len(text)):
    if text[i] == "." or text[i] == "!" or text[i] == "?":
        count += 1
print("Number of sentences in text =", count)

#4
exp=input("Enter an arithmetic expression")
try:
    for i in range(len(exp)):
        if exp[i] == "+":
            num1, num2 = exp.split("+")
            res = (int(num1) + int(num2))
        elif exp[i] == "-":
            num1, num2 = exp.split("-")
            res = (int(num1) - int(num2))
        elif exp[i] == "/":
            num1, num2 = exp.split("/")
            res = (int(num1) / int(num2))
        elif exp[i] == "*":
            num1, num2 = exp.split("*")
            res = (int(num1) * int(num2))
    print(res)
except ZeroDivisionError:
    print("Сan't divide by zero")
