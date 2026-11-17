# Tier 4 — Conceptual Challenge: Data Translator

## 1. Introduction

This exercise explains how real-world information is represented as data so that a computer can store, process, and communicate it. A computer does not interpret information in exactly the same way a human does. It works with representations and follows instructions to process them.

## 2. Identifying the data

| Customer information | Kind of information | Explanation |
|---|---|---|
| Victor | Text | The customer's name, represented using characters. |
| 30 | Number | The customer's age. |
| 150000.50 | Number | The customer's account balance, including a fractional part. |
| Yes | True/false state (Boolean) | Indicates whether the account is active. |

The account status can be represented using two possible Boolean values:

- Active = `True`
- Inactive = `False`

Because Victor's account is active in the example, its status is `True`.

## 3. How information is represented digitally

A computer stores information using digital representations. At the lowest level, digital information is represented using binary digits called bits:

- `0`
- `1`

Different kinds of information require suitable representations:

- **Text:** Characters in a name such as Victor are encoded using a character-encoding system, such as Unicode, and represented digitally.
- **Numbers:** Values such as 30 and 150000.50 are stored using numerical representations. The system must preserve the value and the decimal part of the balance accurately.
- **Boolean state:** The account status is represented as one of two states, `True` or `False`. A system may encode these states using values such as 1 and 0.

The exact internal representation depends on the computer system and the data format it uses.

The general process is:

**Real-world information → Data representation → Digital/binary representation → Stored by the computer → Processed when needed**

## 4. What could happen if the account balance is stored incorrectly?

Suppose Victor's actual account balance is 150000.50, but the computer incorrectly records it as 15000.

This could cause several problems:

1. **Withdrawals:** If Victor tries to withdraw more than 15000, the system may report insufficient funds, even though his actual balance is higher.
2. **Account statements:** His statement may display an incorrect balance, creating a difference between his actual funds and the amount shown by the bank.
3. **Payments:** Payments may be rejected if the system believes he does not have enough money.
4. **Customer trust:** Victor may lose confidence in the bank because the system is showing and processing incorrect financial information.
5. **Bank records:** Incorrect balances can also cause reconciliation problems and inaccurate financial records.

This shows why data must be represented, stored, and interpreted accurately.

## 5. Why computers need data representation

Data representation allows a computer system to store information in a structured form and process it according to instructions.

For example, when a bank employee searches for a customer named Victor, the banking system can use the stored customer information to find the matching record and retrieve the relevant account details.

The computer does not understand the name Victor in the same way a human does. It compares and processes the stored representation using instructions in the software.

## 6. What is data?

Data is information represented in a form that a computer can store, process, and communicate.

The customer's name, age, account balance, and account status are examples of data. Each needs an appropriate representation so that the computer can handle it correctly.

## 7. Conclusion

This exercise has shown that computers work with representations of real-world information. Text, numbers, and Boolean states are represented in ways that allow a computer to store and process them digitally. If information is represented or interpreted incorrectly, the computer may produce incorrect results. Therefore, accurate data representation is important for reliable computer systems.