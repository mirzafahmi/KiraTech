# KiraTech Inventory Project

## Table of Contents
- [KiraTech Inventory Project](#kiratech-inventory-project)
  - [Table of Contents](#table-of-contents)
  - [How to Setup the project locally](#how-to-setup-the-project-locally)
  - [Super User Credential](#super-user-credential)

## How to Setup the project locally

1. Create Virtual Environment
   Change directory in the root of the project (same directory with README.MD). And run this command in terminal to create virtual enviroment.
   ```
    python -m venv venv
   ```

2. Activate Virtual Environment
   For Windows
   ```
    source venv\Scripts\activate
   ```
   For Mac/Linux
   ```
    source venv/bin/activate
   ```
3. Install Dependencies:
   To install the required packages for this project, run the following command in your terminal
   ```
   pip install -r requirements.txt
   ```
4. Run migration (skip this step if db.sqlite3 already exist in project folder)
   ```
   python manage.py migrate
   ```

5. Run seeder (skip this step if db.sqlite3 already exist in project folder)
   This will populate the database with some data and create super user.
    ```
      python manage.py seed_inventory
    ```
6. Run development server
   ```
   python manage.py runserver
   ```
7. Run test (need to run while the development server running)
   Open new terminal and activate the virtual enviroment as in step 2. Then run test command:
   ```
   python manage.py test
   ```

## Super User Credential
   ```
   Username: Admin
   Password: admin123
   ```