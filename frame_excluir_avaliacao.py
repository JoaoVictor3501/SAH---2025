import tkinter as tk  #Importa o tkinter
from tkinter import messagebox

'''
Tela responsável por excluir a avaliação do usuário
'''

class ExcluirAvaliacao(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller  #Instancia o controlador
        
        self.titulo = tk.Label(self, text="Tela Confirmar Exclusão", font=("Arial", 14))
        self.titulo.pack(pady=10)

        self.confirmar = tk.Label(self, text="Digite o email completo para confirmar a exclusão:")
        self.confirmar.pack()
        
        self.entrada_email = tk.Entry(self, width=30)
        self.entrada_email.pack(pady=5)

        self.botao_confirmar = tk.Button(self, text="Confirmar", command=self.confirmar_exclusao)
        self.botao_confirmar.pack(pady=5)

        self.botao_voltar = tk.Button(self, text="Cancelar", command=lambda: controller.trocar_tela("detalhes_avaliacao"))
        self.botao_voltar.pack(pady=5)
        
    def confirmar_exclusao(self): #Funcão responsável por excluir a avaliação
        email_digitado = self.entrada_email.get().strip().lower()
        avaliacao = self.controller.pegar_avaliacao_para_excluir()
        
        #Verifica se tem uma avaliacao para exibir
        if not avaliacao:
            messagebox.showerror('Erro, nenhuma avaliação para excluir!')
            return
        
        email_original = avaliacao.get("Email", "").strip().lower()
       
        #Verifica se o email digitado é igual ao original
        if email_digitado == email_original:
            self.controller.excluir_avaliacao(avaliacao)
            messagebox.showinfo("Avaliação foi excluída!")
            self.entrada_email.delete(0,tk.END)
            self.controller.trocar_tela("lista_avaliacoes")
        
        else:
            messagebox.showerror("Exclusão não autorizada")
            self.entrada_email.delete(0,tk.END)
            self.controller.trocar_tela("lista_avaliacoes")                