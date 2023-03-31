from datetime import date

# initializing constructor
# and passing arguments in the
# format year, month, date
# my_date = date(1996, 12, 11)
#
# print("Date passed as argument is", my_date)
""" date in python """
# from datetime import date
# while True:
#     date_components = input('Enter a date formatted as YYYY-MM-DD: ')
#     print(date_components)   # string
#
#     date_components = date_components.split('-')
#     print(date_components)
#     try:
#         startdate= date(int(date_components[0]), int(date_components[1]), int(date_components[2]))
#         print(startdate)  # valid date
#         break
#     except Exception as e:
#         print(e)
#         print("not valid date please enter it again ")

""" egyptian phone number """
import re

# def ask_for_phone_number():
#     pattern = r"^01[0125][0-9]{8}$"
#     while True:
#         phone= input('please enter phone number: ')
#         if re.match(pattern, phone):
#             print("valid phone")
#             return phone
#         else:
#             print("not valid -- please enter it a gain ")
#
#
# p = ask_for_phone_number()
# print(p)



""" edit delete project """

def get_all_books():
    fileobj = open("books.txt", 'r')
    books = fileobj.readlines()
    fileobj.close()
    return books


def save_all_books(books):
    fileobj = open("books.txt", 'w')
    fileobj.writelines(books)
    fileobj.close()
    return True


def delete_book():
    id = input("please enter book_id")
    ## check if the book in books.txt
    books = get_all_books()
    for index, book in enumerate(books):
        book_details = book.strip('\n')
        book_details = book_details.split(':')
        if book_details[0]==id and book_details[4]=="1":
            selected_book = index
            break
    else:
        print("====> book not found , or you are not authoriezed to book -===")
        return

    del books[selected_book]  # delete book from the books list
    # print(books)
    deleted = save_all_books(books)
    if deleted:
        print("====> books deleted successfully ====")




delete_book()






