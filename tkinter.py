## MYSQL CRUD OPERATIONS USING TKINTER
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector

# Replace these with your actual database credentials
host = "localhost"
user = "root"
password = ""
database = "tk_trial"

# Establish the connection
connection = mysql.connector.connect(
    # Replace these with your actual database credentials
    host = "####", ### edit this
    user = "####" ,### edit this
    password = "######", ### edit this
    database = "#####"   #### edit this
)

# Create a cursor to interact with the database
cursor = connection.cursor()

root = Tk()
root.geometry("500x300")
root.title("Mysql crud")

# Define global variables for entry fields
id_entry = None
name_entry = None
phone_entry = None
def insert():
    id_label = Label(root, text="ID")
    id_label.pack()
    id_entry = Entry(root)
    id_entry.pack()

    name_label = Label(root, text="Name")
    name_label.pack()
    name_entry = Entry(root)
    name_entry.pack()

    phone_label = Label(root, text="Phone")
    phone_label.pack()
    phone_entry = Entry(root)
    phone_entry.pack()

    
def insert():
    id_label = Label(root, text="ID")
    id_label.pack()
    id_entry = Entry(root)
    id_entry.pack()

    name_label = Label(root, text="Name")
    name_label.pack()
    name_entry = Entry(root)
    name_entry.pack()

    phone_label = Label(root, text="Phone")
    phone_label.pack()
    phone_entry = Entry(root)
    phone_entry.pack()

    def insert_records():
        # Get values from the entry fields
        id = id_entry.get()
        name = name_entry.get()
        phone = phone_entry.get()

        # Check if any of the fields are empty
        if not id or not name or not phone:
            MessageBox.showinfo("ALERT", "Please enter all fields")
        else:
            try:
                # Execute the INSERT query
                query = "INSERT INTO person (id, name, phone) VALUES (%s, %s, %s)"
                cursor.execute(query, (id, name, phone))

                # Commit the changes to the database
                connection.commit()

                MessageBox.showinfo("Success", "Record inserted successfully")
            except Exception as e:
                MessageBox.showerror("Error", f"Error inserting record: {str(e)}")

        # Clear the entry fields after insertion
        id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')

    insert_button = Button(root, text="Insert", command=insert_records)
    insert_button.pack()

def delete():
    global id_entry
    
    # Create a new window for the delete operation
    delete_window = Toplevel(root)
    delete_window.title("Delete Record")

    # Create labels and entry field for ID in the delete window
    id_label = Label(delete_window, text="Enter ID to delete:")
    id_label.pack()
    id_entry = Entry(delete_window)
    id_entry.pack()

    def delete_record():
        id_to_delete = id_entry.get()
        if not id_to_delete:
            MessageBox.showinfo("ALERT", "Please enter the ID to delete")
        else:
            # Execute the DELETE query
            query = "DELETE FROM person WHERE id = %s"
            cursor.execute(query, (id_to_delete,))
            connection.commit()
            MessageBox.showinfo("Success", "Record deleted successfully")
            delete_window.destroy()

    # Create a button to trigger the delete operation
    delete_button = Button(delete_window, text="Delete", command=delete_record)
    delete_button.pack()

def update():
    global id_entry, name_entry, phone_entry
    
    # Create a new window for the update operation
    update_window = Toplevel(root)
    update_window.title("Update Record")

    # Create labels and entry fields for ID, Name, and Phone in the update window
    id_label = Label(update_window, text="Enter ID to update:")
    id_label.pack()
    id_entry = Entry(update_window)
    id_entry.pack()

    name_label = Label(update_window, text="New Name:")
    name_label.pack()
    name_entry = Entry(update_window)
    name_entry.pack()

    phone_label = Label(update_window, text="New Phone:")
    phone_label.pack()
    phone_entry = Entry(update_window)
    phone_entry.pack()

    def update_record():
        id_to_update = id_entry.get()
        new_name = name_entry.get()
        new_phone = phone_entry.get()
        
        if not id_to_update or not new_name or not new_phone:
            MessageBox.showinfo("ALERT", "Please enter all fields")
        else:
            # Execute the UPDATE query
            query = "UPDATE person SET name = %s, phone = %s WHERE id = %s"
            cursor.execute(query, (new_name, new_phone, id_to_update))
            connection.commit()
            MessageBox.showinfo("Success", "Record updated successfully")
            update_window.destroy()

    update_button = Button(update_window, text="Update", command=update_record)
    update_button.pack()



# Create buttons for insert, delete, and update operations in the main window
insert_button = Button(root, text="Insert", command=insert)
insert_button.pack()

delete_button = Button(root, text="Delete", command=delete)
delete_button.pack()

update_button = Button(root, text="Update", command=update)
update_button.pack()

root.mainloop()
