# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    #separator
    print("-" * 60)

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Please enter the balance for Savings Account: "))
    savings_interest = float(input("Please enter the Interest Rate for Savings Account: "))
    savings_maturity = int(input("Please enter the number of months for Savings Account: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Interest earned on Savings Account: ${savings_interest_earned:.2f}")
    print(f"Updated Savings Account balance: ${updated_savings_balance:.2f}")

    #separator
    print("-" * 10)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Please enter the balance for CD Account: "))
    cd_interest = float(input("Please enter the Interest Rate for CD Account: "))
    cd_maturity = int(input("Please enter the number of months for CD Account: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Interest earned on CD Account: ${cd_interest_earned:.2f}")
    print(f"Updated CD Account balance: ${updated_cd_balance:.2f}")
    
    #separator
    print("-" * 60)

if __name__ == "__main__":
    # Call the main function.
    main()
