from abc import ABC,abstractmethod

class DB(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self,field,new_field):
        pass
