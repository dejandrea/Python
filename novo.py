# POO

#definindo a classe
class Contact_details:
#definindo os atributos
  def __init__(self,name,phoneNumber,email,address):
    self.contactName = name
    self.phoneNumber = phoneNumber
    self.contactEmail = email
    self.contactAddress = address

#criando um dicionário com os dados 
    self.person = {
        "name":self.contactName,
        "phoneNumber":self.phoneNumber,
        'email':self.contactEmail,
        'address':self.contactAddress
    }
  
  def displayContact(self,contact_list):
    print(contact_list)

  def addContactDetails(self,contact_list):
    contact_list.append(self.person)

contact1 = Contact_details("Andrea",73988483134,'dejandrea@gmail.com','Rua Juraci Benfica,103')
contact2 = Contact_details("João",73988483134,'joao@gmail.com','Rua Juraci Benfica,103')
contact3 = Contact_details("Pedro",73988483134,'pedro@gmail.com','Rua Juraci Benfica,103')
contact4 = Contact_details("Bryan",73988483134,'bryan@gmail.com','Rua Juraci Benfica,103')


listaContatos = []
contact1.addContactDetails(listaContatos)
contact2.addContactDetails(listaContatos)
contact3.addContactDetails(listaContatos)
contact4.addContactDetails(listaContatos)
contact1.displayContact(listaContatos)
