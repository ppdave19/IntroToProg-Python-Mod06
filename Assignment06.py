# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: A Course Registration Program using JSON, functions, and structured error handling.
# Change Log: Parth Dave, 08/20/2025, Modified Lab Code Modul06-Lab03 and Completed Assignment
# ------------------------------------------------------------------------------------------ #

import json

# Constants

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''

# Define the program's data

FILE_NAME: str = "Enrollments.json"
menu_choice: str = ''
students: list = []

# Defining - Class called - FileProcessor

class FileProcessor:
    """ Created Class
    Added function to read and write to JSON files
    A collection of processing layer functions that work with Json files
    ChangeLog: Parth Dave, 08/20/25, File IO handling class created
    """

    # When the program starts, read the file data into table
    # Extract the data from the file
    # Read from the Json file

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads student data from a JSON file into a list of dictionaries

        Args:
            file_name (str): The name of the file to read from
            student_data (list): The list to store the data into
        """

        file = None
        try:
            file = open(file_name, "r")
            data = json.load(file)
            student_data.extend(data)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except json.JSONDecodeError as e:
            IO.output_error_messages("File is empty or has invalid JSON format.", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes the student data to a JSON file

        Args:
            file_name (str): The name of the file to write to
            student_data (list): The data to write to the file
        """
        file = None
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            print("The following data was saved to the file:")
            IO.output_student_courses(student_data)
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

class IO:
    """
    Created IO Class: A collection of presentation layer functions that manage user input and output
    Added Function for Error Handling
    Added Function to print menu
    Added Function to input user choice
    Added Function to input Student Registration Data
    Added function to output current registration data

    ChangeLog:
    Parth Dave,08/20/2025,Created Class

    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """This function displays custom error messages to the user

        Args:
            message (str): Error message to display
            error (Exception, optional): The exception object
        """
        print(message, end="\n\n")

        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """This function displays the a menu of choices to the user

        changelog: Parth Dave, 08/20/2025
        Args:
            menu (str): The menu string to display

        """
        print()
        print(menu)
        print() # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice() -> str:
        """This function gets a menu choice from the user

        Returns:
            str: The user's menu choice
        """
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """This function gets the first name, last name, and ccourse from the user

        Args:
            student_data (list): The list to append new student record to
        """
        try:
            first_name = input("Enter the student's first name: ")
            if not first_name.isalpha():
                raise ValueError("First name must only contain letters.")

            last_name = input("Enter the student's last name: ")
            if not last_name.isalpha():
                raise ValueError("Last name must only contain letters.")

            course_name = input("Enter the course name: ")
            if not course_name:
                raise ValueError("Course name cannot be empty.")

            student = {"FirstName": first_name,
                       "LastName": last_name,
                       "CourseName": course_name}
            student_data.append(student)

            print(f"\nSuccessfully registered {first_name} {last_name} for {course_name}.\n")

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """This function displays current registration list

        Args:
            student_data (list): The list of student dictionaries
        """
        if not student_data:
            print("No student registrations found.\n")
            return

        print("\nCurrent Student Enrollments:")
        print("-" * 50)
        for student in student_data:
            print(f"{student['FirstName']}, {student['LastName']}, {student['CourseName']}")
        print("-" * 50 + "\n")

# Beginning of the main body of this script

# Load existing data from the file at the start
FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks

while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1": # Enter Student Registration
        IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2": # Display current data
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3": # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4": # End the program
        print("Exiting the program. Goodbye!")
        break # out of the while loop

