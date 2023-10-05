#1
# with open('hw13one.txt','r',encoding="utf-8") as file1, open('hw13two.txt','r',encoding="utf-8") as file2:
#     lines1=file1.readlines()
#     lines2=file2.readlines()
#     diff = set(lines1) - set(lines2)
#     for line in diff:
#         print(line)
#2
# with open("hw13one.txt", "r", encoding="utf-8") as file:
#     lines = 0
#     symbs = 0
#     digits = 0
#     for line in file:
#         lines += 1
#         symbs +=len(line.strip())
#         for char in line:
#             if char.isdigit():
#                 digits += 1
#     print(lines,symbs,digits)
# with open("stat.txt", "w", encoding="utf-8") as file:
#     file.write("Number of symbols: " + str(symbs) + "\n")
#     file.write("Number of lines: " + str(lines) + "\n")
#     file.write("Number of digits: " + str(digits) + "\n")

#3
# with open("hw13one.txt", "r", encoding="utf-8") as file, open('withoutLastLine.txt','w',encoding="utf-8") as filewll:
#     lines=file.readlines()
#     lines=lines[:-1]
#     filewll.writelines(lines)

#4
# with open("hw13one.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     print(len(max(lines, key=len)))

#5

import datetime
diary = "diary.txt"
while True:
    print("Menu")
    print("'1' to add data")
    print("'2' to watch data")
    print("Any other key to exit")
    action = input("Choose the action:")

    if action == "1":
            data = input("Enter data ")
            with open('diary.txt', "a+", encoding="utf-8") as file:
                file.writelines(f"{(datetime.datetime.now())}: {data}\n")
    elif action == "2":
            with open('diary.txt', "r", encoding="utf-8") as file:
                for line in file:
                    print(line)
                    print("-----------------------")
    else: break

