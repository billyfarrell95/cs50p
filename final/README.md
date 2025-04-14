# CS50P Final Project

## Requirements
[View project requirements](https://cs50.harvard.edu/python/2022/project/)

## Functionality
* Create SQLite Database
    * Create table for ```items```
        * ```id``` (auto generated)
        * ```name```
        * ```purchase_price```
        * ```purchase_date```
        * ```purchase_location```
* Get user input and run actions
    * Provide usage instructions: ```(v)iew, (a)dd, (d)elete, (s)earch, (cl)ear, (ex)port or (e)xit```
    * View data
        1. Formats database rows as table by converting a ```list``` to a table using ```tabulate``` and prints the list
    * Add data
        1. Accepts and validates name, date, price and location
        2. Adds the validated input item to a list
        3. Executes ```INSERT``` to add the ```item``` to the ```items``` database table
    * Delete data
        1. Gets input for an ```id``` and validates it is an ```int```
        2. Checks if a row with ```id``` exists before executing ```DELETE```
    * Update data
        1. TODO
    * Search for data based on item ```name```
        1. Gets input for search term and validates the ```str```
        2. Query the database: ```SELECT * FROM items WHERE name LIKE CONCAT('%', ?, '%')``` and fetches the data
        3. Prints the data in a table or a "No items found message"
    * Clear user input history
        1. Clears user input history using ```os.system("cls")``` or ```os.system("clear")```
    * Export data
        1. Queries all of data in the database
        2. Formats as an ```HTML``` table using ```tabulate```
        3. Creates or updates the ```HTML``` file as ```output.html```
        4. Asks the user if they would like to open. If so, opens using: ```webbrowser.open("output.html", new=0)```
    * Exit the script
        1. The user can input ```e``` from the main menu level to exit the script
    * Cancel action
        1. While adding, deleting, or searching data, the user can input ```c``` to cancel the operation