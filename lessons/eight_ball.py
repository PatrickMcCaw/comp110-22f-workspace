from random import randint

questions: str = input("Ask a yes/no question...")
response: int = randint(0, 2)

if response == 0:
    print("Yes, definitely")
elif response == 1:
    print("Ask a gain later")
elif response == 2:
    print("Sure, I guess")
else:
    print("My sources say no")
