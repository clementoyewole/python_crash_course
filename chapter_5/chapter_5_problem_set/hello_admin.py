# create a list of users name plus admin
name = ['mubaraq', 'nina', 'james', 'janet', 'admin', 'clement']
# ask for the user name
user_name = input("What's your name? ").strip().lower()
# if admin in name print a special greeting
if user_name in name and user_name == "admin":
    print("Hello Admin, would you like to see status quotes?")
# if user_name on name and not admin print a message
elif user_name in name and user_name != "admin":
    print(f"Hello {user_name}, thank you for logging in again.")
# detect mistakes or intruders
else:
    print("You're not on the list... are you an intruder or you mispelled your name? ")