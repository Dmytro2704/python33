#Task 1

# try:
#     x = int(input("Введите целое число"))
#     y = int(input("Введите степень"))
# except ValueError as ex:
#     print(ex)
#     print("Неверный тип введенных данных")
# except NameError as ax:
#     print(ax)
#     print("Вы ввели букву или символ, вместо числа")
# except Exception:
#     print("Что-то пошло не так...")
# finally:
#     print("Процесс завершен")
# print("Результат вычислений х в степени у =", x**y)


#Task2

# number = input("Введите число: ")
# new_number = 0
# try:
#     for digit in number:
#         if digit != "3" and digit != "6":
#             new_number += digit
#     print("Номер без цифр 3 и 6:", new_number)
# except ValueError:
#         print("Неверный тип введенных данных")
# except TypeError:
#         print("Введенное значение не является целым числом")
# except Exception:
#         print("Что-то пошло не так...")
# finally:
#         print("Процесс завершен")

#Task3

# try:
#     num1=float(input("Введите первое число"))
#     num2=float(input("Введите второе число"))
#     sign = input("Выберите действие +,-,/,*")
#     if sign=='+': print(num1+num2)
#     elif sign=='-': print(num1-num2)
#     elif sign=='/': print(num1/num2)
#     elif sign=='*': print(num1*num2)
#     else: print("Неправильно введен знак")
# except (ValueError, TypeError): print("Неправильно введено число")
# except ZeroDivisionError: print("На ноль делить нельзя!")
# except Exception: print("Ошибка ввода данных")
# finally:
#     print("Процесс завершен")

#Task4
import random
secret_code = [random.randint(1, 6) for _ in range(4)]
try:
    while True:
        guess = input("Введите попытку: ")
        guess_list = list(map(int, guess))
        correct = 0
        incorrect = 0
        if len(guess_list)==4:
            for i in range(4):
                if guess_list[i] == secret_code[i]:
                    correct += 1
                elif guess_list[i] in secret_code:
                    incorrect += 1
            print("Верных цифр:", correct)
            print("Неправильных цифр:", incorrect)
            if correct == 4:
                print("Вы угадали!")
                break
        else: print("Число должно состоять из четырех цифр")
except (ValueError, TypeError): print("Введены буквы или символы вместо цифр")
except Exception: print("Ошибка ввода данных")
finally:
    print("Процесс завершен")