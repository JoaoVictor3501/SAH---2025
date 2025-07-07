from pymongo import MongoClient

class BancoMongodb:
    #Criando e Conectando Banco de dados e a tabela (coleção)
    def __init__(self):
        try: #Tenta conecatar ao banco
            self.client = MongoClient("mongodb://localhost:27017") #Conecta ao banco
            self.db = self.client["Avaliação"] #Seleciona o banco avaliacao
            self.avaliacoesdb = self.db["Avaliacao_db"] #cria a tabela ou coleção avaliacao_db
       
        except Exception as erro: #Apresenta um erros e ele não conseguir conectar ao banco
            print('Erro ao conectar o banco de dados', erro)
            
    def tratar_dados(self,dados_avaliacao):
        #lista os campos obrigatórios que devem ser preenchidos corretamente
        campos_obrigatorios = ["Nome", "Email", "Ano", "Cidade", "Hotel", "Tipo de Quarto Contratado",
                           "Quantidade de Hospedes", "Tempo de Hospedagem", "Valor pago",
                           "Satisfação Atendimento", "Satisfação com a Comida", "Satisfação com o Quarto" , 'Feedback']
        
        for c in campos_obrigatorios:
            valor = dados_avaliacao.get(c, '').strip()#Pega os campos preenchidos e tira os espaços
            
            if not valor or valor.startswith('Selecione') or valor.startswith('Opções'): #Se não tiver valor ou se o valor estiver padrão como o combobox ele mostra um erro
                return False, f'O Campo "{c}" está vazio\nPreencha o campo Corretamente! '
            
            if c == 'Nome' and not valor.replace(" ","").isalpha(): #No campo de nome somente texto é aceito
                return False, f'vSomente Texto Por favor!'
            
            if c == 'Ano' :
                if not valor.isdigit():  #No campo ano somente números serão aceitos
                    return False, f'Somente números'
                
                ano = int(valor)
                if ano < 2000 or ano > 2025: #No campo de ano só aceita ano entre 2000 de 2025 
                     return False, 'Digite um ano válido entre 2000 e 2025'
           
            if c == 'Valor pago': #No campo do valor pago somente valores reais serão aceitos.
                #Caso o usuário insira uma virgula ela será substituída por ponto.
                valor = valor.replace(",",".") 
                try: 
                    valor_float = float(valor)
                    if valor_float <= 0: #Verifica se o valor não é menor que
                        return False , 'O valor não pode ser negativo'
                except:
                    return False, f'Somente números são aceitos!. Use vírgula o ou ponto como separador decimal exemplo: 1,00' 
            
            if c == 'Email': #No email ele verifica se o tamanho é menor que 5 caracteres
                if len(valor) < 3:
                    return False , f'Email muito curto'
                
                if '@' not in valor: #Verifica se tem @ no email
                    return False , f'Erro, É necessário colocar @ no email'
                
                dominios_validos = ['@gmail.com', "@outlook.com", "@hotmail.com"] #Verifíca se termina com os domínios permitidos  
                if not any(valor.endswith(dom) for dom in dominios_validos):
                    return False, f'Utilize um domínio válido como gmail.com , @outlook.com@ ou hotmail.com!' 
        
        return True, F'Todos os dados foram preenchidos!' #Retorna verdadeiro caso ele preencha as informações corretamente
    
    #Pega todas as avaliações
    def lista_avaliacoes(self):
        return self.avaliacoesdb.find()         
                   
    #Salva
    def salvar_avaliacao(self,dados_avaliacao):
        try: #Tenta salvar e se conseguir retorna verdadeiro retorna com a mensagem
            self.avaliacoesdb.insert_one(dados_avaliacao)    
            return True, f'Sucesso ao salvar os dados, Verifique a tela de consulta!' 
        
        except: #Retorna falso e uma mensagem
          return False , f'Erro ao Salvar os dados!'

    #Exclui
    def excluir(self,id):
        try:
            self.avaliacoesdb.delete_one({"_id": id}) #Tenta excluir a avaliação utilizando o id dela , se conseguir retorna verdadeiro
            return True
        
        except Exception as e:
            print('Erro ao excluir' , e)
            return False #Retorna falso se der erro
    