# Hotel Management System

## Overview

The Hotel Management System is a Python-based application designed to manage customer and booking information efficiently. It allows users to add, remove, and display details about customers and their bookings. This program uses JSON files to store and retrieve data.

## Features

1. **Add Customer Information**
2. **Add Booking Information**
3. **Remove Specific Customer Information**
4. **Remove Specific Booking Information**
5. **Display All Customer Information**
6. **Display All Booking Information**
7. **Display Booking Information For A Specific Customer**
8. **About The Program**

## How to Use

### 1. Add Customer Information
- Choose option (1) from the main menu.
- Enter the customer's name, phone number, email address, and home address.
- The system will save these details for future reference.

### 2. Add Booking Information
- Choose option (2) from the main menu.
- Ensure the customer details are already added.
- Enter the customer's name (must match the existing customer details).
- Provide check-in and check-out dates, room type, number of guests, special requests, payment method, and ID details.
- The system will save the booking details linked to the customer.

### 3. Remove Specific Customer Information
- Choose option (3) from the main menu.
- Enter the number of customer details you want to remove.
- Provide the name of the customer to remove their details from the records.

### 4. Remove Specific Booking Information
- Choose option (4) from the main menu.
- Enter the name of the customer to remove their booking details from the records.

### 5. Display All Customer Information
- Choose option (5) from the main menu.
- The system will display all the saved customer details.

### 6. Display All Booking Information
- Choose option (6) from the main menu.
- The system will display all the saved booking details.

### 7. Display Booking Information For A Specific Customer
- Choose option (7) from the main menu.
- Enter the name of the customer to view their booking details.

### 8. About The Program
- Choose option (8) from the main menu to view the help guide.

### 9. Quit
- Choose option (9) from the main menu to exit the program.

## Files

- `hotel.py`: The main program file containing all the functionality.
- `customer_detail.txt`: JSON file storing customer information.
- `booking_detail.txt`: JSON file storing booking information.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/hotel-management-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd hotel-management-system
    ```
3. Run the program:
    ```bash
    python hotel.py
    ```

## Usage

Run the program and follow the on-screen instructions to add, remove, and view customer and booking information.

## Dependencies

- Python 3.x
- JSON module (comes pre-installed with Python)

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request. For any issues, please open an issue on GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or suggestions, feel free to contact me at [apooravmukherjee@gmail.com].

---

Thank you for using the Hotel Management System!
