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
        print("4 - Alterar dados do usuario.")
        print("5 - Deletar usuario.")
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
            
            
            # case "3":
            #     try:
            #         # criando um dicionario chamado usuario
            #         usuario = {}      

            #         campos = ('nome', 'cpf', 'e-mail', 'profissao')
            #         print(f"Arquivos aberto: {ler_arquivo}.jason\n")
            #         usuario['codigo'] = len(usuarios)
                    
            #         for campo in campos:
            #             usuario[campo] =  input(f"Informe o campo {campo.capitalize()}:")
                 
            #         usuarios.append(usuario)
            #         print(m.salvar_dados(usuarios, ler_arquivo))

            #     except Exception as e:
            #         print(f"Não foi possível realizar a operação. {e}.")
            #     finally:
            #         continue
                


            case "3":
                try:
                    print(f"Arquivo aberto: {ler_arquivo}.json\n")
                    p.codigo = len(usuarios)
                    p.nome = input("Informe o nome: ")
                    p.cfp = input("Informe o cpf: ")
                    p.email = input("Informe o e-mail: ")
                    p.profissao = input("Informe a profissão: ")
                    usuario = dict(codigo=p.codigo, nome=p.nome, cpf=p.cpf, email=p.email, profissao=p.profissao)
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuarios, ler_arquivo))
                except Exception as e:
                    print(f"Não foi possível realizar a operação. {e}.")
                finally:
                    continue
            
            case "4":
                try:
                    print(f"Arquivo aberto: {ler_arquivo}.json.\n")
                    codigo = int(input("Informe o código do usuário que deseja alterar os dados: "))
                    for campo in usuarios[codigo]:
                        print(f"Valor atual do campo {campo}: {usuarios[codigo].get(campo)}")

                        novo_dado = input(f"Informe o novo dado do campo {campo} ou aperte 'Enter' caso deseje manter o mesmo valor: ")
                        if novo_dado:
                            usuarios[codigo][campo] = novo_dado
                        else:
                            ...
                    print(m.salvar_dados(usuarios, ler_arquivo))
                except Exception as e:
                    print(f"Não foi possível alterar os dados. {e}.")
                finally:
                    continue

            case "5":
                try:
                    print(f"Arquivo aberto: {ler_arquivo}.json.\n")
                    codigo = int(input("Informe o código do usuário que deseja deletar: "))
                    nome_deletado = usuarios[codigo]['nome']
                    confirmacao = input(f"Deseja deletar o usuário {nome_deletado}? Digite 'SIM' para confirmar.").upper()
                    if confirmacao == 'SIM':
                        del(usuarios[codigo])

                        # alteração no json
                        print(m.salvar_dados(usuarios, ler_arquivo))
                        print(f"Usuário {nome_deletado} deletado com sucesso.")
                    else:
                        print(f"Usuário {nome_deletado} não foi excluído")
                        
                except Exception as e:
                    print(f"Não foi possível deletar o arquivo. {e}.")
                finally:
                    continue


            case _:
                print("Opção inválida.")
                continue


