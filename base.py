class Field:
    base = None
    def __init__(self,name):
        self.name = name
    
    def type_check(self,other):
        if not isinstance(other,self.base):
            raise Exception(f"Type mismatch expected {self.base} but got {type(other)}")
    
class DB: 
    qstmt = ""
    def select(self,*args):
        self.qstmt = "SELECT "+",".join(args)
        return self
    
    def from_(self,bucket:str):
        self.qstmt += " FROM " + bucket
        return self
    
    def filter(self,qst:str):
        self.qstmt += " WHERE " + qst
        return self
    
    def get(self):
        return self.qstmt