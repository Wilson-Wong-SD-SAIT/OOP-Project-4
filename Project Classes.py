class Doctor:
    def __init__(self, doctor_id='', name='', specialization='', working_time='', qualification='', room_number=''):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"


class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    def read_doctors_file(self):
        # Read data from doctors.txt and populate self.doctors list
        pass

    def format_dr_info(self, doctor):
        return str(doctor)

    def enter_dr_info(self):
        doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Specialization: ")
        working_time = input("Enter Working Time: ")
        qualification = input("Enter Qualification: ")
        room_number = input("Enter Room Number: ")

        return Doctor(doctor_id, name, specialization, working_time, qualification, room_number)

    def search_doctor_by_id(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor...")

    def search_doctor_by_name(self, doctor_name):
        for doctor in self.doctors:
            if doctor.name == doctor_name:
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor...")

    def display_doctor_info(self, doctor):
        print("Doctor Information:")
        print("ID:", doctor.doctor_id)
        print("Name:", doctor.name)
        print("Specialization:", doctor.specialization)
        print("Working Time:", doctor.working_time)
        print("Qualification:", doctor.qualification)
        print("Room Number:", doctor.room_number)

    # Implement other methods as per the requirements


def main():
    doctor_manager = DoctorManager()

    while True:
        print("\nMenu:")
        print("1. Search Doctor by ID")
        print("2. Search Doctor by Name")
        print("3. Display Doctor Information")
        print("4. Add New Doctor")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            doctor_id = input("Enter Doctor ID to search: ")
            doctor_manager.search_doctor_by_id(doctor_id)
        elif choice == "2":
            doctor_name = input("Enter Doctor Name to search: ")
            doctor_manager.search_doctor_by_name(doctor_name)
        elif choice == "3":
            doctor_id = input("Enter Doctor ID to display: ")
            doctor_manager.display_doctor_info(doctor_id)
        elif choice == "4":
            new_doctor = doctor_manager.enter_dr_info()
            doctor_manager.doctors.append(new_doctor)
            # Save the updated doctors list to file
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
