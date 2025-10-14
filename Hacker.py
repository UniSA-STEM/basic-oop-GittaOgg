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

    def __init__(self, name, rig =[], inventory =[],trace_level = 0):
        self.name = name
        self.rig = rig
        self.inventory = inventory
        self.trace_level = trace_level
        self.inventory.append(Asset('CrytoToken','used for ....'))



    def __str__(self):
        inventory_str = ''
        for item in self.inventory:

            inventory_str = inventory_str + f'{item.__str__()}\n'

        if self.rig == []:
            rig_str = 'has no rig'
        else:
            rig_str = f'has a rig called {self.rig}'

        return (f'**********\nHacker\'s name is {self.name} and has a trace level of {self.trace_level}.'
                f'\n{self.name} {rig_str}' 
                f'\n{self.name}\'s inventory consists of: \n{inventory_str}'
                f'\n**********\n')


    def AcquireRig(self):
        for item in self.inventory:
            if item.get_name() == 'CrytoToken':
                name = input('Enter the name of your rig: ')
                self.inventory.remove(item)
                self.rig.append(Rig(name))
                break
        else:
            print('No cryptotokens found')



hack1 = Hacker('TestHacker',crypto_token=3)
print(hack1)
hack1.AcquireRig()
print(hack1)
hack1.AcquireRig()
print(hack1)