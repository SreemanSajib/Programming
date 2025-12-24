import random
random.seed(1234)

# ASCII art for the choices
ROCK_ART = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER_ART = r"""
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS_ART = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

HASH_LINE = "#" * 25


def choice_name(choice: int) -> str:
    if choice == 1:
        return "rock"
    if choice == 2:
        return "paper"
    if choice == 3:
        return "scissors"
    return "unknown"


def choice_art(choice: int) -> str:
    if choice == 1:
        return ROCK_ART
    if choice == 2:
        return PAPER_ART
    if choice == 3:
        return SCISSORS_ART
    return ""


def get_player_choice() -> int:
    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")
        choice_str = input("Your choice: ")
        try:
            choice = int(choice_str)
        except ValueError:
            print("Unknown option.")
            continue

        if choice in (0, 1, 2, 3):
            return choice
        else:
            print("Unknown option.")


def play_round(player_name: str,
               stats_player: dict,
               stats_bot: dict) -> bool:
    """Play one round. Return False if player chose to quit."""
    choice = get_player_choice()
    if choice == 0:
        return False

    bot_choice = random.randint(1, 3)

    print("Rock! Paper! Scissors! Shoot!\n")

    player_name_choice = choice_name(choice)
    bot_choice_name = choice_name(bot_choice)

    # Player choice display
    print(HASH_LINE)
    print(f"{player_name} chose {player_name_choice}.")
    print(choice_art(choice))
    print(HASH_LINE)
    print(f"RPS-3PO chose {bot_choice_name}.")
    print(choice_art(bot_choice))
    print(HASH_LINE)

    # Decide winner
    if choice == bot_choice:
        print(f"Draw! Both players chose {player_name_choice}.")
        stats_player["draws"] += 1
        stats_bot["draws"] += 1
    else:
        # winning combinations for player
        player_wins = (
            (choice == 1 and bot_choice == 3) or  # rock beats scissors
            (choice == 2 and bot_choice == 1) or  # paper beats rock
            (choice == 3 and bot_choice == 2)     # scissors beat paper
        )
        if player_wins:
            print(f"{player_name} {player_name_choice} "
                  f"beats RPS-3PO {bot_choice_name}.")
            stats_player["wins"] += 1
            stats_bot["losses"] += 1
        else:
            print(f"RPS-3PO {bot_choice_name} "
                  f"beats {player_name} {player_name_choice}.")
            stats_bot["wins"] += 1
            stats_player["losses"] += 1

    print()  # blank line before next menu
    return True


def main() -> None:
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")

    player_stats = {"wins": 0, "losses": 0, "draws": 0}
    bot_stats = {"wins": 0, "losses": 0, "draws": 0}

    while True:
        if not play_round(player_name, player_stats, bot_stats):
            break

    # Show final results
    print("Results:")
    print(f'{player_name} - wins ({player_stats["wins"]}), '
          f'losses ({player_stats["losses"]}), '
          f'draws ({player_stats["draws"]})')
    print(f'RPS-3PO - wins ({bot_stats["wins"]}), '
          f'losses ({bot_stats["losses"]}), '
          f'draws ({bot_stats["draws"]})')
    print("\nProgram ending.")


if __name__ == "__main__":
    main()
