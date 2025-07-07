import tkinter as tk #Importa o tkinter
'''
Tela responsável por mostrar os detalhes da avaliação selecionada
Aqui o usuário pode excluir ou retornar a tela de lista de avaliações
'''

class FrameDetalhes(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller #Instancia o controller para pode excluir ou mudar de tela
        self.labels = [] #Armazena os labels 

        #Título
        self.titulo = tk.Label(self, text='DETALHES DA AVALIAÇÃO', font=('Arial', 12))
        self.titulo.pack(pady=10)
        
        #Container onde os dados da avaliação serão exibidos
        self.container_detalhes = tk.Frame(self)
        self.container_detalhes.pack()

        #Botão para excluir
        self.botao_excluir = tk.Button(self, text="Excluir", command=self.excluir)
        self.botao_excluir.pack(pady=5)

        #Botão para voltar
        self.botao_voltar = tk.Button(self, text="Voltar", command=self.voltar)
        self.botao_voltar.pack(pady=5)

        #Guarda os dados da avaliação que está sendo exibida
        self.avaliacao_atual = None 
    
    #Exibe o que o usuário preencheu
    def mostrar_dados(self, dados):
        self.dados = dados
        
        #Remove os labels antigos
        for label in self.labels:
            label.destroy()
        self.labels.clear()
        
        #Mostra os dados com os novos labels
        for c, v in dados.items():
            if c == "Email":
                v = v[:3] + "***@***"
            texto = f"{c}: {v}"
            self.label = tk.Label(self.container_detalhes, text=texto)
            self.label.pack(anchor='w')
            self.labels.append(self.label)
    
    #Envia o usuário para a tela responsável por excluir
    def excluir(self):
        self.controller.trocar_tela('excluir_avaliacao')

    #Volta para a tela de lista
    def voltar(self):
        self.controller.trocar_tela("lista_avaliacoes")
