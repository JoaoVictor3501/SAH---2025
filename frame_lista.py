import tkinter as tk

'''
Tela responsável por listar todas as avaliações já feitas , possui o nome e o email mascarado,
ela também possui um botão para visualizar os detalhes de outras avaliações
'''
class FrameLista(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent) #Container onde o frame será exibido
        self.controller = controller  #Instancia o controlador
        self.labels = [] #Armazena os labels na lista

        self.titulo = tk.Label(self, text='Lista de Avaliações', font=('Arial', 16)) #Título
        self.titulo.pack(pady=10)

        self.container = tk.Frame(self) #Container onde as avaliações serão listadas
        self.container.pack()
        
        self.botao_voltar = tk.Button(self,text='Voltar para Tela 1' , command= lambda: controller.trocar_tela('coleta1'))
        self.botao_voltar.pack()    #Botão para voltar a tela 1

    def atualizar_lista(self):
        #limpa os dados antigos
        for widget in self.container.winfo_children():
            widget.destroy()

        #Exibe as avaliações que foram feitas pelos usuários com o nome e email mascarado e um botão para mostrar a avaliação
        avaliacoes = self.controller.pegar_lista_avaliacoes()
        for avaliacao in avaliacoes:
            nome = avaliacao.get('Nome', '')
            email = avaliacao.get('Email', '')
            email_mascarado = email[:2] + "***@***"
            
            linha = tk.Frame(self.container)
            label = tk.Label(linha, text=f"Nome: {nome} | Email: {email_mascarado}")
            label.pack(side='left',padx=5)

            botao_detalhes = tk.Button(linha, text="Mostrar detalhes",
                            command=lambda av=avaliacao: self.controller.mostrar_detalhes(av))
            
            botao_detalhes.pack(side='right', padx=5)
            linha.pack(fill='x', pady=2)
