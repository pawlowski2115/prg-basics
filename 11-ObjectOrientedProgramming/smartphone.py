from contact import Contact
from contact_list import ContactList


def main():
    con = ContactList()
    con.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
    con.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
    con.add_contact(Contact("George Small", "smallg@google.pl", "222999100"))
    con.add_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))
    con.display_contacts()

if __name__ == "__main__":
    main()