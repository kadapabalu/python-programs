import random
while True:
    input("Press Enter to roll the dice")
    print("Dice:", random.randint(1, 6))
    if input("Roll again? (y/n): ").lower() != "y":
        break
