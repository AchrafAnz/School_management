from tkinter import*
from tkinter import ttk
paiements_window_open = False

Al_Manar = Tk()
Al_Manar.geometry('1100x750+20+20')
Al_Manar.title('Al_Manar_School')
#Al_Manar.iconbitmap('C:\\users\Achraf\Desktop\\al_manar_school\\3986707-building-education-school-school-icon_112987.ico')

def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"


def focus_previous_widget(event):
    
        event.widget.tk_focusPrev().focus()
        return "break"
    
#--------------------------HEADER-------------------------

Header_label= Label(Al_Manar,text='Al_Manar_School',font=30,fg='black',bg='#7B7C7E')
Header_label.pack(fill=X)



#---------------------------------------------------------------------------------------------------
#------------------------- COMBOBOXES AND THEIR LABELS And button ----------------------------------

Matiere_label = Label(Al_Manar,text='Matière',font=20)
Matiere_label.place(x=10,y=60)

Matière_Combobox= ttk.Combobox(Al_Manar,value=('Maths','Physics','Svt','Philosophie','Arabe','Education_islamique'),state='readonly')
Matière_Combobox.place(x=10,y=90)

Matière = Matière_Combobox.get()


Niveau1_label = Label(Al_Manar,text='Niveau',font=20)
Niveau1_label.place(x=200,y=60)
Niveau1_Combobox= ttk.Combobox(Al_Manar,value=('Bac_2eme','Bac_1er','Tron_commun','College_3eme','College_2eme','College_1er'),state='readonly')
Niveau1_Combobox.place(x=200,y=90)

Niveau1 = Niveau1_Combobox.get()

Groupe_label = Label(Al_Manar,text='Groupe',font=20)
Groupe_label.place(x=400,y=60)
Groupe_Combobox= ttk.Combobox(Al_Manar,value=('1','2','3','4','5'),state='readonly')
Groupe_Combobox.place(x=400,y=90)

Groupe=Groupe_Combobox.get()

Chercher_Button = Button(Al_Manar,text='Chercher',bg='#9B979C',fg='black',font=15)
Chercher_Button.place(x=600,y=80)


import mysql.connector 
from mysql.connector import Error
import tkinter as tk

def connect_db():
   try: 
        connection = mysql.connector.connect(
        host='localhost',
        user= 'root',
        password='',
        database='Al_Manar_School'
                                            )
        if connection.is_connected():
            print('Connection au database avec succsès')
            return connection
   except Error as e:
       print(f"connection to database failed: {e}")
       return None

    
result123 = ''
#-----------------------------------------------------------------------
def searsh_students():
    Selected_Subject = Matière_Combobox.get()
    Selected_level = Niveau1_Combobox.get()
    Selected_group = Groupe_Combobox.get()           
    
    connection = connect_db()
    if connection : 
        cursor = connection.cursor()
        if Selected_group and Selected_level and Selected_Subject :  
            query = f"SELECT* FROM {Selected_Subject} WHERE Niveau = %s AND groupe = %s"
            cursor.execute(query,(Selected_level,Selected_group))
            results = cursor.fetchall()
            
            for row in tree.get_children():
                tree.delete(row)
        
            if results :
                 indexe = 1
                 from datetime import datetime
                 for data in results :
                   data = list(data)
    # Formatage de la date si nécessaire
                   if data[1]:  # Supposons que date_ajout est à l'index 9
                      data[1] = datetime.strptime(str(data[1]), '%Y-%m-%d').strftime('%d/%m/%Y')
                   # Replace None values with '___'
                   data = tuple('___' if value is None else value for value in data)
                   tree.insert('', 'end', values=(indexe,)+data)
                   indexe += 1
            else : 
                print("pas d'etudiants jusqu'a maintenant")
                Listbox_students.delete(0, tk.END)
                alert_message= "  Pas d'etudiants jusqu'a maintenant"
                Listbox_students.insert(0, alert_message)
                Listbox_students.itemconfig(tk.END, fg="blue")
            cursor.close()
            connection.close()
        else : 
            
                Listbox_students.delete(0, tk.END)
                err_message1= "   Données insufisants remplissez toutes"
                err_message_suivi1 = "     les cases !!!!"
                Listbox_students.insert(0, err_message1)
                Listbox_students.insert(1,err_message_suivi1)
                Listbox_students.itemconfig(0, fg="red")
                Listbox_students.itemconfig(1, fg="red")
                global result123
                result123 = 'stop'
                return
                
    else : 
                Listbox_students.delete(0, tk.END)
                Listbox_students.delete(1,tk.END)
                err_message2= " Connection au database impossible !!!"
                err_message2_suivi="  lancer votre serveur dans Xampp puis"
                err_message2_suivi1=" réessayer"
                Listbox_students.insert(0, err_message2)
                Listbox_students.insert(1,err_message2_suivi)
                Listbox_students.insert(2,err_message2_suivi1)
                Listbox_students.itemconfig(0, fg="red")
                Listbox_students.itemconfig(1, fg="red")
                Listbox_students.itemconfig(2, fg="red")


#-------------------------------------- la 2 ieme fenetre -------------------------------------------------------------




