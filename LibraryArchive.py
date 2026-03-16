#12/02/26

import random

class Book:
    def __init__(self,isbn,title):
        self.isbn = isbn
        self.title = title
    def bookType(self):
        pass

class EBook(Book):
    def __init__(self,isbn,title,file_size):
        super().__init__(isbn,title)
        self.extra = file_size
    def bookType(self):
        return "EBook"

class Hardcover(Book):
    def __init__(self,isbn,title,weight):
        super().__init__(isbn,title)
        self.extra = weight
    def bookType(self):
        return "Hardcover"

def quicksort(array):

    if len(array) <= 1:
        return array

    less = []
    equal = []
    more = []
    pivot = array[0].isbn
    for book in array:
        if book.isbn < pivot:
            less.append(book)
        elif book.isbn > pivot:
            more.append(book)
        else:
            equal.append(book)

    return quicksort(less) + equal + quicksort(more)

def binary(array,search):

    isbns = []
    for book in array:
        isbns.append(book.isbn)

    low = 0
    high = len(array)-1
    mid = (low+high)//2

    while isbns[mid]!=search and high>=low:
        if isbns[mid] == search:
            high = -1
        elif isbns[mid]>search:
            high = mid-1
            mid = (low+high)//2
        elif isbns[mid]<search:
            low = mid+1
            mid = (low+high)//2

    if isbns[mid]==search:
        return mid
    else:
        return -1

books = []
bookNames = ["Hungry Hungry Caterpillar","Romeo and Juliet","Pride and Prejudice","The Great Gatsby","Animal Farm","To Kill A Mockingbird","The Hobbit","The Bible","The Catcher In The Rye","The Da Vinci Code"]
for i in range(0,len(bookNames)):
    newISBN = random.randint(100000,999999)
    variable = random.randint(100,1000)
    if i%2==0:
        newBook = EBook(newISBN,bookNames[i],variable)
    else:
        newBook = Hardcover(newISBN,bookNames[i],variable)
    books.append(newBook)

books = quicksort(books)

print(" ISBN   | Book Name")

print("--------------------------------------")
for book in books:
    print(" "+str(book.isbn),"| ",book.title)

print("")
print("What is the ISBN number of the book you want")
request = 0
while request < 100000 or request > 999999:
    try:
        request = int(input(" -> "))
        if request < 100000 or request > 999999:
            print("Please enter a valid number")
    except ValueError:
        print("Please enter an integer")

print("")
index = binary(books,request)
if index == -1:
    print("Sorry, that isbn doesn't match with any book")
else:
    print(books[index].title,"was found")
    if books[index].bookType() == "EBook":
        print("It is an EBook")
        print("The file size is",books[index].extra,"megabyte")
    else:
        print("It is a Hardcover")
        print("The weight is",books[index].extra,"grams")

