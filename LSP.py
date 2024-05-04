# Liskov Substitution Principle
from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self) -> bool:
        pass

class BasicAuth(Authentication):
    def __init__(self, password_source: str):
        self.password_source = password_source
    
    def authenticate(self) -> bool:
        password = self.get_password()
        return True

    def get_password(self) -> str:
        return self.password_source

class PassAuth(BasicAuth):
    def authenticate(self) -> bool:
        return True

class DNAAuth(BasicAuth):
    def authenticate(self) -> bool:
        return True

def auth_user(auth_method: Authentication) -> bool:
    return auth_method.authenticate()