
class Simbolo():
    
    # token -> String   lexema -> String   palabraReservada -> boolena
    def __init__(self, token, lexema, palabraReservada):
        self.token = token
        self.lexema = lexema
        self.palabraReservada = palabraReservada

    def __str__(self):
        return f"Simbolo: Lexema = {self.lexema}     Token = {self.token}     Palabra Reservada = {self.palabraReservada} /n"

    def diccionario(self):
        diccionario = {"token" : self.token, "lexema" : self.lexema, "palabra reservada" : self.palabraReservada}
        return diccionario

if __name__ == "__main__":
    pass
    


