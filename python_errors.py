seasons = ['Spring', 'Summer', 'Fall', 'Winter'] # Ex. 1
print('My favorite season is ', seasons[3])

for number in range(10): # Ex. 2
 # use a if the number is a multiple of 3, otherwise use b
 if (number % 3) == 0:
   message = "message" + "a"
 else:
   message = "message" + "b"
print(message)

name = input() # Ex. 3
for letter in name:
    if letter.isdigit():
        raise Exception ("Contains number")
for letter in name:
    if letter == " ":
        raise Exception ("Has spaces")
if name[0].islower():
    raise Exception ("Does not start with uppercase letter")
    
def division(): # Ex. 4
    x = input()
    while not x.isdigit():
        print("Type integer")
        x = input()
    y = input()
    while not y.isdigit() or int(y) == 0:
        print("Type number again until number is not 0")
        y = input()
    z = int(x)/int(y)
    print(z)
division()
    
year = int(input("Greetings! What is your year of origin?")) # Ex. 5
if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")