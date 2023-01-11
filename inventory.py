# Compulsory Task 1

#========The beginning of the class==========

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = int(quantity)

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        shoe_details = f"Country:  {self.country}\n"
        shoe_details += f"Code:\t  {self.code}\n"
        shoe_details += f"Product:  {self.product}\n"
        shoe_details += f"Cost:\t  {self.cost}\n"
        shoe_details += f"Quantity: {self.quantity}\n"
        return shoe_details




#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    file = open("inventory.txt", "r")

    lines = file.readlines()

    for line in range(1, (len(lines))):
        try:
            shoe_data = lines[line].split(",")
            shoe_item = Shoe(shoe_data[0], shoe_data[1], shoe_data[2], shoe_data[3], shoe_data[4])
            shoe_list.append(shoe_item)
        except IndexError:
            continue



def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    shoe_country = input("Please enter the country:")
    shoe_code = input("Please enter the code:")
    shoe_product = input("Please enter the product:")
    shoe_cost = float(input("Please enter the cost:"))
    shoe_quantity = int(input("Please enter the quantity:"))

    new_shoe = Shoe(shoe_country, shoe_code, shoe_product, shoe_cost, shoe_quantity)
    shoe_list.append(new_shoe)

def view_all():

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

    for item in shoe_list:
        print(item.__str__(), end="")
        print('\n')

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    lowest = min(shoe_list, key = lambda shoe: shoe.quantity)
    choice = input(f"The shoe with the lowest quantity is {lowest.product}. There are only {lowest.quantity} left.\n"
          f"Do you want to restock?")
    if choice.lower() == "yes":
        add_quantity = int(input("How many pairs would you like to add?"))
        lowest.quantity = lowest.quantity + add_quantity

        file = open("inventory.txt", "w")
        for i in shoe_list:
            shoe_data = i.country, i.code, i.product, str(i.cost), str(i.quantity)
            shoe_data_joined = ",".join(shoe_data)
            file.write(shoe_data_joined+"\n")


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''


    while True:
        code_input = input("Please enter item code:").upper()
        if_found = 0

        for i in shoe_list:
                if code_input == i.code:
                    shoe_choice = i
                    print(shoe_choice)
                    if_found += 1
                    break
        if if_found == 0:
            print("Shoe not found.")
            continue
        break

def value_per_item():
    '''
        This function will calculate the total value for each item.
        Please keep the formula for value in mind: value = cost * quantity.
        Print this information on the console for all the shoes.
        '''
    for i in shoe_list:
        shoe_cost = float(i.get_cost())
        shoe_quantity = int(i.get_quantity())
        shoe_value = shoe_cost * shoe_quantity
        print(f'''{i}Item Value: {shoe_value}\n''')


def highest_qty():

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    highest = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"\nFor sale:\n{highest.product}: {highest.cost}\n")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

# Call the "read_shoes_data" function to get the list of shoes
# Menu calls the appropriate function depending on user choice

read_shoes_data()

user_choice = ""

while user_choice != "quit":

    user_choice = input('''Please select an option:
    c - capture shoe data
    va - view all the shoes
    rs - restock a shoe
    s - search for a shoe
    v - get the value of a shoe
    h - find the shoe with the highest value
    e - exit''').lower()

    if user_choice == "c":
        capture_shoes()

    elif user_choice == "va":
        view_all()

    elif user_choice == "rs":
        re_stock()

    elif user_choice == "s":
        search_shoe()

    elif user_choice == "v":
        value_per_item()

    elif user_choice == "h":
        highest_qty()

    elif user_choice == "e":
        print("Goodbye")
        exit()

    else:
        print("Oops - incorrect input")