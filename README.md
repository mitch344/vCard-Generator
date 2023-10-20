# vCard Generator

A simple and user-friendly application to manage and create vCards using a graphical user interface (GUI). Built with Tkinter, this application allows for easy management of contact information such as names, phone numbers, addresses, emails, and professional details.

<img src="https://raw.githubusercontent.com/MitchellKopczyk/vCard-Generator/b5e5ddbf1da65b5e683cde621ead12ab7aa4c9bd/image.png"/>
<div style="display: flex; justify-content: space-between; padding: 10px;">
    <img src="image2.png" alt="Image 2" width="300" height="700" style="max-width: 48%;" />
    <img src="image3.png" alt="Image 3" width="300" height="700" style="max-width: 48%;" />
</div>

## Features

### Add Contacts
- Manually add contacts by entering details like First Name, Last Name, Mobile Number, Home Phone, Address, Email, Organization, and Title.

### Load vCards
- Load existing vCards into the application.
- Option to merge the loaded vCard contacts with the existing contacts in the application.

### Update Contacts
- Modify the details of a selected contact and update the information as needed.

### Remove Contacts
- Select and remove contacts from the application.

### Generate vCards
- Export the contact information from the application into a vCard file which can be shared and used in other applications and devices.

### Merge vCards
- Easy to merge multiple vCards into one.

### Clear Entries
- An option to clear all input fields, preparing for a new contact entry.

### Treeview Display
- Contacts are displayed in a treeview which makes it easy to view and select contacts.

## Usage

- Run the application and use the GUI to manage contacts and vCards.
- Use the buttons provided to add, remove, update, and export contact information.
- Use the `Load vCard` button to load existing vCards into the application. You can choose to merge the loaded vCards or replace the existing entries.

## Notes

- When loading vCards, the application will only process and display specific properties. Additional properties in the vCard that are not explicitly handled by the application will be ignored.

## Dependencies

- Tkinter: A standard GUI library for Python is used to build the application interface.

## License

This project is licensed under the MIT License.

