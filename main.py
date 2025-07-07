import tkinter as tk
from controller import Controller
'''
MAIN inicia  o programa
'''
if __name__ == "__main__":
    root = tk.Tk() #Cria a janela pai
    
    root.geometry("600x400") #Coloca um tamanho para a tela
    
    root.title("Sistema de Avaliações") #Coloca o título
    
    app = Controller(root) #Cria o controllador e passa como argumento a janela pai root que vai ter os frames dentro
    
    root.mainloop() #Inicia o loop da interface para manter a janela aberta
