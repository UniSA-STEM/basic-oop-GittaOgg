"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import Rig
import Asset


class Hacker:

    def __init__(self, name, rig =[], inventory =[],trace_level = 0):
        self.name = name
        self.rig = rig
        self.inventory = inventory
        self.trace_level = trace_level
        self.inventory.append(Asset.Asset('CryptoToken','used for acquiring or repairing rigs'))



    def __str__(self):
        inventory_str = ''
        for item in self.inventory:

            inventory_str = inventory_str + f'{item.__str__()}\n'

        if self.rig == []:
            rig_str = 'has no rig'
        else:
            rig_str = f'has a rig called {self.rig[0].get_name()}'

        return (f'**********\nHacker\'s name is {self.name} and has a trace level of {self.trace_level}.'
                f'\n{self.name} {rig_str}' 
                f'\n{self.name}\'s inventory consists of: \n{inventory_str}'
                f'**********\n')


    def AcquireRig(self):
        if self.rig != []:
            print(f'{self.name} already has a rig.')
        else:
            for item in self.inventory:
                if item.get_name() == 'CryptoToken':
                    name = input('Enter the name of your rig: ')
                    self.inventory.remove(item)
                    self.rig.append(Rig.Rig(name))
                    print(f'Rig {name} has been acquired.')
                    break
            else:
                print('No cryptotokens found')


    def repair_rig(self):
        if self.rig == []:
            print('No rig found.')
        else:
            if self.rig[0].get_damage_counter()== 0:
                print('No repair needed')
            else:
                if self.scan_inventory('CryptoToken'):
                    self.rig[0].repair()
                    print(f'{self.rig[0].get_name()} has been repaired.')



    def upgrade_rig(self):
        if self.rig == []:
            print('No rig found.')
        else:
            if self.rig[0].get_upgrade_level() == 3:
                print('No further upgrades possible')
            else:
                if self.scan_inventory('Hardware Patch'):
                    self.rig[0].upgrade()
                    print(f'{self.rig[0].get_name()} has been upgraded.')



    def scan_inventory(self, asset_name):
        for item in self.inventory:
            if item.get_name() == asset_name:
                self.inventory.remove(item)
                print(f'{item.get_name()} has been used.')
                return True
            else:
                print(f'No {item} found')
                return False





hack1= Hacker('hackname')
print(hack1)


