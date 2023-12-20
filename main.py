
import random


alphabets= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols= ('''+    -    *    **    /    //    %    <<    >>   &    |
^    ~    <     >    <=   >=    ==   !=    <>   +=
-=   *=   /=   //=   %=   **=   &=   |=    ^=   >>=  <<= ''').split()

print(symbols)

numbers =("1", "2", "3", "4" , "5", "6", "7", "8", "9", "0")
print(numbers)

print("Welcome to the password generator. ")

password= " "
my_letters= int(input("How many letters would you like to have ?\n"))
my_symbols= int(input("How many symbols would you like to have ?\n"))
my_numbers= int(input("How many numbers would you like to have ?\n"))

for char in range(0, my_letters+1):
    password+=random.choice(alphabets)

for char in range(0, my_symbols+1):
    password+=random.choice(symbols)  

for char in range(0, my_numbers+1):
    password+=random.choice(numbers)

print(password)
