'''
  MASSIVE TODO: Pytermgui
                from pynput import keyboard

  TODOs:
  - special characters
  - control characters
  - input() is slow and needs enter, switch to pynput
  - Practice wrong keystrokes concept (more info in readme) [Almost done]
'''

import random

fingers = {
    "left_pinky", "left_ring", "left_middle", "left_pointer", "left_thumb", 
    "right_pinky", "right_ring", "right_middle", "right_pointer", "right_thumb"
}

# Add special characters
key_mappings = {
    "left_pinky":['1','q','a','z'],
    "left_ring":['2','w','s','x'],
    "left_middle":['3','e','d','c'],
    "left_pointer":['4','r','f','v','5','t','g','b'],
    "left_thumb":[' '],
    "right_pinky":['0','p'],
    "right_ring":['9','o','l'],
    "right_middle":['8','i','k'],
    "right_pointer":['7','u','j','m','6','y','h','n'],
    "right_thumb":[' '],
}


def welcome():
    print("Welcome to finger Whack A Mole!\n\n")

def show_keyset(finger):
    print(f"Mole Whacker Finger: {finger}")
    moles = key_mappings.get(finger,[])
    print("Moles: " + ','.join(moles))
    print("goodLuck! ------------------------------\n")

def practice_keyset(finger):
    missed_moles = []
    moles = key_mappings.get(finger, [])
    last_mole = moles[0]
    for i in range(15):
        visible_mole = moles[random.randint(0,(len(moles) - 1))]
        while visible_mole == last_mole:
            visible_mole = moles[random.randint(0,(len(moles) - 1))]
        last_mole = visible_mole
        print("mole: " + visible_mole)
        whack = str(input()) # Update after keypress detection implemented
        if whack == visible_mole:
            print("SCORE!")
        else:
            missed_moles.append(visible_mole)
            print("Mole Wins")
    if len(missed_moles) != 0:
        practice_keystroke(moles, missed_moles.pop())

def practice_keystroke(moles, practice_mole):
    for i in range(15):
        print("practice mole: " + practice_mole)
        whack = str(input())
        if whack == practice_mole:
            print("SCORE!")
        else:
            print("PracticeMore!")
            i -= 1
        visible_mole = moles[random.randint(0,(len(moles) - 1))]
        while visible_mole == practice_mole:
            visible_mole = moles[random.randint(0,(len(moles) - 1))]
        print("mole: " + visible_mole)
        whack = str(input())
        if whack == visible_mole:
            print("SCORE!")
        else:
            print("Mole Wins")


if __name__ == "__main__":
    welcome()
    for finger in fingers:
        show_keyset(finger)
        practice_keyset(finger)
    # goodbye()
