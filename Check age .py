# Function to check age
def check_age(age):
    if age >= 10:
        if age <= 20:
            return "The person is between 10 and 20 years old."
        else:
            return "The person is older than 20 years."
    else:
        return "The person is younger than 10 years."

# Input from user
try:
    user_age = int(input("Please enter the age of the person: "))
    result = check_age(user_age)
    print(result)
except ValueError:
    print("Invalid input! Please enter a valid age.")
