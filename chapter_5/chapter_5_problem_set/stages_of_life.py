# ask the user for their age
person_age = int(input("How old are you? "))

if person_age < 2:
    print("You're a baby.")
elif person_age < 4:
    print("You're a toddler.")
elif person_age < 13:
    print("You're a kid.")
elif person_age < 20:
    print("You're a teenager.")
elif person_age < 65:
    print("You're an adult.")
else:
    print("You're an elder.")