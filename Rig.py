"""
File: Rig.py
Description: Module for the class Rig for the "Into the Grid" game.
Author: Natasha Hunter
ID: 110439590
Username: hunny006
Git Repository: https://github.com/UniSA-STEM/basic-oop-GittaOgg
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
import Asset


class Rig:

    """
    A class which represents rigs in the game.

    Attributes
    ------------
    name: str
        name of the rig
    damage_counter: int
        amount of damage taken by rig
    damage_value: float
        damage done with every hit to rig
    upgrade_level: int
        how many upgrades the rig has had
    max_assets: int
        maximum number of assets able to be stored in rig's drive
    time: int
        rig's internal clock
    removable_drive: list
        storage for the rig to hold assets
    condition: str
        string representation of damage_count

    Methods
    -------

    get_name:
        returns the name of the rig
    get_condition:
        returns condition of the rig
    get_upgrade_level:
        returns the number of upgrades the rig has had
    get_damage_counter:
        returns the amount of damage taken by rig
    add_to_drive(asset):
        adds assets to the rig's drive
    remove_from_drive(asset):
        removes assets from the rig's drive
    repair:
        repairs rig to pristine condition
    upgrade:
        upgrades rig 1 level
    generate_asset:
        generates a new asset
    check_drive(asset):
        checks the rig's removable for asset
    scan_drive(asset):
        checks the rig's removable for asset and removes if found
    """

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
        """ Sets string representation of damage_counter as condition, returns condition, increases rig's timer """
        self.time += 1
        if self.damage_counter == 0:
            self.condition = 'Pristine'
        elif 0 < self.damage_counter < 2:
            self.condition = 'Damaged'
        else:
            self.condition = 'Broken'
        return self.condition

    def get_name(self):
        """ Returns the name of the rig, increases rig's timer  """
        self.time += 1
        return self.name

    def get_upgrade_level(self):
        """ Returns the number of upgrades the rig has had, increases rig's timer """
        self.time += 1
        return self.upgrade_level

    def get_damage_counter(self):
        """ Returns the amount of damage taken by rig, increases rig's timer """
        self.time += 1
        return self.damage_counter

    def add_to_drive(self, asset):
        """
        Adds assets to the rig's drive, if there is space. Increases rig's timer

        Parameters:
            asset (string): name of the asset to add to the rig's drive

        """
        self.time += 1
        if len(self.removable_drive)  >= self.max_assets:
            print('Rig has full removable drive')
        else:
            self.removable_drive.append(asset)

    def remove_from_drive(self, asset):
        """
        Removes assets from the rig's drive. Increases rig's timer

        Parameters:
             asset(string): asset to be removed from rig's drive
        """
        self.time += 1
        self.removable_drive.remove(asset)


    def repair(self):
        """ Repairs rig to pristine condition, if the rig has any damage. Increases rig's timer """
        if self.damage_counter == 0:
            print('No repair needed')
        else:
            self.time += 1
            self.damage_counter = 0
            self.condition = 'Pristine'



    def upgrade(self):
        """ Upgrades rig 1 level and increases rig's timer """
        if self.upgrade_level >= 3:
            print('unable to upgrade further.')
        else:
            self.time += 1
            self.max_assets += 1
            self.damage_value -= 0.25
            self.upgrade_level += 1

    def generate_asset(self):
        """Generates a new asset """
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
        """
        Checks the rig's removable drive for asset, increases rig's timer

        Parameters:
            asset (string): name of the asset to check for

        """
        self.time += 1
        for item in self.removable_drive:
            if item.get_name() == asset:
                return True
        else:
            return False

    def scan_drive(self, asset):
        """
        Checks the rig's removable drive for asset. Removes asset if found. increases rig's timer

        Parameters:
            asset (string): name of the asset to check for

        """
        self.time += 1
        for item in self.removable_drive:
            if item.get_name() == asset:
                self.removable_drive.remove(item)
                return True
        else:
            return False
