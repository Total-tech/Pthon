print("welcome to yovi's  library\n\n")
list=["'The Great Gatsby' by F. Scott Fitzgerald","'To Kill a Mockingbird' by Harper Lee"," 'Harry Potter and the Sorcerer's Stone' by J.K. Rowling",
      "'1984' by George Orwell","'The Catcher in the Rye' by J.D. Salinger","Every Other Harry Potter Book"," 'The Hobbit' by J.R.R. Tolkien",
      "'Fahrenheit 451' by Ray Bradbury"]
Lenders = {1:"sanket parmar",8:"krish" }
def see_option_again():
    print("1.to list of Book")
    print("2.To add new Book")
    print("3.To lend-Book")
    print("4.To retun Book")
    return "5.To exit"

while(1):
 l = len(list)
 print(see_option_again())
 i=0
 while(1):
    try:
        a = int(input("Type a number:"))
        while a > 5 or a < 1:
            print("Your input is not valid")
            a = int(input("Please insert again : "))
        break
    except ValueError:
        print("please Enter the numer")

 if a==1:

    for y  in list :
        i+=1
        print(i,y)
        print("unavelable books")
        for key, value in Lenders.items():
            s= int(key)-1
            print(f"{list[s]} taken by {value}")

 elif a==2:
    f = input("Please enter a Book Name:\n")
    list.append(f)
    for y in list:
        i += 1
        print(i, y)
 elif a==3:


    while (1):
        try:
            d = int(input("choice your book number "))
            while d > l or d < 1:
                print("Your input is not valid")
                d = int(input("Please insert again : "))
                continue
        except ValueError:
            print("")
        key = d
        if key in Lenders:
            print(f"book is alrady take by {Lenders[d]}")
            print("please try another books")
        else:
            n = input("Enter your name")
            Lenders.update({int(d): n})
            break

 elif a==4:
    while (1):
        try:
            d = int(input("print your return book number "))
            while d > l or d < 1:
                print("Your input is not valid")
                d = int(input("Please insert again : "))
                continue
        except ValueError:
            print("")
        for i in Lenders:
             if d==i:
                Lenders.pop(i)
                print("your boook is return successfuly")

                break
             else:
                print("invalid input , somthing is wrong")
                break


        break
 elif a==5:
     print("thank your for visit yovi's library")
     print("HAVE A NICEDAY")
     break