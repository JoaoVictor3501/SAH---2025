import tkinter as tk
from view.frame_lista import FrameLista
from view.frame_detalhes import FrameDetalhes
from view.frame_coleta1 import FrameColeta
from view.frame_coleta2 import FrameColeta2
from view.frame_resumo import FrameResumo
from view.frame_excluir_avaliacao import ExcluirAvaliacao
from model import BancoMongodb
#Importa as views e o model que se comunica com o banco(Mongodb) 
'''
Classe responsável por controllar a aplicação
Gerencia as telas , se comunica com o model e a view
'''
class Controller:
    def __init__(self, root):
        self.frames = {}             #Armazena os frames exemplo coleta1 : FrameColeta
        self.root = root             #Jela principal
        self.model = BancoMongodb()  #Cria o banco para fazer o acesso a ele salvar / excluir
        self.dados_avaliacao = {}    #Recebe os dados e os armazena temporariamente para serem enviados ao banco
        
        #Cria o Container para posicionar os frames e o coloca dentro da janela principal
        self.container = tk.Frame(root) 
        self.container.pack()
        
        #Instancia todas as telas e as associa ao dicionário a uma chave para fazer a troca de tela
        self.frames["coleta1"] = FrameColeta(self.container, self) #Indica que serão colocados dentro de container
        self.frames["coleta2"] = FrameColeta2(self.container, self)
        self.frames["resumo"] = FrameResumo(self.container, self)
        self.frames["lista_avaliacoes"] = FrameLista(self.container, self)
        self.frames["detalhes_avaliacao"] = FrameDetalhes(self.container, self)
        self.frames["excluir_avaliacao"] = ExcluirAvaliacao(self.container, self)
        
        for frame in self.frames.values(): #<- percorre os frames e os posiciona no mesmo lugar com o tkraise na funcao trocar_tela
            frame.grid(row=0,column=0,sticky="nsew")
        self.trocar_tela('coleta1')
   
    #Troca de tela com base na chave passada
    def trocar_tela(self,trocar):
        if trocar == "resumo":
            self.frames["resumo"].atualizar()
        elif trocar == "lista_avaliacoes":
            self.frames['lista_avaliacoes'].atualizar_lista()
                
        self.frames[trocar].tkraise()    

    #Atualiza os dados temporários no dicionário com os dados da tela 1 e 2 (coleta1 , coleta2)
    def salvar_parcial(self,dados):
        self.dados_avaliacao.update(dados)
    
    #Trata avaliacao antes de salvar
    def avaliacao_completa(self):
        sucesso , mensagem = self.model.tratar_dados(self.dados_avaliacao)
        return {'sucesso': sucesso , 'mensagem': mensagem}    
    
    #Salva avaliacao    
    def salvar_(self):
        sucesso , mensagem = self.model.salvar_avaliacao(self.dados_avaliacao)
        return {'sucesso': sucesso , 'mensagem': mensagem}    

    #Valida e salva a avaliacao se estiver correta (todos os campos estiverem preenchidos corretamente)
    def enviar_avaliacao(self):
        resultado = self.avaliacao_completa()
        if not resultado['sucesso']:
            return resultado
        return self.salvar_()
    
    #Retorna os dados para a tela resumo 
    def exibir_dados(self):
        return self.dados_avaliacao
    
    #Pega todas as avaliacoes do banco  
    def pegar_lista_avaliacoes(self):
        return self.model.lista_avaliacoes()
    
    #Pega a avaliação selecionada para excluir
    def pegar_avaliacao_para_excluir(self):
        return getattr(self, "avaliacao_para_excluir", None)
    
    #Define a avaliacao atual mostra os detalhes dela
    def mostrar_detalhes(self,avaliacao):
        self.avaliacao_para_excluir = avaliacao
        self.frames['detalhes_avaliacao'].mostrar_dados(avaliacao)
        self.trocar_tela('detalhes_avaliacao')
    
    #Exclui a avaliação , atualiza a lista e volta para tela de lista
    def excluir_avaliacao(self, avaliacao):
        if "_id" in avaliacao:
            self.model.excluir(avaliacao["_id"])
        self.frames['lista_avaliacoes'].atualizar_lista()
        self.trocar_tela("lista_avaliacoes")       
            
    #Limpa os dados do usuário
    def resetar(self):
        self.dados_avaliacao = {}
        self.frames['coleta1'].zerar_campos()
        self.frames['coleta2'].zerar_campos()    