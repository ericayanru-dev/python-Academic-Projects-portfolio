"""
Author: Eric Ayanru
Course: CSE110
Project: Text-Based Adventure Game

Description:
A looping text adventure game where players choose between three mysterious doors—WOODEN, STONE, or IRON—
each leading to its own interactive storyline. Players make choices along the way to escape or face consequences.
"""

def wooden_path():
    print("\nWOODEN DOOR Path:")
    print("You step into a glowing forest. Rustling comes from nearby bushes.")

    print("\nChoices:")
    print("1. FOLLOW - Follow the glowing path.")
    print("2. INVESTIGATE - Check the noise in the bushes.\n")

    while True:
        choice = input("What will you do? ").strip().upper()
        print()
        if choice == "FOLLOW":
            print("You find an ancient sword. A shadowy figure appears! Do you FIGHT or RUN?")
            decision = input("What do you do? ").strip().upper()
            print("You win and escape!" if decision == "FIGHT" else "You run but get lost in the forest...")
            break
        elif choice == "INVESTIGATE":
            print("You find a wounded wolf. HELP or LEAVE it?")
            decision = input("What do you do? ").strip().upper()
            print("The wolf leads you to safety!" if decision == "HELP" else "You're left alone in the dark forest...")
            break
        else:
            print("Invalid input. Please choose FOLLOW or INVESTIGATE.")

def stone_path():
    print("\nSTONE DOOR Path:")
    print("You enter a dark cave. A golden chalice sits on a pedestal.")

    print("\nChoices:")
    print("1. TAKE - Try to take the chalice.")
    print("2. IGNORE - Leave it and explore deeper.\n")

    while True:
        choice = input("What will you do? ").strip().upper()
        print()
        if choice == "TAKE":
            print("The cave begins to collapse! Do you RUN or HOLD ON?")
            decision = input("What do you do? ").strip().upper()
            print("You escape but lose the chalice." if decision == "RUN" else "You are buried under the rocks...")
            break
        elif choice == "IGNORE":
            print("You find an ancient door with a riddle. SOLVE it or FORCE it?")
            decision = input("What will you do? ").strip().upper()
            print("You unlock a hidden treasure!" if decision == "SOLVE" else "You trigger a trap and get stuck...")
            break
        else:
            print("Invalid input. Please choose TAKE or IGNORE.")

def iron_path():
    print("\nIRON DOOR Path:")
    print("You find a futuristic lab with robotic arms and a central computer.")

    print("\nChoices:")
    print("1. TRY - Try to hack the computer.")
    print("2. SEARCH - Look around the room.\n")

    while True:
        choice = input("What do you do? ").strip().upper()
        print()
        if choice == "TRY":
            print("Alarm triggered! Do you HIDE or ESCAPE?")
            decision = input("What do you do? ").strip().upper()
            print("You hide and escape safely!" if decision == "HIDE" else "Security bots catch you...")
            break
        elif choice == "SEARCH":
            print("You find a journal. READ or IGNORE it?")
            decision = input("What do you do? ").strip().upper()
            print("You find the password and escape!" if decision == "READ" else "You miss the key to escape...")
            break
        else:
            print("Invalid input. Please choose TRY or SEARCH.")

def main():
    while True:
        print("\nYou wake up in a mysterious underground dungeon with three doors in front of you.")
        print("\nChoices:")
        print("1. WOODEN - Enter the wooden door.")
        print("2. STONE - Enter the stone door.")
        print("3. IRON - Enter the iron door.")
        print("4. EXIT - Exit the game.\n")

        door = input("Which door do you pick? ").strip().upper()

        if door == "WOODEN":
            wooden_path()
        elif door == "STONE":
            stone_path()
        elif door == "IRON":
            iron_path()
        elif door == "EXIT":
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid input. Please enter WOODEN, STONE, IRON, or EXIT.")

if __name__ == "__main__":
    main()
