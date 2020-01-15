import functools
# Document at least 3 use cases of the * and ** operators

# * and ** can be used for unpacking


# Used case 1
# It can be used to get the middle items, i.e, items in the 
# list excluding the first and last
list_of_languages = ["Javascript", "python", "Java", "C"]
a, *b, _ = list_of_languages 
print(b)
print(a)
print(_)

# It can also be used to get all items, excluding the specified
# exclude the first and print the rest
x, *remaining = list_of_languages
print(remaining)

# just print the last item
*remaining, d = list_of_languages
print(d)

# They can also be used to tell python to accept any specific number of arguament 
# and name arguament
def add(*args, **kwargs):
    return args * 3

# It can be use to split a string
kk = "kingsley"
split_kings = [*kk]
print(split_kings)


# add all the digits of a number together
num = 12345
split_num = [*str(num)]
mapp = functools.reduce(lambda a, b: int(a) + int(b), split_num)
print(mapp)


# **
# sum all the values of the name arguments
def sum_kwargs(**kwargs):
    cont = []
    for key, value in kwargs.items():
        cont.append(value)
    return sum(cont)

kk = sum_kwargs(kk = 12, name = 13, loan = 3000000)
print(kk)

