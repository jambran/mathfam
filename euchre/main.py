from data_structures.player import Player
from data_structures.round import Round


def main():
    print('starting a game of euchre')
    print("Please input the names of the 4 players. Player 1 and 3 will be on a team,"
          "and likewise with players 2 and 4.")
    player1_name = input("What is Player 1's name?")
    player2_name = input("What is Player 2's name?")
    player3_name = input("What is Player 3's name?")
    player4_name = input("What is Player 4's name?")
    players = [Player(player1_name),
               Player(player2_name),
               Player(player3_name),
               Player(player4_name),
               ]

    print(f'We have {player1_name} and {player3_name} on one team,'
          f'{player2_name} and {player4_name} on the other!')

    # option to do "deal goes to the first black jack here?

    play_again = True
    while play_again:
        round = Round(players)
        winners = round.play()
        print(f"Congrats to our winning team, {winners}!\n")

        response = input('Would you like to play again? [y/n]')
        play_again = response.lower().startswith('y')

    names = ','.join([str(player) for player in players])
    print(f'Thanks for playing, {names}!')


if __name__ == '__main__':
    main()
