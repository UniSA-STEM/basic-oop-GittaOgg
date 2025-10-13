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
            return f'**********\n<{self.name}>: <{self.description}> [Encrypted]\n**********\n'
        else:
            return f'**********\n<{self.name}>: <{self.description}>\n**********\n'




spike1 = Asset("DataSpike", "data spike", True)
print(spike1)