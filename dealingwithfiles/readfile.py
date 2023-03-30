

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
""" read data from the file """
try:
    fileobj =open("mycv.txt", 'r')
except Exception as e:
    print(e)
else:
    print(fileobj)  # TextIOWrapper ===> you use it to read the content from the file
    "# read file content from the begining into one string "
    # data = fileobj.read()  # read file content from the begining into one string
    # print(data)
    "read file content line by line "
    # line =fileobj.readline()
    # print(line)
    # line = fileobj.readline()
    # print(line)
    'read file lines -> all'
    # lines = fileobj.readlines()  # detect \n at the end of the string
    # print(lines)
    'loop over the fileobj '
    for l in fileobj:
        print(l)


    data= fileobj.read()
    print(f"data=#{data}#")

    fileobj.seek(0)
    data = fileobj.read()
    print(f"data=#{data}#")















