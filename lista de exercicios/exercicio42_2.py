import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Certifique-se de ter a biblioteca PIL/Pillow instalada

def verificar_triangulo():
    try:
        r1 = float(entry_r1.get())
        r2 = float(entry_r2.get())
        r3 = float(entry_r3.get())

        if (r1 + r2) > r3 and (r1 + r3) > r2 and (r3 + r2) > r1:
            resultado_label.config(text='Triângulo formado', fg='green', font=('Arial', 14, 'bold'))
            
            if r1 == r2 == r3:
                resultado_tipo.config(text='Triângulo equilátero', fg='blue', font=('Arial', 12))
            elif r1 != r2 and r1 != r3 and r2 != r3:
                resultado_tipo.config(text='Triângulo escaleno', fg='blue', font=('Arial', 12))
            else:
                resultado_tipo.config(text='Triângulo isósceles', fg='blue', font=('Arial', 12))

        else:
            resultado_label.config(text='Essas medidas não formam um triângulo', fg='red', font=('Arial', 14, 'bold'))
            resultado_tipo.config(text='', font=('Arial', 12))

    except ValueError:
        messagebox.showerror('Erro', 'Entrada inválida. Certifique-se de digitar um número válido.')

# Configuração da janela
root = tk.Tk()
root.title('Verificador de Triângulo')


# Entradas
entry_frame = tk.Frame(root)
entry_frame.pack()

label_r1 = tk.Label(entry_frame, text='Lado AB:')
entry_r1 = tk.Entry(entry_frame)
label_r2 = tk.Label(entry_frame, text='Lado CD:')
entry_r2 = tk.Entry(entry_frame)
label_r3 = tk.Label(entry_frame, text='Lado EF:')
entry_r3 = tk.Entry(entry_frame)

label_r1.grid(row=0, column=0, padx=5, pady=5)
entry_r1.grid(row=0, column=1, padx=5, pady=5)
label_r2.grid(row=1, column=0, padx=5, pady=5)
entry_r2.grid(row=1, column=1, padx=5, pady=5)
label_r3.grid(row=2, column=0, padx=5, pady=5)
entry_r3.grid(row=2, column=1, padx=5, pady=5)

# Botão para verificar o triângulo
verificar_button = tk.Button(root, text='Verificar', command=verificar_triangulo, bg='green', fg='white', font=('Arial', 12, 'bold'))
verificar_button.pack(pady=10)

# Resultados
resultado_label = tk.Label(root, text='', font=('Arial', 14, 'bold'))
resultado_tipo = tk.Label(root, text='', font=('Arial', 12))

resultado_label.pack()
resultado_tipo.pack()

root.mainloop()
