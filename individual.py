#   This is a directory for a hospital that allows the workers to sift through the patient.txt file.
#   It allows user entry to control any addition to the file aswell as editing old information that
#   The patients have inside the file. This program also allows the hospital to check a user by their
#   ID and will display a list of everyones information in an easy to read fashion.

#Made By Seth Dijkstra (902667) 
#seth.dijkstra@edu.sait.ca

#                    (Year-Mo-Dy)
#   Last Edit Made on 2022-12-04



#   importing my class from another folder, using an abbreviation of 'PC' to represent patient class
import patient_classes as PC


#   Displays patients menu options, accepts and returns user’s choice
def patientsMenu():

    #Variable to help run/end the program
    runProgram = 0
    while runProgram == 0:

        #patient menu display and options.
        print("\nPatient Menu\n0 - Return to Main Menu\n1 - Display patient's list\n2 - Search for patient by ID\n3 - Add Patient\n4 - Edit Patient info")
        userInput = int(input("Enter Option: "))

        match userInput:

            case 0:
                #choosing this option ends the program and writes and new information to the patients.txt file.
                print('\nExiting the Program.... Have a nice day!')
                writePatientToFile()
                runProgram +=1

            case 1:
                #This option will allow the user to the the patients file in a format that is simple to read
                displayPatientList()

            case 2: 
                #User can see if the patient exist by entering the ID that corresponds to the person.
                searchPatientById()

            case 3:
                #This choice prompts the user to input information to the patients list.
                addPatientToList()

            case 4:
                #Gather the ID of patient to change information on, then will update the list, display the changes and then write it to the file.
                id = searchPatientById()
                editPatientInfo(id)


#   Asks the user to enter patient information (attributes), then creates and returns a new Patient object
def enterPatientInfo():

    id = int(input("\nEnter patient ID: "))
    name = str(input("Enter patient name: "))
    diagnosis = str(input("Enter patient diagnosis: "))
    gender = str(input("Enter patient gender: "))
    age = int(input("Enter patient age: "))

    #format the patients information
    format = PC.Patient(id,name,diagnosis,gender,age)
    return format

#   Reads “patients.txt” file into a list of Patient objects
def readPatientFile():
    plist = []
    #Found a way to open files without having to close them, heard this way is better practice.
    with open('patients.txt') as file:
        file.readline()
        for line in file:
            #remove the formatting of the file and changes it to how we want it in a list
            items = line.strip().split("_")
            patient = PC.Patient(items[0],items[1],items[2],items[3],items[4])
            #add to list
            plist.append(patient)
        return plist

#   Searches the list of Patient objects for a specified patient ID using the patient ID that the user enters.
#   Returns Patient object or -1 if not found.
def searchPatientById():
    size = len(plist)
    id = (input("\nEnter Patient ID: "))
    for patient in plist:
        idNum = patient.getId()
        if idNum == id:
            print(patient)
        else:
            size-=1
            if size == 0:
                print(f'Patient with ID {id} not in patient file')
    return id

#   Finds patient ID in the list of Patient objects, prompts for new values and updates the remaining attributes
def editPatientInfo(id):
    for patient in plist:
        idnum = patient.getId()
        if idnum == id:
            patient.set_name(input("Enter new patient name: "))
            patient.set_diagnosis(input("Enter new patient diagnosis: "))
            patient.set_gender(input("Enter new patient gender: "))
            patient.set_age(input("Enter new patient age: "))
            print("The patients file has been updated! ")
            print("Here is the updated list: ")
            writePatientToFile()
            (displayPatientList())
            id += '1'

#   Displays all the Patients’ information(attributes) in patients list
def displayPatientList():
    plist = readPatientFile()
    print(f'\n{"ID"}{"Name":>6}{"Diagnosis":>15}{"Gender":>10}{"Age":>6}')
    print(f'{"--"}{"----":>6}{"---------":>15}{"------":>10}{"---":>6}')
    for new in plist:
        print(new)
    
#   Writes “patients.txt” file from the list of Patient objects, maintaining correct formatting
def writePatientToFile():
    with open('patients.txt','w') as f:
        f.write("ID_Name_Diagnosis_Gender_Age")
        #re-write with updated information based on plist
        for patient in plist:
            f.write(PC.Patient.formatPatientInfo(patient))

#   Gets new Patient object (with user-entered patient information) and adds it to the patients list
def addPatientToList():
    plist.append(enterPatientInfo())


#   Makes the patient list avaliable to all functions and will initialize patients menu to run.
def main():
    global plist
    plist = readPatientFile()
    patientsMenu()


#   Initialize the code, runs main function
if __name__ == '__main__':
    main()