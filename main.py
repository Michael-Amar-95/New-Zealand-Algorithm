start = 10000
spend_lst = [1200, 900, 354, 1300, 550, 620, 550, 715]
total = sum(spend_lst)
print("Total:", total)
money_left = start - total
print("You have", money_left, "dollars")
average = total / len(spend_lst)
print("The average per week:", average)
weeks_left = money_left / average
print("You have approx.", weeks_left, "weeks left to travel")

print("\n**************************************\n")

# In this script I check if the average of the list is contained in the list
grades = [81, 70, 75, 96, 99, 100, 87, 80, 100]
print("Testing the following grades list:", grades)

# DO NOT CHANGE THIS LINE:
print("Your solution: ", end="")

# First, we compute the sum of the grades in the list
total = sum(grades)

# Next, we compute the length of the list
length = len(grades)

# Then, we compute the average value of the list
avg = total / length

# We can now check whether the average is in the list
result = avg in grades

# And finally, we can print the result we got
print(result)