def Lancer_Liste_etudiant():
      import tkinter as tk
      global Listbox_students
      Listbox_students = tk.Listbox(Al_Manar, width=60, height=5)
      Listbox_students.place(x=720, y=60)
      Selected_Subject = Matière_Combobox.get()
      Selected_level = Niveau1_Combobox.get()
      Selected_group = Groupe_Combobox.get() 
      if not Selected_group or not Selected_level or not Selected_Subject :
          return
      Header_label_Frame= Frame(width='2000',height='30',bg='#7294BF')
      Header_label_Frame.place(x=1,y=180)

      Header_label= Label(Header_label_Frame,text='Liste des étudiants',font=30,fg='black',bg='#7294BF')
      Header_label.place(x=550,y=1)

      

      Nom2_label = Label(Al_Manar,text='Nom',font=20)
      Nom2_label.place(x=10,y=210)
      Nom2_entry = Entry(Al_Manar,justify='center')
      Nom2_entry.bind("<Return>", focus_next_widget)
      Nom2_entry.bind("<Right>", focus_next_widget)
      Nom2_entry.bind("<Left>", focus_previous_widget)
      Nom2_entry.place(x=10,y=240)
      Nom2=Nom2_entry.get()

      prénom2_label = Label(Al_Manar,text='Prénom',font=20)
      prénom2_label.place(x=150,y=210)
      prénom2_entry = Entry(Al_Manar,justify='center')
      prénom2_entry.bind("<Return>", focus_next_widget)
      prénom2_entry.bind("<Right>", focus_next_widget)
      prénom2_entry.bind("<Left>", focus_previous_widget)
      prénom2_entry.place(x=150,y=240)
      prénom2=prénom2_entry.get()

      telephone1_label = Label(Al_Manar,text='telephone1',font=20)
      telephone1_label.place(x=300,y=210)
      telephone1_entry = Entry(Al_Manar,justify='center')
      telephone1_entry.bind("<Return>", focus_next_widget)
      telephone1_entry.bind("<Right>", focus_next_widget)
      telephone1_entry.bind("<Left>", focus_previous_widget)
      telephone1_entry.place(x=300,y=240)
      telephone1=telephone1_entry.get()

      telephone2_label = Label(Al_Manar,text='telephone2',font=20)
      telephone2_label.place(x=450,y=210)
      telephone2_entry = Entry(Al_Manar,justify='center')
      telephone2_entry.bind("<Return>", focus_next_widget)
      telephone2_entry.bind("<Right>", focus_next_widget)
      telephone2_entry.bind("<Left>", focus_previous_widget)
      telephone2_entry.place(x=450,y=240)
      telephone2=telephone2_entry.get()

      paiement_label = Label(Al_Manar,text='montant de paiement',font=20)
      paiement_label.place(x=600,y=210)
      paiement_entry = Entry(Al_Manar,justify='center')
      paiement_entry.bind("<Return>", focus_next_widget)
      paiement_entry.bind("<Right>", focus_next_widget)
      paiement_entry.bind("<Left>", focus_previous_widget)
      paiement_entry.place(x=600,y=240)
      montant_paiement=paiement_entry.get()

      

     
      Listbox_students1 = Listbox(Al_Manar,width=30,height=4)
      Listbox_students1.bind("<Left>", focus_previous_widget)
      Listbox_students1.place(x=900,y=220)
      Listbox_students1.delete(0,tk.END)
      Listbox_students1.delete(1,tk.END)
      Listbox_students1.delete(2,tk.END)
      Listbox_students1.insert(0,f"   {Matière_Combobox.get()}")
      Listbox_students1.insert(1,f"   {Niveau1_Combobox.get()}")
      Listbox_students1.insert(2,f"   Groupe : {Groupe_Combobox.get()}")
      Listbox_students1.itemconfig(0,fg='blue')
      Listbox_students1.itemconfig(1,fg='blue')
      Listbox_students1.itemconfig(2,fg='blue')
      
      
      def Ajouter_Eleve():
        matiere = Matière_Combobox.get()
        niveau = Niveau1_Combobox.get()
        groupe = Groupe_Combobox.get()
        nom = Nom2_entry.get()
        prenom = prénom2_entry.get()
        tele1 = telephone1_entry.get()
        tele2 = telephone2_entry.get()
        paiement = paiement_entry.get()
    
        connection = connect_db()
        if connection : 
          cursor = connection.cursor()
          try:
            if nom and prenom and tele1 and tele2 and paiement : 
              #cursor.execute("insert into %s values (null,%s,%s,%s,%s,%s,%s,%s,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null)",(matiere,niveau,groupe,nom,prenom,tele1,tele2,paiement))
              query = "INSERT INTO `{}` (`Niveau`, `groupe`, `Nom`, `Prenom`, `telephone1`, `Telephone2`, `Paiement`) VALUES (%s, %s, %s, %s, %s, %s, %s)".format(matiere)
              values = (niveau, groupe, nom, prenom, tele1, tele2, paiement)
              cursor.execute(query, values)
              connection.commit()
              
              Listbox_students.delete(0, tk.END)
              success_message = "Etudiant ajouté avec succès"
              Listbox_students.insert(0, success_message)
              Listbox_students.itemconfig(tk.END, fg="green")
            
              Nom2_entry.delete(0,tk.END)
              prénom2_entry.delete(0,tk.END)
              telephone1_entry.delete(0,tk.END)
              telephone2_entry.delete(0,tk.END)
              paiement_entry.delete(0,tk.END)

              searsh_students()
            else : 
                Listbox_students.delete(0, tk.END)
                error_message = "Remplissez toutes les cases svp !!!"
                Listbox_students.insert(0, error_message)
                Listbox_students.itemconfig(tk.END, fg="red")  
          except Error as e : 
            Listbox_students.delete(0, tk.END)
            error_message = f"Erreur : {e}"
            Listbox_students.insert(0, error_message)
            Listbox_students.itemconfig(tk.END, fg="red")
          finally:
            cursor.close()
            connection.close()    
        else : 
           Listbox_students.delete(0, tk.END)

           error_message = "Erreur de connexion à la base de données"
           Listbox_students.insert(0, error_message)
           Listbox_students.itemconfig(tk.END, fg="red")

      ajouter_Button = Button(Al_Manar,text='Ajouter',bg='#727CBF',fg='black',font=15,command=Ajouter_Eleve)
      ajouter_Button.place(x=810,y=220)
    

#TREEVIEW  
    
      global tree 
      columns = ("order","ID" ,"Date d'ajout","Niveau", "groupe",  "Nom", "Prénom","telephone1", "telephone2", "Montant_paiement","Mois_09","Date_Paiement_Mois_09","Montant_Paye_Au_Mois_09","Mois_10","Date_Paiement_Mois_10","Montant_Paye_Au_Mois_10","Mois_11","Date_Paiement_Mois_11","Montant_Paye_Au_Mois_11","Mois_12","Date_Paiement_Mois_12","Montant_Paye_Au_Mois_12","Mois_01","Date_Paiement_Mois_01","Montant_Paye_Au_Mois_01","Mois_02","Date_Paiement_Mois_02","Montant_Paye_Au_Mois_02","Mois_03","Date_Paiement_Mois_03","Montant_Paye_Au_Mois_03","Mois_04","Date_Paiement_Mois_04","Montant_Paye_Au_Mois_04","Mois_05","Date_Paiement_Mois_05","Montant_Paye_Au_Mois_05","Mois_06","Date_Paiement_Mois_06","Montant_Paye_Au_Mois_06","Mois_07","Date_Paiement_Mois_07","Montant_Paye_Au_Mois_07")
      tree = ttk.Treeview(Al_Manar, columns=columns, show='headings')
       # Define headings
      tree.heading("order", text="Ordre")
      tree.heading("ID",text="ID (unique) ")
      tree.heading("Date d'ajout",text="Date d'ajout ")
      tree.heading("Niveau", text="Niveau")
      tree.heading("groupe", text="Groupe")
      tree.heading("Nom", text="Nom")
      tree.heading("Prénom", text="Prénom")
      tree.heading("telephone1", text="Téléphone 1")
      tree.heading("telephone2", text="Téléphone 2")
      tree.heading("Montant_paiement", text="Montant_paiement")
      tree.heading("Mois_09",text="Mois 9")
      tree.heading("Date_Paiement_Mois_09",text="Date_Paiement_Mois_09")
      tree.heading("Montant_Paye_Au_Mois_09",text="Montant_Payé_Au_Mois_09")
      tree.heading("Mois_10",text="Mois 10")
      tree.heading("Date_Paiement_Mois_10",text="Date_Paiement_Mois_10")
      tree.heading("Montant_Paye_Au_Mois_10",text="Montant_Payé_Au_Mois_10")
      tree.heading("Mois_11",text="Mois 11")
      tree.heading("Date_Paiement_Mois_11",text="Date_Paiement_Mois_11")
      tree.heading("Montant_Paye_Au_Mois_11",text="Montant_Payé_Au_Mois_11")
      tree.heading("Mois_12",text="Mois 12")
      tree.heading("Date_Paiement_Mois_12",text="Date_Paiement_Mois_12")
      tree.heading("Montant_Paye_Au_Mois_12",text="Montant_Payé_Au_Mois_12")
      tree.heading("Mois_01",text="Mois 1")
      tree.heading("Date_Paiement_Mois_01",text="Date_Paiement_Mois_01")
      tree.heading("Montant_Paye_Au_Mois_01",text="Montant_Payé_Au_Mois_01")
      tree.heading("Mois_02",text="Mois 2")
      tree.heading("Date_Paiement_Mois_02",text="Date_Paiement_Mois_02")
      tree.heading("Montant_Paye_Au_Mois_02",text="Montant_Payé_Au_Mois_02")
      tree.heading("Mois_03",text="Mois 3")
      tree.heading("Date_Paiement_Mois_03",text="Date_Paiement_Mois_03")
      tree.heading("Montant_Paye_Au_Mois_03",text="Montant_Payé_Au_Mois_03")
      tree.heading("Mois_04",text="Mois 4")
      tree.heading("Date_Paiement_Mois_04",text="Date_Paiement_Mois_04")
      tree.heading("Montant_Paye_Au_Mois_04",text="Montant_Payé_Au_Mois_04")
      tree.heading("Mois_05",text="Mois 5")
      tree.heading("Date_Paiement_Mois_05",text="Date_Paiement_Mois_05")
      tree.heading("Montant_Paye_Au_Mois_05",text="Montant_Payé_Au_Mois_05")
      tree.heading("Mois_06",text="Mois 6")
      tree.heading("Date_Paiement_Mois_06",text="Date_Paiement_Mois_06")
      tree.heading("Montant_Paye_Au_Mois_06",text="Montant_Payé_Au_Mois_06")
      tree.heading("Mois_07",text="Mois 7")
      tree.heading("Date_Paiement_Mois_07",text="Date_Paiement_Mois_07")
      tree.heading("Montant_Paye_Au_Mois_07",text="Montant_Payé_Au_Mois_07")


      for col in columns:
        tree.column(col, width=160, anchor=CENTER, stretch=NO) 


      Tree_scrollbar_y = Scrollbar(Al_Manar, orient=VERTICAL, command=tree.yview)
      Tree_scrollbar_y.config(command=tree.yview)

      Tree_scrollbar_x = Scrollbar(Al_Manar, orient=HORIZONTAL, command=tree.xview)
      Tree_scrollbar_x.config(command=tree.xview)
      
      tree.config(yscrollcommand=Tree_scrollbar_y.set, xscrollcommand=Tree_scrollbar_x.set)
      tree.place(x=20,y=300,width=1000,height=400)
      Tree_scrollbar_y.place(relx=0.5, rely=0.5, anchor='w', x=500, y=120,height=350,) # Adjust 'x' and 'height' as needed
      Tree_scrollbar_x.place(relx=0.5, rely=0.5, anchor='n', x=1,y=330, width=900)


      

      def Open_Paiements_window(event):
       global paiements_window_open, Paiements_window
    
       if paiements_window_open:
        # Si la fenêtre est déjà ouverte, on la met au premier plan
        Paiements_window.lift()
        return
    
       paiements_window_open = True
       try: 
        
        selected_item = tree.selection()[0]  # Get selected item
        student_data = tree.item(selected_item)['values']  # Get data of selected item
        List_Of_Paid_months =[]
        for index, value in enumerate(student_data):
           if value =='✅':
              List_Of_Paid_months.append(index)  
        List_Of_Paid_months1 = []        
        for k in List_Of_Paid_months : 
           if k == 10 :  List_Of_Paid_months1.append('09')
           if k == 13 :  List_Of_Paid_months1.append('10')
           if k == 16 :  List_Of_Paid_months1.append('11')
           if k == 19 :  List_Of_Paid_months1.append('12')
           if k == 22 :  List_Of_Paid_months1.append('01')
           if k == 25 :  List_Of_Paid_months1.append('02')
           if k == 28 :  List_Of_Paid_months1.append('03')
           if k == 31 :  List_Of_Paid_months1.append('04')
           if k == 34 :  List_Of_Paid_months1.append('05')
           if k == 37 :  List_Of_Paid_months1.append('06')
           if k == 40 :  List_Of_Paid_months1.append('07')
                          
        
        
    # Create new window
        
        Paiements_window = Toplevel(Al_Manar)
        Paiements_window.geometry("1440x500")
        Paiements_window.config(background='#E3ECED') 

        Student_name=student_data[5]
        Student_surname = student_data[6]
        
        
    
        if Student_name != str(Student_name) : 
            Student_name = str(Student_name)
        if Student_surname != str(Student_surname) : 
            Student_surname = str(Student_surname)

       

        Header_Paiements_frame = Frame(Paiements_window,width=800,height=30,bg='#94CE9B')
        Header_Paiements_frame.place(x=351,y=1)
        Name_surname_label=Label(Header_Paiements_frame,text=Student_name+' '+Student_surname,bg='#94CE9B',font=10)
        Name_surname_label.place(x=330,y=1)
        Header_student_paiement = Label(Header_Paiements_frame,text='Ajouter paiement pour :',font=10,fg='black',bg='#94CE9B')
        Header_student_paiement.place(x=110,y=1)
    # create modificatiom : 
        Modification_frame = Frame(Paiements_window,width=1000,height=30,bg='#706981')
        Modification_frame.place(x=950,y=1)
        Modification_label=Label(Modification_frame,text='Modification pour : '+Student_name+' '+Student_surname,bg='#706981',font=10,fg='#DED4FB')
        Modification_label.place(x=80,y=1)
        
        
