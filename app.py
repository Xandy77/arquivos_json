# importa as classes
import os
from pessoa import *
from Manipulador import *

if __name__ == "__main__":

    # instaciar os objetos
    p = Pessoa(0, '', '', '', '')
    m = Manipulador()

    while True:
        # menu
        print("1 - Criar um novo arquivo JSON.")
        print("2 - Abrir e ler arquivo JSON.")
        print("3 - Salvar novo usuario.")
        print("0 - Sair do programa.")

        opcao = input("Informe a opção desejada: ")

        # Limpeza do console(tela)
        os.system("cls")

        match opcao: 
            case "0":
                break
            
            case "1":
                novo_arquivo = input("Informe o nome do arquivo que deseja criar: ")
                print(m.criar_arquivo(novo_arquivo))
                continue 

            case "2":
                ler_arquivo = input("Informe o nome do arquivo que deseja abrir: ")
                try:
                    os.system("cls")
                    usuarios = m.abrir_arquivo(ler_arquivo)
                    print(f"Arquivo aberto: {ler_arquivo}.json.\n")
                    
                    # para ler(imprimir) de forma organizada(na ordem certa) os dados
                    for i in range(len(usuarios)):
                        for campo in usuarios[i]:
                            print(f"{campo.capitalize()}: {usuarios[i].get(campo)}.")
                        print(f"\n{'-'*30}\n")
                
                except Exception as e:
                    print(f"Não foi possível abrir o arquivo. {e}.")
                
                # para retornar ao inicio do menu(para não ter que repetir o comando dentro do try e for)
                finally:
                    continue
            case "3":
                try:
                    # criando um dicionario chamado usuario
                    usuario = {}      

                    campos = ('nome', 'cpf', 'e-mail', 'profissao')
                    print(f"Arquivos aberto: {ler_arquivo}.jason\n")
                    usuario['codigo'] = len(usuarios)
                    
                    for campo in campos:
                        usuario[campo] =  input(f"Informe o campo {campo.capitalize()}:")
                 
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuarios, ler_arquivo))

                except Exception as e:
                    print(f"Não foi possível realizar a operação. {e}.")
                finally:
                    continue


            case _:
                print("Opção inválida.")
                continue


