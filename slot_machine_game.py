# Python Slot Machine Game
import random
import time

# To Spin Row
def spin_row():
    # Declaring the list of symbols
    symbols = ['🍬', '🍓', '🏵️ ', '🧡', '❓']

    #Creating a list comprehension 
    # This will return a list of 3 random symbols from the symbols list
    # This is a more concise way to achieve the same result
    return [random.choice(symbols) for _ in range(3)]

# Count down wait before printing the row
def countdown(seconds): 
    while seconds > 0:
        print(f"{seconds}s", end='...')
        time.sleep(0.5)
        seconds -= 1
    print("\n")  # Print a new line after the countdown is complete


# To print row 
def print_row(row):
    print("-------------")  # Print a line for visual separation
    print(" | ".join(row))  # Join the symbols with a | and print them
    print("-------------\n")  # Print another line for visual separation

# If the user wins, they will get a payout
def get_payout(row, bet):
    # Check if all symbols in the row are the same
    if row[0] == row[1] == row[2]:
        if row[0] == '🍬':
            return bet * 3 # Payout for 3 candies
        
        elif row[0] == '🍓':
            return bet * 5 # Payout for 3 strawberries
        
        elif row[0] == '🏵️ ':
            return bet * 8 # Payout for 3 flowers
        
        elif row[0] == '🧡':
            print("Jackpot! You hit the orange hearts!")
            return bet * 15 # Payout for 3 orange hearts
        
        elif row[0] == '❓':
            return bet * 1 # Payout for 3 question marks
        
    return 0  # Return 0 if no payout condition is met (no win or mixed symbols)
        

# Main function 
def main():
    balance = 100 # Initial balance set to $100

    # Welcome message
    print("********************************************")
    print("  Welcome to the Python Slots Machine Game ")
    print("     Symbols: | 🍬 | 🍓 | 🏵️  | 🧡 | ❓ |")
    print("********************************************")

    # Game loop , player can play until they run out of balance
    while balance > 0:
        print(f"Current Balance: ${balance:.2f}")

        # Prompt user to place a bet
        bet = input("Place your bet: $ ")

        # Validate bet amount
        if not bet.isdigit():
            print("\nPlease enter a valid number.\n")
            continue
        
        # Type cast bet to float
        bet = float(bet)

        # Checking if bet more than balance
        if bet > balance:
            print("\n Insufficient funds!\n")
            continue
        
        # Check if bet is less than or equal to 0
        if bet <= 0:
            print("\nBet must be greater than 0.\n")
            continue

        # Deducting the bet from balance
        balance -= bet

        # Spinning the slot machine
        row = spin_row()
        print("\nSpinning...")

        # Countdown before showing the result
        countdown(3)

        # Print the row of symbols
        print_row(row)

        # Check if the player won
        payout = get_payout(row, bet)

        if payout > 0 :
            print(f"You won ${payout:.2f}!")
        else:
            print("Better luck next time!\n")
            if balance <= 0:
                print("You have run out of balance.\n")
                print("*****************************")
                print("\tGame Over")
                print("*****************************")
                break
        
        balance += payout

        # Ask the player if they want to play again
        play_again = input("Do you want to spin again? (Y/N): ")

        # Check if the player wants to continue
        if play_again.lower() != 'y':
            print("********************************************************")
            print(f"Thank you for playing! Your final balance is: ${balance:.2f}")
            print("********************************************************")
            break


# Creating the if __name__ == "__main__":
if __name__ == "__main__":
    main()  # Call the main function to start the game
