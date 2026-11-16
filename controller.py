from model import SuspeitoModel
from view import SuspeitoView


class SuspeitoController:
    def __init__(self):
        self.model = SuspeitoModel()
        self.view = SuspeitoView()

    def iniciar(self):
        while True:
            opcao = self.view.exibir_menu()
            if opcao == '1':
                nome, crime, nivel = self.view.obter_dados_suspeito()
                try:
                    self.model.salvar_suspeito(nome, crime, nivel)
                    self.view.mostrar_mensagem("Registro arquivado com sucesso!")
                except ValueError as erro:
                    self.view.mostrar_mensagem(f"Erro de validação: {erro}")
            elif opcao == '2':
                dados = self.model.listar_todos()
                self.view.mostrar_lista(dados)
            elif opcao == '3':
                suspeito_id = self.view.obter_id_remocao()
                try:
                    if self.model.deletar_suspeito(suspeito_id):
                        self.view.mostrar_mensagem("Registro removido do cofre.")
                    else:
                        self.view.mostrar_mensagem("ID não encontrado.")
                except ValueError:
                    self.view.mostrar_mensagem("Erro: O ID deve ser um número inteiro.")
            elif opcao == '4':
                minimo = self.view.obter_periculosidade_minima()
                try:
                    dados = self.model.filtrar_por_periculosidade(minimo)
                    self.view.mostrar_lista(dados)
                except ValueError:
                    self.view.mostrar_mensagem("Erro: O nível mínimo deve ser um número inteiro.")
            elif opcao == '0':
                self.view.mostrar_mensagem("Encerrando sistema...")
                break
            else:
                self.view.mostrar_mensagem("Opção inválida!")