from base import Field
class String(Field):
    base = str
    def __init__(self,name):
        super().__init__(name)
        
    def __eq__(self,other):
        self.type_check(other)    
        return f'''{self.name}="{other}"'''

class Integer(Field):
    base = int
    def __init__(self,name):
        super().__init__(name)
    
    def __eq__(self,other):
        self.type_check(other)
        return f'''{self.name}={other}'''
    
    def __gt__(self,other):
        self.type_check(other)
        return f'''{self.name} > {other}'''

class Array(Field):
    
    def __init__(self,name,contained):
        super().__init__(name)
        self.base = contained
        
    def _in(self,other):
        self.type_check(other)
        return f'''{other} IN {self.name}'''
