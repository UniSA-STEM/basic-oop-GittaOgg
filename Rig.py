"""
File: Rig.py
Description: Module for the class Rig for the "Into the Grid" game.
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random

import Asset


class Rig:

    def __init__(self, name):
        self.damage_counter = 0
        self.name = name
        self.upgrade_level = 0
        self.damage_value = 1
        self.max_assets = 5
        self.time = 0
        self.removable_drive = []
        self.removable_drive.append(Asset.Asset('Data Spike','Used in battles'))
        self.removable_drive.append(Asset.Asset('Data Spike','Used in battles'))
        self.condition = 'Pristine'



    def __str__(self):
        asset_list = ''
        for asset in self.removable_drive:
            asset_list = asset_list + f'{asset.__str__()}\n'

        self.time += 1
        return (f'**********\nRig\'s name is {self.name} and is currently {self.condition} ({self.damage_counter})'
                f' with an upgrade level of {self.upgrade_level}. {self.name} can hold a maximum of {self.max_assets} in '
                f'the removable drive \n{self.name}\'s removable drive contains: \n{asset_list}**********\n')


    def __eq__(self, other):
        return self.name == other.name

    def get_condition(self):
        self.time += 1
        if self.damage_counter == 0:
            self.condition = 'Pristine'
        elif 0 < self.damage_counter < 2:
            self.condition = 'Damaged'
        else:
            self.condition = 'Broken'
        return self.condition


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
                if item.get_name() == removing:
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
        acceptable = ['Crypto Token','Hardware Patch','Security Chip','Data Spike']
        item = acceptable[random.randint(0,3)]
        if item == 'Crypto Token':
            description = 'Acquire or Repair Rigs'
            new = Asset.Asset(item,description)
        elif item == 'Hardware Patch':
            description = 'For upgrading rigs'
            new = Asset.Asset(item,description)
        elif item == 'Security Chip':
            description = 'For encrypting or decrypting assets'
            new = Asset.Asset(item,description)
        else:
            description = 'Used in battles'
            new = Asset.Asset(item,description)
        return new

    def check_drive(self, asset):
        self.time += 1
        for item in self.removable_drive:
            if item.get_name() == asset:
                return True
        else:
            return False

    def scan_drive(self, asset):
        self.time += 1
        for item in self.removable_drive:
            if item.get_name() == asset:
                self.removable_drive.remove(item)
                return True
        else:
            return False
