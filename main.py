import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
from PIL import Image, ImageTk
import os

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    for file in files:
        listbox.insert(tk.END, file)

def merge_pdfs():
    files = listbox.get(0, tk.END)
    if not files:
        messagebox.showwarning("Brak plików", "Wybierz pliki PDF do połączenia.")
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_path:
        try:
            merger = PdfMerger()
            for pdf in files:
                merger.append(pdf)
            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Sukces", "Pliki zostały połączone pomyślnie!")
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")

def clear_files():
    listbox.delete(0, tk.END)

# Tworzenie głównego okna
root = tk.Tk()
root.title("Combine PDF :)")
root.geometry("400x500")
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "favicon.ico")
root.iconbitmap(icon_path)
def add_logo():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "Naglak.png")
        logo_img = Image.open(icon_path)  # Podaj ścieżkę do pliku z logiem
        logo_img = logo_img.resize((250, 100))  # Zmiana rozmiaru loga
        logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(root, image=logo_photo)
        logo_label.image = logo_photo  # Referencja do obrazu (aby go nie usunęło)
        logo_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się wczytać loga: {e}")

# Wywołanie funkcji dodającej logo
add_logo()

# Lista plików
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
listbox.pack(pady=10)

# Przyciski
select_button = tk.Button(root, text="Wybierz pliki PDF", command=select_files)
select_button.pack(pady=5)

merge_button = tk.Button(root, text="Połącz PDF", command=merge_pdfs)
merge_button.pack(pady=5)

clear_button = tk.Button(root, text="Wyczyść listę", command=clear_files)
clear_button.pack(pady=5)

root.mainloop()
