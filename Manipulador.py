# importa biblioteca
import json  

# classe Arquivo Json
class Manipulador:
    def criar_arquivo(self, nome_arquivo): # parametros
        try:
            usuarios = [
                {
                    'codigo': 0,
                    'nome': 'Admin',
                    'cpf': '000.000.000-01',
                    'e-mail': 'admin@admin.com.br',
                    'profissao': 'Administrador'
                }
            ]

            # serializando(convertendo) objeto python como json
            json_dados = json.dumps(usuarios, ensure_ascii=False)
            with open(f"{nome_arquivo}.json", "w", encoding="utf-8") as f: # utf-8 é para fazer a troca dos acentos
                f.write(json_dados)
                return f"{nome_arquivo}.json criado com sucsso."

        except Exception as e:
            return f"Não foi possível criar o arquivo. {e}."
    
    
    def abrir_arquivo(self, nome_arquivo):       
        with open(f"{nome_arquivo}.json", "r", encoding="utf-8") as f: 
            dados = json.load(f)
        return dados
    
    def salvar_dados(self, usuarios, nome_arquivo):
        try:
            with open(f"{nome_arquivo}.json", "w", encoding="utf-8") as f:
                 json.dump(usuarios, f)  # Escreve o JSON no arquivo
            return f"Dados salvos com sucesso."
        except Exception as e:
            return f"Não foi possível salvar os dados. {e}. "
    
    # destrutor
    def __del__(self):
        return "Manipulador destruído."
    
