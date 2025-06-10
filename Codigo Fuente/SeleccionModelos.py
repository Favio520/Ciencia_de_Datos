import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps
import subprocess
import os
import sys

# Ruta segura para acceder a archivos dentro de un .exe creado con pyinstaller
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # solo existe en ejecutable
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ========== FUNCIONES ==========
def ejecutar_notebook(nombre_notebook):
    try:
        subprocess.run([
            "jupyter", "nbconvert", "--to", "notebook",
            "--execute", "--inplace", nombre_notebook
        ], check=True)
        messagebox.showinfo("Éxito", f"{nombre_notebook} ejecutado correctamente.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar {nombre_notebook}:\n{e}")

def ejecutar_todos():
    notebooks = [
        "CRISP_DM_ARIMA_SARIMA_SARIMAX.ipynb",
        "CRISP_DM_LSTM.ipynb",
        "CRISP_DM_PROPHET.ipynb"
    ]
    for nb in notebooks:
        try:
            subprocess.run([
                "jupyter", "nbconvert", "--to", "notebook",
                "--execute", "--inplace", nb
            ], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error al ejecutar {nb}:\n{e}")
            return
    messagebox.showinfo("Éxito", "Todos los notebooks fueron ejecutados correctamente.")

# === Efecto hover para botones ===
def hover_effect(boton, color_hover, color_normal):
    boton.bind("<Enter>", lambda e: boton.config(bg=color_hover))
    boton.bind("<Leave>", lambda e: boton.config(bg=color_normal))

# === Ventana principal ===
root = tk.Tk()
root.title("Ejecutor de Modelos Predictivos")
root.geometry("600x450")
root.resizable(False, False)

# === Fondo ===
fondo_img = Image.open(resource_path("fondo.png"))
fondo_img = fondo_img.resize((600, 450), Image.Resampling.LANCZOS)
fondo = ImageTk.PhotoImage(fondo_img)
background_label = tk.Label(root, image=fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# === Contenedor central flotante ===
frame = tk.Frame(root, bg="#d4d4d4", bd=2, relief="ridge")
frame.place(relx=0.5, rely=0.6, anchor="center")  # bajamos el menú

# === Estilo general ===
BOTON_COLOR = "#1e88e5"
BOTON_HOVER = "#1565c0"
BOTON_TODOS_COLOR = "#43a047"
BOTON_TODOS_HOVER = "#2e7d32"
TEXTO_COLOR = "white"

# === Título ===
label = tk.Label(frame, text="Modelos Predictivos", font=("Helvetica", 16, "bold"), bg=frame["bg"], fg="#333")
label.pack(pady=(10, 15))

# === Botones individuales ===
botones_info = [
    ("ARIMA / SARIMA / SARIMAX", "CRISP_DM_ARIMA_SARIMA_SARIMAX.ipynb"),
    ("LSTM", "CRISP_DM_LSTM.ipynb"),
    ("PROPHET", "CRISP_DM_PROPHET.ipynb"),
]

for texto, notebook in botones_info:
    btn = tk.Button(frame, text=texto,
                    command=lambda n=notebook: ejecutar_notebook(n),
                    font=("Arial", 12, "bold"), bg=BOTON_COLOR, fg=TEXTO_COLOR,
                    activebackground=BOTON_HOVER, relief="flat", width=32, pady=6,
                    cursor="hand2")
    btn.pack(pady=5)
    hover_effect(btn, BOTON_HOVER, BOTON_COLOR)

# === Botón todos ===
btn_all = tk.Button(frame, text="Ejecutar Todos",
                    command=ejecutar_todos,
                    font=("Arial", 12, "bold"), bg=BOTON_TODOS_COLOR, fg=TEXTO_COLOR,
                    activebackground=BOTON_TODOS_HOVER, relief="flat", width=32, pady=6,
                    cursor="hand2")
btn_all.pack(pady=(10, 15))
hover_effect(btn_all, BOTON_TODOS_HOVER, BOTON_TODOS_COLOR)

root.mainloop()