import tkinter as tk
from sys import exit 
'''
Tela resposável por mostrar a avaliação do usuário
'''
class FrameResumo(tk.Frame):  #Indica que a classe vai ser um Frame
    def __init__(self,parent,controller):
        super().__init__(parent) #Coloca o frame dentro do container
        self.controller = controller  #Instancia o controlador
        self.labels = [] #Armazena os labels
        self.botoes() #Deixa os botões fixos na tela
        
    def botoes(self):
        self.titulo = tk.Label(self,text="Resumo da Avaliação",font=("Arial",12))
        self.titulo.pack(pady=10)
        
        self.container = tk.Frame(self)
        self.container.pack()
        
        self.botao_nova_atualizacao = tk.Button(self, text='Nova Atualização',command=self.recomecar)
        self.botao_nova_atualizacao.pack(side='right',pady=5)
        
        self.botao_sair = tk.Button(self,text='Sair' , command=exit)
        self.botao_sair.pack(side="left") 
    
    def atualizar(self):
        '''
        Mostra os dados da avaliação atual e retorna para tela 1
        Limpa os labels antigos da tela também
        '''
        
        for l in self.labels:
            l.destroy()    
        self.labels.clear()
        
        dados = self.controller.exibir_dados()
        for c , v in dados.items():
            texto = f'{c} : {v}'
            l = tk.Label(self.container , text=texto) 
            l.pack()
            
            self.labels.append(l)
            
    #limpa os dados e volta para tela 1        
    def recomecar(self):
        self.controller.resetar()
        self.controller.trocar_tela('coleta1')                 