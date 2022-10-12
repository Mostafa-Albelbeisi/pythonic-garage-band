from abc import abstractmethod, ABC
from unicodedata import name

# This is first class
class Band:
    instances=[] 
    def __init__(self, name, members):
        self.name=name
        self.members=members
        Band.instances.append(self)

    def play_solos(self):
        solos=[]
        for i in self.members:
             solos.append(i.play_solo())
        return solos
    
    def __str__(self):
        return f'Our band is {self.name}'
    def __repr__(self):
        return f"Band instance. Name = {self.name}"

    @classmethod
    def to_list(cls):
        return cls.instances   

# Here we create a base class, this class will be inherited to other class,
class Musician(ABC):
        members = []
        def __init__(self, name):
            self.name = name
            # Musician.members.append(self.name)
        def play_solos(self):
            return ""
        def get_instrument(self):
            return ""
        def __str__(self):
            return f"My name is {self.name} and I play {self.get_instrument()}"
        def __repr__(self):
            return f"{self.__class__.__name__} instance. Name = {self.name}"
        def play_solo(self):
            return self.play_solos()

            

#Create a Guitarist class
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)
        # Here as long as it is inhert from Musician Calss, so we don't to define a new function for to str and repr.
    # def __str__(self):
    #     return f"My name is {self.name} and I play guitar"
    # def __repr__(self):
    #     return f"Guitarist instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "guitar"
    @staticmethod
    def play_solo():
        return "face melting guitar solo"  

#Create a Drummer class
class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
        # And here like Guitarist class
    # def __str__(self):
    #     return f"My name is {self.name} and I play drums"
    # def __repr__(self):
    #     return f"Drummer instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "drums"
    @staticmethod
    def play_solo():
        return "rattle boom crash"
#Create a Bassist class    
class Bassist(Musician):
    def __init__(self,name):
        super().__init__(name)
        #And here the same 
    # def __str__(self):
    #     return f"My name is {self.name} and I play bass"
    # def __repr__(self):
    #     return f"Bassist instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "bass"
    @staticmethod
    def play_solo():
        return "bom bom buh bom"