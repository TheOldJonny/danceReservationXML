import xml.etree.ElementTree as ET
import os

class SchoolReservations:
    def __init__(self, school_name):
        self.school_name = school_name
    
        # it initializes the root of the xml file        
        self.root = ET.Element('Scuola', nome = self.school_name)
        
        # person = ET.SubElement(root, 'person')
        
    def addPerson(self, person_name, person_surname, package_name):
        
        condition = self.isAlreadyRegistered(person_name=person_name, person_surname=person_surname)
        if condition:
            print("Persona trovata")
            return False
        
        person = ET.SubElement(self.root, 'persona')
        name = ET.SubElement(person, 'nome')
        name.text = person_name
        name = ET.SubElement(person, 'cognome')
        name.text = person_surname
        package = ET.SubElement(person, 'pacchetto')
        package.text = package_name
        presence = ET.SubElement(person, 'presenza')
        presence.text = 'No'
        return True
    
    def removePerson(self, person_name, person_surname):
        for person in self.root.findall('persona'):
            if person.find('nome').text.lower() == person_name.lower() and person.find('cognome').text.lower() == person_surname.lower():
                self.root.remove(person)
                return True
        
        return False
        
        
    def isAlreadyRegistered(self, person_name, person_surname):
        for person in self.root.findall('persona'):
            if person.find('nome').text.lower() == person_name.lower() and person.find('cognome').text.lower() == person_surname.lower():
                return True
            
        return False           
               
    def checkIn(self, person_name, person_surname):
        for person in self.root.findall('persona'):
            if person.find('nome').text.lower() == person_name.lower() and person.find('cognome').text.lower() == person_surname.lower():
                person.find('presenza').text = 'Sì'
                return True
            
        return False
    
    def __len__(self):
        return len(self.root.findall('persona'))
       
    @staticmethod     
    def writeReservationsXML(filename, root):
        try:
            tree = ET.ElementTree(root)
            ET.indent(tree=tree, level = 1)
            tree.write(filename, encoding="utf-16")
            return True
        except:
            return False
        
    @staticmethod
    def readReservationsXML(filename):
        # method that read an xml file and returns an instance of school reservations
        try:
            xml_tree = ET.parse(filename)

            root = xml_tree.getroot()

            el = root.find('Scuola')
            myInstance = SchoolReservations(root.find('Scuola'))
            myInstance.root = root
            return myInstance
        except:
            return None
            

        
        
        
        
if __name__ == "__main__":
    sr = SchoolReservations("Ritmoteque")
    # sr.addPerson("Jonathan", "Campeggio", "red")

    # sr.addPerson("Luca", "Lucente", "blue")
    # sr.addPerson("Giacomo", "Baldini", "gold")

    # sr.removePerson("Luca", "Lucente")

    # sr.checkIn("Giacomo", "Baldini")

    # print(len(sr))

    # sr.writeReservationsXML("gino.xml", sr.root)
    
    # my_el = sr.readReservationsXML("gino.xml")
    
    sr.writeReservationsXML("aaaa.xml", sr.root)
    
        
    







