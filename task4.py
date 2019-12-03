class Contactlist(list):
    # def __init(self, name, surname):
    #     self.name = name
    #     self.surname = surname
    #     Contacts.all_contacts.append(self)
    
    def search(self, name):

        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = Contactlist()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

c1 = Contact('John A.', 'johna@example.net')
c2 = Contact('John B', 'johnb@example.net')
c3 = Contact('Jenna C', 'johnc@example.net')
print([c.name for c in Contact.all_contacts.search('John')])

