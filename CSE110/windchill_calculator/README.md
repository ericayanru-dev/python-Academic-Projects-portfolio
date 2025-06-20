# Windchill Calculator

**Author:** Eric Ayanru  
**Course:** CSE110 – Introduction to Programming  
**Project Type:** Weather Tool / Scientific Calculator  
**Language:** Python

---

## Description

This program calculates the **wind chill temperature** based on user input.

Features:
- Accepts both **Fahrenheit** and **Celsius**
- Converts Celsius input automatically
- Calculates windchill for wind speeds from **5 mph to 60 mph**
- Loops until user chooses to exit
- Built-in **input validation**

---

## Formula Used

The **windchill formula** (valid for T  50°F and V > 3 mph):


---

## How to Run

```bash
python windchill_calculator.py

Sample Output

What is the temperature? 10
Fahrenheit or Celsius (F/C)? f

Wind Chill Results for 10.0°F:
  At wind speed  5 mph → Windchill: 1.24F
  At wind speed 10 mph → Windchill: -3.54F
  ...
  At wind speed 60 mph → Windchill: -18.64F

Would you like to calculate again? (yes/no): no
Goodbye!