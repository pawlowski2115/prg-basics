from contact import Contact

class ContactList:
    def __init__(self):
        self.contact_list = []

    def add_contact(self, contact_obj):
        self.contact_list.append(contact_obj)

    def display_contacts(self):
        for i in self.contact_list:
            print(f"{i.name:20}   {i.email:20}   {i.telephone}")