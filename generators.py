# Document at least 3 use cases of generators

# Generators can be used to loop through a large files

# example 1
def sum_numbers(a):
    num = 0
    while num <= a:
        yield num
        num += 1

kk = sum_numbers(1000000000)

b = 0
for i in kk:
    a = i
    b += a
# print(b)


# example 2
def filter_multiple_numbers(a, b):
    for i in range(a):
        if i % b == 0:
            yield i
        
ff = filter_multiple_numbers(100000000, 7)

for i in ff:
    print(i)


# example 3

