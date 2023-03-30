import time

def register():
    name = input("please enter name: ")
    id = round(time.time())
    data = f'{id}:{name}\n'
    fileobj = open('users.txt','a')
    fileobj.write(data)
    fileobj.close()

def login():
    name= input("please enter user name: ")
    fileobj = open("users.txt", 'r')
    users = fileobj.readlines()
    for user in users:
        user_data= user.split(':')
        print(user_data)
        username = user_data[1].strip('\n')
        if username==name:
            print("===loged in")
            break
    else:
        print('---- user not found ')





def mainmenu():
    choice = input("please enter 1 for register , 2 for login: ")
    if choice=='1':
        register()
    elif choice=='2':
        login()

mainmenu()



# generate(4,5)
# [5,6,7,8]


# abdulrahman


