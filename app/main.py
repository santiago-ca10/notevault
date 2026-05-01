from app.ui.main_window import App


class Application:
    """Clase principal encargada de iniciar la aplicación."""

    def __init__(self):
        # Inicializa la interfaz principal
        self.app = App()

    def run(self):
        """
        Ejecuta el ciclo principal de la aplicación.
        """
        self.app.mainloop()


if __name__ == "__main__":
    Application().run()