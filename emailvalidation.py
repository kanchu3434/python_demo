import re

# Define a function for
# for validating an Email
def check(s):
	pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
	if re.match(pat,s):
		print("Valid Email")
	else:
		print("Invalid Email")

# Driver Code
if __name__ == '__main__':

	# Enter the email
	email = "kanchan326@gmail.com"

	# calling run function
	check(email)

	email = "harshada.patil@our-earth.org"
	check(email)

	email = "vaibhavii326.com"
	check(email)
