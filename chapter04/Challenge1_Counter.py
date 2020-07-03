# Challenge 1
# Write a program that counts for the user. Let the user enter the starting
# number, the ending number, and the amount by which to count

# Welcome user
print("\t\tHello. Welcome to my number counter.")

# request parameters from user
num_start = int(input("Please select starting number for counter: "))
num_end = int(input("Please select ending number to count: "))
step = int(input("In what intervals would you like me to count? "))

# Add condition for non uniform stepping
if (num_end-num_start) % step:
    print("\nStart and end points cannot be evenly distributed at selected step. This is the best I can do:")
else:
    print("")
    
# Start counting
for i in range(num_start, num_end+1, step):
    print(i, end=" ")

input("\n\nCount complete. press 'Enter' key to exit") 
