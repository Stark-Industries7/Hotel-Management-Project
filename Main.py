import json as js
import sys

class hotel:
    def __init__(self):
        self.file_name = "customer_detail.txt"
        self.customer_info = []
        try:
            with open(self.file_name,'r') as f:
                self.customer_info = js.load(f)
        except(FileNotFoundError, js.JSONDecodeError):
            self.customer_info = []

    def save_customer_info(self):
        with open(self.file_name,'w') as f:
            js.dump(self.customer_info,f,indent=4)

    def add_customer_info(self):
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
    def remove_customer_info(self):
        while True:
            try:
                num = int(input("Enter The Number Of Customer Details You want to Remove -->"))
                if num < len(self.customer_info):
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

    def show_customer_info(self):
        if self.customer_info:
            print("| name | phone | email | address |")
            for info in self.customer_info:
                print(f'| {info["Name"]} | {info["Phone"]} | {info["Email"]} | {info["Address"]} |')  
        else:
            print("No Customer Details Are Present In The Hotel Records!")
    def about(self):
        print("How to use the Program")

# Class Object Initialisation
Func = hotel()

# Main Program
def main():
  while True:
      print("__________________Welcome To The Hotel Management System__________________")
      print("(1) Add Customer Information")
      print("(2) Remove Specific Customer Information")
      print("(3) Display All Customer Information")
      print("(4) About The Program")
      print("(5) Quit")
      try:
        choice = int(input("Please Enter The Number Of Choice You Want to Do --> "))
        if choice == 1:
          Func.add_customer_info()
        elif choice == 2:
          Func.remove_customer_info()
        elif choice == 3:
            Func.show_customer_info()  
        elif choice == 4:
            Func.about()
        elif choice == 5:
            sys.exit()    
        else:
            print("Please Type The Given Numbers For Operation Of Code!")
      except:
        print('Invalid Value Format Please Input Numeric Values!')

if __name__ == "__main__":
    main()

