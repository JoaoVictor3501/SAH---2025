import tkinter as tk #importa o tkinter
from tkinter import ttk
from tkinter import messagebox
'''
Tela responsável pela segunda parte da coleta de dados
'''
class FrameColeta2(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent) #Herda o CONTAINER PARA POSICIONAR O FRAME/TELA
        self.controller = controller #Instancia o controlador
        self.coleta2()
    
    def coleta2(self):
        self.titulo = tk.Label(self, text='AVALIAÇÃO')
        self.titulo.grid(row=0,column=0,columnspan=2,sticky='w')
        
        self.quarto = tk.Label(self,text='Quarto escolhido')
        self.quarto.grid(row=1,column=0,sticky='w')
        self.quartos = ['Standard','Deluxe','Suite']
        self.combo_quartos = ttk.Combobox(self,values=self.quartos)
        self.combo_quartos.set('Opções de Quarto')
        self.combo_quartos.grid(row=1,column=1,padx=5,pady=5,sticky='w')
        
        self.hospedes = tk.Label(self,text='Tipo de Hospedes')
        self.hospedes.grid(row=2,column=0,sticky='w')
        self.hospedes_opções = ['Solteiro','Casal','Familia']
        self.combo_hospedes = ttk.Combobox(self,values=self.hospedes_opções)
        self.combo_hospedes.set('Opções de Hospedes')
        self.combo_hospedes.grid(row=2,column=1,padx=5,pady=5,sticky='w')
    
        self.tempo_hospedagem = tk.Label(self,text='Tempo de Hospedagem')
        self.tempo_hospedagem.grid(row=3,column=0,sticky='w')
        self.entrada_tempo_hospedagem = tk.Entry(self)
        self.entrada_tempo_hospedagem.grid(row=3,column=1,padx=5,pady=5,sticky='w')
        
        self.valor_hospedagem = tk.Label(self,text='Valor Total Pago')
        self.valor_hospedagem.grid(row=4,column=0,sticky='w')
        self.entrada_valor_hospedagem = tk.Entry(self)
        self.entrada_valor_hospedagem.grid(row=4,column=1,padx=5,pady=5,sticky='w')
        
        #Criando e associando radionbutton
        self.sat_atendimento = tk.StringVar()
        self.sat_comida = tk.StringVar()
        self.sat_quarto = tk.StringVar()
        
        self.satisfacao_atendimento = tk.Label(self, text="Atendimento")
        self.satisfacao_atendimento.grid(row=5,column=0,padx=5,pady=5,sticky='w')
        
        self.sat_atendimento_ruim = ttk.Radiobutton(self, text="Ruim", variable=self.sat_atendimento, value="Ruim")
        self.sat_atendimento_ruim.grid(row=5,column=1,sticky='w')
        
        self.sat_atendimento_bom = ttk.Radiobutton(self, text="Bom", variable=self.sat_atendimento, value="Bom")
        self.sat_atendimento_bom.grid(row=5,column=2,padx=5,pady=5,sticky='w')
        
        self.satisfacao_comida = tk.Label(self, text="Comida")
        self.satisfacao_comida.grid(row=6,column=0,padx=5,pady=5,sticky='w')
        
        self.sat_comida_ruim = ttk.Radiobutton(self, text="Ruim", variable=self.sat_comida ,value="Ruim")
        self.sat_comida_ruim.grid(row=6, column=1, sticky='w')
        
        self.sat_comida_bom = ttk.Radiobutton(self, text="Bom", variable=self.sat_comida, value="Bom")
        self.sat_comida_bom.grid(row=6,column=2,sticky='w')
        
        self.satisfacao_quarto = tk.Label(self, text="Quarto")
        self.satisfacao_quarto.grid(row=7,column=0,sticky='w')
        
        self.sat_quarto_ruim = ttk.Radiobutton(self, text="Ruim", variable=self.sat_quarto, value="Ruim")
        self.sat_quarto_ruim.grid(row=7,column=1,sticky='w')
        
        self.sat_quarto_bom = ttk.Radiobutton(self, text="Bom", variable=self.sat_quarto, value="Bom")
        self.sat_quarto_bom.grid(row=7,column=2,sticky='w')
        
        self.feedback = tk.Label(self,text='Deixe o seu Feedback')
        self.feedback.grid(row=8,column=0,sticky='w')
        
        self.entrada_feedback = tk.Entry(self)
        self.entrada_feedback.grid(row=8,column=1,columnspan=2,padx=5,pady=5,sticky="w")
        
        self.voltar = tk.Button(self,text='Voltar', command=lambda: self.controller.trocar_tela("coleta1"))
        self.voltar.grid(row=9,column=0)
        
        self.salvar_e_exibir = tk.Button(self,text='Salvar e Exibir', command=self.enviar_dados)
        self.salvar_e_exibir.grid(row=9,column=1)
    
    #Envia os dados pro controller    
    def enviar_dados(self): #Aciona a função responsável por guardar os dados e os exibe para o usuário
        dados = {
            "Tipo de Quarto Contratado": self.combo_quartos.get(),
            "Quantidade de Hospedes": self.combo_hospedes.get(),
            "Tempo de Hospedagem": self.entrada_tempo_hospedagem.get(),
            "Valor pago": self.entrada_valor_hospedagem.get(),
            "Satisfação Atendimento": self.sat_atendimento.get(),
            "Satisfação com a Comida": self.sat_comida.get(),
            "Satisfação com o Quarto": self.sat_quarto.get(),
            "Feedback": self.entrada_feedback.get()
        }
        self.controller.salvar_parcial(dados)
        
        resultado = self.controller.enviar_avaliacao()
        if resultado ['sucesso']:
            messagebox.showinfo('Sucesso', resultado['mensagem'])
            self.controller.trocar_tela("resumo")
        else:
            messagebox.showerror('Falha', resultado['mensagem'])
    
    #Limpa todos os campos 
    def zerar_campos(self):
         self.combo_quartos.set("Opções de Quarto")
         self.combo_hospedes.set("Opções de Hospedes")
         self.entrada_tempo_hospedagem.delete(0,tk.END)
         self.entrada_valor_hospedagem.delete(0,tk.END)
         self.entrada_feedback.delete(0,tk.END)
         self.sat_atendimento.set('')
         self.sat_comida.set('')
         self.sat_quarto.set('')          