from sqlalchemy import Column, Integer, String
class User:
    id = Column(String(50), primary_key=True)
    email = Column(String(150))
    password = Column(String(50))
    name = Column(String(150))
    role = Column(Integer)

    def __init__(self, id, email, password, name, role='user'):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.role = role

    # Getter setter for id
    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value   

    # Getter setter for email
    def get_email(self):
        return self.email

    def set_email(self, value):
        self.email = value

    # Getter setter for password
    def get_password(self):
        return self.password

    def set_password(self, value):
        self.password = value

    # Getter setter for name
    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value        

    # Getter setter for role
    def get_role(self):
        return self.role

    def set_role(self, value):
        self.role = value          