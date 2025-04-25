languages = ["telugu", "tamil", "hindi"]
print(len(languages))

grades = [10, 45, 67, 23, 99]

print(sum(grades))
print(len(grades))

for i in grades:
    print(i)

word = str(input("enter a string to reverse it!"))
reversed_word = ""
for i in word:
    reversed_word = i + reversed_word
print("The reversed word id", reversed_word)


# Calculate the average score and return it
def get_average_score(scores):
    total = sum(scores)
    subject_count = len(scores)
    average_score = total / subject_count
    return average_score


scores = [55, 64, 75, 80, 65]
average_score = get_average_score(scores)
print(average_score)  # Output: 67.8


# Function to compute grade
def compute_grade(average_score):
    if average_score >= 80.0:
        grade = "A"
    elif average_score >= 60.0:
        grade = "B"
    elif average_score >= 50.0:
        grade = "C"
    else:
        grade = "F"

    return grade


average_score = 67.8
grade = compute_grade(average_score)
print(grade)  # Output: B