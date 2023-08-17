class Doctor:

    def __init__(self, doctor_id=" ", name=" ", specialization=" ", working_time=" ", qualification=" ", room_number=" " ):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization
        self.__working_time = working_time
        self.__qualification = qualification
        self.__room_number = room_number

    def get_doctor_id(self):
        return self.__doctor_id

    def get_doctor_name(self):
        return self.__name

    def get_doctor_specialization(self):
        return self.__specialization

    def get_doctor_working_time(self):
        return self.__working_time

    def get_doctor_qualification(self):
        return self.__qualification

    def get_doctor_room_number(self):
        return self.__room_number

    def set_doctor_id(self, new_id):
        self.__doctor_id = new_id

    def set_doctor_name(self, new_name):
        self.__name = new_name

    def set_doctor_specialization(self, new_specialization):
        self.__specialization = new_specialization

    def set_doctor_working_time(self, new_working_time):
        self.__working_time = new_working_time

    def set_doctor_qualification(self, new_qualification):
        self.__qualification = new_qualification

    def set_doctor_room_number(self, new_room_number):
        self.__room_number = new_room_number

    def __str__(self):
        return "_".join([self.get_doctor_id(),
                         self.get_doctor_name(),
                         self.get_doctor_specialization(),
                         self.get_doctor_working_time(),
                         self.get_doctor_qualification(),
                         self.get_doctor_room_number()])

class DoctorManager:

    def __init__(self):
        self.doctor_list = []
        # Load doctors data from doctors.txt into self.doctor_list
        self.read_doctors_file()

    def format_dr_info(self,doctor):
        # Formats doctor object information similarly to the format used in doctors TXT file
        return doctor.__str__()

    def enter_dr_info(self):
        # Create and return new doctor object based on user's inputs
        new_doctor = Doctor(input("Enter the doctor’s ID: "),
                            input("Enter the doctor’s name: "),
                            input("Enter the doctor’s specility: "),
                            input("Enter the doctor’s timing (e.g., 7am-10pm): "),
                            input("Enter the doctor’s qualification: "),
                            input("Enter the doctor’s room number: "))
        return new_doctor

    def read_doctors_file(self):
        with open ('Project Data\doctors.txt', 'r') as file:
            # Skip 1st line of file as it is not doctor info
            lines = file.readlines()[1:]
            # Create an object for each doctor record and append it to the self.doctor_list
            for line in lines:
                doctor_id, name, specialization, working_time, qualification, room_number = line.split("_")
                self.doctor_list.append(Doctor(doctor_id, name, specialization, working_time, qualification, room_number))

    def search_doctor_by_id(self, search_id):
        for doctor in self.doctor_list:
            if search_id == doctor.get_doctor_id():
                # the first line is for titles as in project output file
                print(f'{"Id":<5}{"Name":<23}{"Speciality":<16}{"Timing":<16}{"Qualification":<16}{"Room Number":<11}',end="\n\n")
                return self.display_doctor_info(doctor)
        # If the doctor does not exist, output:
        print("Can't find the doctor with the same ID on the system")

    def search_doctor_by_name(self, search_name):
        for doctor in self.doctor_list:
            if search_name == doctor.get_doctor_name():
                # the first line is for titles as in project output file
                print(f'{"Id":<5}{"Name":<23}{"Speciality":<16}{"Timing":<16}{"Qualification":<16}{"Room Number":<11}',end="\n\n")
                return self.display_doctor_info(doctor)
        # If the doctor does not exist, output:
        print("Can't find the doctor with the same name on the system")

    def display_doctor_info(self, doctor):
        # Display doctor object information as in the project output file
        print(f'{doctor.get_doctor_id():<5}', end="")
        print(f'{doctor.get_doctor_name():<23}', end="")
        print(f'{doctor.get_doctor_specialization():<16}', end="")
        print(f'{doctor.get_doctor_working_time():<16}', end="")
        print(f'{doctor.get_doctor_qualification():<16}', end="")
        print(f'{doctor.get_doctor_room_number():<11}')

    def edit_doctor_info(self, edit_doctor_id):
        # Searches the doctors list to find the doctor who has the entered id
        for doctor in self.doctor_list:
            if edit_doctor_id == doctor.get_doctor_id():
                # If the doctor exists, get the new values for attributes from the user.
                doctor.set_doctor_name(input("Enter new name: "))
                doctor.set_doctor_specialization(input("Enter new specility: "))
                doctor.set_doctor_working_time(input("Enter new timing (e.g., 7am-10pm): "))
                doctor.set_doctor_qualification(input("Enter new qualification: "))
                doctor.set_doctor_room_number(input("Enter new room number: "))

                # Writes the updated doctors list to doctors.txt
                self.write_list_of_doctors_to_file()
                # Confirms that the doctor has been edited
                print(f"Doctor whose ID is {doctor.get_doctor_id()} has been added")
                return
        # If the doctor does not exist, output:
        print("Can’t find the doctor….")

    def display_doctors_list(self):
        # the first line is for titles as in project output file
        print(f'{"Id":<5}{"Name":<23}{"Speciality":<16}{"Timing":<16}{"Qualification":<16}{"Room Number":<11}', end="\n\n")
        # the remaining lines are for displaying doctors' info
        for doctor in self.doctor_list:
            self.display_doctor_info(doctor)

    def write_list_of_doctors_to_file(self):
        # Iterates through doctors list
        with open('Project Data\doctors.txt', 'w') as file:
            # Write back the original first line
            file.write("id_name_specilist_timing_qualification_roomNb" + "\n")
            # Each doctor information must be formatted using format_dr_info() before writing it in the doctors.txt file
            for doctor in self.doctor_list:
                file.write(f"{self.format_dr_info(doctor)}\n")

    def add_dr_to_file(self):
        # Get the new doctor object
        new_doctor = self.enter_dr_info()
        # Appends the new doctor object to doctors list
        self.doctor_list.append(new_doctor)
        with open('Project Data\doctors.txt', 'a') as file:
            # New doctor information must be formatted using format_dr_info() before appending it in the doctors.txt file
            file.write(f"{self.format_dr_info(new_doctor)}\n")
        # Confirms that a new doctor has been added
        print(f"Doctor whose ID is {new_doctor.get_doctor_id()} has been added")

