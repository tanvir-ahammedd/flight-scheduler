class Aircraft:
    def __init__(self, make, code, typ, flight_range):
        self.make = make
        self.code = code
        self.typ = typ
        self.flight_range = flight_range
        
    def get_make(self):
        return self.make
    
    def __repr__(self):
        return f'Aircraft make: {self.make} code: {self.code} type: {self.typ} range: {self.flight_range}'