message = input("Your name? ").strip().title()
print(message)

message = input("Who's the president of nigeria? ").strip().title()
if message.startswith("Tinubu"):
    print("Correct!")
elif message.startswith("Bola"):
    print("Correct!")
elif message.startswith("Ahmad"):
    print("Correct!")
elif message.startswith("Bola Ahmad Tinubu"):
    print("Correct!")
else:
    print("Wrong!")