"""
Author: Eric Ayanru
Course: CSE110
Project: Loan Qualification Decision Maker

Description:
This program simulates a simplified loan qualification process based on user-rated inputs:
loan size, credit history, income, and down payment. Based on preset rules, it determines
whether or not a loan should be approved.
"""

def main():
    print("Loan Qualification Checker")
    print("Rate each category from 1 (low) to 10 (high).")

    # Get user ratings
    loan = float(input("Loan size rating (1–10): "))
    credit = float(input("Credit history rating (1–10): "))
    income = float(input("Income level rating (1–10): "))
    payment = float(input("Down payment rating (1–10): "))
    print()

    should_loan = False

    # Decision logic
    if loan >= 5:
        if credit >= 7 and income >= 7:
            should_loan = True
        elif credit >= 7 or income >= 7:
            should_loan = payment >= 5
    else:  # loan < 5
        if credit < 4:
            should_loan = False
        elif income >= 7 or payment >= 7:
            should_loan = True
        else:
            should_loan = False

    # Output decision
    if should_loan:
        print("The decision is YES — This is a good loan.")
    else:
        print("The decision is NO — You should not loan this money.")

if __name__ == "__main__":
    main()