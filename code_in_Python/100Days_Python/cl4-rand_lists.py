


# =======================================================================
# Day 4 Final
# Rock Paper Scissors
#
# import random
#
# rock = "⛰"
# paper = "🗒"
# scissors = "✀"
# c_map = [rock, paper, scissors]
#
# print(f' Welcome to a game of {rock} - {paper} - {scissors} ')
# user_choice = int(input(f'\nEnter a choice ( 0 = {rock}, 1 = {paper}, 2 = {scissors} ). '))
# computer_choice = random.randint(0, 2)
#
# if user_choice == computer_choice:
#     print(f'\n User Chose {c_map[user_choice]} and computer chose {c_map[computer_choice]} ')
#     print(" Result = Nobody Wins ")
# elif user_choice == 0 & computer_choice == 1:
#     print(f'\n User Chose {c_map[user_choice]} and computer chose {c_map[computer_choice]} ')
#     print(" Result = You Lose ")
# elif user_choice == 1 & computer_choice == 2:
#     print(f'\n User Chose {c_map[user_choice]} and computer chose {c_map[computer_choice]} ')
#     print(" Result = You Lose ")
# elif user_choice == 2 & computer_choice == 0:
#     print(f'\n User Chose {c_map[user_choice]} and computer chose {c_map[computer_choice]} ')
#     print(" Result = You Lose ")
# else:
#     print(f'\n User Chose {c_map[user_choice]} and computer chose {c_map[computer_choice]} ')
#     print(" Result = You Win ")


# =======================================================================
# Day 4 Exercise 3
# TODO: Make this a Full Fledged Game
# TODO: Check for Errors during input, make sure that the score stays after each tries.
# TODO: If All boxes are 'x' then Game is Over.

# def calc_pos(pos, t_map):
#     x = int(pos[0]) - 1
#     y = int(pos[1]) - 1
#     print(f'You Entered Positions {x + 1} & {y + 1}')
#     if x < 0 or x > 3 or y < 0 or y > 3:
#         print(" Position Values Should be between 0 and 3 ")
#     else:
#         t_map[x][y] = "x"
#         for val in t_map:
#             print(val)
#
# def init(row1, row2, row3):
#     t_map = [row1, row2, row3]
#     print(f'{row1}\n{row2}\n{row3}')
#     print(f'\nEnter Positions between 1-3 as (12 or 31) ')
#     position = input(" Where do you want to put the treasure? ")
#     calc_pos(position, t_map)
#
# def main():
#     row1 = ["⬜", "⬜", "⬜"]
#     row2 = ["⬜", "⬜", "⬜"]
#     row3 = ["⬜", "⬜", "⬜"]
#     init(row1, row2, row3)
#     again = int(input(f"\nPlay Again (0=No,1=Yes)? "))
#     if again:
#         main()
#     else:
#         print("Thank You ")
#
# if __name__ == "__main__":
#     main()

# =======================================================================
# Exercise 1:
# Generate Random numbers. 0 means Heads and 1 means Tails.
#
# import random
#
# def coin_toss():
#     if random.randint(0, 1):
#         print("Heads")
#     else:
#         print("Tails")
#
# def main():
#     coin_toss()
#
# if __name__ == "__main__":
#     main()

