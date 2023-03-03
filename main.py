# This program calculates the number of days a person has spent on earth

# import the datetime module to work with dates
import datetime

# Get the current date
today = datetime.date.today()

#Print a welcome message here
print("Hello!,Welcome,Input your Age in number to get the approximate number of days you've spent on earth")
print()
print()
# Ask the user to enter their age
age = input("What is your age? ")

    


# Convert the age to an integer
age = int(age)

# Calculate the number of days the person has lived
days_lived = age * 365.25  # taking into account leap years

# Print the result
print()
print("You have lived for approximately", int(days_lived), "days.")
