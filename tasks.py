



# no_of_items = int(input("please enter number: "))
#
# print(no_of_items)
#
# no_of_items = input("please enter number: ")
# if no_of_items.isdigit():
#     no_of_items= int(no_of_items)
#     print(no_of_items)
# else:
#     print("--- please enter valid number.")

################################################

## vowels

message = 'nIce to meet you'

# no_of_vowels=0
# for char in message.lower():
#     if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
#         no_of_vowels +=1
#     print(f"char = {char}")
#
#
# print(f"no of vowels = {no_of_vowels}")

no_of_vowels=0
breif_version=''
for char in message.lower():
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        no_of_vowels +=1
    else:
        breif_version +=char



print(f"no of vowels = {no_of_vowels}")
print(f"string after removing vowels = {breif_version}")












