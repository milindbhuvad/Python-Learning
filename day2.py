# Day 2: Strings, lists, loops, dictionaries, and conditions

# 1. String operations
name = "Milind Bhuvad"
print("String Operations:")
print(name.upper())
print(name.lower())
print(name.title())
print(len(name))
print(name.replace("Milind", "Ishanvi"))
print()

# 2. Checking text in a string
email = "milindbhuvad1988@gmail.com"
print("Email Check:")
print("gmail" in email)

if "gmail" in email:
    print("This is a Gmail address.")
print()

# 3. List operations
skills = ["Python", "Java", "C++", "JavaScript"]
print("Skills List:")
print(skills)
print(len(skills))
print(skills[0])
print(skills[3])

skills.append("SQL")
print(skills)

skills.remove("C++")
print(skills)
print()

# 4. Looping through a list
print("Looping Through Skills:")
for skill in skills:
    print(skill)
print()

# 5. Range function
print("Range Example:")
for i in range(5):
    print(i)

print("More Range Example:")
for i in range(1, 6):
    print(i)
print()

# 6. Dictionary example
person = {
    "name": "Milind Bhuvad",
    "age": 35,
    "city": "New York"
}

print("Dictionary Example:")
print(person)
print(person["name"])
print(person["age"])
print(person["city"])

person["email"] = "milindbhuvad1988@gmail.com"
print(person)

if "email" in person:
    print("Email exists in the dictionary.")
print()

# 7. List of dictionaries
employees = [
    {"name": "Milind", "role": "PHP Developer", "experience": 8},
    {"name": "Rahul", "role": "Node Developer", "experience": 5},
    {"name": "Amit", "role": "Python Developer", "experience": 4}
]

print("Employee Details:")
for employee in employees:
    print(f"Name: {employee['name']}, Role: {employee['role']}, Experience: {employee['experience']} years")
print()

# 8. if-elif-else statement
print("Voting Check:")
age = 25
if age < 18:
    print("You are not eligible to vote.")
elif 18 <= age < 65:
    print("You are eligible to vote.")
else:
    print("You are eligible to vote and can also participate in senior citizen programs.")
print()

# Practical example — skill checker
name = "Milind"

skills = [
    "PHP",
    "Laravel",
    "MySQL",
    "AWS",
    "Docker"
]

print(f"Developer: {name}")
print("Skills:")

for skill in skills:
    print(f"- {skill}")

#Practical employee example
employees = [
    {
        "name": "Milind",
        "experience": 8,
        "salary": 54757
    },
    {
        "name": "Rahul",
        "experience": 5,
        "salary": 45000
    },
    {
        "name": "Amit",
        "experience": 3,
        "salary": 35000
    }
]

for employee in employees:

    if employee["experience"] >= 8:
        level = "Senior"
    elif employee["experience"] >= 5:
        level = "Mid Level"
    else:
        level = "Junior"

    print(
        f"{employee['name']} - "
        f"{level} - "
        f"₹{employee['salary']}"
    )