'''
  MASSIVE TODO: Pytermgui
                from pynput import keyboard

  TODOs:
  - special characters
  - control characters
  - input() is slow and needs enter, switch to pynput
  - Practice wrong keystrokes concept (more info in readme)
'''

import random

fingers = {
    "left_pinky", "left_ring", "left_middle", "left_pointer", "left_thumb", 
    "right_pinky", "right_ring", "right_middle", "right_pointer", "right_thumb"
}

key_mappings = {
    "left_pinky":['1','q','a','z'],
    "left_ring":['2','w','s','x'],
    "left_middle":['3','e','d','c'],
    "left_pointer":['4','r','f','v','5','t','g','b','5','t','g','b'],
    "left_thumb":['space'],
    "right_pinky":['0','p'],
    "right_ring":['9','o','l'],
    "right_middle":['8','i','k'],
    "right_pointer":['7','u','j','m','6','y','h','n'],
    "right_thumb":['space'],
}


def welcome():
  print("Welcome to finger Whack A Mole!\n\n")

def show_keyset(finger):
  print(f"Mole Whacker Finger: {finger}")
  moles = key_mappings.get(finger,[])
  print("Moles: " + ','.join(moles))
  print("goodLuck! ------------------------------\n")

def practice_keyset(finger):
  for i in range(15):
    moles = key_mappings.get(finger, [])
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
