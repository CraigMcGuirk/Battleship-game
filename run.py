import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

#  Needs to be fixed


def get_slot_machine_spin():
    symbol_count = {
        "A": 2,
        "B": 4,
        "C": 6,
        "D": 8
    }
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

# 1


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if not amount.isdigit():
            print("Please enter a number.")
            continue

        amount = int(amount)
        if amount <= 0:
            print("Amount must be greater than 0.")
            continue  
        
        return amount

# 3


def get_number_of_lines():
    while True:
        lines = input(
            "How many lines would like to bet on (1-" + str(MAX_LINES) + ")? ")
        if not lines.isdigit():
            print("Please enter a number.")
            continue

        lines = int(lines)

        if 1 > lines > MAX_LINES:
            print("You must enter a valid number of lines.")
            continue
           
        return lines

# 4


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if not amount.isdigit():
            print("Please enter a number.")
            continue

        amount = int(amount)

        if MIN_BET > amount > MAX_BET:
            print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")   
            continue
                
        return amount
        

# 5


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                "You do not have enough to bet that amount,"
                f"your current balance is: ${balance}")
            break

    print(
        f"You are betting ${bet} on {lines} lines." 
        f"Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin()
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:{winning_lines}")
    return winnings - total_bet


# 2


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()