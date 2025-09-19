class Student:
    #basic attendance tracking
    
    def __init__(self, name):
        self.name = name
        self.total_classes = 0
        self.attended_classes = 0

    def mark_attendance(self):
        #Allows the student to input their attendance.
        status = input(f"{self.name}, are you Present or Absent? ")
        if status == "present":
            self.attended_classes += 1
            self.total_classes += 1
        elif status == "absent":
            self.total_classes += 1
        else:
            print("Invalid input! Please enter 'Present' or 'Absent'.")

    def display_attendance(self):
        """Displays the student's attendance summary."""
        if self.total_classes > 0:
            percentage = (self.attended_classes / self.total_classes) * 100
        else:
            percentage = 0  
        
        print("\nAttendance Summary:")
        print("Student Name:", self.name)
        print("Total Classes:", self.total_classes)
        print("Classes Attended:", self.attended_classes)
        print("Attendance Percentage:", round(percentage, 2), "%")

# student information
student_name = input("Student Name: ")
student = Student(student_name)


for _ in range(5):  #number of classes
    student.mark_attendance()

#displays all the attendance summary in an orderly manner.
student.display_attendance()
