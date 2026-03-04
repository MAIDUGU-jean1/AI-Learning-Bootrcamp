# Define a list of students as (name, score) tuples
students = [
    ("Alice", 88),
    ("Bob", 72),
    ("Charlie", 95),
    ("Diana", 60),
    ("Ethan", 77)
]

# Function to convert a numeric score to a letter grade
def grade_from_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Print a report for each student
print("Student Report:")
for name, score in students:
    grade = grade_from_score(score)
    print(f"Student: {name}, Score: {score}, Grade: {grade}")