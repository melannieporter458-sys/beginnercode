import time

def countdown(t):
	"""
	Countdown timer function
	t: total seconds for the countdown
	"""

	while t:
		# divmod() returns the quotient and remainder
		mins, secs = divmod(t, 60)
		# Format the time string as MM:SS with leading zeros
		timer = '{:02d}:{:02d}'.format(mins, secs)
		# Print the time on the same line, overwriting the previous output
		print(timer, end="\r")
		# Pause the program for 1 second
		time.sleep(1)
		# Decrement the time
		t -= 1

	print('Blast off!') # Print a final message after the loop finishes

# Get user input for the countdown duration in seconds
seconds = input("Enter the countdown time in seconds: ")

# Validate and convert the input to an integer
try: 
	seconds = int(seconds)
	if seconds <= 0:
		print("Please enter a positive number. ")
	else: 
		countdown(seconds)
except ValueError:
	print("Invalid input. Please enter a whole number.")
