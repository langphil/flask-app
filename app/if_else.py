#not - is evaluated first
#and - is evaluated second
#or - is evaluated third

def first(number):
    if number == 2:
        return "First!"
    elif number == 0:
        return "Second!"
    else:
        return "Third!"

print first(2)
print first(0)
print first(3)
