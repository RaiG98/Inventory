# Inventory
## About the programme:
This code is a simple inventory management system for shoes. The code defines a Shoe class, which holds information about a shoe, such as its country of origin, code, product name, cost, and quantity in stock. The class also has several methods, such as get_cost() and get_quantity(), which return the cost and quantity of a shoe, respectively, and __str__(), which returns a string representation of the shoe.

The code also defines a list called shoe_list, which is used to store a list of Shoe objects. The code also defines several functions that operate on the shoe_list:

read_shoes_data(): This function reads data from a text file called inventory.txt and creates Shoe objects with the data, which are then appended to the shoe_list.
capture_shoes(): This function allows a user to enter data about a shoe and creates a Shoe object with the data, which is then appended to the shoe_list and written to the inventory.txt file.
view_all(): This function outputs the data of all shoes in the shoe_list to the terminal in an easy-to-read format using tabulate package.
search_shoe(): This function allows the user to search for a shoe in the shoe_list by product name, product code or country of origin, it will return the shoes that match the search criteria.
remove_shoe(): This function allows the user to remove a shoe from the shoe_list by product code or product name, it will remove the shoe if it matches the criteria
The code uses the try-except statements for error handling when reading the inventory.txt file and when capturing data for new shoes. It also uses the tabulate package to format the output for the view_all() function in an easy-to-read format.

Overall, this code provides a simple way to keep track of shoes in stock by allowing the user to view, add, and remove shoes from the inventory and storing the data in a text file.

## How to use the programme:
1. Ensure the inventory.txt file is in the same directory as the inventory.py file
1. run inventory.py
