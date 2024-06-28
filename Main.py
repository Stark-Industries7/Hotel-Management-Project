import json as js
# import sys

class hotel:
    def __init__(self):
        """This __init__ function will initialise all the files where the customer details and there 
        respective booking details are stored.        
        """        
        self.customer_file_name = "customer_detail.txt"
        self.customer_info = []
        self.booking_file_name = "booking_details.txt"
        self.booking_info = []
        
        try: #this will check if the customer details file is located in the system or not if not then it will initialise a empty list
            with open(self.customer_file_name,'r') as f:
                self.customer_info = js.load(f)
        except(FileNotFoundError, js.JSONDecodeError):
            self.customer_info = []

        try: #this will check if the booking details file is located in the system or not if not then it will initialise a empty list
            with open(self.booking_file_name, 'r') as f:
                self.booking_info = js.load(f)
        except(FileNotFoundError, js.JSONDecodeError):
            self.booking_info = []

    def save_customer_info(self): 
        """
        this will save the customer details in the customer file in the text format using JSON
        """        
        with open(self.customer_file_name,'w') as f:
            js.dump(self.customer_info,f,indent=4)

    def save_booking_info(self): 
        """
        this will save the booking details in the customer file in the text format using JSON
        """        
        with open(self.booking_file_name,'w') as f:
            js.dump(self.booking_info,f,indent=4)        

    def add_customer_info(self): 
        """
        This Will add customer data to the file named customer_detail.txt in a list format containing dictionary of the customer data
        """        
        while True:
            try:
                name = input("Please Enter Your Name --> ")
                phone = int(input("Please Enter Your Phone Number --> "))
                email = input("Please Enter Your Email Address --> ")
                address = input("Please Enter Your Home Address --> ")
                self.customer_info.append({"Name":name,"Phone":phone,"Email":email,"Address":address})
                self.save_customer_info()

                print(f"The Details For Name: {name} Saved In The Hotel Records!")
                another_customer = input("Do You Want to Add Details Of Another Customer(Yes/No) --> ").lower()
                if another_customer not in ['yes','y']:
                    break
                
            except ValueError:
                print("Please Input Correct Format:(Phone Number)")
    
    def add_booking_info(self): 
        """
        This Will add customer booking data to the file named booking_details.txt in a list format containing dictionary of the booking data
        """        
        while True:
            try:
              name = input("Please Enter Your Name for Booking --> ")
              # Check if customer details exist
              customer_exists = any(info["Name"].lower() == name.lower() for info in self.customer_info)
              if not customer_exists:
                    print("Customer details not found. Please add customer details first.")
                    break
                
              check_in_date = input("Please Enter Check-in Date (YYYY-MM-DD) --> ")
              check_out_date = input("Please Enter Check-out Date (YYYY-MM-DD) --> ")
              room_type = input("Please Enter Room Type (e.g., Single, Double, Suite) --> ")
              number_of_guests = int(input("Please Enter Number of Guests --> "))
              special_requests = input("Please Enter Any Special Requests --> ")
              payment_method = input("Please Enter Payment Method (e.g., Credit Card) --> ")
              card_number = input("Please Enter Card Number --> ")
              expiry_date = input("Please Enter Card Expiry Date (MM/YY) --> ")
              cvv = input("Please Enter Card CVV --> ")
              id_type = input("Please Enter ID Type (e.g., Passport) --> ")
              id_number = input("Please Enter ID Number --> ")

              self.booking_info.append({
                    "Name": name,
                    "Check-in Date": check_in_date,
                    "Check-out Date": check_out_date,
                    "Room Type": room_type,
                    "Number of Guests": number_of_guests,
                    "Special Requests": special_requests,
                    "Payment Method": payment_method,
                    "Card Details": {
                        "Number": card_number,
                        "Expiry Date": expiry_date,
                        "CVV": cvv
                    },
                    "ID Type": id_type,
                    "ID Number": id_number
                })
              self.save_booking_info()

              print(f"The Booking Details For Name: {name} Saved In The Hotel Records!")
              another_booking = input("Do You Want to Add Another Booking (Yes/No) --> ").lower()
              if another_booking not in ['yes', 'y']:
                break

            except ValueError as e:
                print(f"Error: {e}. Please Input Correct Format For Each Field.")

    def remove_customer_info(self):
        """This will remove the customer data from the file with the desired name of the person 
        """        
        while True:
            try:
                num = int(input("Enter The Number Of Customer Details You want to Remove -->"))
                if num > len(self.customer_info):
                    raise ValueError(f"Invalid Number Of Query: There Are only {len(self.customer_info)} Customer Details Present in the Hotel Record!")
                for _ in range(num):
                     name = input("Please Enter The Name Of The Customer To remove Details --> ")
                     for info in self.customer_info:
                         if info["name"].lower() == name.lower():
                             self.customer_info.remove(info)
                             self.save_customer_info()
                             print(f"The Customer Details Of the Person {name} is Deleted From The Hotel Records!")
                             break
            except ValueError as e:                                        
                print(e)

    def remove_booking_info(self):
        """
        This will remove the customer Booking data from the file with the desired name of the person
        """        
        while True:
            try:
                name = input("Please Enter The Name Of The Customer To Remove Booking --> ")
                found = False
                for info in self.booking_info:
                    if info["Name"].lower() == name.lower():
                        self.booking_info.remove(info)
                        self.save_booking_info()
                        print(f"The Booking Details Of the Person {name} is Deleted From The Hotel Records!")
                        found = True
                        break
                if not found:
                    print(f"No Booking Found For The Name: {name}")
                another_booking = input("Do You Want to Remove Another Booking (Yes/No) --> ").lower()
                if another_booking not in ['yes', 'y']:
                    break
            except ValueError as e:
                print(e)
    
    def show_booking_info(self):
        """
        This Will show the booking details of all the person who are registerd with the hotel and if there data is present in the hotel records
        """        
        if self.booking_info:
            print("| Name | Check-in Date | Check-out Date | Room Type | Number of Guests | Special Requests | Payment Method | ID Type | ID Number |")
            for info in self.booking_info:
                print(f'| {info["Name"]} | {info["Check-in Date"]} | {info["Check-out Date"]} | {info["Room Type"]} | {info["Number of Guests"]} | {info["Special Requests"]} | {info["Payment Method"]} | {info["ID Type"]} | {info["ID Number"]} |')
        else:
            print("No Booking Details Are Present In The Hotel Records!")                        

    def show_booking_for_customer(self):
        """
        This Will show the customer booking details of the person who is registerd with the hotel and his or her data is present in the hotel records
        """        
        name = input("Please Enter The Name Of The Customer To Show Booking Details --> ")
        found = False
        for info in self.booking_info:
            if info["Name"].lower() == name.lower():
                print(f'| {info["Name"]} | {info["Check-in Date"]} | {info["Check-out Date"]} | {info["Room Type"]} | {info["Number of Guests"]} | {info["Special Requests"]} | {info["Payment Method"]} | {info["ID Type"]} | {info["ID Number"]} |')
                found = True
                break
        if not found:
            print(f"No Booking Found For The Name: {name}")

    def show_customer_info(self):
        """
        This will show the customer info of all the persons who are registered with the hotel and if there details are present in the hotel records
        """        
        if self.customer_info:
            print("| name | phone | email | address |")
            for info in self.customer_info:
                print(f'| {info["Name"]} | {info["Phone"]} | {info["Email"]} | {info["Address"]} |')  
        else:
            print("No Customer Details Are Present In The Hotel Records!")
    
    def about(self):
        """
        This will give the thorough introduction of the whole program to the users who are not well knowledged with this program and are using it for the first time 
        """        
        print("""
        Welcome to the Hotel Management System!

        This system allows you to manage customer and booking information efficiently. Here are the main features and how to use them:

        1. Add Customer Information:
            - Choose option (1) from the main menu.
            - Enter the customer's name, phone number, email address, and home address.
            - The system will save these details for future reference.

        2. Add Booking Information:
            - Choose option (2) from the main menu.
            - Ensure the customer details are already added.
            - Enter the customer's name (must match the existing customer details).
            - Provide check-in and check-out dates, room type, number of guests, special requests, payment method, and ID details.
            - The system will save the booking details linked to the customer.

        3. Remove Specific Customer Information:
            - Choose option (3) from the main menu.
            - Enter the number of customer details you want to remove.
            - Provide the name of the customer to remove their details from the records.

        4. Remove Specific Booking Information:
            - Choose option (4) from the main menu.
            - Enter the name of the customer to remove their booking details from the records.

        5. Display All Customer Information:
            - Choose option (5) from the main menu.
            - The system will display all the saved customer details.

        6. Display All Booking Information:
            - Choose option (6) from the main menu.
            - The system will display all the saved booking details.

        7. Display Booking Information For A Specific Customer:
            - Choose option (7) from the main menu.
            - Enter the name of the customer to view their booking details.

        8. About The Program:
            - Choose option (8) from the main menu to view this help guide.

        9. Quit:
            - Choose option (9) from the main menu to exit the program.

        Please follow the prompts on the screen to input the required information. If you need any assistance, refer back to this guide by selecting option (8) from the main menu.

        Enjoy using the Hotel Management System!
        """)

