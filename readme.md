# Chrono Counter

Chrono Counter is a Python program that calculates how many times a specific weekday
occurs between two user-defined dates.

It uses efficient date arithmetic instead of looping through every single day,
making it accurate and fast even for large date ranges.

---

## Features
- User-defined **start date** and **end date**
- Accepts weekday names (Monday → Sunday)
- Handles leap years automatically
- Optimized logic (no brute-force looping)

---

## How It Works (Logic)
1. Convert input dates into `datetime.date` objects
2. Jump directly to the **first occurrence** of the target weekday
3. Count how many full 7-day intervals fit until the end date

This avoids unnecessary computation and calendar errors.

---

## Weekday Mapping
| Day       | Value |
|----------|-------|
| Monday   | 0 |
| Tuesday  | 1 |
| Wednesday| 2 |
| Thursday | 3 |
| Friday   | 4 |
| Saturday | 5 |
| Sunday   | 6 |

---

## Requirements
- Python 3.10 or higher

---

## How to Run

```bash
python chrono_counter.py
