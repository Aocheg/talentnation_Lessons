# TIER 2 — FIELD EXERCISE: ALGORITHM THINKING

## Project: The Digital Translator

### 1. Understanding the Problem

The problem is to design clear, ordered instructions for an ATM so that a customer can withdraw money from their bank account.

The ATM must check each requirement before proceeding with a withdrawal and respond correctly when something goes wrong.

### 2. Understanding Important Terms

- **Problem:** The task that needs to be solved. In this exercise, the customer wants to withdraw money from their bank account.
- **Algorithm:** A sequence of ordered steps and decisions used to solve a problem.
- **Program:** The actual code written in a programming language to make a computer execute an algorithm.

An algorithm is the plan, while a program is the coded implementation of that plan.

### 3. ATM Withdrawal Algorithm

**START**

1. Ask the customer to insert their ATM card.
2. Attempt to read the card.
3. If the ATM cannot read the card, display: "Unable to read card. Please remove your card and try again."
4. Return the card if possible and end the session.
5. If the card is readable, check whether it is valid.
6. If the card is invalid, display an appropriate error message and end the session according to the bank's security policy.
7. If the card is valid, request the customer's PIN.
8. Verify the PIN through the bank's authentication system.
9. If the PIN is incorrect, display: "Incorrect PIN. Please try again."
10. Allow another attempt while the permitted attempt limit has not been reached.
11. If the maximum number of attempts is reached, block or retain the card according to the bank's security policy and end the session.
12. If the PIN is correct, allow the customer to select the withdrawal option.
13. Request the withdrawal amount.
14. Validate that the requested amount is greater than zero and is a valid withdrawal amount.
15. Retrieve the customer's available account balance.
16. Compare the requested withdrawal amount with the available balance.
17. If the requested amount exceeds the available balance, reject the withdrawal and display: "Insufficient balance."
18. Do not deduct any money from the customer's account.
19. Allow the customer to enter another amount or cancel the transaction.
20. If the account balance is sufficient, check whether the ATM has enough physical cash in suitable denominations.
21. If the ATM does not have enough cash, reject the withdrawal and display: "Unable to dispense the requested amount. Please try a smaller amount or use another ATM."
22. Do not debit the customer's account for a withdrawal that cannot be dispensed.
23. If both the account balance and ATM cash are sufficient, send the withdrawal request to the bank for authorisation.
24. Wait for confirmation from the bank.
25. If the bank declines the transaction, do not dispense cash and display an appropriate error message.
26. If a network failure occurs before confirmation is received, do not dispense cash.
27. Record the transaction as pending or having an unknown outcome.
28. When communication is restored, check the transaction status with the bank using its transaction reference.
29. If the bank confirms that the account was debited but no cash was dispensed, follow the bank's reversal or reconciliation procedure.
30. If the bank confirms that the transaction is authorised, instruct the ATM to dispense the requested cash.
31. Check whether the cash dispenser successfully dispensed the money.
32. If cash dispensing fails after the account was debited, record the failure and follow the bank's reversal or reconciliation procedure.
33. If cash is successfully dispensed, display: "Please take your cash."
34. Offer the customer a receipt.
35. Return the ATM card if it has not already been returned.
36. End the session.

**END**

### 4. Handling the Five Required Failure Conditions

#### A. ATM Cannot Read the Card

The ATM should not request the PIN if it cannot read the card information needed to identify and process it.

It should display an error message, return the card where possible, and end the session.

#### B. Incorrect PIN

The ATM should reject the authentication attempt and display:

"Incorrect PIN. Please try again."

The customer may try again while the permitted attempt limit has not been reached.

If the maximum number of attempts is reached, the ATM should follow the bank's security policy.

#### C. Insufficient Account Balance

The ATM should compare the requested withdrawal amount with the customer's available account balance.

If the requested amount is greater than the available balance:

- Reject the withdrawal.
- Display an insufficient balance message.
- Do not deduct money.
- Allow the customer to enter a different amount or cancel.

#### D. Insufficient ATM Cash

The ATM should check whether it has enough physical cash to dispense the requested amount.

If the ATM does not have enough cash:

- Reject the withdrawal.
- Display an appropriate error message.
- Do not deduct money from the customer's account.
- Allow the customer to enter a smaller amount or use another ATM.

#### E. Network or Transaction Failure

The ATM should not dispense cash without clear bank authorisation.

However, failure to receive confirmation does not necessarily mean that the bank did not process the transaction.

The ATM should record the transaction reference, check its status when communication is restored, and follow the bank's reversal or reconciliation procedure if money was deducted but cash was not dispensed.

### 5. Conditions for a Successful Withdrawal

A withdrawal should only be reported as successful when:

1. The card is readable and valid.
2. The customer's PIN is correct.
3. The requested withdrawal amount is valid.
4. The customer's account has sufficient available funds.
5. The ATM has sufficient physical cash.
6. The bank authorises the transaction.
7. The ATM successfully dispenses the requested cash.

If any required condition is not satisfied, the ATM must not report the withdrawal as successful.

### 6. Why Validation Must Happen Before Withdrawal

The ATM should first validate the account balance and available ATM cash before proceeding with a withdrawal.

This is because there are two separate requirements:

**Account balance validation:** The customer must have enough available money in their bank account to cover the requested withdrawal.

**ATM cash validation:** The machine must have enough physical cash to dispense the requested amount.

Both conditions must be satisfied before the withdrawal proceeds.

A customer may have enough money in their account while the ATM does not have enough physical cash. Similarly, the ATM may have enough cash while the customer's account balance is insufficient.

Therefore, a successful withdrawal should only proceed when all the necessary requirements are met.

### 7. Reflection

This exercise taught me that an algorithm is more than a list of instructions. It must contain clear steps, decisions, conditions, and responses to possible failures.

I also learned that different problems require different responses. An incorrect PIN is an authentication problem, insufficient balance is an account problem, insufficient ATM cash is a machine-resource problem, and a network failure can make the transaction outcome uncertain.

Most importantly, I learned that a computer system should validate the necessary conditions before executing a transaction and should not report success unless the required success conditions have been confirmed.