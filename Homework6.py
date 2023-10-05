# #1
# text =input("Enter text")
# sentences =text.split(".")
# newSentences = []
# for sentence in sentences:
#   sentence = sentence.strip()
#   if not sentence:
#     continue
#   sentence = sentence.capitalize()
#   newSentences.append(sentence)
# newText = '. '.join(newSentences)
# print(newText)
# d=0
# for s in text:
#     if  s.isdigit():
#         d+= 1
# print("Количество цифр:", d)
# sign="!"
# print("Количество !:", text.count(sign))
# signs = {".",",","!","?",":",":","..."}
# print("Количество знаков препинания:", len(list(filter(lambda s: s in signs, text))))

#2
# numbers = [int(number) for number in input("Введите список целых чисел: ").split()]
# number= int(input("Введите число, которое необходимо найти: "))
# count = numbers.count(number)
# print("Количество '", number, "' в списке = ", count)

#3
# numbers = [int(number) for number in input("Введите список целых чисел: ").split()]
# print("Сумма чисел =", sum(numbers), "Среднее арифметическое =", sum(numbers)/len(numbers))

