class SecureClass:
    def init(self, secure_field):
        self.secure_field = secure_field

    def get_secure_field(self):
        return self.secure_field

    def set_secure_field(self, value):
        if self.validate(value):
            self.secure_field = value
        else:
            raise ValueError("Invalid value")

    def __validate(self, value): #Metoda prywatna
        return isinstance(value, int) and value > 0

secure = SecureClass(123)
print(secure.get_secure_field()) 
secure.set_secure_field(456) 
print(secure.get_secure_field())