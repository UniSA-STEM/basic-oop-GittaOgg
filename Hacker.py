"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import Rig

class Hacker:

    def __init__(self, name, crypto_token =1, rig = False,rig_name = None, security_chip = 0, hardware_patch = 0,trace_level = 0 ):
        self.name = name
        self.crypto_token = crypto_token
        self.rig = rig
        self.security_chip = security_chip
        self.hardware_patch = hardware_patch
        self.trace_level = trace_level
        self.rig_name = rig_name


    def __str__(self):
        #  add rig name to return string here.
        if self.rig== False:
            rig_words = 'has no rig'
        else:
            rig_words = f'has a rig called {self.rig_name}'

        return (f'**********\nHacker\'s name is {self.name}, {rig_words} and a trace level of {self.trace_level}.'
                f'\n{self.name}\'s inventory consists of: \n{self.crypto_token} crypto tokens'
                f' \n{self.security_chip} security chips \n{self.hardware_patch} hardware patches.\n**********\n')

    def AcquireRig(self):
        if self.crypto_token >= 1 and self.rig == False:
            self.crypto_token -= 1
            self.rig = True
            self.rig_name = input('Enter Rig Name: ')
            return self.rig_name
        elif self.crypto_token < 1:
            print(f'{self.name} does not have enough crypto-tokens (1) to purchase a rig.')
        else:
            print(f'{self.name} owns max allowable rigs (1).')


    def encrypt_item (self):
        if self.security_chip < 1:
            print(f'{self.name} does not have enough security-chips (1) to encrypt an asset.')
        else:
            allowable= [1,2,3]
            enc_item = input('Enter asset to encrypt: 1 (Crypto Token), 2 (Security Chip) or 3 (Hardware Patch): ')
            while enc_item not in allowable:
                print('Not a valid choice- choose 1, 2 or 3')
                enc_item = input('Enter asset to encrypt: 1 (Crypto Token), 2 (Security Chip) or 3 (Hardware Patch): ')
            if enc_item == '1':
                # deal with ownership of assets, encrypting and decrypting specifics, etc.



hack1 = Hacker('TestHacker',crypto_token=3)
print(hack1)
hack1.AcquireRig()
print(hack1)
hack1.AcquireRig()
print(hack1)