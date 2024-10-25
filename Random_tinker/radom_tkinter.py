import tkinter as tk
from tkinter import messagebox
def hesapla_gerilim():
    try:
        akim = float(akim_entry.get())
        direnc = float(direnc_entry.get())
        gerilim = akim * direnc
        sonuc_label.config(text=f"Gerilim (v): {gerilim:.2f} volt")
    except ValueError:
        messagebox.showerror("Hata", "Lürfen geçerli sayılar gitin.")
def hesapla_akim():
    try:
        gerilim = float(gerilim_entry.get())
        direnc = float(direnc_entry.get())
        akim = gerilim / direnc
        sonuc_label.config(text=f"Akım (A): {akim:.2f} Amper")
    except ValueError:
        messagebox.showerror("hata", "Lütfen geçerli sayılar girin.")
def hesapla_direnc():
    try:
        gerilim = float(gerilim.entry.get())
        akim = float(akim.entry.get())
        direnc = gerilim / akim
        sonuc_label.config(text=f"Direnç (R): {direnc:.2f} ohm")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin.")
#Ana pencereyi oluştur
root = tk.Tk()
root.title("Ohm kanunu hesaplayıcı")

#Gerilim, akım ve direnç için etiket ve giriş alanları
gerilim_label = tk.Label(root, text="Gerilim (V):")
gerilim_label.grid(row=0, column=0)
gerilim_entry = tk.Entry(root)
gerilim_entry.grid(row=0, column=1)