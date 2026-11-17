# Py-SECTION 1 MISSION PROJECT — THE DIGITAL TRANSLATOR

Mission: mission-03
Squad: Solo 399

This repository was created for the Squad mission workspace.

Use this repository for the team's implementation. Commit and push all meaningful work to Gitea, then submit the Mission for inspection from TalentNation when the Squad is ready.



# Py-SECTION 1 Mission Project — The Digital Translator

## Project overview

The Digital Translator mission explores how computers work with information. It develops the habit of translating real-world requests into clear data, instructions, processing steps, and outputs that a computer can follow.

The project is organized into five tiers. The focus is on understanding and explaining computer concepts—not writing Python code for these exercises.

## Mission objectives

By completing the five tiers, this project demonstrates an understanding of:

- Why instructions must be clear, precise, and ordered.
- How to describe an algorithm and account for possible failures.
- How a computer uses input, processing, and output.
- How different kinds of information are represented as data.
- How data, programs, instructions, processing, storage, and output work together in a simple system.

## Repository structure

```text
digital-translator/
├── README.md
├── tier-1/
│   └── literal-assistant.md
├── tier-2/
│   └── atm-withdrawal-algorithm.md
├── tier-3/
│   └── simple-calculator.md
├── tier-4/
│   └── data-translator.md
└── tier-5/
    └── online-store-architecture.md
```

## Tier summaries

### Tier 1 — Basic Understanding: The Literal Assistant

Translates the vague instruction “Make me breakfast” into precise, ordered steps. It considers ingredients, quantities, equipment, preparation, safety, assumptions, and how to determine when the task is complete.

**Main lesson:** A computer cannot safely rely on unstated assumptions. Instructions need to be explicit.

### Tier 2 — Field Exercise: Algorithm Thinking — The ATM

Describes an ATM cash-withdrawal process as an algorithm, including card and PIN validation, balance and cash checks, transaction authorization, and possible failure cases.

**Main lesson:** An algorithm is a sequence of steps for solving a problem. It is the plan that can later be translated into a program.

### Tier 3 — Practical Exercise: Input → Processing → Output — The Simple Calculator

Identifies the inputs, processing operations, and outputs for addition, subtraction, multiplication, and division using 20 and 5. It also considers how division by zero should be handled.

**Main lesson:** A computer receives input, processes it according to instructions, and produces output.

### Tier 4 — Conceptual Challenge: Data Translator

Classifies customer information such as a name, age, account balance, and account status. It explains data representation, binary information, and the consequences of an incorrectly represented account balance.

**Main lesson:** Data is information represented in a form a computer can store, process, and communicate.

### Tier 5 — Architecture Challenge: Explain the Whole System — The Online Store

Explains how an online store receives a customer's product selection and quantity, calculates the total price, stores order information, and displays an output or confirmation.

**Main lesson:** A computer system brings together input, data, programs, instructions, processing, storage, and output to solve a real-world problem.

## Key concepts across the mission

- **Computer:** An electronic machine that receives data, processes it according to instructions, stores information, and produces or communicates output.
- **Program:** A set of instructions written for a computer to follow.
- **Algorithm:** An ordered set of steps for solving a problem or completing a task.
- **Data:** Information represented in a form that a computer can store, process, and communicate.
- **Input:** Data or information supplied to a system.
- **Processing:** Operations performed on input data according to instructions.
- **Output:** The result produced or communicated by a system.
- **Storage:** Keeping data so it can be retrieved and used later.
- **Binary:** A number system using the digits 0 and 1, which underlies digital storage and processing.

## Overall system model

The mission builds toward this general model:

```text
Real-world problem
        ↓
      Input
        ↓
       Data
        ↓
Program and instructions
        ↓
    Processing
        ↓
   Stored data
        ↓
      Output
```

The exact order and interaction of storage and processing can vary by system. The important idea is that a computer works with represented information and follows instructions to process it.

## Final reflection

A computer does not understand the real world directly. It works with representations of information and follows instructions for processing those representations. Therefore, instructions and data must be represented clearly and correctly for a computer system to produce reliable results.