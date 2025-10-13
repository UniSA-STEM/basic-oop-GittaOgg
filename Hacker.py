"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:

    def __init__(self, name, crypto_token =1, rig = False, security_chip = 0, hardware_patch = 0,trace_level = 0 ):
        self.name = name
        self.crypto_token = crypto_token
        self.rig = rig
        self.security_chip = security_chip
        self.hardware_patch = hardware_patch
        self.trace_level = trace_level


    def __str__(self):
        if self.rig== False:
            rig_words = 'has no rig'
        else:
            rig_words = 'has rig'
        #  add rig name to return string here.
        return f'Hacker\'s name is {self.name} and {rig_words}. {self.name}\'s trace level is {self.trace_level}. {self.name}\'s inventory consists of \n{self.crypto_token} crypto tokens \n{self.security_chip} security chips \n{self.hardware_patch} hardware patches.'




hack1 = Hacker('Hacker')
print(hack1)