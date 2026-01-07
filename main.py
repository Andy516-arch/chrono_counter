from datetime import date, timedelta

def count_weekday(start_date, end_date, target_weekday):
    """
    Counts how many times a specific weekday occurs between two dates.
    target_weekday: Monday=0 ... Sunday=6
    """

    days_to_target = (target_weekday - start_date.weekday()) % 7
    first_target_day = start_date + timedelta(days=days_to_target)

    if first_target_day > end_date:
        return 0

    total_days = (end_date - first_target_day).days
    return (total_days // 7) + 1


# ---------------- MAIN PROGRAM ----------------

print("=== Chrono Counter ===\n")

# ---- START DATE ----
print("Enter START date")
s_year = int(input("Year (YYYY): "))
s_month = int(input("Month (MM): "))
s_day = int(input("Day (DD): "))

# ---- END DATE ----
print("\nEnter END date")
e_year = int(input("Year (YYYY): "))
e_month = int(input("Month (MM): "))
e_day = int(input("Day (DD): "))

start = date(s_year, s_month, s_day)
end = date(e_year, e_month, e_day)

# Safety check
if start > end:
    print("\nError: Start date must be before end date.")
    exit()

# ---- WEEKDAY INPUT (NAME) ----
weekday_map = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6
}

day_input = input(
    "\nEnter weekday name (Monday, Tuesday, ... Sunday): "
).strip().lower()

if day_input not in weekday_map:
    print("Error: Invalid weekday name.")
    exit()

TARGET_DAY = weekday_map[day_input]

# ---- CALCULATION ----
result = count_weekday(start, end, TARGET_DAY)

# ---- OUTPUT ----
print(
    f"\nNumber of {day_input.capitalize()}s from {start} to {end}: {result}"
)
