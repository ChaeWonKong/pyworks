class Student:
    def __init__(self, nationality, gender, race):
        self.nationality = nationality
        self.gender = gender
        self.race = race


leon = Student("Korea", "Male", "Asian")
kevin = Student("Korea", "Male", "Asian")

arr = [leon, kevin]
print(arr[0].race)
