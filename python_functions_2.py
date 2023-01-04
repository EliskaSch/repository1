def string_upper_lower(s): #Ex. 4
    total={"uppercase_letters":0, "lowercase_letters":0}
    for letter in s:
        if letter.isupper():
            total["uppercase_letters"]+=1
        elif letter.islower():
            total["lowercase_letters"]+=1
    print("String:", s)
    print("Uppercase letters:", total["uppercase_letters"])
    print("Lowercase letters:", total["lowercase_letters"])

string_upper_lower("Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers, where’s the peck of pickled peppers Peter Piper picked?")


def meal_vouchers(lunch_cost, meal_voucher_value): #Ex. 5
    number_of_vouchers = lunch_cost//meal_voucher_value
    cash = lunch_cost - (number_of_vouchers * meal_voucher_value)
    print("Lunch cost", lunch_cost, "CZK")
    print("Pay in cash", cash, "CZK")
    print("Pay in meal vouchers", number_of_vouchers, "pcs,", meal_voucher_value, "CZK each")

meal_vouchers(500, 74)


def compute_factorial(x): #Ex. 6
    if x==1:
        return x
    else:
        return x*compute_factorial(x-1)

compute_factorial(10)