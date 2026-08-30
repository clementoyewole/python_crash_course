# make a list of your favourite fruits
favourite_fruits = ['banana', 'apple', 'orange', 'carrot', 'pineapple']
# ask thr users for their favourite fruits
your_fruits = input("What's your favourite fruit? ").strip().lower()
# check if a certain fruits is in the list
if your_fruits in favourite_fruits:
    print(f"You really like {your_fruits.title()}!")
else:
    print(f"{your_fruits.title()} is a good fruit, but not on the list.")