from tkinter import StringVar, BooleanVar, IntVar
from customtkinter import filedialog, set_appearance_mode, CTkButton, CTkLabel, CTkOptionMenu, CTkCheckBox, CTk, CTkInputDialog, CTkEntry
from tkinter import messagebox
from dance_reservations import SchoolReservations
import xml.etree.ElementTree as ET

class ModifyReservations:
    def __init__(self, parent, reservations, filename_xml):
        self.myParent = parent
        
        self.static_name = StringVar()
        self.static_name.set("nome")
        
        self.static_surname = StringVar()
        self.static_surname.set("cognome")
        
        self.static_package = StringVar()
        self.static_package.set("pacchetto")
        
        self.name = StringVar()
        self.name.set("")
        
        self.surname = StringVar()
        self.surname.set("")
        
        self.package = StringVar()
        self.package.set("")
        
        self.label_name = CTkLabel(self.myParent, textvariable = self.static_name)
        self.label_name.place(relx = 0.01, rely = 0.1)
        
        self.label_surname = CTkLabel(self.myParent, textvariable = self.static_surname)
        self.label_surname.place(relx = 0.01, rely = 0.2)
        
        self.label_package = CTkLabel(self.myParent, textvariable = self.static_package)
        self.label_package.place(relx = 0.01, rely = 0.3)
        
        self.entry_name = CTkEntry(self.myParent, placeholder_text="Inserisci il nome", textvariable=self.name)
        self.entry_name.place(relx = 0.2, rely = 0.1)
        
        self.entry_surname = CTkEntry(self.myParent, placeholder_text="Inserisci il cognome", textvariable=self.surname)
        self.entry_surname.place(relx = 0.2, rely = 0.2)
        
        self.entry_package = CTkEntry(self.myParent, placeholder_text="Inserisci il pacchetto", textvariable=self.package)
        self.entry_package.place(relx = 0.2, rely = 0.3)
        
        self.add_btn = CTkButton(self.myParent, command = lambda: self.OnAdd(), text="Aggiungi")
        self.add_btn.place(relx = 0.01, rely = 0.4)
        
        self.delete_btn = CTkButton(self.myParent, command = lambda: self.OnDelete(), text="Rimuovi")
        self.delete_btn.place(relx = 0.35, rely = 0.4)
        
        self.check_in = CTkButton(self.myParent, command = lambda: self.OnCheckIn(), text="Check in")
        self.check_in.place(relx = 0.75, rely = 0.4)
        
        self.save_btn = CTkButton(self.myParent, command = lambda: self.OnSave(), text="Salva")
        self.save_btn.place(relx = 0.2, rely = 0.7)
        
        self.cancel_btn = CTkButton(self.myParent, command = lambda: self.OnCancel(), text="Annulla")
        self.cancel_btn.place(relx = 0.6, rely = 0.7)
        
        self.Reservations = reservations
        self.filename_xml = filename_xml
        
        
        
        
        
    def OnAdd(self):
        if self.name.get() == '' or self.surname.get() == '' or self.package.get() == '':
            messagebox.showerror(title="ERRORE", message="I campi nome e cognome e pacchetto non possono essere lasciati vuoti per questa azione.")
            self.save_btn.configure(state = "disabled")
            return False
        
        if (self.Reservations.addPerson(self.name.get(), self.surname.get(), self.package.get())):
            messagebox.showinfo(title="SUCCESSO", message="La persona è stata correttamente aggiunta. Premi Salva per salvare le modifiche")
            self.name.set("")
            self.surname.set("")
            self.package.set("")
            self.save_btn.configure(state = "normal")
            return True
        
        else:
            messagebox.showerror(title="ERRORE", message="La persona è stata già inserita nel database di questa scuola")
            self.name.set("")
            self.surname.set("")
            self.package.set("")
            self.save_btn.configure(state = "disabled")
            return False  
        
    def OnCheckIn(self):
        # do not change the package name
        if self.name.get() == '' or self.surname.get() == '':
            messagebox.showerror(title="ERRORE", message="I campi nome e cognome non possono essere lasciati vuoti per questa azione.")
            return False
            
        if (self.Reservations.checkIn(self.name.get(), self.surname.get())):
            messagebox.showinfo(title="SUCCESSO", message="Hai effettuato correttamente il check in. Premi Salva per salvare le modifiche")
            self.name.set("")
            self.surname.set("")
            self.package.set("")
            self.save_btn.configure(state = "normal")
            return True
        else:
            messagebox.showerror(title="ERRORE", message="Non è stato possibile effettuare il check in per la persona richiesta.")
            self.name.set("")
            self.surname.set("")
            self.package.set("")
            self.save_btn.configure(state = "disabled")
            return False
            
    def OnCancel(self):
        self.myParent.destroy()
        
    def OnSave(self):
        
        condition = self.Reservations.writeReservationsXML(self.filename_xml, self.Reservations.root)
        if condition:
            messagebox.showinfo(title="SUCCESSO", message="Modifiche correttamente salvate.")
            self.name.set("")
            self.surname.set("")
            self.package.set("")
            return True
        else:
            messagebox.showerror(title="ERRORE", message="Impossibile scrivere le modifiche")
            self.name.set("")
            self.surname.set("")
            self.package.set("")
            return False  
    
    def OnDelete(self):
        if self.name.get() == '' and self.surname.get() == '':
            messagebox.showerror(title="ERRORE", message="I campi nome e cognome non possono essere lasciati vuoti per questa azione.")
            return False
        
        if (self.Reservations.removePerson(self.name.get(), self.surname.get())):
            messagebox.showinfo(title="SUCCESSO", message="La persona è stata correttamente rimossa. Premi il tasto ok per confermare.")
            self.name.set("")
            self.surname.set("")
            self.package.set("")
            return True
        
        else:
            messagebox.showerror(title="ERRORE", message="Non è stato rimuovere la prenotazione. Controllare se la persona è registrata nel database.")
            self.name.set("")
            self.surname.set("")
            self.package.set("")
            return False