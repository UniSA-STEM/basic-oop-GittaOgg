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

    def __eq__(self, other):
        return isinstance(other, Asset) and self.name == other.name and self.description == other.description


    def get_encryption(self):
        return self.encrypted


    def encrypt(self):
        if not self.encrypted:
            self.encrypted = True

    def decrypt(self):
        if self.encrypted:
            self.encrypted = False


    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_encryption(self):
        return self.encrypted


