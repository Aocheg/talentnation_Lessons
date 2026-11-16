# Tier 3 — Practical Exercise: Input → Processing → Output

## Mission: The Simple Calculator

### 1. Introduction

A calculator receives information from the user, performs an operation on that information, and displays a result. This can be explained using three stages:

- **Input:** The information supplied to the calculator.
- **Processing:** The operation the calculator performs on the input.
- **Output:** The result produced by the calculator.

For this exercise, the calculator receives these two numbers:

- `number_1 = 20`
- `number_2 = 5`

It performs addition, subtraction, multiplication, and division.

### 2. Addition

- **Input:** 20 and 5
- **Processing:** Add the two numbers (`20 + 5`)
- **Output:** 25

Calculation: `20 + 5 = 25`

### 3. Subtraction

- **Input:** 20 and 5
- **Processing:** Subtract the second number from the first number (`20 - 5`)
- **Output:** 15

Calculation: `20 - 5 = 15`

### 4. Multiplication

- **Input:** 20 and 5
- **Processing:** Multiply the two numbers (`20 × 5`)
- **Output:** 100

Calculation: `20 × 5 = 100`

### 5. Division

- **Input:** 20 and 5
- **Processing:** Divide the first number by the second number (`20 ÷ 5`)
- **Output:** 4

Calculation: `20 ÷ 5 = 4`

### 6. Summary Table

| Operation | Input | Processing | Output |
|---|---|---|---:|
| Addition | 20 and 5 | 20 + 5 | 25 |
| Subtraction | 20 and 5 | 20 - 5 | 15 |
| Multiplication | 20 and 5 | 20 × 5 | 100 |
| Division | 20 and 5 | 20 ÷ 5 | 4 |

### 7. What Happens If the User Tries to Divide by Zero?

A calculator must not attempt to divide a number by zero because division by zero is undefined in ordinary arithmetic. For example, `20 ÷ 0` does not produce a valid numerical answer.

A well-designed calculator should:

1. Check the second number before carrying out division.
2. If the second number is zero, stop the division operation.
3. Display a clear message, such as **“Error: Cannot divide by zero.”**
4. Allow the user to enter another number or choose another operation.

The calculator should not display a misleading result or crash because of this invalid operation.

### 8. Understanding Input, Processing, and Output

The calculator follows the same basic pattern for each operation:

1. **Input:** It receives the two numbers from the user.
2. **Processing:** It follows the selected mathematical operation using those numbers.
3. **Output:** It displays the answer to the user.

The input stays the same in this exercise, but the processing changes depending on the operation selected. Because the operation changes, the output also changes.

### 9. Conclusion

This exercise shows that a computer program works with information provided as input, follows instructions to process that information, and produces an output. It also needs to handle invalid situations, such as trying to divide by zero, in a clear and safe way.

**The basic model is: Input → Processing → Output.**