class Patient:
    # Represents a patient with information such as ID, name, disease, gender, and age
    def __init__(self, pid=" ", name=" ", disease=" ", gender=" ", age=" "):
        # Initializes a Patient object using patient information.
        self.__pid = pid
        self.__name = name
        self.__disease = disease
        self.__gender = gender
        self.__age = age

    # Getters
    def get_pid(self):
        return self.__pid

    def get_name(self):
        return self.__name

    def get_disease(self):
        return self.__disease

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    # Setters
    def set_name(self, new_name):
        self.__name = new_name

    def set_disease(self, new_disease):
        self.__disease = new_disease

    def set_gender(self, new_gender):
        self.__gender = new_gender

    def set_age(self, new_age):
        self.__age = new_age

    def __str__(self):
        # Returns a formatted string representation of the Patient object
        return "_".join([self.get_pid(),
                         self.get_name(),
                         self.get_disease(),
                         self.get_gender(),
                         self.get_age()])

class PatientManager:
    def __init__(self):
        self.patients = []
        # Load patient data from patients.txt into self.patients
        self.read_patients_file()

    def format_patient_info_for_file(self, patient):
        # Formats doctor object information similarly to the format used in patients TXT file
        return patient.__str__()

    def enter_patient_iInfo(self):
        # Create and return new patient object based on user's inputs
        pid = input("Enter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")

        patient = Patient(pid,name,disease,gender,age)
        return patient

    def read_patients_file(self):
        with open('Project Data\patients.txt', 'r') as file:
        # Skip 1st line of file as it is not patient info
            lines = file.readlines()[1:]
        for line in lines:
        # Create an object for each patient record and append it to the self.patients
            pid, name, disease, gender, age = line.split("_")
            self.patients.append(Patient(pid, name, disease, gender, age))

    def search_patient_by_id(self, search_patient):
        # Searching for the patient with their ID
        for patient in self.patients:
            # If found display the patient's info
            if search_patient == patient.get_pid():
                return self.display_patient_info(patient)
        # If not found outputs the above text
        print("Can't find the Patient with the same id on the system")

    def display_patient_info(self, patient):
        # Display patient object information as in the project output file
        print(f'{patient.get_pid():<5}', end="")
        print(f'{patient.get_name():<23}', end="")
        print(f'{patient.get_disease():<16}', end="")
        print(f'{patient.get_gender():<16}', end="")
        print(f'{patient.get_age():<3}')

    def edit_patient_info_by_id(self, patient_id):
        # Asks the user to enter the patient id which the user wants to edit
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                patient.set_name(input("Enter new Name: "))
                patient.set_disease(input("Enter new disease: "))
                patient.set_gender(input("Enter new gender: "))
                patient.set_age(input("Enter new age: "))
                # Writes the updated patients list to patients.txt
                self.write_list_of_patients_to_file()
                # Confirms that the patient has been edited
                print(f"Patient whose ID is {patient_id} has been edited..")
                return
        # If the doctor does not exist, output:
        print("Cannot find the patient.")

    def display_patients_list(self):
        # the first line is for titles as in project output file
        print(f'{"ID":<5}{"Name":<23}{"Disease":<16}{"Gender":<16}{"Age":<16}', end="\n\n")
        # the remaining lines are for displaying patients' info
        for patient in self.patients:
            self.display_patient_info(patient)

    def write_list_of_patients_to_file(self):
        # Iterates through patients list
        with open("Project Data\patients.txt", "w") as file:
            for patient in self.patients:
                # Each patient information must be formatted using format_patient_info_for_file() before writing it in the doctors.txt file
                file.write(f"{self.format_patient_info_for_file(patient)}\n")

    def add_patient_to_file(self):
        # Get the new patient object
        new_patient = self.enter_patient_iInfo()
        # Appends the new patient object to patients list
        self.patients.append(new_patient)
        with open("Project Data\patients.txt", "a") as file:
            # Formats this information to match the patients.txt format
            file.write(f"{self.format_patient_info_for_file(new_patient)}\n")
        # Confirms that a new doctor has been added
        print(f"Patient whose ID is {new_patient.get_pid()} has been added")

