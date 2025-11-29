import random
class BoggleBoard:
  
    def __init__(self):
        print('Welcome the the fantastic game of Boggle!')
        print("""
    ____\n
    ____\n
    ____\n
    ____\n""")
    def dice_picker(self):
        dice_list = []
        dice = 
        for i in dice_list:
            dice_list.append(i, ",")
        print(dice_list)

    def shake(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for i in range(4):
            print(''.join(random.choices(alphabet, k=4)))
       


boggle_game1 = BoggleBoard()
boggle_game1.shake()
boggle_game1.dice_picker()