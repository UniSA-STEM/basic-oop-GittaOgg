"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random

import Asset


class Rig:

    def __init__(self, name, damage_counter= 0, upgrade_level = 0, damage_value = 1, max_assets = 5,
                 removable_drive=[], time =0):
        self.damage_counter = damage_counter
        self.name = name
        self.upgrade_level = upgrade_level
        self.damage_value = damage_value
        self.max_assets = max_assets
        self.time = time
        self.removable_drive = removable_drive
        self.removable_drive.append(Asset.Asset('DS1','DataSpike'))
        self.removable_drive.append(Asset.Asset('DS2','DataSpike'))
        if self.damage_counter == 0:
            self.condition = 'Pristine'
        elif 0 < self.damage_counter < 2:
            self.condition = 'Damaged'
        else:
            self.condition = 'Broken'



    def __str__(self):
        asset_list = '\n*'
        for asset in self.removable_drive:
            asset_list = asset_list + asset.get_description() + '\n*'

        self.time += 1
        return (f'**********\nRig\'s name is {self.name} and is currently {self.condition} ({self.damage_counter})'
                f' with an upgrade level of {self.upgrade_level}. {self.name} can hold a maximum of {self.max_assets} in '
                f'the removable drive \n{self.name}\'s removable drive contains: \n{asset_list}**********\n')

    def check_condition(self):
        self.time += 1
        return f'{self.condition} ({self.damage_counter})'

    def get_name(self):
        self.time += 1
        return self.name

    def get_upgrade_level(self):
        self.time += 1
        return self.upgrade_level

    def get_damage_value(self):
        self.time += 1
        return self.damage_value

    def get_max_assets(self):
        self.time += 1
        return self.max_assets

    def get_condition(self):
        self.time += 1
        return self.condition

    def get_damage_counter(self):
        self.time += 1
        return self.damage_counter

    def get_removable_drive(self):
        self.time += 1
        return self.removable_drive

    def add_to_drive(self, asset):
        self.time += 1
        if len(self.removable_drive)  >= self.max_assets:
            print('Rig has full removable drive')
        else:
            self.removable_drive.append(asset)

    def remove_from_drive(self):
        self.time += 1
        removing = input('Enter name of asset to retrieve, or enter "All" to retrieve all assets: ')
        if removing == 'All':
            removal_list = []
            for item in reversed(self.removable_drive):
                if item.get_encryption()==False:
                    self.removable_drive.remove(item)
                    removal_list.append(item)
                    print(removal_list)
                return removal_list
        else:
            for item in self.removable_drive:
                if item.get_description() == removing:
                    self.removable_drive.remove(item)
                    return removing
            else:
                print(f'There are no {removing}s in rig\'s removable drive')


    def repair(self):
        if self.damage_counter == 0:
            print('No repair needed')
        else:
            self.time += 1
            self.damage_counter = 0
            self.condition = 'Pristine'
            return f'{self.name} has been repaired to {self.condition}'


    def upgrade(self):
        if self.upgrade_level >= 3:
            print('unable to upgrade further.')
        else:
            self.time += 1
            self.max_assets += 1
            self.damage_value -= 0.25
            self.upgrade_level += 1

    def generate_asset(self):
        acceptable = ['CryptoToken','HardwarePatch','SecurityChip','DataSpike']
        CT_Count = 2
        HP_Count = 1
        DS_Count = 3
        SC_Count = 1
        description = random.shuffle(acceptable)
        if description == 'CryptoToken':
            abbrev = 'CT'+str(CT_Count)
            new = Asset.Asset(abbrev,description)
            CT_Count += 1
        elif description == 'HardwarePatch':
            abbrev = 'HP'+str(HP_Count)
            new = Asset.Asset(abbrev,description)
            HP_Count += 1
        elif description == 'SecurityChip':
            abbrev = 'SC'+str(SC_Count)
            new = Asset.Asset(abbrev,description)
            SC_Count += 1
        else:
            abbrev = 'DS'+str(DS_Count)
            new = Asset.Asset(abbrev,description)
            DS_Count += 1
        return new

