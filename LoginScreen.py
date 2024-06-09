
from ttkbootstrap import Button,Entry,Label,Frame

from TodoListScreen import ToDoList
class LoginScreen(Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self.controller = controller
        self.title_label = None
        self.sign_label = None
        self.sign_input = None
        self.sign_password = None
        self.sign_input_password = None
        self.login_button = None
        self.createLogin()

    def createLogin(self):
        self.title_label = Label(text="Sign In Screen")
        self.title_label.grid(row=0, column=1)

        self.sign_label = Label(text="Sign In")
        self.sign_label.grid(row=1, column=1)

        self.sign_input = Entry()
        self.sign_input.grid(row=1, column=2, padx=10, pady=10)

        self.sign_password = Label(text="Password")
        self.sign_password.grid(row=2, column=1)

        self.sign_input_password = Entry(show="*")
        self.sign_input_password.grid(row=2, column=2, padx=10, pady=10)

        self.login_button = Button(text="Login",command=self.login)
        self.login_button.grid(row=1, column=3, padx=10, pady=10)

    def login(self):
        # For now, we simply switch to the ToDoList
        self.controller.show_frame(ToDoList)
