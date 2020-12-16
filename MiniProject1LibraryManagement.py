class library :
    list_of_books = ['BhagavadGeeta','2666','All About Love','Desert Solitaire','Disgrace','Geek Love',
                     'Gilead','Giovanni\'s Room','A Good Man Is Hard to Find','The Handmaid\'s Tale','The Hitchhiker\'s Guide to the Galaxy',
                     'If on a Winter\'s Night a Traveler','Infinite Jest','The Left Hand of Darkness','Lolita','Man\'s Search for Meaning',
                     'Maus','Never Let Me Go','A People\'s History of the United States','The Phantom Tollbooth','Poems','Slaughterhouse-Five','Things Fall Apart']
    due_list = {}
    def displayBooks(self):
        return self.list_of_books

    def lendBook(self,book_name,lender):
        if book_name in self.list_of_books :
            self.due_list[book_name] = lender
            #print(self.due_list)
            self.list_of_books.remove(book_name)
            #print(self.list_of_books)
            print(f'Here is your book {book_name} , Njoy your book!!')
        else :
            print('The book which you have asked is not avliable in the library currently ')


    def addBook(self,book_name):
        self.list_of_books.append(book_name)

    def returnBook(self,book_name):
        self.list_of_books.append(book_name)

if __name__ =='__main__':
    mylibrary = library()
    # print(mylibrary.displayBooks())
    while (True):
        print(
            "          Welcome to Monlu's Library\n Please choose one of follwing services \n 1.Display Bokks list \n 2.Lend A Book\n 3.Add A Book\n 4.Return A Book")
        choice = int(input())
        if (choice == 1):
            print(mylibrary.displayBooks())
        elif choice == 2:
            book_name = input("Enter the name of book you want to lend")
            lender = input("Kindly let us know your good name")
            mylibrary.lendBook(book_name,lender)

        elif choice == 3:
            book_name = input("Enter the name of book you want to add")
            mylibrary.addBook(book_name)
            print(f'your book {book_name} is added to Monlu\'s library successfully')
        elif choice == 4:
            book_name = input("Enter the name of book you want to return")
            mylibrary.returnBook(book_name)
            print(f"your Book {book_name} is returned successfully.")
        else:
            print("Invalid Input")