# Class Object Initialisation
Func = hotel()

# Main Program
def main():
    while True:
        print("__________________Welcome To The Hotel Management System__________________")
        print("(1) Add Customer Information")
        print("(2) Add Booking Information")
        print("(3) Remove Specific Customer Information")
        print("(4) Remove Specific Booking Information")
        print("(5) Display All Customer Information")
        print("(6) Display All Booking Information")
        print("(7) Display Booking Information For A Specific Customer")
        print("(8) About The Program")
        print("(9) Quit")
        try:
            choice = int(input("Please Enter The Number Of Choice You Want to Do --> "))
            if choice == 1:
                Func.add_customer_info()
            elif choice == 2:
                Func.add_booking_info()
            elif choice == 3:
                Func.remove_customer_info()
            elif choice == 4:
                Func.remove_booking_info()
            elif choice == 5:
                Func.show_customer_info()
            elif choice == 6:
                Func.show_booking_info()
            elif choice == 7:
                Func.show_booking_for_customer()
            elif choice == 8:
                Func.about()
            elif choice == 9:
                break    
            else:
                print("Please Type The Given Numbers For Operation Of Code!")
        except ValueError:
            print('Invalid Value Format Please Input Numeric Values!')

# calling of the main() function
if __name__ == "__main__":
    main()

