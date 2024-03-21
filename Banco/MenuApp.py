class Menu:

    @staticmethod
    def montar_menu():
        separador = "_____" * 10
        menu = """
            1 - Criar conta
            2 - Exibir extrato
            3 - Realizar operações financeiras
            4 - Sair
        """
        menu_sem_espacos = '\n'.join(line.strip() for line in menu.split('\n'))
        menu_completo = f"{separador}{menu_sem_espacos}{separador}"
        return menu_completo
