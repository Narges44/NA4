from datetime import date

#first name /  last name /  national_code /  date of birth / address / library register code 
# add people
def add1 () :
    national_cood = input (" national_cood :    ")
    if national_cood not in libarys.keys() :
        first_name = input (" first_name :    ")
        last_names = input (" last_name :     ")
        date_of_birth= input (" date_of_birth :    ")
        address = input (" address :     ")
        libary_register_cood  ="s"+ national_cood
        registery_date = date.today()
        libary= {
            "first_name" : first_name,
            "last_names" : last_names,
            "national_cood" : national_cood,
            "date_of_birth" : date_of_birth,
            "address" : address,
            "libary_register_cood" :  libary_register_cood ,
            "registery_date" : registery_date 
        }
        libarys[national_cood ] = libary
    else:
        print (f"{ national_cood  } : exist !! " ) 
            

#display
def display1 ():
    for key , value in libarys.items ():
        print (key)
        for x,y in value.items():
            print (f"{x} ----- {y}")

#remove
def remove1 (national_cood) :
    for i in national_cood:
        if  i  in libarys.keys ():
            libarys.pop(i)
        else :
            print (f"{ i } : not found !! " )  


#edit
def edit(national_cood):
    for i in national_cood:
        if i in libarys.keys():
            national_cood=input("new national_cood:")
            if national_cood not in libarys.keys():
                first_name = input (" first_name :    ")
                last_names = input (" last_name :     ")
                date_of_birth= input (" date_of_birth :    ")
                address = input (" address :     ")
                libarys["national_cood"]=first_name or libarys["national_cood"]
                libarys["first_name"]=first_name or libarys["first_name"]
                libarys["last_names"]=first_name or libarys["last_names"]
                libarys["date_of_birth"]=first_name or libarys["date_of_birth"]
                libarys["address"]=first_name or libarys["address"]
                print("edited")
            else:
                print("not found")
                

        
#help
def help1 ():
        print(" add ------ you can add national_code and according to add the rest of the specifications and become a member of the libary . ")
        print (" remove ------ you can remove national_code and the rest of the specifications  .")
        print (" edit ------ you can edit your all specifications. ")
        print (" display ------ you can show all specifications. ")
        print (" exit ------ you can exit this program whenever you want. ")
        
        

#book
#add_book
def add () :
    cood_book = input (" cood_book :      ")
    if cood_book not in libarysp.keys() :
        names_of_book = input (" names_of_book :    ")
        names_writer = input (" name_writer :     ")
        year_of_publication= input (" year_of_publication:    ")
        field_of_book = input ("field_of_book :     ")
        
        libary= {
            "names_of_book" : names_of_book ,
            "names_writer" : names_writer ,
            "year_of_publication" : year_of_publication ,
            "field_of_book" : field_of_book ,
        
        }
        libarysp[cood_book ] = libary
    else:
        print (f"{ cood_book  } : exist !! " )


#remove
def remove (cood_book) :
    for i in cood_book:
        if i in libarysp.keys ():
            libarysp.pop(i)
        else :
            print (f"{ i } : not found !! " )


#display
def display ():
    for key , value in libarysp.items ():
        print (key)
        for x,y in value.items():
            print (f"{x} ***** {y}")
    

#edit
def edit(cood_book):
    for i in cood_book :
        if i  in libarys.keys():
            names_of_book = input (" names_of_book :    ")
            names_writer = input (" name_writer :     ")
            year_of_publication= input (" year_of_publication:    ")
            field_of_book = input ("field_of_book :     ")
            libarys["names_of_book"]=first_name or libarys["names_of_book"]
            libarys["names_writer"]=first_name or libarys["names_writer"]
            libarys["year_of_publication"]=first_name or libarys["year_of_publication"]
            libarys["field_of_book"]=first_name or libarys["field_of_book"]
            print("edited")
        else:
            print("not found")


                              
#search
def search():
    user = input (" search for name /// field  ???     ")
    if user == "name" :
        p = input ("name    " )
        if p in libarysp.keys ():
            q = {}
            q = libarysp[p]
            print (q)
        else :
            print (f"{ p } : not found !! " )
    elif user == "field":
        k = input ("field      " )
        if k in libarysp.keys():
            z = {}
            z = libarysp[k]
            print (z)
        else:
            print (f"{ k } : please look carefully ):  !! " )
    else:
        print (f"{ coment } : not found !! " )


        

#help
def help ():
        print(" add ------ you can add book and the specifications (:  ")
        print (" remove ------ you can remove book and the specifications  .")
        print (" edit ------ you can edit your all specifications. ")
        print (" borrow ------ you can see who borrowed this book .  ")
        print (" display ------ you can show all specifications. ")
        print (" search ------ you can search as code_book or libary_cood_book . ")
        print (" exit ------ you can exit this program whenever you want. ")


#borrow
def borrow ():
    u = input(" cood_book ?    ")
    if u in libarysp :
        user2 = input (" national_cood of borrow ?     ")
        if user2 in libarys :
            user3 = input (" date of lending ?      ")
            user4 = input (" a went after date of lending !       ")
            print (" you can borrow a book :)    ")
        else:
            print (" sorry baby , we can not lending :)  ")
    elif user not in libarysp :
        print (f'{user} : not in labary ')
    else :
        print (f"{user} : not found ")



while True :
    user = input(" human or book ???? or exit ???  or borrow ???    ")
    if user == "borrow" :
        borrow()
    elif user == "human" :
        libarys = {}
        while True :
            user = input (" add , remove , edit , help , exit ,display , delit   ")
            if user == "add":
                add1()
            elif user == "remove":
                display()
                national_cood=input("enter a number:")
                national_cood=national_cood.split()
                remove1(national_cood)
            elif user == "edit":
                display()
                national_cood=input("enter a number:")
                national_cood=national_cood.split()
                edit1(national_cood)
            elif user == "help":
                help1()
            elif user == "":
                pass
            elif user == "exit":
                break
            elif user == "display":
                display1()
            else :
                print (f"{user} : command not found !!!! ")
    elif user == "book" :
        libarysp = {}
        while True :
            user = input (" add , remove , edit , search , help , exit ,display   ")
            if user == "add":
                add()
            elif user == "remove":
                display()
                cood_book=input("number:")
                cood_book=cood_book.split()
                remove(cood_book)
            elif user == "edit":
                display()
                cood_book=input("number:")
                cood_book=cood_book.split()
                edit(cood_book)
            elif user == "search":
                search()
            elif user == "help":
                help()
            elif user == "":
                pass
            elif user == "exit":
                break
            elif user == "display":
                display()
            else :
                print (f"{user} : command not found !!!! ")
    elif user == " " :
        pass
    elif user == "exit" :
        break
    else:
        print (f"{user} : command not found !!!! ")
        
