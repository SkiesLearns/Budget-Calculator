"""
Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and
entertainment. These objects should allow for depositing and withdrawing funds from each category, as well computing
category balances and transferring balance amounts between categories
"""

import re

class Budget_App:

    def __init__(self, name, balance, savings: dict = {}):
        self.name = name
        self.balance = balance
        self.savings = savings

    def cat_budget(self):
        options = {
            'housing': 0.25,
            'insurance': 0.15,
            'transport': 0.1,
            'savings': 0.1,
            'personal': 0.05,
            'recreation': 0.05,
            'utilities': 0.1,
            'giving': 0.05
        }

        print(f"""Hey {self.name}! Once finished, type 'DONE'
===============================================================================
Please type which of the following you need to budget from our list.
{", ".join(options.keys()).title()}""")
        while True:
            user_choice = input(': ').lower()

            if user_choice == 'done':
                print('Budgeting calculated.')
                break
            else:
                user_cost = format(options[user_choice] * self.balance, '.2f')
                self.savings[user_choice] = float(user_cost)
                print(f'({user_choice.title()} added)')

    def show_budget(self):
        print(f"{self.name.title()}'s budget.")
        output = ""
        for item, amount in self.savings.items():
            output += f'\n{item.title()} | Budget recommended: £{amount}\n'.replace('_', ' ')
        print(output)

    def manage_budget(self):
        user_change = input('Please enter which part of your budget you wish to change\n: ')

        try:
            user_calc = input('Type \'ADD\' or \'REMOVE\' to change quantity: ').lower()
            if user_calc not in ['add', 'remove']:
                raise ValueError
            quantity = int(input(f'Enter how many you wish to {user_calc}: '))
            if user_calc == 'add':
                self.savings[user_change] += quantity
                print('Successfully added!')
            elif user_calc == 'remove':
                self.savings[user_change] -= quantity
                if self.savings[user_change] < 0:
                    self.savings[user_change] = 0
                    print(f'Insufficient, {user_change} set to £0.')
                else:
                    print('Successfully removed!')

        except KeyError:
            print("Input doesn't match provided categories.")
        except ValueError:
            print(f"Response required 'ADD' or 'REMOVE'")


def main():
    print('Welcome to my budgeting app!')
    while True:
        user_name = input('Enter your name: ').title()
        if not re.match("^[A-Za-z]*$", user_name):
            print("Only letters are allowed")
        else:
                break


    try:
        user_balance = int(input('Enter budget: '))
    except ValueError:
        print('Numbers only')

    budget = Budget_App(user_name, user_balance)
    budget.cat_budget()

    while True:
        user_decide = input("""===============================================================================
To display your recommended budget type 'SHOW'
To change how money is in one category type 'MANAGE'
To edit your categories for your budget type 'CAT'
To exit the budget app type 'EXIT'
: """).lower()
        if user_decide == 'exit':
            print('Closing...')
            break
        elif not user_decide == 'quit':
            action = getattr(budget, f'{user_decide}_budget')()


if __name__ == '__main__':
    main()

"""
Known bugs 
-
Successfully added prints 5* when adding. [ FIXED ]
-
When adding or subtracting value it adds or subtracts from all values. [ FIXED ] 
-
Subtract doesn't work [ FIXED ]
"""
