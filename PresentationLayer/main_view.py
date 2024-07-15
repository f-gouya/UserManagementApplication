from PresentationLayer.window import Window
from PresentationLayer.login import LoginFrame
from PresentationLayer.register import RegisterFrame
from PresentationLayer.home import HomeFrame
from PresentationLayer.user_management import UserManagementFrame


class MainView:
    def __init__(self):
        self.window = Window()

        self.frames = {}

        self.add_frame("user_management", UserManagementFrame(self.window))
        self.add_frame("home", HomeFrame(self.window, self))
        self.add_frame("register", RegisterFrame(self.window, self))
        self.add_frame("login", LoginFrame(self.window, self))

        self.window.show_form()

    def add_frame(self, name, frame):
        self.frames[name] = frame
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        return frame
