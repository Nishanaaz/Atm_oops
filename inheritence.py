class user:
    def login(self):
        print("login")
    def register(self):
        print("register")
class student(user):
    def enroll(self):
        print("enroll")
    def review(self):
        print("Review")
stu1=student()
stu1.login()

 