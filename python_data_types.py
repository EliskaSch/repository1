1256983%28 #dedictvi

(((12**52)%15)<8) or ((3**5)>100) #overeni_matematickych_vysledku_1

(5*(3**3)) != (900/75) #overeni_matematickych_vysledku_2

"[[]]" [0:2:1] + "PYTHON" + "[[]]" [2:4:1] #baleni_do_zavorek

"Python" [4:6:1]*4 #mnozeni_pismen_1

"Perl" [2]*6 #mnozeni_pismen_2

"python" [0:3:1].upper() + "python" [3:6:1].lower() #hratky_s_retezci_1

"python" [0]*len("python") #hratky_s_retezci_2

"git" [0]*len("git") #hratky_s_retezci_3

print(7+3*2) #vyreseni_chyby_1 (I get 13)

print("7" + str(3*2)) #vyreseni_chyby_2 (I get 76)

print("7" + "3*2") #vyreseni_chyby_3 (I get 73*2)

print("7" + 3*2) #vyreseni_chyby_4 (I get an error because we are trying to add a string and a number)

hobby = "writing" #hobby_promenna
"My hobby is {0}".format(hobby)

hobbies = ["writing", "reading", "watching movies", "gaming", "math riddles", "painting"] #prace_se_seznamy
print(hobbies[0])
print(hobbies[-1])
del hobbies

cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec', 'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice'] #razeni_mest
cities.sort()
"*".join(cities)