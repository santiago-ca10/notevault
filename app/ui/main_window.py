import customtkinter as ctk
from tkinter import messagebox
from app.services.note_service import NoteService
from app.utils.helpers import tiempo_relativo

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NoteVault")
        self.geometry("800x500")

        self.service = NoteService()
        self.nota_actual = None

        # CONTENEDOR
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, fill="both")

        # ---------------- LISTA ----------------
        self.frame_lista = ctk.CTkFrame(self.container)
        self.frame_lista.pack(expand=True, fill="both")

        self.search_entry = ctk.CTkEntry(
            self.frame_lista, placeholder_text="🔍 Buscar..."
        )
        self.search_entry.pack(padx=10, pady=10, fill="x")
        self.search_entry.bind("<KeyRelease>", self.buscar_notas)

        self.notes_frame = ctk.CTkScrollableFrame(self.frame_lista)
        self.notes_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.btn_new = ctk.CTkButton(
            self.frame_lista, text="+ Nueva Nota", command=self.nueva_nota
        )
        self.btn_new.pack(pady=10)

        # ---------------- EDITOR ----------------
        self.frame_editor = ctk.CTkFrame(self.container)

        self.btn_back = ctk.CTkButton(
            self.frame_editor, text="← Volver", command=self.mostrar_lista
        )
        self.btn_back.pack(pady=5)

        self.title_entry = ctk.CTkEntry(
            self.frame_editor, placeholder_text="Título"
        )
        self.title_entry.pack(fill="x", padx=10, pady=10)

        self.content_text = ctk.CTkTextbox(self.frame_editor)
        self.content_text.pack(expand=True, fill="both", padx=10, pady=10)

        self.btn_save = ctk.CTkButton(
            self.frame_editor, text="Guardar", command=self.guardar_nota
        )
        self.btn_save.pack(pady=5)

        self.btn_delete = ctk.CTkButton(
            self.frame_editor, text="Eliminar", fg_color="red",
            command=self.eliminar_nota
        )
        self.btn_delete.pack(pady=5)

        self.cargar_notas()

    # ---------------- NAV ----------------

    def mostrar_lista(self):
        self.frame_editor.pack_forget()
        self.frame_lista.pack(expand=True, fill="both")

    def mostrar_editor(self):
        self.frame_lista.pack_forget()
        self.frame_editor.pack(expand=True, fill="both")

    # ---------------- DATA ----------------

    def cargar_notas(self):
        for widget in self.notes_frame.winfo_children():
            widget.destroy()

        notas = self.service.obtener_notas()

        for nota in notas:
            self.crear_tarjeta(nota)

    def crear_tarjeta(self, nota):
        # ✅ FRAME BIEN CREADO Y MOSTRADO
        frame = ctk.CTkFrame(
            self.notes_frame,
            corner_radius=12,
            border_width=1
        )
        frame.pack(fill="x", pady=6, padx=8)

        titulo = nota.get("titulo", "")
        contenido = nota.get("contenido", "")

        # preview limpio
        preview = contenido.split("\n")[0][:40]
        if len(contenido) > 40:
            preview += "..."

        # fecha segura
        fecha = nota.get("fecha")
        texto_fecha = tiempo_relativo(fecha) if fecha else ""

        # titulo
        lbl_titulo = ctk.CTkLabel(
            frame,
            text=titulo,
            font=("Segoe UI", 15, "bold"),
            anchor="w"
        )
        lbl_titulo.pack(anchor="w", padx=10, pady=(6, 0))

        # preview
        lbl_preview = ctk.CTkLabel(
            frame,
            text=preview,
            font=("Segoe UI", 12),
            text_color="gray",
            anchor="w"
        )
        lbl_preview.pack(anchor="w", padx=10)

        # fecha
        lbl_fecha = ctk.CTkLabel(
            frame,
            text=texto_fecha,
            font=("Segoe UI", 10),
            text_color="gray",
            anchor="e"
        )
        lbl_fecha.pack(anchor="e", padx=10, pady=(0, 5))

        # hover
        def on_enter(e):
            if self.nota_actual != nota:
                frame.configure(fg_color="#2f2f2f")

        def on_leave(e):
            if self.nota_actual != nota:
                frame.configure(fg_color="transparent")

        frame.bind("<Enter>", on_enter)
        frame.bind("<Leave>", on_leave)

        for w in frame.winfo_children():
            w.bind("<Enter>", on_enter)
            w.bind("<Leave>", on_leave)

        # click
        def seleccionar(e):
            self.nota_actual = nota
            self.abrir_nota(nota)
            self.resaltar_seleccion()

        frame.bind("<Button-1>", seleccionar)
        for w in frame.winfo_children():
            w.bind("<Button-1>", seleccionar)

        frame.nota = nota

    # ---------------- ACCIONES ----------------

    def abrir_nota(self, nota):
        self.nota_actual = nota

        self.title_entry.delete(0, "end")
        self.title_entry.insert(0, nota["titulo"])

        self.content_text.delete("1.0", "end")
        self.content_text.insert("1.0", nota["contenido"])

        self.mostrar_editor()

    def nueva_nota(self):
        self.nota_actual = None
        self.title_entry.delete(0, "end")
        self.content_text.delete("1.0", "end")
        self.mostrar_editor()

    def guardar_nota(self):
        titulo = self.title_entry.get()
        contenido = self.content_text.get("1.0", "end").strip()

        if not titulo:
            messagebox.showerror("Error", "El título es obligatorio")
            return

        if self.nota_actual:
            self.service.actualizar_nota(titulo, contenido)
        else:
            self.service.crear_nota(titulo, contenido)

        self.cargar_notas()
        self.mostrar_lista()

    def eliminar_nota(self):
        if not self.nota_actual:
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar nota?"):
            self.service.eliminar_nota(self.nota_actual["titulo"])
            self.nueva_nota()
            self.cargar_notas()
            self.mostrar_lista()

    def buscar_notas(self, event):
        texto = self.search_entry.get().lower()

        for widget in self.notes_frame.winfo_children():
            widget.destroy()

        notas = self.service.obtener_notas()

        for nota in notas:
            if texto in nota["titulo"].lower():
                self.crear_tarjeta(nota)

    def resaltar_seleccion(self):
        for widget in self.notes_frame.winfo_children():
            if hasattr(widget, "nota"):
                if widget.nota == self.nota_actual:
                    widget.configure(fg_color="#1f6aa5")
                else:
                    widget.configure(fg_color="transparent")


if __name__ == "__main__":
    app = App()
    app.mainloop()