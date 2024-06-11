The Phonebook App 


is a simple Django-based web application that allows users to manage their contacts and their multiple phone numbers. Users can add new contacts, assign multiple phone numbers to each contact, view all contacts, and access contact details including their phone numbers.

Installation
-To set up the Phonebook App on your local machine, follow these steps:

NOTE {PLEASE COPY EVERY NUMBERED LINE IN YOUR TERMINAL WITHOUT THE NUBER AND THE DASH}

Clone the repository:

bash
*Copy code
1-git clone https://github.com/mohmmedshaker69/task
2-cd myproject

bash
*Copy code
1-pip install -r requirements.txt
2-Apply database migrations:

bash
Copy code
1-python manage.py makemigrations
2-python manage.py migrate
Start the development server:

bash
Copy code
1-python manage.py runserver
Access the application in your web browser at http://127.0.0.1:8000/.

Usage
Adding Contacts
Navigate to the home page.
Click on the "Add Contact" button.
Fill in the contact details, including the name and phone number(s).
Click the "Submit" button to add the contact.
Viewing Contacts
Navigate to the home page.
View all the contacts listed on the page.
Viewing Contact Details
Navigate to the home page.
Click on the name of a contact to view its details.
The details page will display the contact's name along with all associated phone numbers.
Adding Multiple Phone Numbers
When adding or editing a contact, use the provided form to input multiple phone numbers for the contact
Contributing
Contributions to the Phonebook App are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

![Screenshot (99)](https://github.com/mohmmedshaker69/task/assets/89956676/007b42aa-0395-44e6-9df6-936958b98339)
