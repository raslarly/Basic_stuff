import tkinter as tk
from tkinter import messagebox

def hesapla_gerilim():
    try:
        akim = float(akim_entry.get())
        direnc = float(direnc_entry.get())
        gerilim = akim * direnc
        sonuc_label.config(text=f"Gerilim (V): {gerilim:.2f} Volt")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin.")

def hesapla_akim():
    try:
        gerilim = float(gerilim_entry.get())
        direnc = float(direnc_entry.get())
        akim = gerilim / direnc
        sonuc_label.config(text=f"Akım (I): {akim:.2f} Amper")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin.")

def hesapla_direnc():
    try:
        gerilim = float(gerilim_entry.get())
        akim = float(akim_entry.get())
        direnc = gerilim / akim
        sonuc_label.config(text=f"Direnç (R): {direnc:.2f} Ohm")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin.")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Ohm Kanunu Hesaplayıcı")

# Gerilim, Akım ve Direnç için etiket ve giriş alanları
gerilim_label = tk.Label(root, text="Gerilim (V):")
gerilim_label.grid(row=0, column=0)
gerilim_entry = tk.Entry(root)
gerilim_entry.grid(row=0, column=1)

akim_label = tk.Label(root, text="Akım (I):")
akim_label.grid(row=1, column=0)
akim_entry = tk.Entry(root)
akim_entry.grid(row=1, column=1)

direnc_label = tk.Label(root, text="Direnç (R):")
direnc_label.grid(row=2, column=0)
direnc_entry = tk.Entry(root)
direnc_entry.grid(row=2, column=1)

# Hesaplama butonları
gerilim_buton = tk.Button(root, text="Gerilim Hesapla", command=hesapla_gerilim)
gerilim_buton.grid(row=3, column=0)

akim_buton = tk.Button(root, text="Akım Hesapla", command=hesapla_akim)
akim_buton.grid(row=3, column=1)

direnc_buton = tk.Button(root, text="Direnç Hesapla", command=hesapla_direnc)
direnc_buton.grid(row=3, column=2)

# Sonuç gösterim alanı
sonuc_label = tk.Label(root, text="")
sonuc_label.grid(row=4, columnspan=3)

# Pencereyi çalıştır
root.mainloop()
