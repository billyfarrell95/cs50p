# CS50P Final Project

## Requirements
* Your project must be implemented in Python.
* Your project must have a `main` function and three or more additional functions. At least three of those additional functions must be accompanied by tests that can be executed with `pytest`.
    * Your `main` function must be in a file called `project.py`, which should be in the “root” (i.e., top-level folder) of your project.
    * Your 3 required custom functions other than `main` must also be in `project.py` and defined at the same indentation level as `main` (i.e., not nested under any classes or functions).
    * Your test functions must be in a file called `test_project.py`, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with `test_` (`test_custom_function`, for example, where `custom_function` is a function you’ve implemented in `project.py`).
* You are welcome to implement additional classes and functions as you see fit beyond the minimum requirement.
* Implementing your project should entail more time and effort than is required by each of the course’s problem sets.
Any `pip`-installable libraries that your project requires must be listed, one per line, in a file called `requirements.txt` in the root of your project.


* Create DB if it does not exist
    * Create table
        * id (auto generated)
        * name
        * purchase price
        * purchase date
        * purchase location
* User input
    * Add item
        * Add to DB
        * Prints the item that was added
        * Continues prompting until cancelled
    * Delete item
        * Delete from DB by ID
        * Continues prompting until cancelled
    * View items
        * HTML?
        * Export as CSV
    * Clear history, does not exit program
    * Exit with message
    * Cancels the current operation (delete, add)