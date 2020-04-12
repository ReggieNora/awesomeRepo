#Create a new list called shopping_list

shopping_list = []

#Create a function called add_to_list that delcares a parameter
def show_help():
	print("What should we pick up at the store?")
	print("""
	* Enter 'DONE' to stop adding items.
	* Enter 'HELP' for this help. 
	* Enter 'SHOW' to show list.
	""")


def add_to_list(item):
	shopping_list.append(item)
	# Notify user that the item was added and state number of items in the list. 
	print("Added! List has {} item(s).".format(len(shopping_list)))


def show_list():
	print("Here is your list:")
	for item in shopping_list:
		print(item)

show_help()
while True:
	new_item = input("> ") 

	if new_item == 'DONE':
		break
	elif new_item == 'HELP': 
		show_help()
		continue
	elif new_item == 'SHOW':
		show_list()
		continue

	add_to_list(new_item)

show_list()