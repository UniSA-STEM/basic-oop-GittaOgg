"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset():

    def __init__(self, name, description, encrypted =False):
        self.name = name
        self.description = description
        self.encrypted = encrypted

    def __str__(self):
        if self.encrypted==True:
            return f'**********\n<{self.name}>: <{self.description}> [Encrypted]\n'
        else:
            return f'**********\n<{self.name}>: <{self.description}>\n'

    def get_encryption(self):
        return self.encrypted


    def encrypt(self):
        if self.encrypted==True:
            print(f'{self.name} is already encrypted')


    def decrypt(self):
        if self.encrypted==True:
            self.encrypted = False


    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_encryption(self):
        return self.encrypted


ass1 = Asset('HP1','testhardwarepatch', encrypted=True)
print(ass1)
ass1.encrypt()
print(ass1)
ass1.decrypt()
print(ass1)