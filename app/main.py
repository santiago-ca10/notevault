from app.ui.main_window import App

class Application:
    def __init__(self):
        self.app = App()

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    Application().run()