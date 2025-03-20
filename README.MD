# KiraTech Inventory Project

## Table of Contents
- [KiraTech Inventory Project](#kiratech-inventory-project)
  - [Table of Contents](#table-of-contents)
  - [How to Setup the project locally](#how-to-setup-the-project-locally)
  - [Default Super User Credential](#default-super-user-credential)

## How to Setup the project locally

1. Create Virtual Environment:
   <br>
   Change directory in the root of the folder (same directory with README.MD). And run this command in terminal to create virtual enviroment.
   <br>
   For Windows
   ```
    python -m venv venv
   ```
   For Mac/Linux
   ```
    python3 -m venv venv
   ```

2. Activate Virtual Environment:
   <br>
   For Windows
   ```
    source venv\Scripts\activate
   ```
   For Mac/Linux
   ```
    source venv/bin/activate
   ```
3. Install Dependencies:
   <br>
   To install the required packages for this project, run the following command in your terminal
   ```
   pip install -r requirements.txt
   ```

4. Change directory to the project folder:
   <br>
   Make sure you're in the same directory as `manage.py`:
   ```
   cd inventory_project
   ```

5. Run migration (skip this step if db.sqlite3 already exist in project folder and schema already set up):
   <br>
   For Windows
   ```
   python manage.py migrate
   ```
   For Mac/Linux
   ```
   python3 manage.py migrate
   ```

6. Run seeder (skip this step if db.sqlite3 already populated with seed data):
   <br>
   This will populate the database with sample inventory data and create a superuser for admin access.
   <br>
   For Windows
   ```
      python manage.py seed_inventory
   ```
   For Mac/Linux
   ```
      python3 manage.py seed_inventory
   ```

7. Run development server:
   <br>
   For Windows
   ```
   python manage.py runserver
   ```
   For Mac/Linux
   ```
   python3 manage.py runserver
   ```

8. Run test:
   <br>
   You can run tests without starting the development server.
   <br>
   For Windows
   ```
   python manage.py test
   ```
   For Mac/Linux
   ```
   python3 manage.py test
   ```


## Default Super User Credential
   ```
   Username: Admin
   Password: admin123
   ```