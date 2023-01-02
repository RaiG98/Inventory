from tabulate import tabulate

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost
        
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity
        pass
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        return f"{self.product} ({self.code}) is from {self.country}, it costs us {self.cost} and we have {self.quantity} in stock."
        
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============

# This function will read the inventory.txt and input each line as Shoe objects in The shoe_list.
def read_shoes_data():
    try:
        inventory_file = open('inventory.txt', 'r')
    except:
        print("The inventory file does not seem to exist in this directory")
    # Since the first line is only a key for reading the text file, the code will read the fist line of the file before iterating though the loop.
    inventory_file.readline()
    # This will iterate through the rest of the file and turn each line into a Shoe object to then be appended to the shoe_list.
    try:
        for line in inventory_file:
            shoe_data_list = line.split(',')
            shoe_list.append(Shoe(shoe_data_list[0], shoe_data_list[1], shoe_data_list[2], float(shoe_data_list[3]), int(shoe_data_list[4])))
    except:
        print("It seems some of the shoe items have either not been entered correctly in the file or have some missing data.")
    inventory_file.close
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''


def capture_shoes():
    print("Please enter the data of the shoe you would like to enter into the system: ")
    country = input("Enter the country the shoe is from: ")
    code = input("Enter the product code: ")
    product = input("Enter the name of the product: ")
    # This will check whether the user entered a number and gives them another chance if not.
    while True:
        try:
            cost = float(input("Enter the cost of the product: "))
            break
        except:
            print("The cost of the product needs to be a number. Try again.")
    while True:
        try:
            quantity = int(input("Enter the quantity we have in stock: "))
            break
        except:
            print("The quantity of the product needs to be an integer number. Try again.")
    
    # This will append the shoe to the end of the file in the correct format.
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    with open('inventory.txt', 'a') as inv_file:
        inv_file.write(f"\n{shoe_list[-1].country},{shoe_list[-1].code},{shoe_list[-1].product},{shoe_list[-1].cost},{shoe_list[-1].quantity}")
    print("\nThe shoe item has been added to the system.")
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

# This function will output the files data to the terminal in an easy to read format.
def view_all():
    temp_shoe_list = [["Product:", "Product Code:", "Country:", "Cost:", "Stock:"]]
    temp_shoe_list += [[x.product, x.code, x.country, x.cost, x.quantity] for x in shoe_list]
    print(tabulate(temp_shoe_list))
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

# This function will find the item with the lowest amount of stock and give the user the option to add to that items current stock.
def re_stock():
    min = float('inf')
    lowest_stock = None
    for shoe in shoe_list:
        if shoe.quantity < min:
            min = shoe.quantity
            lowest_stock = shoe
    print(f"The shoe we have lowest in stock is {lowest_stock.product} ({lowest_stock.code}), we have {lowest_stock.quantity} in stock.")
    yes_no = input("Would you like to add to the current stock of this shoe? Enter \'yes\' or \'no\'. ")
    while True:
        if yes_no.lower() == 'yes':
            while True:
                try:
                    # This will add to the stocks current value and rewrite the whole inventory.txt file with that specific change.
                    add = int(input("How much are you adding to the current stock? "))
                    i = shoe_list.index(lowest_stock)
                    shoe_list[i].quantity += add
                    with open('inventory.txt', 'w') as inventory_file:
                        inventory_file.write("Country,Code,Product,Cost,Quantity")
                        for shoe in shoe_list:
                            inventory_file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
                    print(f"\n{lowest_stock.product}\'s stock quantity has been updated in the system.")
                    return
                except:
                    print("\nYou need to enter a whole number. Try again.")
        elif yes_no.lower() == 'no':
            return
        else:
            print("It seems you have not entered \'yes\' or \'no\'. Try again.")

# This function will find the product corresponding to the product code entered by the user. 
# If the programme does not find the product, the user will be able to either try again or exit the feature.
def search_shoe():
    while True:
        search_for = input("Please input the product code for the item you would like to see the details of, if you would like to exit this feature, type \'exit\'.\n: ")
        if search_for.lower() == 'exit':
            return
        for shoe in shoe_list:
            if shoe.code.lower() == search_for.lower():
                return print(F"\n{shoe}\n")
        print("\nThe program could not find an item with that product code. Please try again.\n")

# This function will display the total value of each item in stock.
def value_per_item():
    # The first item in the value shoe list will be a table header.
    value_shoe_list = [["Product:", "Product Code:", "value:"]]
    # Each shoe in shoe_list and its corresponding instance variable will be appended to the value_shoe list so that it will be displayed properly with tabulate.
    value_shoe_list += [[x.product, x.code, (x.cost * x.quantity)] for x in shoe_list]
    print(tabulate(value_shoe_list))

# This function will find the item with the highest quantity in stock and print it to the terminal.
def highest_qty():
    max = float('-inf')
    highest_stock = None
    for shoe in shoe_list:
        if shoe.quantity > max:
            max = shoe.quantity
            highest_stock = shoe
    print(f"The shoe that is highest in stock is {highest_stock.product} ({highest_stock.code}), we have {highest_stock.quantity} in stock. This shoe is on sale.")


#==========Main Menu=============

read_shoes_data()

# This will create a menu for the user which they can use repeatedly.
while True:
    menu = input('''\nSelect one of the following options below:
    va - View all shoe items
    a - Add a shoe
    vv - View the total value of each item in stock
    s - Search for a shoe using a product code
    ls - Find the lowest stocked item and choose to restock
    hs - Find the highest stocked item
    e - Exit
    : ''').lower().strip(" ")
    print()
    if menu == "va":
        view_all()
    elif menu == "a":
        capture_shoes()
    elif menu == "vv":
        value_per_item()
    elif menu == "s":
        search_shoe()
    elif menu == "ls":
        re_stock()
    elif menu == "hs":
        highest_qty()
    elif menu == "e":
        exit()
    else:
        print("It seems you have enter a value that does not correspond to one of the options. Try again.")