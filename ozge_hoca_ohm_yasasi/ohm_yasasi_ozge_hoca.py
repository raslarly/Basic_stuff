import tkinter as tk
from tkinter import ttk

# Eşdeğer direnç hesaplamaları için fonksiyonlar
def calculate_ohms_law():
    try:
        voltage = float(voltage_entry.get())
        current = float(current_entry.get())
        resistance = voltage / current
        result_label.config(text=f"Direnç (R): {resistance:.2f} Ω")
    except ValueError:
        result_label.config(text="Lütfen geçerli bir sayı girin")

def calculate_series_resistance():
    try:
        resistances = [float(value) for value in resistance_values.get().split(",")]
        equivalent_resistance = sum(resistances)
        series_result_label.config(text=f"Eşdeğer Direnç (Seri): {equivalent_resistance:.2f} Ω")
    except ValueError:
        series_result_label.config(text="Lütfen geçerli değerler girin")

def calculate_parallel_resistance():
    try:
        resistances = [float(value) for value in resistance_values.get().split(",")]
        equivalent_resistance = 1 / sum(1/r for r in resistances if r != 0)
        parallel_result_label.config(text=f"Eşdeğer Direnç (Paralel): {equivalent_resistance:.2f} Ω")
    except ValueError:
        parallel_result_label.config(text="Lütfen geçerli değerler girin")

# Ana pencere ve sayfalar
root = tk.Tk()
root.title("Ohm Kanunu ve Direnç Hesaplama")
root.geometry("400x300")

notebook = ttk.Notebook(root)
ohm_frame = ttk.Frame(notebook)
resistance_frame = ttk.Frame(notebook)
notebook.add(ohm_frame, text="Ohm Yasası")
notebook.add(resistance_frame, text="Seri/Paralel Direnç")
notebook.pack(expand=True, fill="both")

# Ohm Yasası Sayfası
tk.Label(ohm_frame, text="Gerilim (V):").grid(row=0, column=0, padx=10, pady=5)
voltage_entry = tk.Entry(ohm_frame)
voltage_entry.grid(row=0, column=1)

tk.Label(ohm_frame, text="Akım (I):").grid(row=1, column=0, padx=10, pady=5)
current_entry = tk.Entry(ohm_frame)
current_entry.grid(row=1, column=1)

calc_button = tk.Button(ohm_frame, text="Hesapla", command=calculate_ohms_law)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(ohm_frame, text="Direnç (R):")
result_label.grid(row=3, column=0, columnspan=2)

# Seri ve Paralel Direnç Sayfası
tk.Label(resistance_frame, text="Dirençleri Girin (Virgülle Ayırın):").grid(row=0, column=0, padx=10, pady=5)
resistance_values = tk.Entry(resistance_frame)
resistance_values.grid(row=0, column=1)

series_button = tk.Button(resistance_frame, text="Seri Eşdeğer Direnç", command=calculate_series_resistance)
series_button.grid(row=1, column=0, pady=5)

parallel_button = tk.Button(resistance_frame, text="Paralel Eşdeğer Direnç", command=calculate_parallel_resistance)
parallel_button.grid(row=1, column=1, pady=5)

series_result_label = tk.Label(resistance_frame, text="Eşdeğer Direnç (Seri):")
series_result_label.grid(row=2, column=0, columnspan=2)

parallel_result_label = tk.Label(resistance_frame, text="Eşdeğer Direnç (Paralel):")
parallel_result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
