# Interface Segregation Principle
from abc import ABC, abstractmethod

class CreateService(ABC):
    @abstractmethod
    def save(self, data):
        pass

class RetrieveService(ABC):
    @abstractmethod
    def get(self, id):
        pass

class UpdateService(ABC):
    @abstractmethod
    def update(self, id, data):
        pass

class DeleteService(ABC):
    @abstractmethod
    def delete(self, id):
        pass

class UserService(CreateService, RetrieveService, UpdateService, DeleteService):
    def save(self, data):
        print("User was saved")
    
    def get(self, id):
        print("User was retrieved")
    
    def update(self, id, data):
        print("User was updated")
    
    def delete(self, id):
        print("User was deleted")

class OrderService(CreateService, RetrieveService, UpdateService):
    def save(self, data):
        print("Order was saved")
    
    def get(self, id):
        print("Order was retrieved")
    
    def update(self, id, data):
        print("Order was updated")
