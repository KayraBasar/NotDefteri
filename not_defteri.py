import tkinter as tk
from tkinter import messagebox, font
import os

FILE_NAME = "notes.txt"

def load_notes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())

def save_notes():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        notes = listbox.get(0, tk.END)
        for note in notes:
            f.write(note + "\n")
    messagebox.showinfo("Bilgi", "Notlar kaydedildi!")

def add_note():
    note = entry.get()
    if note:
        listbox.insert(tk.END, note)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Boş not eklenemez!")

def delete_note():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Uyarı", "Silmek için bir not seçin!")

def clear_notes():
    listbox.delete(0, tk.END)

def edit_note():
    selected = listbox.curselection()
    if selected:
        # Seçili notu giriş kutusuna getir
        note = listbox.get(selected)
        entry.delete(0, tk.END)
        entry.insert(0, note)
        # Seçili notu listeden sil, düzenlenmiş hali tekrar eklenecek
        listbox.delete(selected)
    else:
        messagebox.showwarning("Uyarı", "Düzenlemek için bir not seçin!")

def toggle_bold():
    current_font = listbox.cget("font")
    f = font.nametofont(current_font)
    if f.actual()["weight"] == "normal":
        f.configure(weight="bold")
    else:
        f.configure(weight="normal")
    listbox.config(font=f)

def toggle_italic():
    current_font = listbox.cget("font")
    f = font.nametofont(current_font)
    if f.actual()["slant"] == "roman":
        f.configure(slant="italic")
    else:
        f.configure(slant="roman")
    listbox.config(font=f)

# Ana pencere
root = tk.Tk()
root.title("Not Defteri")

# Giriş alanı
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Butonlar
add_button = tk.Button(root, text="Not Ekle", command=add_note)
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Seçili Notu Düzenle", command=edit_note)
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Seçili Notu Sil", command=delete_note)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Tümünü Temizle", command=clear_notes)
clear_button.pack(pady=5)

save_button = tk.Button(root, text="Kaydet", command=save_notes)
save_button.pack(pady=5)

bold_button = tk.Button(root, text="Kalın Yazı", command=toggle_bold)
bold_button.pack(pady=5)

italic_button = tk.Button(root, text="İtalik Yazı", command=toggle_italic)
italic_button.pack(pady=5)

# Liste kutusu
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Varsayılan font
default_font = font.Font(family="Arial", size=12)
listbox.config(font=default_font)

# Uygulama açılırken notları yükle
load_notes()

root.mainloop()