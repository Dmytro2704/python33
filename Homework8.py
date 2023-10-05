
#1
myStr = input("Enter string to remove digits: ")
delDigits = lambda str: ''.join(filter(lambda x: not x.isdigit(), str))
newStr = delDigits(myStr)
print(newStr)

#2
numbers = [1, 2, 3, 4, 5]
sumLambda = lambda x: sum(x)
aveLambda = lambda x: sum(x) / len(x)
print("Sum =", sumLambda(numbers),"Average =", aveLambda(numbers))

#3
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = lambda l1, l2: l1 + l2
print(l3(l1, l2))

#4
def gcd(x,y):
    if x==0:
        return y
    elif y==0:
        return x
    else:
        return gcd(y, x % y)
num1 = int(input("First number"))
num2 = int(input("Second number"))
res = gcd(num1, num2)
print("Greatest Common Divisor =", res)

#5

import random

def play_game(secret_code, count=0):
    try:
        guess = input("Введите попытку: ")
        guess_list = list(map(int, guess))
        correct = 0
        incorrect = 0
        count += 1

        if len(guess_list) == 4:
            for i in range(4):
                if guess_list[i] == secret_code[i]:
                    correct += 1
                elif guess_list[i] in secret_code:
                    incorrect += 1

            print("Коров:", correct)
            print("Быков:", incorrect)

            if correct == 4:
                print("Вы угадали с", count, "попыток!")
            else:
                play_game(secret_code, count)
        else:
            print("Число должно состоять из четырех цифр")
            play_game(secret_code, count)

    except (ValueError, TypeError):
        print("Введены буквы или символы вместо цифр")
        play_game(secret_code, count)
    except Exception:
        print("Ошибка ввода данных")
        play_game(secret_code, count)
secret_code = [random.randint(1, 6) for _ in range(4)]
print(secret_code)
play_game(secret_code)