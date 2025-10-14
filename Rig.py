"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Rig:

    def __init__(self, name, damage_counter= 0, upgrade_level = 0, damage_value = 1, max_assets = 5,
                 removable_drive=None):
        self.damage_counter = damage_counter
        self.name = name
        self.upgrade_level = upgrade_level
        self.damage_value = damage_value
        self.max_assets = max_assets
        self.removable_drive = removable_drive
        if self.removable_drive is None:
            self.removable_drive = ['DataSpike', 'DataSpike']
        if self.damage_counter == 0:
            self.condition = 'Pristine'
        elif 0 < self.damage_counter < 2:
            self.condition = 'Damaged'
        else:
            self.condition = 'Broken'



    def __str__(self):
        asset_list = '\n*'
        for asset in self.removable_drive:
            asset_list = asset_list + asset + '\n*'

        return (f'**********\nRig\'s name is {self.name} and is currently {self.condition} with an upgrade level '
                f'of {self.upgrade_level}. \n{self.name}\'s removable drive contains: {asset_list}**********\n')



    def get_name(self):
        return self.name

    def get_upgrade_level(self):
        return self.upgrade_level

    def get_damage_value(self):
        return self.damage_value

    def get_max_assets(self):
        return self.max_assets

    def get_condition(self):
        return self.condition

    def get_damage_counter(self):
        return self.damage_counter

    def get_removable_drive(self):
        return self.removable_drive

    def add_to_drive(self, asset):
        if len(self.removable_drive)  >= self.max_assets:
            print('Rig has full removable drive')
        else:
            self.removable_drive.append(asset)

    def remove_from_drive(self, asset):
        if asset in self.removable_drive:
            self.removable_drive.remove(asset)
        else:
            print(f'There are no {asset}\'s in {self.name}\'s removable drive')


    def repair(self):
        if self.damage_counter == 0:
            print('No repairs necessary')
        else:
            self.damage_counter = 0
            self.condition = 'Pristine'


    def upgrade(self):
        self.max_assets += 1
        self.damage_value -= 0.25
        self.upgrade_level += 1
