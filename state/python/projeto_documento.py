from __future__ import annotations
from abc import ABC, abstractmethod

# Classe que sofre com as mudanças de estado
class Documento:
    _state = None
    _conteudo = ""
    
    def __init__(self, state: State, conteudo: str) -> None:
        # Define o estado inicial
        self.transitionTo(state)
        # Define o conteudo do documento
        self._conteudo = conteudo
    
    """
    Permite a mudança de estado em tempo de execução
    """
    def transitionTo(self, state: State):
        self._state = state
        self._state.context = self
    
    # Envia o documento para moderação ou publica em caso de aceite
    def publicar(self):
        self._state.publicar()
    
    # Devole o rascunho
    def rejeitar(self):
        self._state.rejeitar()
    
    # Altera o conteudo do documento
    def editar(self, conteudo: str):
        self._conteudo = conteudo
        self._state.editar()
        

class State(ABC):
    @property
    def context(self) -> Documento:
        return self._context

    @context.setter
    def context(self, context: Documento) -> None:
        self._context = context

    @abstractmethod
    def publicar(self) -> None:
        pass

    @abstractmethod
    def rejeitar(self) -> None:
        pass
    
    @abstractmethod
    def editar(self) -> None:
        pass

"""
Classes concretas que implementam comportamentos.
"""
class Rascunho(State):
    def publicar(self) -> None:
        print("Enviando o documento para o moderador...")
        # Realiza a mudança de estado
        self.context.transitionTo(Moderacao())
    def editar(self) -> None:
        print("Documento modificado com sucesso!")
    def rejeitar(self) -> None:
        pass

class Moderacao(State):
    def publicar(self) -> None:
        print("Documento publicado com sucesso!")
        self.context.transitionTo(Publicado())
    
    def rejeitar(self) -> None:
        print("O Moderador rejeitou o documento. Devolvendo o documento para rascunho...")
        self.context.transitionTo(Rascunho())
        
    def editar(self) -> None:
        print("Nao foi possivel editar, pois o documento esta com o moderador.")

class Publicado(State):
    def publicar(self) -> None:
        print("Aviso: documento ja publicado!")
        # Nao muda de estado
    
    def editar(self) -> None:
        print("Documento modificado com sucesso! Voltando para rascunho.")
        self.context.transitionTo(Rascunho())
    
    def rejeitar(self) -> None:
        print("O documento ja esta publicado, entao nao ha o que rejeitar.")
        pass

conteudo = input("Digite o conteudo: ")
documento = Documento(Rascunho(), conteudo)
documento.publicar() # Aqui o documento está em rascunho, então vai ser enviado para moderação, mudando estado para Moderacao()
documento.publicar() # Neste momento, o moderador vai enviar para publicação, mudando o estado para Publicado()
documento.publicar() # Aqui não vai fazer nada, só vai dar um aviso que o documento já foi publicado

# Experimente executar outros métodos
conteudo = input("Digite o novo conteudo: ")
documento.editar(conteudo) # Aqui muda de estado para Rascunho novamente
documento.publicar() # Depois envia para moderação
documento.rejeitar() # Porém aqui, o moderador não aprovou o documento, volta para rascunho

    
    
    