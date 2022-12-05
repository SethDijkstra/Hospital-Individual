class Patient:
    #Initialization function
    def __init__(self,id, name, diagnosis, gender, age ):
        self.id = id
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age
    #Use to set the ID of the input from user (Helps with the search for patient by ID)
    def getId(self):
        return self.id
    #All setter functions are used to edit the patient file then format them afterwards
    def set_id(self,id):
        self.id = id
    def set_name(self,name):
        self.name = name
    def set_diagnosis(self,diagnosis):
        self.diagnosis = diagnosis
    def set_gender(self,gender):
        self.gender = gender
    def set_age(self, age):
        self.age = age
    #Easy method to pass the objects through and format them into the file
    def formatPatientInfo(self):
        file_formatting = f'\n{self.id}_{self.name}_{self.diagnosis}_{self.gender}_{self.age}'
        return file_formatting


    #When displaying the list from file, this method will help organize the information to the user, making it easier to read and understand.
    def __str__(self):
        return f'{self.id:<4}{self.name:<10}{self.diagnosis:<13}{self.gender:<9}{self.age}'

    
        
        