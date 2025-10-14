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



