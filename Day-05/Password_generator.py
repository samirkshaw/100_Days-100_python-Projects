import random

lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
             "n","o","p","q","r","s","t","u","v","w","x","y","z"]

uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
             "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

numbers   = ["0","1","2","3","4","5","6","7","8","9"]

symbols   = ["!","@","#","$","%","^","&","*","(",")","_","-",
             "+","=","?","/","<",">","."]
nr_lowercase = int(input("How many lowercase letters? "))
nr_uppercase = int(input("How many uppercase letters? "))
nr_numbers   = int(input("How many numbers? "))
nr_symbols   = int(input("How many symbols? "))

password = []
password += random.choices(lowercase, k=nr_lowercase)
password += random.choices(uppercase, k=nr_uppercase)
password += random.choices(numbers,   k=nr_numbers)
password += random.choices(symbols,   k=nr_symbols)

random.shuffle(password)
final_password = "".join(password)
print(f"Your password is {final_password}")

