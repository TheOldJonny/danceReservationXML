from tkinter import StringVar, BooleanVar, IntVar
from customtkinter import filedialog, set_appearance_mode, CTkButton, CTkLabel, CTkOptionMenu, CTkCheckBox, CTk, CTkInputDialog, CTkEntry, CTkScrollableFrame
from tkinter import messagebox
from dance_reservations import SchoolReservations
import xml.etree.ElementTree as ET
from CTkTable import *

class VisualizeReservations:
    def __init__(self, parent, reservations):
        self.myParent = parent
        self.Reservations = reservations
        
        value = [["Nome","Cognome", "Pacchetto", "Check-in"]]

        table = CTkTable(master=self.myParent, row=1, column=4, values=value, header_color='grey')
        table.pack(expand=False, fill="both", padx=20, pady=20)
        
        # table.add_row(values=["Gino", "Pino", "gold"])
        
        counter = 0
        for person in self.Reservations.root.findall('persona'):
            name = person.find('nome').text
            surname = person.find('cognome').text
            package = person.find('pacchetto').text
            presence = person.find('presenza').text
            
            table.add_row(values=[name, surname, package, presence])
            counter+=1
            # if (presence == "Sì"):
            #     table.edit_row(row_index + 1, fg_color = 'green')
            
        for index in range(1, counter+1):
            row = table.get_row(index)
            if row[3] == 'Sì':
                table.edit_row(index, fg_color = 'green', border_color = 'green')
            
                
            
            
        

