#1
basketballPlayers={}
print("Enter 1 to add basketball player ")
print("Enter 2 to remove basketball player ")
print("Enter 3 to find basketball player ")
print("Enter 4 to change basketball player`s height ")
print("Enter 5 to print")
print("Any other symbol to exit")

while True:
    action = input("Choose the action")
    if action == '1':
        name = input("Enter player`s name")
        height = input("Enter player`s height")
        basketballPlayers[name] = height
    elif action == '2':
        name = input("Enter player`s name")
        del basketballPlayers[name]
    elif action == '3':
        name = input("Enter player`s name")
        if name in basketballPlayers:
            print(basketballPlayers.get(name))
        else:
            print('There is no this player in base')
    elif action == '4':
        name = input("Enter player`s name")
        height = input("Enter player`s height")
        basketballPlayers[name] = height
    elif action == '5':
        print(basketballPlayers)
    else:
        break

#2
dictionary = {}
def add_word(english, french):
    dictionary[english] = french
def remove_word(english):
    del dictionary[english]
def find_word(english):
    return dictionary.get(english, None)
def update_word(english, new_french):
    dictionary[english] = new_french
def print_dict():
    print(dictionary)
while True:
    print("Menu:")
    print("1. Add word")
    print("2. Delete word")
    print("3. Find word")
    print("4. Change translation")
    print("5. Print dictionary")
    print("Any other key to EXIT")

    choice = input("Choose the action: ")

    if choice == "1":
        english = input("Enter word in English ")
        french = input("Enter translation in French ")
        add_word(english, french)
    elif choice == "2":
        english = input("Enter word in English  ")
        remove_word(english)
    elif choice == "3":
        english = input("Enter word in English ")
        french = find_word(english)
        if french is not None:
            print(f"The {english} translated in French: {french}")
        else:
            print(f"There is no {english} in dictionary")
    elif choice == "4":
        english= input("Enter word in English ")
        new_french = input("Enter new translation in French  ")
        update_word(english, new_french)
    elif choice == "5":
        print_dict()
    else:
        break

#3

firm = {}

def add_worker(fio, phone, email, position, office, skype):
    data= {
    "fio": fio,
    "phone": phone,
    "email": email,
    "position": position,
    "office": office,
    "skype": skype
  }
    firm[fio] = data

def remove_worker(fio):
    del firm[fio]
def find_worker(fio):
    return firm.get(fio, None)
def update_worker(fio, **kwargs):
    firm[fio].update(kwargs)
def print_dict():
    print(firm)
while True:
    print("Menu:")
    print("1. Add worker")
    print("2. Delete worker")
    print("3. Find worker")
    print("4. Change worker`s data")
    print("5. Print data")
    print("Any other key to EXIT")

    choice = input("Choose the action: ")

    if choice == "1":
        fio = input("Enter worker`s full name")
        phone = input("Enter worker`s phone")
        email = input("Enter worker`s email ")
        position = input("Enter worker`s position ")
        office = input("Enter a number of worker`s office ")
        skype = input("Enter worker`s skype ")
        add_worker(fio, phone, email, position, office, skype)
    elif choice == "2":
        fio = input("Enter worker`s full name")
        remove_worker(fio)
    elif choice == "3":
        fio = input("Enter worker`s full name")
        data = find_worker(fio)
        if data is not None:
            print(data)
        else:
            print(f"There is no {fio} in base")
    elif choice == "4":
        fio = input("Enter worker`s full name")
        kwargs={}
        while True:
            print("What do you want to change?:")
            print("1. Name")
            print("2. Phone")
            print("3. Email")
            print("4. Position")
            print("5. Office number")
            print("6. Skype")
            print("7. Nothing")

            choice = input("Choose the action")

            if choice == "1":
                fio = input("Enter new name")
                kwargs["fio"] = fio
            elif choice == "2":
                phone = input("ВEnter new phone")
                kwargs["phone"] = phone
            elif choice == "3":
                email = input("Enter new email")
                kwargs["email"] = email
            elif choice == "4":
                position = input("Enter new position")
                kwargs["position"] = position
            elif choice == "5":
                office = input("Enter new office number")
                kwargs["office"] = office
            elif choice == "6":
                skype = input("Enter new skype")
                kwargs["skype"] = skype
            elif choice == "7":
                break
            update_worker(fio, **kwargs)
    elif choice == "5":
        print_dict()
    else:
        break

#4
books= {}

def add_book(author, title, genre, year, pages, publisher):
    data= {
    "author": author,
    "title": title,
    "genre": genre,
    "year": year,
    "pages": pages,
    "publisher": publisher
  }
    books[title] = data

def remove_book(title):
    del books[title]
def find_book(title):
    return books.get(title, None)

def update_book(title, **kwargs):
    books[title].update(kwargs)
def print_dict():
    print(books)
while True:
    print("Menu:")
    print("1. Add book")
    print("2. Delete book")
    print("3. Find book")
    print("4. Change book`s data")
    print("5. Print data")
    print("Any other key to EXIT")

    choice = input("Choose the action: ")

    if choice == "1":
        author = input("Enter author")
        title = input("Enter title")
        genre = input("Enter genre")
        year = input("Enter year")
        pages = input("Enter pages")
        publisher = input("Enter publisher")
        add_book(author, title, genre, year, pages, publisher)
    elif choice == "2":
        title = input("Enter title")
        remove_book(title)
    elif choice == "3":
        title = input("Enter title")
        data = find_book(title)
        if data is not None:
            print(data)
        else:
            print(f"There is no {title} in base")
    elif choice == "4":
        title = input("Enter title")
        kwargs={}
        while True:
            print("What do you want to change?:")
            print("1. Author")
            print("2. Title")
            print("3. Genre")
            print("4. Year")
            print("5. Pages")
            print("6. Publisher")
            print("7. Nothing")

            choice = input("Choose the action")

            if choice == "1":
                author = input("Enter new author")
                kwargs["author"] = author
            elif choice == "2":
                title = input("Enter new title")
                kwargs["title"] = title
            elif choice == "3":
                genre = input("Enter new genre")
                kwargs["genre"] = genre
            elif choice == "4":
                year = input("Enter new year")
                kwargs["year"] = year
            elif choice == "5":
                pages = input("Enter new pages")
                kwargs["pages"] = pages
            elif choice == "6":
                publisher = input("Enter new publisher")
                kwargs["publisher"] = publisher
            elif choice == "7":
                break
            update_book(title, **kwargs)
    elif choice == "5":
        print_dict()
    else:
        break



