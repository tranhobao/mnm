my_string = input(" nhap chuoi")
def bai1(my_string):
    if my_string.isnumeric():
        print('The string is number only')
    else:
        print(my_string.lower())
        print(my_string.upper())
        print(my_string.title())
bai1(my_string)