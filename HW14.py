#1
import json
import os

countryDict={'Ukraine': 'Kyiv', 'UK':'London'}

def saveData(fileName):
    with open(fileName,'w') as file:
        json.dump(countryDict,file, indent=4)
        print(f"Data saved in {fileName}")
def loadData(fileName):
    global countryDict
    try:
        with open(fileName, 'r') as file:
            countryDict = json.load(file)
    except Exception:
        countryDict = {}
    print(f"Data loaded from {fileName}")
def addCountry(country,capital):
    loadData('countries.json')
    if country not in countryDict:
        countryDict[country]=capital
        saveData('countries.json')
        print(f'{country} with capital in {capital} added to dict')
    else:
        print(f'{country} is already in dict')
def deleteCountry(country):
    loadData('countries.json')
    if country in countryDict:
        del countryDict[country]
        saveData('countries.json')
        print(f'{country} deleted from dict')
    else:
        print(f'There is no {country} in dict')

def findCountry(fileName, country):
    loadData(fileName)
    if country in countryDict:
        print(f'The capital of {country} is {countryDict[country]}')
    else:
        print(f'There is no {country} in dict')
def editData(fileName, country, newCapital):
    loadData(fileName)
    if country in countryDict:
        countryDict[country]=newCapital
        saveData(fileName)
        print(f'The capital of {country} was changed to {newCapital}')
    else:
        print(f'There is no {country} in dict')
saveData('countries.json')
addCountry("USA","Washington")
addCountry("Poland","Warzawa")
deleteCountry('UK')
findCountry('countries.json','USA')
editData('countries.json','Poland',"Warsaw")


#2

def load_data(fileName):
    if os.path.isfile(fileName):
        with open(fileName, 'r') as file:
            try:
                data = json.load(file)
            except FileNotFoundError:
                data = {}
    else:
        data = {}

    return data

def save_data(fileName, data):
    with open(fileName,'w') as file:
        json.dump(data,file, indent=4)

def add_data(data, last_name,first_name, age):
    if last_name not in data:
        data[last_name]={'first_name':first_name,'age':age}
        print(f'{last_name} added to data')
    else:
        print(f'{last_name} was already in data')
def edit_data(data,last_name, new_first_name,new_age):
    if last_name in data:
        data[last_name]={'first_name':new_first_name,'age':new_age}
        print(f'{last_name} firstname and age were changed in data')
    else:
        print(f'There is no {last_name} in data')
def delete_data(data, last_name):
    if last_name in data:
        del data[last_name]
        print(f"{last_name} deleted.")
    else:
        print(f"{last_name} not found in data")

def search_by_last_name(data, last_name):
    if last_name in data:
        print(f"Lastname: {last_name}")
        print(f"Firstname: {data[last_name]['first_name']}")
        print(f"Age: {data[last_name]['age']}")
    else:
        print(f"{last_name} not found in data")


def search_by_age(data, age):
    found_data = []
    for last_name, item in data.items():
        if item['age'] == age:
            found_data.append(last_name)

    if found_data:
        print(f"Personal with age {age}:")
        for last_name in found_data:
            print(f"{last_name} {data[last_name]['first_name']}")
    else:
        print(f"Personal with age {age} not found")
def search_by_letter(data,letter):
    found_data = []
    for last_name, item in data.items():
        if last_name.startswith(letter.upper()):
            found_data.append(last_name)
    if found_data:
        print(f"Personal with lastname starts from {letter}:")
        for last_name in found_data:
            print(f"{last_name} {data[last_name]['first_name']} {data[last_name]['age']}")
    else:
        print(f"Personal with lastname starts from {letter} not found")
data=load_data('data.json')
while True:
    print("Menu")
    print("1. Add person")
    print("2. Edit person")
    print("3. Delete person")
    print("4. Search by lastname")
    print("5. Search by age")
    print("6. Search by first letter in lastname")
    print("7. Print from file")
    print('8. Save data')
    print("Any other key to save and exit")

    action = input("Choose the action: ")
    if action == "1":
        last_name = input("Lastname: ")
        first_name = input("Firstname: ")
        age = int(input("Age: "))
        add_data(data, last_name, first_name, age)
    elif action == "2":
        last_name = input("Enter lastname to edit data")
        new_first_name = input("New firstname: ")
        new_age = int(input("New age: "))
        edit_data(data, last_name, new_first_name, new_age)
    elif action == "3":
        last_name = input("Enter lastname to delete data ")
        delete_data(data, last_name)
    elif action == "4":
        last_name = input("Enter lastname to search: ")
        search_by_last_name(data, last_name)
    elif action == "5":
        age = int(input("Enter age to search: "))
        search_by_age(data, age)
    elif action == "6":
        letter = input("Enter first letter in lastname ")
        search_by_letter(data, letter)
    elif action == "7":
        for last_name in data:
            print(f"{last_name} {data[last_name]['first_name']} age = {data[last_name]['age']} years")
    elif action=="8":
        save_data('data.json', data)
        print('Data saved')
    else:
        save_data('data.json', data)
        break






