from sys import argv

script_name, work_hours, salary_per_hour, bonus = argv

print(int(work_hours) * int(salary_per_hour) + int(bonus))

# Example: python hw4ex1.py 2 3 4 Output: 10