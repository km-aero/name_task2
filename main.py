from newusers_class import *
# read the txt file
# create 10 object from said file

user_list = []

with open('names.txt','r') as f:
    x = f.readlines()
    for i in x:
        user = NewUsers(i.rstrip('\n'))
        user_list.append(user)

print(user_list[3].name)
user_list[3].create_info_file()