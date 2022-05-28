import inflect
p= inflect.engine()

names = []
while True:
    try:
        name = input ("Name: ")
        names.append(name)
    except E0FError:
            print()
            break
output = p.join(names)
print("Adieu, adieu, to " + output)
