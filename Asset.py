"""
File: Asset.py
Description: Module for the class Asset for the "Into the Grid" game.
Author: Natasha Hunter
ID: 110439590
Username: hunny006
Git Repository: https://github.com/UniSA-STEM/basic-oop-GittaOgg
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset():

    """
    A class which represents assets in the game.

    Attributes
    ------------
    name : str
        name of the asset
    description: str
        describing what the asset is used for
    encrypted: bool
        describing if the asset is encrypted or not

    Methods
    -------
    get_encryption:
        returns the encryption of the asset
    get_name:
        returns the name of the asset
    get_description:
        returns the description of the asset
    encrypt:
        encrypts the asset
    decrypt:
        decrypts the asset

    """


    def __init__(self, name, description, encrypted =False):
        self.name = name
        self.description = description
        self.encrypted = encrypted

    def __str__(self):
        if self.encrypted:
            return f'**********\n<{self.name}>: <{self.description}> [Encrypted]\n'
        else:
            return f'**********\n<{self.name}>: <{self.description}>\n'

    def __eq__(self, other):
        return isinstance(other, Asset) and self.name == other.name and self.description == other.description


    def get_encryption(self):
        return self.encrypted

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def encrypt(self):
        """ If asset is not encrypted, encrypts it. """
        if not self.encrypted:
            self.encrypted = True

    def decrypt(self):
        """ If asset is encrypted, decrypts it. """
        if self.encrypted:
            self.encrypted = False