def main():
    # Initiates doctor manager class and patient manager class for operations
    doctor_manager = DoctorManager()
    patient_manager = PatientManager()

    while True:
        print("Welcome to Alberta Hospital (AH) Managment system")
        menu_choice = input("Select from the following options, or select 3 to stop:\n1 - 	Doctors\n2 - 	Patients\n3 -	    Exit Program\n")

        if menu_choice == "1":
            while True:
                print("\nDoctors Menu:")
                choice = input("1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n")

                if choice == "1":
                    doctor_manager.display_doctors_list()
                elif choice == "2":
                    doctor_manager.search_doctor_by_id(input("Enter the doctor Id: "))
                elif choice == "3":
                    doctor_manager.search_doctor_by_name(input("Enter the doctor name: "))
                elif choice == "4":
                    doctor_manager.add_dr_to_file()
                elif choice == "5":
                    doctor_manager.edit_doctor_info(input("Please enter the id of the doctor that you want to edit their information: "))
                elif choice == "6":
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

        elif menu_choice == "2":
            while True:
                print("\nPatients Menu:")
                choice = input("1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n")

                if choice == "1":
                    patient_manager.display_patients_list()
                elif choice == "2":
                    patient_manager.search_patient_by_id(input("Enter the Patient Id: "))
                elif choice == "3":
                    patient_manager.add_patient_to_file()
                elif choice == "4":
                    patient_manager.edit_patient_info_by_id(input("Please enter the id of the Patient that you want to edit their information:"))
                elif choice == "5":
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

        elif menu_choice == "3":
            print("Thanks for using the program. Bye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
