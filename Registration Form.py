from tkinter import *
root = Tk()
root.title("Pentagon Construction Company")
root.geometry("500x300")


def getvals():
    print("User has been Registered.")

# Headings
Label(root,text="PENTAGON REGISTRATION FORM", font="Calibri 20",). grid(row=0, column=3)

# Field Name
user_name = Label(root, text="Name")
user_e_mail = Label(root, text="E-Mail")
user_Mobile = Label(root, text="Mobile No.")
user_Date_of_birth = Label(root, text="Date of Birth")
user_Country = Label(root, text="Country")
user_Gender = Label(root, text="Gender")
user_country_of_residence = Label(root, text="Country of Residence")
user_Address = Label(root, text="Address")

# Packing Fields
user_name.grid(row=1, column=2)
user_e_mail.grid(row=2, column=2)
user_Mobile.grid(row=3, column=2)
user_Date_of_birth.grid(row=4, column=2)
user_Gender.grid(row=5, column=2)
user_Country.grid(row=6, column=2)
user_country_of_residence.grid(row=7, column=2)
user_Address.grid(row=8, column=2)

#Variable for Storing Data
user_namevalue = StringVar
user_e_mailvalue = StringVar
user_Mobileevalue = StringVar
user_Date_of_birthvalue = StringVar
user_Countryvalue = StringVar
user_Gendervalue = StringVar
user_country_of_residencevalue = StringVar
user_Addressvalue = StringVar
checkvalue = IntVar

# Creating Entry Field
user_nameentry = Entry(root, textvariable=user_namevalue)
user_e_mailentry = Entry(root, textvariable=user_e_mailvalue)
user_Mobileentry = Entry(root, textvariable=user_Mobileevalue)
user_Date_of_birthentry = Entry(root, textvariable=user_Date_of_birthvalue)
user_Countryentry = Entry(root, textvariable=user_Countryvalue)
user_Genderentry = Entry(root, textvariable=user_Gendervalue)
user_country_of_residenceentry = Entry(root, textvariable=user_country_of_residencevalue)
user_Addressentry = Entry(root, textvariable=user_Addressvalue)

#Packing Entry Field
user_nameentry.grid(row=1, column=3)
user_e_mailentry.grid(row=2, column=3)
user_Mobileentry.grid(row=3, column=3)
user_Date_of_birthentry.grid(row=4, column=3)
user_Genderentry.grid(row=5, column=3)
user_Countryentry.grid(row=6, column=3)
user_country_of_residenceentry.grid(row=7, column=3)
user_Addressentry.grid(row=8, column=3)


# Creating Checkbox
checkbutton = Checkbutton(text="Remember me.", variable=checkvalue)

# Packing Checkbox
checkbutton.grid(row=9, column=3)

# Register Button
button = Button(root, text="Register", command=getvals).grid(row=11, column=3)

# Terms and conditions button
Checkbutton(root, text="agree our terms and conditions",). grid(row=13, column=3)






root.mainloop()






