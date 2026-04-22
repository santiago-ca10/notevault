import customtkinter as ctk
from tkinter import messagebox
from app.services.note_service import NoteService

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NoteVault")
        self.geometry("700x500")

        self.service = NoteService()

        # ------------------ LAYOUT ------------------
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # ----------- PANEL IZQUIERDO (LISTA) ----------
        self.frame_list = ctk.CTkFrame(self)
        self.frame_list.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.label_list = ctk.CTkLabel(self.frame_list, text="Notas")
        self.label_list.pack(pady=10)

        self.listbox = ctk.CTkTextbox(self.frame_list, width=200)
        self.listbox.pack(expand=True, fill="both", padx=10, pady=10)

        self.btn_refresh = ctk.CTkButton(
            self.frame_list, text="Refrescar", command=self.cargar_notas
        )
        self.btn_refresh.pack(pady=5)

        # ----------- PANEL DERECHO (FORM) ----------
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.label_title = ctk.CTkLabel(self.frame_form, text="Título")
        self.label_title.pack(pady=5)

        self.entry_title = ctk.CTkEntry(self.frame_form)
        self.entry_title.pack(fill="x", padx=10)

        self.label_content = ctk.CTkLabel(self.frame_form, text="Contenido")
        self.label_content.pack(pady=5)

        self.entry_content = ctk.CTkTextbox(self.frame_form, height=150)
        self.entry_content.pack(fill="both", padx=10, pady=5)

        # ----------- BOTONES ----------
        self.btn_add = ctk.CTkButton(
            self.frame_form, text="Agregar", command=self.agregar_nota
        )
        self.btn_add.pack(pady=5)

        self.btn_update = ctk.CTkButton(
            self.frame_form, text="Actualizar", command=self.actualizar_nota
        )
        self.btn_update.pack(pady=5)

        self.btn_delete = ctk.CTkButton(
            self.frame_form, text="Eliminar", command=self.eliminar_nota
        )
        self.btn_delete.pack(pady=5)

        # cargar notas al iniciar
        self.cargar_notas()

    # ------------------ FUNCIONES ------------------

    def cargar_notas(self):
        self.listbox.delete("1.0", "end")

        notas = self.service.obtener_notas()

        for nota in notas:
            self.listbox.insert(
                "end",
                f"{nota['titulo']}\n{'-'*20}\n"
            )

    def obtener_datos_form(self):
        titulo = self.entry_title.get()
        contenido = self.entry_content.get("1.0", "end").strip()
        return titulo, contenido

    def limpiar_form(self):
        self.entry_title.delete(0, "end")
        self.entry_content.delete("1.0", "end")

    def agregar_nota(self):
        try:
            titulo, contenido = self.obtener_datos_form()
            self.service.crear_nota(titulo, contenido)
            messagebox.showinfo("Éxito", "Nota agregada")
            self.limpiar_form()
            self.cargar_notas()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def actualizar_nota(self):
        try:
            titulo, contenido = self.obtener_datos_form()
            self.service.actualizar_nota(titulo, contenido)
            messagebox.showinfo("Éxito", "Nota actualizada")
            self.cargar_notas()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_nota(self):
        try:
            titulo = self.entry_title.get()
            self.service.eliminar_nota(titulo)
            messagebox.showinfo("Éxito", "Nota eliminada")
            self.limpiar_form()
            self.cargar_notas()
        except Exception as e:
            messagebox.showerror("Error", str(e))