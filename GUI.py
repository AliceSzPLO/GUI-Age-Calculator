# import all functions from the tkinter
from tkinter import *

#import Message Box module
from tkinter import messagebox

#import the Themed tk module
from tkinter import ttk

#import the time date module
from datetime import date

################################################################################

""" METHOD """
                         
# Function for clearing the   
# contents of all text entry boxes 
def clearAll() : 
  
    # deleting the content from the entry box 
    dayField.delete(0, END) 
    monthField.delete(0, END) 
    yearField.delete(0, END) 
    givenDayField.delete(0, END) 
    givenMonthField.delete(0, END) 
    givenYearField.delete(0, END) 
    rsltDayField.delete(0, END) 
    rsltMonthField.delete(0, END) 
    rsltYearField.delete(0, END) 

    result.grid_forget()
    
    dayField.insert(END,'Day')
    monthField.insert(END,'Month')               
    yearField.insert(END,'Years')

    givenDayField.insert(END,'Day')
    givenMonthField.insert(END,'Month')
    givenYearField.insert(END,'Years')


# function for checking error 
def checkError() : 
  
    # if any of the entry field is empty 
    # then show an error message and clear  
    # all the entries 
    if (dayField.get() == "" or monthField.get() == "" 
        or yearField.get() == "" or givenDayField.get() == "" 
        or givenMonthField.get() == "" or givenYearField.get() == "") : 
  
        # show the error message 
        messagebox.showerror(title=None,message="Please enter entry") 
  
        # clearAll function calling 
        clearAll()
        
        return -1

    #Type check
    """
    elif type(dayField.get()) != int or type(monthField.get()) != int or type(yearField.get()) != int or
         type(givenDayField.get()) != int or type(givenMonthField.get()) != int or
         type(givenYearField.get()) != int :

        messagebox.showerror(title='Type Error',message="Only integer type!!!")
    """
    
    

#Function to Calculate the age
     
def calculateAge():
    
    #check for error
    value = checkError()

    

    #if there is a error then value will be - 1
    if value==-1:
        return 

    else:
        # take a value from the respective entry boxes 
        # get method returns current text as string 
        birth_day = int(dayField.get()) 
        birth_month = int(monthField.get()) 
        birth_year = int(yearField.get()) 
  
        given_day = int(givenDayField.get()) 
        given_month = int(givenMonthField.get()) 
        given_year = int(givenYearField.get()) 
          
          
        # if birth date is greater then given birth_month  
        # then donot count this month and add 30 to the date so  
        # as to subtract the date and get the remaining days  
        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
          
        if (birth_day > given_day): 
            given_month = given_month - 1
            given_day = given_day + month[birth_month-1]  
                      
                      
        # if birth month exceeds given month, then  
        # donot count this year and add 12 to the  
        # month so that we can subtract and find out  
        # the difference  
        if (birth_month > given_month): 
            given_year = given_year - 1
            given_month = given_month + 12
                      
        # calculate day, month, year
        calculated_day = given_day - birth_day;  
        calculated_month = given_month - birth_month;  
        calculated_year = given_year - birth_year;

        # Result check
        if (calculated_day<0 or calculated_month<0 or calculated_year < 0):
            messagebox.showerror(title="Variable Error",message="Result must more than 0")

        else:
            #result
            result.config(text="คุณมีอายุ "+str(calculated_year)+" ปี "+str(calculated_month)
                           +" เดือน "+str(calculated_day)+" วัน",bg="white")
            result.config(font=("Tahoma",9))
            result.grid(row=0,column=0)
       
#############################################################################

""" WIDGET MANAGEMENT """
                            
#The Driver Code 
if __name__ == '__main__':

     #Creating the GUI window
     root = Tk()

     #root.config(background='light green')
     root.title('Age Calculator')
     root.geometry('260x290')
     root.resizable(0,0)
     
     #Frame
     bd_frame = Frame(root,width=200)#Birthday
     g_frame = Frame(root,width=200)#Given Day
     b_frame = Frame(root,width=200)#Button 

     #Birthday Entry
     dayField = Entry(bd_frame,justify=CENTER,width=8)
     dayField.insert(END,'Day')
     monthField = Entry(bd_frame,justify=CENTER,width=12)
     monthField.insert(END,'Month')               
     yearField = Entry(bd_frame,justify=CENTER,width=12)
     yearField.insert(END,'Years')

     #Given Day Entry
     givenDayField = Entry(g_frame,justify=CENTER,width=8)
     givenDayField.insert(END,'Day')
     givenMonthField = Entry(g_frame,justify=CENTER,width=12)
     givenMonthField.insert(END,'Month')
     givenYearField = Entry(g_frame,justify=CENTER,width=12)
     givenYearField.insert(END,'Years')

     #Button
     resultantAge = Button(b_frame, text = "Calculate",bg="light green",width=15
                           ,activebackground="green", command = calculateAge)
     clearAllEntry = Button(b_frame, text = "Clear",bg="white",width=15, command = clearAll)
     exitbutton = Button(b_frame,text="Exit",bg="red",width=28,command=root.destroy)
     exitbutton.config(font=('Futara Bold',10))

     rsltYearField = Entry(root) 
     rsltMonthField = Entry(root) 
     rsltDayField = Entry(root)

     #Text Label
     birthday = Label(root,text = "Your Birthday")
     birthday.config(font=('Futara',15))
     g_day = Label(root,text= "Given Day")
     g_day.config(font=('Futara',15))

     #result label
     r_frame = Frame(b_frame,bg="black",width=32,bd=2)
     result_label=Label(r_frame,width=32,bg="white")
     result_label.grid(row=0,column=0)
     result = Label(r_frame)

     #Space Label
     space = Label(root)
     space1 = Label(root)
     space2=Label(root)

     
     #Space
     space.grid(row = 0 )
     space1.grid(row =3 )
     space2.grid(row=6)

     #Text
     birthday.grid(row = 1,column=1)
     g_day.grid(row=4,column=1) 
     
     #Frame
     bd_frame.grid(row = 2 , column=1,padx=5,pady=5)
     g_frame.grid(row=5,column=1,padx=5,pady=5)
     b_frame.grid(row=7,column=1,padx=5,pady=5)
     r_frame.grid(row=0,column=0,columnspan=2)

     #Entry
     dayField.grid(row=1,column=0,padx=3,pady=3)
     monthField.grid(row=1,column=1,padx=3,pady=3)
     yearField.grid(row=1,column=2,padx=3)

     givenDayField.grid(row=1,column=0,padx=3,pady=3)
     givenMonthField.grid(row=1,column=1,padx=3,pady=3)
     givenYearField.grid(row=1,column=2,padx=3,pady=3)

     #Button
     resultantAge.grid(row=1,column=0,padx=2,pady=2)
     clearAllEntry.grid(row=1,column=1,padx=2,pady=2)
     exitbutton.grid(row=3,column=0,columnspan=2)



    

root.mainloop()
