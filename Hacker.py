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
        self.inventory.append(Asset.Asset('CT1','CryptoToken'))



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
                if item.get_description() == 'CryptoToken':
                    name = input('Enter the name of your rig: ')
                    self.inventory.remove(item)
                    self.rig.append(Rig.Rig(name))
                    print(f'Rig {name} has been acquired.')
                    break
            else:
                print('No cryptotokens found')
            self.check_time()


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
            self.check_time()



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
            self.check_time()



    def scan_inventory(self, asset_name):
        for item in self.inventory:
            if item.get_name() == asset_name:
                self.inventory.remove(item)
                print(f'{item.get_name()} has been used.')
                break
                return True
            else:
                print(f'No {item} found')
                return False

    def launch_dataspike(self,target):
        if self.trace_level >= 5:
            print(f'Trace level is at {self.trace_level}. Cannot launch dataspike.')
        else:
            if self.scan_inventory('DataSpike'):
                target.damage_counter -= target.damage_value
                self.trace_level += 1
                print(f'{target.get_name()} has been hit. Damage counter: {target.damage_counter}')
                if target.damage_counter == 2:
                    for item in target.removable_drive:
                        if item.get_encryption == False:
                            target.inventory.remove(item)
                            self.inventory.append(item)
                            print(f'{item.get_name()} has been acquired.\n')

    def encrypt_asset(self, asset):
        if self.trace_level >= 5:
            print(f'Trace level is at {self.trace_level}. Cannot encrypt asset.')
        else:
            if self.scan_inventory('Security Chip')== True:
                for item in self.inventory:
                    if item.get_name() == asset and item.get_encryption == False:
                        item.encrypt()
                        self.inventory.remove('Security Chip')
                        print(f'{asset} has been encrypted.')
                        break

    def store_asset(self):
        if self.trace_level >= 5:
            print(f'Trace level is at {self.trace_level}. Cannot transfer assets.')
        else:
            if self.rig == []:
                print('No rig found.')
            else:
                storing = input('Enter name of asset to store, or enter "All" to store all assets: ')
                if storing == 'All':
                    if len(self.inventory) > self.rig[0].max_assets - len(self.rig[0].removable_drive):
                        print(f'Inventory contains {len(self.inventory)} and {self.rig[0].get_name()} can only store '
                            f'{self.rig[0].max_assets - len(self.rig[0].removable_drive)} more assets.')
                    else:
                        for item in self.inventory:
                            self.inventory.remove(item)
                            self.rig[0].add_to_drive(storing)
                            self.trace_level += 1
                        print('All assets have been stored in rig\'s drive')
                else:
                    for item in self.inventory:
                        if item.get_name() == asset:
                            self.inventory.remove(item)
                            self.rig[0].add_to_drive(asset)
                            print(f'{item.get_name()} has been stored in Rig\'s removable drive.')
                            self.trace_level += 1
                            break

    def retrieve_asset(self):
        if self.trace_level >= 5:
            print(f'Trace level is at {self.trace_level}. Cannot transfer assets.')
        else:
            if self.rig== []:
                print('No rig found.')
            else:
                if type(self.rig[0].remove_from_drive()) == list:
                    for item in self.rig[0].remove_from_drive():
                        self.inventory.append(item)
                        self.trace_level += 1
                self.check_time()

    def check_time(self):
        if self.rig[0].time >= 5:
            new_asset = self.rig[0].generate_asset()
            self.inventory.append(new_asset)
            print(f'{self.rig[0].get_name()} has generated a {new_asset.description} and added to '
                  f'{self.name}\'s inventory.')
            self.rig[0].time = 0



hack1= Hacker('hackname')
print(hack1)


