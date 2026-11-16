# Tier 1 --- The Literal Assistant

## Project: The Digital Translator

### 1. Why "Make me breakfast" is not a complete instruction

The instruction "Make me breakfast" is too vague for a computer or robot
to carry out reliably. It does not explain what food to prepare, how
much to prepare, where the ingredients and equipment are, what steps to
follow, or where to put the finished food.

A human may use experience and common sense to fill in these missing
details. A computer cannot safely rely on those assumptions. It needs
clear information and instructions. This is related to the principle
**Garbage In, Garbage Out (GIGO)**: if the information or instructions
supplied are incorrect or incomplete, the result may also be incorrect.

A computer does not literally panic. Instead, it may be unable to
continue, make an unintended choice, or produce an incorrect result when
important details are missing.

### 2. Breakfast task and available resources

For this exercise, I will prepare:

-   2 fried eggs
-   2 slices of toast

The original scenario makes these resources available:

-   Refrigerator
-   Eggs and bread
-   Butter
-   Frying pan
-   Cooking stove
-   Plate
-   Kitchen table

I will not treat a toaster, vegetable oil, a bowl, a spatula, a lighter,
or a bread cupboard as guaranteed resources because they are not listed
in the scenario.

**Assumptions and conditions:** The instructions below assume that the
eggs and bread are in the refrigerator, that the stove is functioning,
and that a safe, approved way to ignite the stove and handle hot
cookware is available. The exact method for toasting bread is not
specified in the scenario, so I will use the frying pan and stove
already provided. If safe ignition or safe handling equipment is
unavailable, the robot must stop and ask for assistance rather than
improvise.

### 3. Ordered instructions

#### A. Prepare two fried eggs

1.  Go to the refrigerator.
2.  Open the refrigerator and check that at least two eggs and enough
    butter are available.
3.  If fewer than two eggs are available, stop and report that there are
    not enough eggs to complete the requested breakfast.
4.  Remove two eggs and the butter from the refrigerator, then close the
    refrigerator door.
5.  Place the frying pan on the cooking stove.
6.  Check that the stove and cooking area are safe to use.
7.  Ignite the stove using its approved ignition procedure. Do not
    release gas and leave it unignited. If ignition fails, turn off the
    gas supply and stop.
8.  Allow the pan to heat using a suitable low-to-medium heat setting.
9.  Add a small amount of butter to the pan and allow it to melt without
    burning.
10. Crack the first egg into the pan, taking care not to allow shell
    fragments into the pan.
11. Crack the second egg into the pan.
12. Cook the eggs until the whites are fully set and the eggs are safely
    cooked. Do not rely on a fixed cooking time alone because heat and
    cooking conditions can vary.
13. Turn off the stove when the eggs are cooked.
14. Using a safe method for handling hot food and cookware, transfer the
    eggs onto the plate.
15. Mark the egg-preparation task as complete.

#### B. Prepare two slices of toast

1.  Check that at least two slices of bread are available in the
    refrigerator.
2.  If fewer than two slices are available, do not claim that breakfast
    is complete. Report that there is not enough bread.
3.  Remove two slices of bread and close the refrigerator.
4.  Confirm that the frying pan and stove can be used safely for
    toasting. If the pan is still hot from cooking the eggs, handle it
    carefully and use a safe method to continue.
5.  Use the stove and frying pan to toast the two slices. Turn each
    slice as needed so that both sides are toasted without burning.
6.  Inspect both sides of the bread and confirm that they are golden brown and not burnt.
7.  If both sides meet this condition, turn off the stove. If the robot cannot determine 
    whether the bread is properly toasted, stop and request human assistance.
8.  Using a safe method for handling hot food, place the two slices of
    toast on the plate with the eggs.
9.  Mark the toast-preparation task as complete.

### 4. Handling problems and failures.

**Not enough eggs or bread:** Stop the affected task and report which
ingredient is missing. Do not report the breakfast as complete.

**Stove does not ignite:** Stop the process, turn off the gas supply,
and report the ignition failure. Do not repeatedly release gas or
attempt an unapproved ignition method. Ask for an approved alternative
or human assistance.

**Required safe handling method or equipment is unavailable:** Stop the
affected task and request assistance. Do not touch hot cookware or food
with an unsafe method.

**A task is only partly completed:** Report what has been completed and
what remains. Do not mark the whole breakfast as complete.

### 5. Completion conditions

The breakfast is complete only when all of the following conditions are
true:

-   Two eggs have been safely cooked.
-   Two slices of bread have been toasted.
-   The eggs and toast have been placed together on the plate.
-   The stove has been turned off.
-   The plate has been placed on the kitchen table.

If any condition is not met, report the breakfast as incomplete and
identify the remaining task or problem.

### 6. Assumptions versus instructions

An **assumption** is information that the programmer believes to be true
but that has not been confirmed by the task or environment. For example,
saying that bread is stored in a kitchen cupboard would be an assumption
unless the scenario or user confirms that location.

An **instruction** is a clear action that the robot is expected to
perform, such as "remove two eggs from the refrigerator."

In programming, assumptions should not be silently treated as facts. The
programmer should confirm missing information, state reasonable
assumptions clearly, or provide a condition for what the system should
do when the information or resource is unavailable.

### 7. Reflection

This exercise taught me that a computer needs clear, specific, and
ordered instructions. A simple human request can leave out important
details that a person might understand from experience. When designing
instructions for a computer or robot, I must identify the required
inputs, available resources, sequence of actions, possible failures, and
conditions for successful completion. I must also separate facts
provided by the task from assumptions I introduce.