# ...

        Modification_Combobox = ttk.Combobox(Paiements_window, values=('Nom', 'Prenom', 'groupe', 'Niveau', 'Telephone1', 'Telephone2', 'Montant_de_Paiement','Matière'), state='readonly')
        Modification_Combobox.place(x=1000, y=80)
        Modification_Combobox.bind("<<ComboboxSelected>>", lambda x,arg=Modification_Combobox: update_assignment_details(arg))
        enter_Niveau_label = Label(Paiements_window,text="Selectionnez le Niveau ",font=10)
        Niveau_Modification_Combobox = ttk.Combobox(Paiements_window, values=('Bac_2eme','Bac_1er','Tron_commun','College_3eme','College_2eme','College_1er'), state='readonly')
        enter_Niveau_label.place(x=3000,y=60)
        Niveau_Modification_Combobox.place(x=3000,y=88)

        enter_groupe_label = Label(Paiements_window,text="Selectionnez le groupe ",font=10)
        groupe_Modification_Combobox = ttk.Combobox(Paiements_window, values=('1','2','3','4','5'), state='readonly')
        enter_groupe_label.place(x=3000,y=60)
        groupe_Modification_Combobox.place(x=3000,y=88)
        
        enter_matiere_label =Label(Paiements_window,text='Selectonnez la Matiere',font=10)
        enter_matiere_label.place(x=3000,y=60)
        enter_matiere_combobox=ttk.Combobox(Paiements_window,value=('Maths','Physics','Svt','Philosophie','Arabe','Education_islamique'),justify='center',state='readonly')
        enter_matiere_combobox.place(x=3000,y=85)
    
        def update_assignment_details(event):
            Quoi_Modifier1 = Modification_Combobox.get()
            print(Quoi_Modifier1)
            
            if Quoi_Modifier1 == 'Niveau' or Quoi_Modifier1 == 'Matière' or Quoi_Modifier1 == 'groupe':
             if Quoi_Modifier1 == 'Matière' :

                Modification_entry.place_forget()
                Modification_label_entry.place_forget()   
                groupe_Modification_Combobox.place_configure(x=3000,y=88)
                enter_groupe_label.place_configure(x=3000,y=60)             
                enter_Niveau_label.place_configure(x=3000,y=60)
                Niveau_Modification_Combobox.place_configure(x=3000,y=88)
                enter_matiere_combobox.place_configure(x=1200,y=75)
                enter_matiere_label.place_configure(x=1200,y=50)

                 
             elif Quoi_Modifier1 == 'Niveau' :  
               
               groupe_Modification_Combobox.place_forget()
               enter_groupe_label.place_forget()          
               Modification_entry.place_forget()
               Modification_label_entry.place_forget()     
               enter_Niveau_label.place_configure(x=1200,y=50)
               Niveau_Modification_Combobox.place_configure(x=1200,y=75)
               enter_matiere_combobox.place_forget()
               enter_matiere_label.place_forget()

             elif Quoi_Modifier1 == 'groupe':
               
               groupe_Modification_Combobox.place_configure(x=1200,y=75)
               enter_groupe_label.place_configure(x=1200,y=50)             
               Modification_entry.place_forget()
               Modification_label_entry.place_forget()     
               enter_Niveau_label.place_forget()
               Niveau_Modification_Combobox.place_forget()
               enter_matiere_combobox.place_forget()
               enter_matiere_label.place_forget()
                                  
            else : 
               enter_Niveau_label.place_configure(x=3000,y=60)
               Niveau_Modification_Combobox.place_configure(x=3000,y=88)
               Modification_entry.place(x=1200,y=75)
               Modification_label_entry.place(x=1200,y=50)
               enter_matiere_combobox.place_configure(x=3000,y=88)
               enter_matiere_label.place_configure(x=3000,y=60)
               groupe_Modification_Combobox.place_configure(x=3000,y=88)
               enter_groupe_label.place_configure(x=3000,y=60)  

                 

        
            

        Modification_label_combobox=Label(Paiements_window,text='Quoi Modifier ?',font=10)
        Modification_label_combobox.place(x=1000,y=50)
        
        Modification_label_entry=Label(Paiements_window,text='Entrer la modification',font=10)
        Modification_label_entry.place(x=1200,y=50)
        Modification_entry=Entry(Paiements_window,justify='center',font=10)
        Modification_entry.place(x=1200,y=75)
        
        
        Listbox_Modification = tk.Listbox(Paiements_window,width=50,height=5)
        Listbox_Modification.place(x=1050,y=180)
       

        vertical_frame=Frame(Paiements_window,bg='#909497',width=10,height=1000)
        vertical_frame.place(x=950,y=1)

        vertical_frame=Frame(Paiements_window,bg='#909497',width=10,height=1000)
        vertical_frame.place(x=341,y=1)
       


        Supprimer_Paiement_frame = Frame(Paiements_window,bg='#706981',width=599,height=30)
        Supprimer_Paiement_frame.place(x=351,y=280)
        Supprimer_Paiement_label=Label(Supprimer_Paiement_frame,text='Supprimer un mois de paiement pour : '+Student_name+' '+Student_surname,bg='#706981',font=10,fg='#DED4FB')
        Supprimer_Paiement_label.place(x=40,y=1)
        
        

        Mois_a_supprimer_label=Label(Paiements_window,text='Mois_à_supprimer',font=10)
        Mois_a_supprimer_label.place(x=550,y=330)
        
        Listbox_Supprimer_mois = tk.Listbox(Paiements_window,width=50,height=5)
        Listbox_Supprimer_mois.place(x=620,y=400)
        Mois_a_supprimé_dict = {"mois":""}

         
      #-----------------------------------------------------------------------------------------------------------------------------
        def Supprimer_eleve():
            if name_surname_dict["kniya"] !="": 
                        
                        temp_name = name_surname_dict["kniya"]
            else :    
                        temp_name = Student_name
            if name_surname_dict["smiya"] !="": 
                        
                        temp_surname = name_surname_dict["smiya"]
            else :    
                        temp_surname = Student_surname
            def supprimer():               
                cnx1=connect_db()
                if cnx1 : 
                    cursor12=cnx1.cursor()
                    try :
                        if Matiere_changé_dict["Matiere"] == "":
                            subject12 = Matière_Combobox.get()
                        else :
                            subject12 = Matiere_changé_dict["Matiere"]    
                        cursor12.execute(f"delete from {subject12} where Id = {student_data[1]}")
                        cnx1.commit()
                        Listbox_students.delete(0,tk.END)
                        Listbox_students.delete(1,tk.END)
                        Listbox_students.insert(0," Modification faite avec succées")
                        Listbox_students.insert(1," "+temp_name+" "+temp_surname+" est Supprimé avec succées")
                        Listbox_students.itemconfig(0, fg="green")
                        Listbox_students.itemconfig(1, fg="green")
                        cursor12.close()
                        cnx1.close()
                        you_sure_window.destroy()
                        global paiements_window_open
                        paiements_window_open = False
                        Paiements_window.destroy()
                        
                        
                        searsh_students()
                    except Error as e : 
                        error = f"{Error}"    
                        Listbox_students.delete(0,tk.END)
                        Listbox_students.delete(1,tk.END)
                        Listbox_students.insert(0,error)
                        Listbox_students.itemconfig(0, fg="red")

            you_sure_window = Toplevel()
            you_sure_window.geometry("600x200+600+400")
            you_sure_window.resizable(False,False)
            header = Label(you_sure_window,text=' Etes vous sure de Supprimer '+temp_name+' '+temp_surname+' de la liste ??? ',fg='black',bg='silver',font=20)
            header.pack(fill=X)
            Ok_button = Button(you_sure_window,text='Oui',bg='green',font=10,command=supprimer)
            Ok_button.place(x=225,y=110)
            No_button = Button(you_sure_window,text='Non',bg='red',font=10,command=you_sure_window.destroy)
            No_button.place(x=325,y=110)
            

        Supprimer_eleve_frame= Frame(Paiements_window,width=1000,height=30, bg='#706981')
        Supprimer_eleve_frame.place(x=960,y=280)
        Supprimer_eleve_label=Label(Supprimer_eleve_frame,text='Supprimer '+Student_name+' '+Student_surname+' de la liste ',bg='#706981',font=10,fg='#DED4FB')
        Supprimer_eleve_label.place(x=60,y=1)
        Supprimer_eleve_button = Button(Paiements_window,text='Supprimer '+Student_name+' '+Student_surname, font=10, bg='#FF0000',command=Supprimer_eleve)
        Supprimer_eleve_button.place(x=1120,y=350)
        
    

        List12 = []
        name_surname_dict = {"kniya":"","smiya":""}
        Telephone_changés_dict = {"tele1":"","tele2":""}
        Groupe_changés_dict = {"groupe":""}
        Nom_Prenom_changés = {"Nom":"","Prenom":""}
        Niveau_changé_dict = {"Niveau":""}
        Matiere_changé_dict = {"Matiere":""}
        
        cnx=connect_db()
        if Matiere_changé_dict["Matiere"] == "":
                            subject2 = Matière_Combobox.get()
        else :
                            subject2 = Matiere_changé_dict["Matiere"] 
        if cnx:
                cursor1 = cnx.cursor() # Define the query to get the payment status for all months
                query = f"""
    SELECT 
        Mois09, Mois10, Mois11, Mois12, Mois01, Mois02, 
        Mois03, Mois04, Mois05, Mois06, Mois07
    FROM {subject2}
    WHERE Id = {student_data[1]}
    """

                cursor1.execute(query)
                
                result = cursor1.fetchone()

                cursor1.close()
                cnx.close()

    # Check which months are paid
                months = [
        'Mois09', 'Mois10', 'Mois11', 'Mois12', 'Mois01', 
        'Mois02', 'Mois03', 'Mois04', 'Mois05', 'Mois06', 'Mois07'
               ]

                paid_months = list(result)
        mois_payé = []
        for i in range(4,11):
            if paid_months[i] =='✅':
                    mois_payé.append('0'+str(i-3)) 
        for k in range(0,4):
            if paid_months[k] == '✅':
                if k==0 : mois_payé.append('0'+str(k+9)) 
                mois_payé.append(k+9)
                        
        
        
        Mois_a_supprimer_combobox = ttk.Combobox(Paiements_window,values = tuple(mois_payé),state='readonly')
        Mois_a_supprimer_combobox.place(x=550,y=360)
        def supprimer1_mois() :
          le_mois_a_supprimer=Mois_a_supprimer_combobox.get()
          if le_mois_a_supprimer:
            le_mois_a_supprimer=Mois_a_supprimer_combobox.get()
            you_sure_window2 = Toplevel()
            you_sure_window2.geometry("600x200+600+400")
            you_sure_window2.resizable(False,False)
            header2 = Label(you_sure_window2,text="Etes vous sure de Supprimer le Mois "+le_mois_a_supprimer+" des paiements ",fg='black',bg='silver',font=20)
            header2.pack(fill=X)
            
            def supprimer2_mois():   
                global subject
                if Matiere_changé_dict["Matiere"] == "":
                            subject = Matière_Combobox.get()
                else :
                            subject = Matiere_changé_dict["Matiere"]  
                
                mois_int=int(le_mois_a_supprimer)
                cnx=connect_db()
                if cnx : 
                 cursor1=cnx.cursor()
                
                 try :
                  
                    column_mois = f"Mois{mois_int:02d}"
                    
                    column_date_paiement = f"Date_Paiement_Mois{mois_int:02d}"
                    column_montant_paye = f"Montant_Paye_Au_Mois_{mois_int:02d}"

                    query = f"""
                       UPDATE `{subject}`
                        SET `{column_mois}` = NULL,
                     `{column_date_paiement}` = NULL,
                     `{column_montant_paye}` = NULL
                      WHERE `Id` = {student_data[1]}
                            """
                    cursor1.execute(query)
                    cnx.commit()
                    cursor1.close()
                    cnx.close()
                    you_sure_window2.destroy()
                    searsh_students()
                    vertical_table = create_vertical_table(Paiements_window, student_data)
                    Listbox_Supprimer_mois.delete(0,tk.END)
                    Listbox_Supprimer_mois.delete(1,tk.END)
                    Listbox_Supprimer_mois.insert(0," le mois "+le_mois_a_supprimer+" est Supprimé avec succées")
                    Listbox_Supprimer_mois.itemconfig(0, fg="green")

                    values12 = list(Mois_a_supprimer_combobox['values'])
                    values12.remove(Mois_a_supprimer_combobox.get())
                    Mois_a_supprimer_combobox['values'] = values12
                    Mois_a_supprimer_combobox.set('')

                    values123 = list(Mois_combobox['values'])
                    values123.append(le_mois_a_supprimer)
                    Mois_combobox['values'] = values123
                    Mois_combobox.set('')
            




                    return
                                      
                  
                 except Error as e :
                    Listbox_Supprimer_mois.delete(0,tk.END)
                    Listbox_Supprimer_mois.delete(1,tk.END)
                    Listbox_Supprimer_mois.insert(0,f"{Error}")
                    Listbox_Supprimer_mois.itemconfig(0, fg="red")
                    return
            Ok_button2 = Button(you_sure_window2,text='Oui',bg='green',font=10,command=supprimer2_mois)
            Ok_button2.place(x=225,y=110)
            No_button2 = Button(you_sure_window2,text='Non',bg='red',font=10,command=you_sure_window2.destroy)
            No_button2.place(x=325,y=110) 
          else :   
                    Listbox_Supprimer_mois.delete(0,tk.END)
                    Listbox_Supprimer_mois.delete(1,tk.END)
                    Listbox_Supprimer_mois.insert(0,"choisissez le mois a supprimer")
                    Listbox_Supprimer_mois.itemconfig(0, fg="red")
                    return 
             
        

        Supperimer_mois_button = Button(Paiements_window,text='Supprimer Mois',bg='#FF4C4C',font=10,command=supprimer1_mois)
        Supperimer_mois_button.place(x=750,y=350)
        montant_paiement_changé_dict={"montant":""}
        def Modifier():
            
            Quoi_Modifier = Modification_Combobox.get()
            Enter_Modification = Modification_entry.get()
            if Matiere_changé_dict["Matiere"]!="":
                 la_matiere = Matiere_changé_dict["Matiere"]
            else :
                 la_matiere = Matière_Combobox.get()     
            student_id = student_data[1]
            cnx=connect_db()
            Niveau_a_changer = Niveau_Modification_Combobox.get()
            Matiere_a_changer = enter_matiere_combobox.get()
            groupe_a_changer = groupe_Modification_Combobox.get()
           

            if cnx : 
                cursor11 = cnx.cursor()
                
                try : 
                    if Quoi_Modifier=='Matière' and Matiere_a_changer and enter_matiere_combobox.winfo_x()==1200 and enter_matiere_combobox.winfo_y()==75 : 
                                if name_surname_dict["kniya"] !="": 
                                 temp_name = name_surname_dict["kniya"]
                                else :    
                                 temp_name = Student_name
                                if name_surname_dict["smiya"] !="": 
                                 temp_surname = name_surname_dict["smiya"]
                                else :    
                                 temp_surname = Student_surname
                               
                                selected_matiere = Matière_Combobox.get()
                                if Matiere_changé_dict["Matiere"] !="":
                                  selected_matiere = Matiere_changé_dict["Matiere"]
                                
                                if  Matiere_a_changer == selected_matiere or Matiere_a_changer == Matiere_changé_dict["Matiere"]:
                                    Listbox_Modification.delete(0,tk.END)
                                    Listbox_Modification.delete(1,tk.END)
                                    Listbox_Modification.insert(1,temp_name+" "+temp_surname+" existe deja dans la matiere:",Matiere_a_changer)
                                    Listbox_Modification.itemconfig(1, fg="red")
                                    Listbox_Modification.itemconfig(0, fg="red")
                                    cursor11.close()
                                    cnx.close()
                                    return 
                                
                                Listbox_Modification.delete(0,tk.END)
                                Listbox_Modification.delete(1,tk.END)
                                Listbox_Modification.insert(0," Modification faite avec succées")
                                Listbox_Modification.insert(1," "+temp_name+" "+temp_surname+" est transférée vers la Matiere : "+Matiere_a_changer)
                                Listbox_Modification.itemconfig(0, fg="green")
                                Listbox_Modification.itemconfig(1, fg="green")
                                


                                query = "INSERT INTO `{}` VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(Matiere_a_changer)
                                List_info = []
                                #for i in range(1,43) :
                                    #List_info.append(student_data[i])
                                import datetime    
                                #date_obj = datetime.datetime.strptime(temp_values123[1], '%d/%m/%Y')
                                #temp_values123[1]=date_obj.strftime('%Y-%m-%d')

                                if Matiere_changé_dict["Matiere"]=="":
                                  ma_matiere = Matière_Combobox.get()
                                else : 
                                    ma_matiere = Matiere_changé_dict["Matiere"]  
                                Matiere_changé_dict["Matiere"] = Matiere_a_changer
                                query1 = f"SELECT* FROM {ma_matiere} WHERE Id = {student_data[1]}"
                                cursor11.execute(query1)
                                results1 = cursor11.fetchall()
                                temp_values123 = results1[0]
                                values123=tuple(temp_values123)    
                                print(values123)
                                cursor11.execute(query, values123)
                                cnx.commit()
                                delete_query = "delete from "+ma_matiere+" where Id= {}".format(student_data[1])
                                searsh_students()
                                cursor11.execute(delete_query)
                                cnx.commit()
                                searsh_students()
                                cursor11.close()
                                cnx.close()
                                return
                                    


                  
                    if Quoi_Modifier=='Niveau' and Niveau_a_changer and Niveau_Modification_Combobox.winfo_x() == 1200 and  Niveau_Modification_Combobox.winfo_y() == 75 :
                                if name_surname_dict["kniya"] !="": 
                                 temp_name = name_surname_dict["kniya"]
                                else :    
                                 temp_name = Student_name
                                if name_surname_dict["smiya"] !="": 
                                 temp_surname = name_surname_dict["smiya"]
                                else :    
                                 temp_surname = Student_surname
                                selected_niveau = student_data[3]
                                if Niveau_changé_dict["Niveau"]!="":
                                    selected_niveau = Niveau_changé_dict["Niveau"]
                                if Niveau_a_changer == selected_niveau  or Niveau_a_changer == Niveau_changé_dict["Niveau"]: 
                                    Listbox_Modification.delete(0,tk.END)
                                    Listbox_Modification.delete(1,tk.END)
                                    Listbox_Modification.insert(1,temp_name+" "+temp_surname+" existe deja dans le niveau :",Niveau_a_changer)
                                    Listbox_Modification.itemconfig(1, fg="red")
                                    Listbox_Modification.itemconfig(0, fg="red")
                                    cursor11.close()
                                    cnx.close()
                                    return 
                                Niveau_changé_dict["Niveau"] = Niveau_a_changer 
                                Listbox_Modification.delete(0,tk.END)
                                Listbox_Modification.delete(1,tk.END)
                                Listbox_Modification.insert(0," Modification faite avec succées")
                                Listbox_Modification.insert(1," "+temp_name+" "+temp_surname+" est transférée vers le Niveau : "+Niveau_a_changer)
                                Listbox_Modification.itemconfig(0, fg="green")
                                Listbox_Modification.itemconfig(1, fg="green")
                                query = 'update {} set {} = %s where Id = %s'.format(la_matiere, Quoi_Modifier)
                                values23=( Niveau_a_changer, student_id)
                                cursor11.execute(query,values23)
                                cnx.commit()
                                searsh_students()
                                cursor11.close()
                                cnx.close()
                                return
                    if Quoi_Modifier=='groupe' and groupe_a_changer and groupe_Modification_Combobox.winfo_x() == 1200 and  groupe_Modification_Combobox.winfo_y() == 75 :
                            if name_surname_dict["kniya"] !="": 
                                 temp_name = name_surname_dict["kniya"]
                            else :    
                                 temp_name = Student_name
                            if name_surname_dict["smiya"] !="": 
                                 temp_surname = name_surname_dict["smiya"]
                            else :    
                                 temp_surname = Student_surname   
                            selected_groupe = str(student_data[4])     
                            if Groupe_changés_dict["groupe"] !="":
                                selected_groupe = Groupe_changés_dict["groupe"]
                            if groupe_a_changer==selected_groupe:
                                Listbox_Modification.delete(0,tk.END)
                                Listbox_Modification.delete(1,tk.END)
                                Listbox_Modification.insert(1,temp_name+" "+temp_surname+" existe deja dans le goupe :",groupe_a_changer)
                                Listbox_Modification.itemconfig(1, fg="red")
                                Listbox_Modification.itemconfig(0, fg="red")
                                cursor11.close()
                                cnx.close()
                                return 
                            if groupe_a_changer == Groupe_changés_dict["groupe"]:
                                Listbox_Modification.delete(0,tk.END)
                                Listbox_Modification.delete(1,tk.END)
                                Listbox_Modification.insert(1,temp_name+" "+temp_surname+" est deja transféré vers le goupe : ",groupe_a_changer)
                                Listbox_Modification.itemconfig(0, fg="red")
                                Listbox_Modification.itemconfig(1, fg="red")
                                cursor11.close()
                                cnx.close()
                                return
                            
                            
                            else :
                                Groupe_changés_dict["groupe"]=groupe_a_changer
                                Listbox_Modification.delete(0,tk.END)
                                Listbox_Modification.delete(1,tk.END)
                                Listbox_Modification.insert(0," Modification faite avec succées")
                                Listbox_Modification.insert(1," "+temp_name+" "+temp_surname+" est transférée vers le Groupe : "+groupe_a_changer)
                                Listbox_Modification.itemconfig(0, fg="green")
                                Listbox_Modification.itemconfig(1, fg="green")
                                
                                query = 'update {} set {} = %s where Id = %s'.format(la_matiere, Quoi_Modifier)
                                values23=( groupe_a_changer, student_id)
                                cursor11.execute(query,values23) 
                                cnx.commit()
                                searsh_students()
                                return
                            
                    if Quoi_Modifier and Enter_Modification : 
                        if Quoi_Modifier == 'Montant_de_Paiement':
                            if name_surname_dict["kniya"] !="": 
                                 temp_name = name_surname_dict["kniya"]
                            else :    
                                 temp_name = Student_name
                            if name_surname_dict["smiya"] !="": 
                                 temp_surname = name_surname_dict["smiya"]
                            else :    
                                 temp_surname = Student_surname  
                            selected_paiement = student_data[9]
                            if Enter_Modification == selected_paiement : 
                                Listbox_Modification.delete(0,tk.END)
                                Listbox_Modification.delete(1,tk.END)
                                Listbox_Modification.insert(1,"ce montant existe deja :",Enter_Modification)
                                Listbox_Modification.itemconfig(1, fg="red")
                                Listbox_Modification.itemconfig(0, fg="red")
                                cursor11.close()
                                cnx.close()
                                return 
                            if Enter_Modification == montant_paiement_changé_dict['montant'] : 
                                Listbox_Modification.delete(0,tk.END)
                                Listbox_Modification.delete(1,tk.END)
                                Listbox_Modification.insert(1,"ce montant existe deja :",Enter_Modification)
                                Listbox_Modification.itemconfig(1, fg="red")
                                Listbox_Modification.itemconfig(0, fg="red")
                                cursor11.close()
                                cnx.close()
                                return 
                            montant_paiement_changé_dict["montant"]=Enter_Modification
                            Listbox_Modification.delete(0,tk.END)
                            Listbox_Modification.delete(1,tk.END)
                            Listbox_Modification.insert(0," Modification faite avec succées")
                            Listbox_Modification.insert(1," le montant est changée en : "+Enter_Modification)
                            Listbox_Modification.itemconfig(0, fg="green")
                            Listbox_Modification.itemconfig(1, fg="green")
                            query = 'update {} set Paiement = %s where Id = %s'.format(la_matiere, Quoi_Modifier)
                            values23=( Enter_Modification, student_id)
                            cursor11.execute(query,values23) 
                            cnx.commit()
                            searsh_students()
                            return     

                        
                        
                        #if Quoi_Modifier == 'Niveau':
                        if Quoi_Modifier == 'Telephone1' or Quoi_Modifier =='Telephone2' : 
                            
                            if name_surname_dict["kniya"] !="": 
                                 temp_name = name_surname_dict["kniya"]
                            else :    
                                 temp_name = Student_name
                            if name_surname_dict["smiya"] !="": 
                                 temp_surname = name_surname_dict["smiya"]
                            else :    
                                 temp_surname = Student_surname     


                            if Quoi_Modifier == 'Telephone1':
                              selected_tele1 = str(student_data[7])
                              if Telephone_changés_dict["tele1"] != "":
                                  selected_tele1 = Telephone_changés_dict["tele1"]
                              if Enter_Modification == selected_tele1:
                                  Listbox_Modification.delete(0,tk.END)
                                  Listbox_Modification.delete(1,tk.END)
                                  Listbox_Modification.insert(0," le "+Quoi_Modifier+" de "+temp_name+" "+temp_surname+" est deja : "+Enter_Modification)
                                  Listbox_Modification.itemconfig(0, fg="red")
                                  Listbox_Modification.itemconfig(1, fg="red")
                                  cursor11.close()
                                  cnx.close()
                                  return
  
                              if Enter_Modification == Telephone_changés_dict["tele1"] : 
                                  Listbox_Modification.delete(0,tk.END)
                                  Listbox_Modification.delete(1,tk.END)
                                  Listbox_Modification.insert(0," le "+Quoi_Modifier+" de "+temp_name+" "+temp_surname+" est deja changé en "+Enter_Modification)
                                  Listbox_Modification.itemconfig(0, fg="red")
                                  Listbox_Modification.itemconfig(1, fg="red")
                                  cursor11.close()
                                  cnx.close()
                                  return
                            if Quoi_Modifier == 'Telephone2':
                              selected_tele2 = str(student_data[8])
                              if Telephone_changés_dict["tele2"] != "":
                                  selected_tele2 = Telephone_changés_dict["tele2"]
                              if Enter_Modification == selected_tele2:
                                  Listbox_Modification.delete(0,tk.END)
                                  Listbox_Modification.delete(1,tk.END)
                                  Listbox_Modification.insert(0," le "+Quoi_Modifier+" de "+temp_name+" "+temp_surname+" est deja : "+Enter_Modification)
                                  Listbox_Modification.itemconfig(0, fg="red")
                                  Listbox_Modification.itemconfig(1, fg="red")
                                  cursor11.close()
                                  cnx.close()
                                  return
                              if Enter_Modification == Telephone_changés_dict["tele2"] : 
                                  Listbox_Modification.delete(0,tk.END)
                                  Listbox_Modification.delete(1,tk.END)
                                  Listbox_Modification.insert(0," le "+Quoi_Modifier+" de "+temp_name+" "+temp_surname+" est deja changé en "+Enter_Modification)
                                  Listbox_Modification.itemconfig(0, fg="red")
                                  Listbox_Modification.itemconfig(1, fg="red")
                                  cursor11.close()
                                  cnx.close()
                                  return
                            
                            if Quoi_Modifier =='Telephone1' : 
                                    Telephone_changés_dict["tele1"]=Enter_Modification
                            if Quoi_Modifier =='Telephone2' : 
                                    Telephone_changés_dict["tele2"]=Enter_Modification
                            query = 'update {} set {} = %s where Id = %s'.format(la_matiere, Quoi_Modifier)
                            values23=( Enter_Modification, student_id)
                            cursor11.execute(query,values23) 
                            cnx.commit()   
                            Listbox_Modification.delete(0,tk.END)
                            Listbox_Modification.delete(1,tk.END)
                            Listbox_Modification.insert(0," le "+Quoi_Modifier+" de "+temp_name+" "+temp_surname+" est changé en "+Enter_Modification)
                            Listbox_Modification.itemconfig(0, fg="green")  
                            searsh_students()    
                            cursor11.close()
                            cnx.close()
                            return
                            
                            
                        if Quoi_Modifier == 'Nom':
                            if name_surname_dict["kniya"] !="": 
                                 temp_name = name_surname_dict["kniya"]
                            else :    
                                 temp_name = Student_name
                            
                            if name_surname_dict["smiya"] !="": 
                                smiya = name_surname_dict["smiya"]
                            else : smiya = Student_surname
                            selected_nom = str(student_data[5])
                            
                            if Enter_Modification == selected_nom or Enter_Modification==name_surname_dict["kniya"]:
                                name_surname_dict["kniya"]=Enter_Modification
                                Listbox_Modification.delete(0,tk.END)
                                Listbox_Modification.delete(1,tk.END)
                                Listbox_Modification.insert(1,"le nom de  "+temp_name+" "+smiya+" est deja : "+Enter_Modification)
                                Listbox_Modification.itemconfig(0, fg="red")
                                Listbox_Modification.itemconfig(1, fg="red")  
                                cursor11.close()
                                cnx.close()
                                return
                            
                                
                            name_surname_dict["kniya"]=Enter_Modification
                            query = 'update {} set {} = %s where Id = %s'.format(la_matiere, Quoi_Modifier)
                           
                            values23=( Enter_Modification, student_id)
                            cursor11.execute(query,values23) 
                            cnx.commit() 
                            Listbox_Modification.delete(0,tk.END)
                            Listbox_Modification.delete(1,tk.END)
                            Listbox_Modification.insert(0," Modification faite avec succées")
                            Listbox_Modification.insert(1,"le nom de  "+temp_name+" "+smiya+" est changé en : "+Enter_Modification)
                            Listbox_Modification.itemconfig(0, fg="green")
                            Listbox_Modification.itemconfig(1, fg="green")
                            Name_surname_label.config(text=Enter_Modification + ' ' +smiya)  # Update the label
                            Modification_label.config(text='Modification pour : ' + Enter_Modification + ' ' + smiya)  # Update the label 
                            Supprimer_Paiement_label.config(text='Supprimer un mois de paiement pour : '+Enter_Modification+' '+smiya)
                            Supprimer_eleve_label.config(text='Supprimer '+Enter_Modification+' '+smiya+' de la liste ')
                            Supprimer_eleve_button.config(text='Supprimer '+Enter_Modification+' '+smiya, font=10, bg='#FF0000')
                            
                            cursor11.close()
                            cnx.close()
                            print("from nom ",List12)
                            searsh_students()
                            cursor11.close()
                            cnx.close()
                            return
                        if Quoi_Modifier == 'Prenom':
                            if name_surname_dict["smiya"] !="": 
                                 temp_surname = name_surname_dict["smiya"]
                            else :    
                                 temp_surname = Student_surname
                            
                            if name_surname_dict["kniya"] !="": 
                                kniya = name_surname_dict["kniya"]
                            else : kniya = Student_name    
                            selected_prenom = str(student_data[6])
                            
                            if Enter_Modification == selected_prenom or Enter_Modification==name_surname_dict["smiya"]:
                                name_surname_dict["smiya"]=Enter_Modification
                                Listbox_Modification.delete(0,tk.END)
                                Listbox_Modification.delete(1,tk.END)
                                Listbox_Modification.insert(1,"le Prenom de  "+kniya+" "+temp_surname+" est deja : "+Enter_Modification)
                                Listbox_Modification.itemconfig(0, fg="red")
                                 
                                cursor11.close()
                                cnx.close()
                                return
                            
                                
                            name_surname_dict["smiya"]=Enter_Modification
                            query = 'update {} set {} = %s where Id = %s'.format(la_matiere, Quoi_Modifier)
                           
                            values23=( Enter_Modification, student_id)
                            cursor11.execute(query,values23) 
                            cnx.commit() 
                            Listbox_Modification.delete(0,tk.END)
                            Listbox_Modification.delete(1,tk.END)
                            Listbox_Modification.insert(0," Modification faite avec succées")
                            
                            Listbox_Modification.insert(1,"le prenom de  "+kniya+" "+temp_surname+" est changé en : "+Enter_Modification)
                            Listbox_Modification.itemconfig(0, fg="green")
                            Listbox_Modification.itemconfig(1, fg="green")
                            Name_surname_label.config(text=kniya + ' ' + Enter_Modification)  # Update the label
                            Modification_label.config(text='Modification pour : ' + kniya+ ' ' + Enter_Modification)  # Update the label 
                            Supprimer_Paiement_label.config(text='Supprimer un mois de paiement pour : '+kniya+' '+Enter_Modification)
                            Supprimer_eleve_label.config(text='Supprimer '+kniya+' '+Enter_Modification+' de la liste ')
                            Supprimer_eleve_button.config(text='Supprimer '+kniya+' '+Enter_Modification, font=10, bg='#FF0000')
                            print("from prenom ",List12)
                            cursor11.close()
                            cnx.close()
                            cursor11.close()
                            cnx.close()
                            searsh_students()
                        
                            return
                        
                            
                            
                        Listbox_Modification.delete(0,tk.END)
                        Listbox_Modification.delete(1,tk.END)
                        Listbox_Modification.insert(0," Modification faite avec succées")
                        Listbox_Modification.itemconfig(tk.END, fg="green")
                    else : 
                        Listbox_Modification.delete(0,tk.END)
                        Listbox_Modification.delete(1,tk.END)
                        Listbox_Modification.insert(0,"remplissez toutes les cases !!")
                        Listbox_Modification.itemconfig(tk.END, fg="red")
                except Error as e :
                        print(f"erreur {e}")
                        Listbox_Modification.delete(0,tk.END)
                        Listbox_Modification.delete(1,tk.END)
                        Listbox_Modification.insert(0,f"Erreur : {e}")
                        Listbox_Modification.itemconfig(tk.END, fg="red")
                finally : 
                    searsh_students()
                    vertical_table = create_vertical_table(Paiements_window, student_data)
                    vertical_table.place(x=1,y=1)
                    cursor11.close()
                    cnx.close()
            else :
                    Listbox_Modification.delete(0,tk.END)
                    Listbox_Modification.insert(0,"ERREUR DE CONNEXION AU DATABASE !!!")
                    Listbox_Modification.itemconfig(tk.END, fg="red")

            searsh_students()
            vertical_table = create_vertical_table(Paiements_window, student_data)
            vertical_table.place(x=1,y=1)


       
        Modification_Button=Button(Paiements_window,text='Modifier',bg='#867F9B',font=10,command = Modifier,fg='#DED4FB')
        Modification_Button.place(x=1200,y=120)


        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(f"SELECT *, DATE_FORMAT(date_ajout, '%m') AS mois_ajout FROM {Matière_Combobox.get()} WHERE Id={student_data[1]}")
        results1 = cursor.fetchall()
        cursor.close()
        connection.close()
        
        Mois_ajout=int(results1[0][-1])
        List = [9,10,11,12,1,2,3,4,5,6,7]
        i=Mois_ajout
        indice_mois_ajout = List.index(i)
        List=List[indice_mois_ajout:]
        List.sort()
        
        Les_Mois_De_Paiement = []
        
        for k in List:
            if k<= 9 :
                le_mois = '0'+str(k)
            else : 
                le_mois = str(k)
            Les_Mois_De_Paiement.append(le_mois)
        

        Mois_label=Label(Paiements_window,text='Mois',font=10)
        Mois_label.place(x=575,y=50)
        Mois_combobox = ttk.Combobox(Paiements_window,value=tuple(Les_Mois_De_Paiement),state='readonly')
        Mois_combobox.place(x=550,y=80)
        values3 = list(Mois_combobox['values'])

        for k in List_Of_Paid_months1: 
              values3.remove(k)
        Mois_combobox['values'] = values3
        

        Montant_a_payer_Label = Label(Paiements_window,text='Montant à payer',font=10)
        Montant_a_payer_Label.place(x=360,y=50)
        Montant_a_payer_entry = Entry(Paiements_window,justify='center', fg = 'black',bg='white')
        Montant_a_payer_entry.place(x=370,y=82)

        Date_Paiement_label = Label(Paiements_window,text='Date de paiement',font=10)
        Date_Paiement_label.place(x=740,y=50)
        Date_Paiement_entry = Entry(Paiements_window,justify='center', fg = 'black',bg='white')
        Date_Paiement_entry.place(x=750,y=82)

        Listbox_Paiements = tk.Listbox(Paiements_window,width=50,height=5)
        Listbox_Paiements.place(x=450,y=180)
        
        if not values3 :
                    Listbox_Paiements.delete(0, tk.END)
                    success_message = "Tous les mois sont payés Felicitation !!!!"
                    Listbox_Paiements.insert(0, success_message)
                    Listbox_Paiements.itemconfig(tk.END, fg="red")
        Les_mois_payé = []
        def Ajouter_paiement():
        
            Mois_a_payer=Mois_combobox.get()
            if Mois_a_payer == '' :
                    Listbox_Paiements.delete(0, tk.END)
                    erro = "selectionnez un mois !!!!"
                    Listbox_Paiements.insert(0, erro)
                    Listbox_Paiements.itemconfig(tk.END, fg="red")
                    return
               
            print("le Mois_a_payer est:",Mois_a_payer,",")
            mois_int=int(Mois_a_payer)
            Montant_a_payer1=Montant_a_payer_entry.get()
            Date_Paiement10=Date_Paiement_entry.get()
            la_matiere = Matière_Combobox.get()
            student_id = student_data[1]
            connection1=connect_db()
            if connection1:
                cursor2=connection1.cursor()
                try:
                  if Mois_a_payer and Montant_a_payer1 and Date_Paiement10 :
                    column_mois = f"Mois{mois_int:02d}"
                    print(column_mois)
                    column_date_paiement = f"Date_Paiement_Mois{mois_int:02d}"
                    column_montant_paye = f"Montant_Paye_Au_Mois_{mois_int:02d}"

                    query = f"""
                       UPDATE `{la_matiere}`
                        SET `{column_mois}` = '✅',
                     `{column_date_paiement}` = %s,
                     `{column_montant_paye}` = %s
                      WHERE `Id` = %s
                            """
                    values = (Date_Paiement10, Montant_a_payer1, student_id)
                    cursor2.execute(query,values)
                    #cursor2.execute(f"update {Matière} set Mois"+Mois_a_payer+" = '✅' and Date_Paiement_Mois"+Mois_a_payer+f" = '{Date_Paiement10}' and  Montant_Paye_Au_Mois_"+Mois_a_payer+f" = '{Montant_a_payer1}'  ")
                    connection1.commit()
                    
                    temp_values=list(Mois_a_supprimer_combobox['values'])
                    temp_values.append(Mois_a_payer)
                    Mois_a_supprimer_combobox['values'] = temp_values
                    Mois_a_supprimer_combobox.set("")

                    Listbox_Paiements.delete(0, tk.END)
                    success_message = "Paiement ajouté avec succès"
                    Listbox_Paiements.insert(0, success_message)
                    Listbox_Paiements.itemconfig(tk.END, fg="green")
                   
                    values = list(Mois_combobox['values'])
                    values.remove(Mois_combobox.get())
                    Mois_combobox['values'] = values
                    Mois_combobox.set('')
                    Montant_a_payer_entry.delete(0, tk.END)
                    Date_Paiement_entry.delete(0, tk.END)
                  else:
                   Listbox_Paiements.delete(0, tk.END)
                   error_message = "Remplissez toutes les cases svp !!!"
                   Listbox_Paiements.insert(0, error_message)
                   Listbox_Paiements.itemconfig(tk.END, fg="red")
                except Error as e:
                  Listbox_Paiements.delete(0, tk.END)
                  error_message = f"Erreur : {e}"
                  print(error_message)
                  Listbox_Paiements.insert(0, error_message)
                  Listbox_Paiements.itemconfig(tk.END, fg="red")
                finally:
                  cursor2.close()
                  connection1.close()
            else:
              Listbox_Paiements.delete(0, tk.END)
              error_message = "Erreur de connexion à la base de données"
              Listbox_Paiements.insert(0, error_message)
              Listbox_Paiements.itemconfig(tk.END, fg="red")

            searsh_students()  
            vertical_table = create_vertical_table(Paiements_window, student_data)
            vertical_table.place(x=1,y=1)
     

        #--------------------------------------------------TreeView--------------------------------------------------------

        def create_vertical_table(parent, student_data):
    # Create a frame to hold the treeview
          frame = Frame(parent,width=5.7*60,height=600)
          frame.place(x=1,y=1)

    # Create the treeview
          columns = ("Attribute", "Value")
          tree1 = ttk.Treeview(frame, columns=columns, show="headings", height=30)
          tree1.pack(side=LEFT, fill=BOTH, expand=1)

    # Define headings
          tree1.heading("Attribute", text="Attribut")
          tree1.heading("Value", text="Valeur")

    # Set column widths
          tree1.column("Attribute", width=170, anchor=W)
          tree1.column("Value", width=170, anchor=W)

    # Add rows to the treeview
          if Matiere_changé_dict["Matiere"] == "":
                            subject1 = Matière_Combobox.get()
          else :
                            subject1 = Matiere_changé_dict["Matiere"]  
          cnx3 = connect_db()
          if cnx3:
           cursor3=cnx3.cursor()
           query3 = f"SELECT* FROM {subject1} WHERE Id = {student_data[1]}"
           cursor3.execute(query3)
           results3 = cursor3.fetchall()                  
           infos = list(results3[0])   
           months1=[infos[9],infos[12],infos[15],infos[18],infos[21],infos[24],infos[27],infos[30],infos[33],infos[36],infos[39]]   
           
           for i in range(11) :
                if months1[i]== None :
                     months1[i] = '___'
                  
          attributes = [
        ("ID", student_data[1]),
        ("Date d'ajout", student_data[2]),
        ("Matiere",subject1),
        ("Niveau",infos[2]),
        ("Groupe",infos[3]),
        ("Nom",infos[4]),
        ("Prénom",infos[5]),
        ("Téléphone 1",infos[6]),
        ("Téléphone 2",infos[7]),
        ("Montant paiement",infos[8]),
        ("Mois 09",months1[0]),
        ("Mois 10",months1[1]),
        ("Mois 11",months1[2]),
        ("Mois 12",months1[3]),
        ("Mois 01",months1[4]),
        ("Mois 02",months1[5]),
        ("Mois 03",months1[6]),
        ("Mois 04",months1[7]),
        ("Mois 05",months1[8]),
        ("Mois 06",months1[9]),
        ("Mois 07",months1[10])
                                 ]

          for attr, value in attributes:
           tree1.insert("", "end", values=(attr, value))

          return tree1
        
        vertical_table = create_vertical_table(Paiements_window, student_data)
        vertical_table.place(x=1,y=1)
        Ajouter_paiement_Button = Button(Paiements_window,text='Ajouter Paiement💲💰',font=10,bg='#8DEC9A',command=Ajouter_paiement)
        Ajouter_paiement_Button.place(x= 590,y=122)
        Paiements_window.protocol("WM_DELETE_WINDOW", on_closing_paiements_window)
        Paiements_window.mainloop()
        
# Apply initial scaling
        
       except Exception as e : 
          print(f"Error12: {e}")
          paiements_window_open = False

      tree.bind('<Double-1>', Open_Paiements_window)  # Bind selection event  

# bouton de recherche 
Chercher_Button = Button(Al_Manar,text='Chercher',bg='#D6D6D6',fg='black',font=15,command=lambda:[Lancer_Liste_etudiant(),searsh_students()])
Chercher_Button.place(x=600,y=80)
style = ttk.Style()
style.theme_use("clam")  # or another theme of your choice
style.configure("Treeview", 
background="#E3ECED",
foreground="black",
rowheight=22,
fieldbackground="white"
                     )
style.map('Treeview', background=[('selected', '#767874')])
def on_closing_paiements_window():
    global paiements_window_open
    paiements_window_open = False
    Paiements_window.destroy()
Al_Manar.mainloop()