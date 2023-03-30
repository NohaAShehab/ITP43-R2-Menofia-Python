

"""
    simple text file -->

    1- open file  ---> open(filename :str, mode)
    mode ['r', 'w' , 'a']
    r --> read content from the file --> from the begining of the file
    w --> write data from the beginning of the file ---> if file contains data --> remove it
    a --> write data to the file ---> data --> at the end of the file --->
        if file contains -->keep old content

    2- do operation read/write
    --> read . readlines
    --> write .. writelines

    3- close file

"""
""" write data to the file """
" when you open file with write mode ---> file doesn't exist --> try to create "
# try:
#     fileobj =open("students.txt", 'w')
# except Exception as e:
#     print(e)
# else:
#     print(fileobj)
#     # fileobj.write('Ahmed\n')
#     # fileobj.write('Ali')
#     fileobj.writelines(['Ahmed\n', 'Ali\n', 'Mohamed'])  # write iterable
#     fileobj.close()



try:
    fileobj =open("names.txt", 'a')
except Exception as e:
    print(e)
else:
    print(fileobj)
    # fileobj.write('Ahmed\n')
    # fileobj.write('Ali')
    fileobj.writelines(['Ahmed\n', 'Ali\n', 'Mohamed\n'])  # write iterable
    fileobj.close()












