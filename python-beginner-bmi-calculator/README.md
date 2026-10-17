# BMI Calculator

## Internship
Oasis Infobyte – Python Programming Internship

## Task
Task 2 – BMI Calculator

## Objective
The objective of this project is to create a Python program that calculates a user's Body Mass Index (BMI) and classifies the result into standard BMI categories.

## Technologies Used
- Python
- Basic arithmetic
- Input validation
- Conditional statements
- Functions

## Features
- Accepts weight in kilograms.
- Accepts height in metres.
- Calculates BMI using the formula:
  
  BMI = weight / (height²)

- Displays BMI rounded to two decimal places.
- Classifies BMI into:
  - Underweight
  - Normal
  - Overweight
  - Obese
- Rejects non-numeric input.
- Rejects zero and negative values.
- Displays helpful error messages.

## BMI Categories

| BMI Range | Category |
|-----------|----------|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal |
| 25 – 29.9 | Overweight |
| 30 or above | Obese |

## How to Run

1. Install Python.
2. Open the project folder in Visual Studio Code.
3. Open the VS Code terminal.
4. Run the following command:

```bash
python bmi_calculator.py
       
### 2. Format the Example Output properly

Change your Example Output section to:

```markdown
## Example Output

```text
===== BMI CALCULATOR =====
Enter your weight in kg: 60
Enter your height in metres: 1.65

----- Result -----
Your BMI is: 22.04
Category: Normal

### 3. Format Input Validation properly

Change your current section to:

```markdown
## Input Validation

The program handles invalid inputs such as:

- Text instead of numbers
- Zero values
- Negative values

Example:

```text
Enter your weight in kg: abc
Error: Please enter valid numeric values.