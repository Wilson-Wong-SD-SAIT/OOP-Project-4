
class DoctorManager:

    def __init__(self):
        self.doctor_list = []
        # Load doctors data from doctors.txt into self.doctor_list
        self.read_doctors_file()

    def format_dr_info(self,doctor):
        # Formats doctor object information similarly to the format used in doctors TXT file
        return "_".join([doctor.get_doctor_id(),
                         doctor.get_doctor_name(),
                         doctor.get_doctor_specialization(),
                         doctor.get_doctor_working_time(),
                         doctor.get_doctor_qualification(),
                         doctor.get_doctor_room_number()])

    def enter_dr_info(self):
        # Create and return new doctor object based on user's inputs
        new_doctor = Doctor("_".join([input("Enter the doctor’s ID: "),
                                      input("Enter the doctor’s name: "),
                                      input("Enter the doctor’s specility: "),
                                      input("Enter the doctor’s timing (e.g., 7am-10pm): "),
                                      input("Enter the doctor’s qualification: "),
                                      input("Enter the doctor’s room number: ")]))
        return new_doctor

    def read_doctors_file(self):
        with open ('Project Data\doctorsTry.txt', 'r') as file:
            # Skip 1st line of file as it is not doctor info
            lines = file.readlines()[1:]
            # Create an object for each doctor record and append it to the self.doctor_list
            for line in lines:
                self.doctor_list.append(Doctor(line))

    def search_doctor_by_id(self):
        # Asks the user to enter the doctor id which the user wants to search
        search_id = input("Enter the doctor Id: ")
        for doctor in self.doctor_list:
            if search_id == doctor.get_doctor_id():
                # If the doctor exists, use display_doctors_list first to create first line for titles
                return self.display_doctors_list([doctor])
        # If the doctor does not exist, output:
        print("Can’t find the doctor….")

    def search_doctor_by_name(self):
        # Asks the user to enter the doctor name which the user wants to search
        search_name = input("Enter the doctor name: ")
        for doctor in self.doctor_list:
            if search_name == doctor.get_doctor_name():
                # If the doctor exists, use display_doctors_list first to create first line for titles
                return self.display_doctors_list([doctor])
        # If the doctor does not exist, output:
        print("Can’t find the doctor….")

    def display_doctor_info(self, doctor):
        # Display doctor object information as in the project output file
        print(f'{doctor.get_doctor_id():<5}', end="")
        print(f'{doctor.get_doctor_name():<23}', end="")
        print(f'{doctor.get_doctor_specialization():<16}', end="")
        print(f'{doctor.get_doctor_working_time():<16}', end="")
        print(f'{doctor.get_doctor_qualification():<16}', end="")
        print(f'{doctor.get_doctor_room_number():<11}', end="\n")

    def edit_doctor_info(self):
        # Asks the user to enter the doctor id which the user wants to edit
        edit_doctor_id = input("Please enter the id of the doctor that you want to edit their information: ")
        # Searches the doctors list to find the doctor who has the entered id
        for doctor in self.doctor_list:
            if edit_doctor_id == doctor.get_doctor_id():
                # If the doctor exists, get the new values for attributes from the user.
                doctor.set_doctor_id(input("Enter the doctor’s ID: "))
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

    def display_doctors_list(self, doctor_list):
        # the first line is for titles as in project output file
        print(f'{"Id":<5}', end="")
        print(f'{"Name":<23}', end="")
        print(f'{"Speciality":<16}', end="")
        print(f'{"Timing":<16}', end="")
        print(f'{"Qualification":<16}', end="")
        print(f'{"Room Number":<11}', end="\n\n")
        # the remaining lines are for displaying doctors' info
        for doctor in doctor_list:
            self.display_doctor_info(doctor)

    def write_list_of_doctors_to_file(self):
        # Iterates through doctors list
        with open('Project Data\doctorsTry.txt', 'w') as file:
            # Write back the original first line
            file.write("id_name_specilist_timing_qualification_roomNb" + "\n")
            # Each doctor information must be formatted using format_dr_info() before writing it in the doctors.txt file
            for doctor in self.doctor_list:
                doctor_info = self.format_dr_info(doctor)
                file.write(doctor_info)

    def add_dr_to_file(self):
        # Get the new doctor object
        new_doctor = self.enter_dr_info()
        # Appends the new doctor object to doctors list
        self.doctor_list.append(new_doctor)
        # Formats this information to match the doctors.txt format
        new_doctor_info = self.format_dr_info(new_doctor)
        # Appends the new doctor to doctors file
        with open('Project Data\doctorsTry.txt', 'a') as file:
            file.write("\n" + new_doctor_info)
        # Confirms that a new doctor has been added
        print(f"Doctor whose ID is {new_doctor.get_doctor_id()} has been added")






