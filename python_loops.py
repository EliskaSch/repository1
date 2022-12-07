alphabet = 'abcdefghijklmnopqrstuvwxyz' # Ex. 9
zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
set(alphabet).difference(set(zen))

d = {'payton':'An interpreted, object-oriented programming language'} # Ex. 10-a
d["python"] = d.pop("payton")

dictionary = {("name", "surname"):("telephone_number")} # Ex. 10-b

info = {('Name', 'Surname'):('John', 'Doe')} # Ex. 11
print("_".join(info[("Name", "Surname")]))

names_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef', 'Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav', 'Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal', 'Lenka', 'Katerina'] # Ex. 1
name = input()
if name in names_list:
    print("reply")
else:
    print("another reply")
    
spelling_alphabet = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu'} # Ex. 2
user_name = list(input()[::].lower())
for letter in user_name:
    for key, value in spelling_alphabet.items():
        if letter is key:
            print(value)
        else:
            continue

a = [[1,2,3], # Ex. 3-loops
[4,5,6],
[7,8,9]]
b = []
for x in range(3):
    b_row = []
    for row in a:
        b_row.append(row[x])
    b.append(b_row)

a = [[1,2,3], # Ex. 3-list comprehension
[4,5,6],
[7,8,9]]
b = [[row[x] for row in a] for x in range(3)]

shopping_list=["bread", "pasta", "milk", "salt"] # Ex. 4
item = input()
if item in shopping_list:
    print(item)
else:
    shopping_list.append(item)

numbers = list(range(5)) # Ex. 5
numbers_multiplied = [x * x for x in numbers]
favorite = " is my favorite number!"
favorite_number = [str(x) + favorite for x in numbers]
print(numbers_multiplied)
print(favorite_number)

scores = {'John' : 10, 'Emily' : 35, 'Matthew' : 50} # Ex. 7
scores_tripple = {key : value * 3 for key, value in scores.items()}