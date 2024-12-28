# Restaurant Ordering System
This project is a simple Python console application for a restaurant's ordering system. It allows users to order items from a predefined menu, calculates the total cost of the order, and displays it at the end.

# Introduction
The idea for this project came from the need to create a basic interactive program to practice Python skills, particularly handling user input, dictionaries, and conditional logic. The program provides a user-friendly way to simulate ordering food items from a menu.

This application is ideal for beginners who are learning Python and want to work on a small project that involves:

# Input validation
Basic arithmetic operations
Using dictionaries for data storage and retrieval
Functionalities

# Displaying the Menu:
The program displays a list of available food items with their respective prices.
The menu is stored as a dictionary for easy management.
Placing an Order:

The user can enter the name of an item to order.
If the item exists in the menu, it is added to the total cost.
If the item does not exist, the user is informed that the item is unavailable.

# Adding Another Item:
After placing the first order, the user is prompted to decide whether to order another item.
If the user chooses to add another item, they can enter the name of the second item.
Calculating the Total Cost:

The program calculates and displays the total cost of all ordered items.
Case-Insensitive Input Handling:

User input is normalized to handle case sensitivity (e.g., "Pizza" and "pizza" are treated the same).
 
# How It Works
The program starts by displaying a welcome message and the menu.
The user enters the name of the first item they want to order.
If the item exists, it is added to the order, and the user is asked if they want to add another item.
The user can continue adding items or stop ordering.
The program calculates and displays the total cost of the order.

# Code Structure
Menu Dictionary: Stores the food items and their prices.
Input Validation: Ensures user input matches available items in the menu.
Order Total Calculation: Adds up the cost of all ordered items.
User Interaction: Prompts for item selection and decision-making.
Example Usage
Input:
plaintext
Copy code
Welcome to our Restaurant
pizza Rs90
pasta Rs50
Burger Rs70
salad Rs90
coffee Rs80
Enter the name of item you want to order = pizza
Your item pizza has been added to your order
Do you want to add another item? (Yes/No): yes
Enter the name of second item = coffee
Item coffee has been added to your order

# Output:

The total amount for your order is Rs170

# Dynamic Menu:
Allow administrators to update the menu dynamically.
Payment System:
Integrate a payment system to simulate a complete ordering experience.
Technologies Used
Language: Python
Concepts: Dictionaries, Conditional Statements, Loops, User Input
