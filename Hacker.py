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
        self.inventory.append(Asset.Asset('Crypto Token','Acquire or Repair Rigs'))

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

    def __eq__(self, other):
        return self.name == other.name


    def acquire_rig(self):
        if self.rig != []:
            print(f'{self.name} already has a rig.')
        else:
            if self.scan_inventory('Crypto Token') == False:
                print('No Crypto Token found')
            else:
                self.scan_inventory('Crypto Token')
                name = input('Enter the name of your rig: ')
                self.rig.append(Rig.Rig(name))
                print(f'Rig {name} has been acquired')
                self.check_time()

    def repair_rig(self):
        if self.rig == []:
            print('No rig found.')
        else:
            if self.rig[0].get_damage_counter()== 0:
                print('No repair needed')
            else:
                if self.scan_inventory('Crypto Token') == False:
                    print('No Crypto Tokens available to repair rig')
                else:
                    self.scan_inventory('Crypto Token')
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
                for item in self.inventory:
                    if item.get_name() == 'Hardware Patch':
                        self.scan_inventory('Hardware Patch')
                        self.rig[0].upgrade()
                        print(f'{self.rig[0].get_name()} has been upgraded.')
                        break
                else:
                    print('No hardware patches found in inventory')
                self.check_time()

    def check_inventory(self, asset):
        list = []
        for item in self.inventory:
            if item.get_name() == asset:
                list.append(item)
                return list

    def scan_inventory(self, asset):
        for item in self.inventory:
            if item.get_name() == asset:
                self.inventory.remove(item)
                return True
            else:
                return False

    def launch_dataspike(self,target):
        if self.trace_level >= 5:
            print(f'Trace level is at {self.trace_level}. Cannot launch dataspike.')
        else:
            if self.scan_inventory('Data Spike')== False:
                print('No Data Spikes found')
            else:
                self.scan_inventory('DataSpike')
                target.damage_counter -= target.damage_value
                self.trace_level += 1
                print(f'{target.get_name()} has been hit- current damage = {target.damage_counter}')
                if target.damage_counter == 2:
                    for item in reversed(target.removable_drive):
                        if item.get_encryption == False:
                            target.removable_drive.remove(item)
                            self.inventory.append(item)
                            print(f'{item.get_name()} has been acquired.\n')

    def store_asset(self):
        if self.trace_level >= 5:
            print(f'Trace level is at {self.trace_level}. Cannot transfer assets.')
        else:
            if self.rig == []:
                print('No rig found.')
            else:
                storing = input('Enter type of asset to store, or enter "All" to store all assets: ')
                if storing == 'All':
                    if len(self.inventory) > self.rig[0].max_assets - len(self.rig[0].removable_drive):
                        print(f'Inventory contains {len(self.inventory)} and {self.rig[0].get_name()} can only store '
                            f'{self.rig[0].max_assets - len(self.rig[0].removable_drive)} more assets.')
                    else:
                        for item in self.inventory:
                            if item.get_encryption() is False:
                                self.inventory.remove(item)
                                self.rig[0].add_to_drive(item)
                                self.trace_level += 1
                                print(f'{item.get_name} has been moved')

                else:
                    if self.rig[0].max_assets == len(self.rig[0].removable_drive):
                        print('Rig\'s removable drive is full')
                    else:
                        for item in self.inventory:
                            if item.get_name() == storing and item.get_encryption() == False:
                                self.inventory.remove(item)
                                self.rig[0].add_to_drive(item)
                                print(f'{item.get_name()} has been stored in Rig\'s removable drive.')
                                self.trace_level += 1
                                break
                            else:
                                print(f'No decrypted {item.get_name()}\'s found in inventory.')

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


hack1= Hacker('hackman')
hack1.acquire_rig()
hack1.inventory.append(Asset.Asset('Hardware Patch', 'testing'))
print(hack1)
hack1.store_asset()
print(hack1)
print(hack1.rig[0])