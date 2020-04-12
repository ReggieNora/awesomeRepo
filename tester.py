num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def addingNumbers (num1, num2):
	answer = num1 + num2;
	if answer > 1000:
		return answer;
	else:
		print("Answer is lower than 1k")

print("Your number is", addingNumbers(num1, num2))