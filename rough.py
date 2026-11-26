class employee:
    def __init__(self):
        print("Constructor is called")
        self.id = 1234
        self.salary = 50000
        self.post = "Software Engineer"
        print("Constructor was successfully executed")

    def display(self):
        print("ID:", self.id)
        print("Salary:", self.salary)
        print("Post:", self.post)

sam = employee()

