import pacientes_bib as p
import tkinter as tk


#janela Principal
janela_principal = tk.Tk()
janela_principal.title("Hospital Monte Siao")
janela_principal.geometry("400x400")
janela_principal.resizable(False, False)
janela_principal.config(bg= "#40E0D0")

bt_registro = tk.Button(text="Registra Paciente na fila", command=p.registro)
bt_registro.pack()
                        
# Janela de Registro

janela_registro = tk.Tk()
janela_registro.title("Registro")
janela_registro.geometry("400x400")
janela_registro.register(False, False)

# janela da fila
janela_fila = tk.Tk()
janela_fila.title("Fila")
janela_fila.geometry("400x400")
janela_fila.register(False, False)





janela_principal.mainloop()