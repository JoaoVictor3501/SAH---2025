import tkinter as tk #Importa o tkinter e sys 
from tkinter import ttk
import sys 
'''
Tela responsável por coletar os dados do usuário
'''
class FrameColeta(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent) #Herda o CONTAINER PARA POSICIONAR O FRAME/TELA
        self.controller = controller #Instancia o controlador
        self.coleta1()
    
    #coleta os dados do usuário como nome , email , ano hospedagem , cidade e hotel em que ele se hospedou
    def coleta1(self):
        self.titulo = tk.Label(self, text="SAH - Coleta de dados do Usuário")
        self.titulo.grid(row=0,column=0,columnspan=2,padx=10)
        
        self.nome = tk.Label(self,text='Nome')
        self.nome.grid(row=1,column=0,padx=5,pady=5,sticky='w')
        
        self.entrada_nome = tk.Entry(self) #Entrada do nome
        self.entrada_nome.grid(row=1,column=1,padx=5,pady=5,sticky='w')
        
        self.email = tk.Label(self,text='Email')
        self.email.grid(row=2,column=0,padx=5,pady=5,sticky='w')
        
        self.entrada_email = tk.Entry(self) #Entrada email
        self.entrada_email.grid(row=2,column=1,padx=5,pady=5,sticky='w')
        
        self.ano_hospedagem = tk.Label(self,text='Ano de Hospedagem')
        self.ano_hospedagem.grid(row=3,column=0,padx=5,pady=5,sticky='w')
        
        self.entrada_ano_hospedagem = tk.Entry(self) #Entrada do email
        self.entrada_ano_hospedagem.grid(row=3,column=1,padx=5,pady=5,sticky='w')
        
        self.cidade = tk.Label(self,text='Cidade')
        self.cidade.grid(row=4,column=0,sticky='w')
        self.cidades = ['Londrina','Maringá','Curitiba','Rolandia'] #Cria uma lista de cidades 
        
        self.combo_cidades = ttk.Combobox(self,values=self.cidades) #Cria um combobox e nos valores passa a lista de cidades
        self.combo_cidades.set('Selecione a Cidade') #Dentro do combobox coloca uma mensagem para o usuario selecionar uma cidade
        self.combo_cidades.grid(row=4,column=1,padx=5,pady=5,sticky='w')
        
        self.hotel = tk.Label(self,text='Hotel')
        self.hotel.grid(row=5,column=0,sticky='w')
        self.hoteis = ["Hotel Londrina","Hotel Bela Vista","Grand Palace Hotel","Pousada Sol Nascente", #Cria lista de hoteis
                       'Hotel Lago Azul',"Estação Real Hotel",'Hotel Central Plaza'] 
        
        self.combo_hoteis = ttk.Combobox(self,values=self.hoteis) #Cria um combobox e nos valores passa a lista de cidades
        self.combo_hoteis.set('Selecione um Hotel') #Dentro do combobox coloca uma mensagem para o usuario selecionar uma hotel
        self.combo_hoteis.grid(row=5,column=1,padx=10,pady=10,sticky='w')
        
        self.botao_avancar = tk.Button(self,text='Avançar',command=self.avançar) #Cria os botões avançar e consultar
        self.botao_avancar.grid(row=6,column=0,padx=10,pady=10,sticky='e')
        
        self.botao_consultar = tk.Button(self,text='Consultar Avaliações',command=lambda: self.controller.trocar_tela('lista_avaliacoes'))
        self.botao_consultar.grid(row=6,column=1,padx=10,pady=10,sticky='e') #No comando uso lambda para passar um argumento para ir até a tela de lista de avaliações''
        
        self.botao_sair = tk.Button(self,text='Sair', command=sys.exit)
        self.botao_sair.grid(row=6,column=2,padx=10,pady=10,sticky='e')
    
      
    def avançar(self): #Avança para próxima tela e pega os dados da primeira tela
        dados = {
            'Nome': self.entrada_nome.get(),
            'Email': self.entrada_email.get(),
            'Ano': self.entrada_ano_hospedagem.get(),
            'Cidade': self.combo_cidades.get(),
            'Hotel': self.combo_hoteis.get()
        }       
        self.controller.salvar_parcial(dados)
        self.controller.trocar_tela("coleta2")
    
    #Limpa os campos 
    def zerar_campos(self):
        self.entrada_nome.delete(0, tk.END)
        self.entrada_email.delete(0, tk.END)
        self.entrada_ano_hospedagem.delete(0, tk.END)
        self.combo_cidades.set("Selecione a Cidade")
        self.combo_hoteis.set("Selecione o Hotel")              