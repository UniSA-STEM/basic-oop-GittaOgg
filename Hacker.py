"""
File: Hacker.py
Description: Module for the class Hacker for the "Into the Grid" game.
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import Rig
import Asset


class Hacker:

    def __init__(self, name):
        self.name = name
        self.rig = []
        self.inventory = []
        self.trace_level = 0
        self.inventory.append(Asset.Asset('Crypto Token','Acquire or Repair Rigs'))

    def __str__(self):
        inventory_str = ''
        for item in self.inventory:

            inventory_str = inventory_str + f'{item.__str__()}\n'

        if not self.rig:
            rig_str = 'has no rig'
        else:
            rig_str = f'has a rig called {self.rig[0].get_name()} which is in {self.rig[0].get_condition()} condition.'

        return (f'**********\nHacker\'s name is {self.name} and has a trace level of {self.trace_level}.'
                f'\n{self.name} {rig_str}' 
                f'\n{self.name}\'s inventory consists of: \n{inventory_str}'
                f'**********\n')

    def __eq__(self, other):
        return self.name == other.name


    def acquire_rig(self):
        if self.rig:
            print(f'{self.name} already has a rig.')
        else:
            if not self.check_inventory('Crypto Token'):
                print('No Crypto Token found')
            else:
                self.scan_inventory('Crypto Token')
                name = input('Enter the name of your rig: ')
                self.rig.append(Rig.Rig(name))
                print(f'Rig {name} has been acquired')
                self.check_time()



    def repair_rig(self):
        if not self.rig:
            print('No rig found.')
        else:
            if self.rig[0].get_damage_counter()== 0:
                print('No repair needed')
            else:
                if not self.check_inventory('Crypto Token'):
                    print('No Crypto Tokens available to repair rig')
                else:
                    self.scan_inventory('Crypto Token')
                    self.rig[0].repair()
                    print(f'{self.rig[0].get_name()} has been repaired.')
            self.check_time()

    def upgrade_rig(self):
        if not self.rig:
            print('No rig found.')
        else:
            if self.rig[0].get_upgrade_level() == 3:
                print('No further upgrades possible')
            else:
                if not self.check_inventory('Hardware Patch'):
                    print('No hardware patches found in inventory')
                else:
                   self.scan_inventory('Hardware Patch')
                   self.rig[0].upgrade()
                   print(f'{self.rig[0].get_name()} has been upgraded.')
            self.check_time()


    def scan_inventory(self, asset):
        for item in self.inventory:
            if item.get_name() == asset:
                self.inventory.remove(item)
                return True
        else:
            return False


    def check_inventory(self, asset):
        for item in self.inventory:
            if item.get_name() == asset:
                return True
        else:
            return False


    def store_asset(self):
        if self.trace_level >= 5:
            print(f'Trace level is at {self.trace_level}. Cannot transfer assets.')
        else:
            if not self.rig:
                print('No rig found.')
            else:
                storing = input('Enter type of asset to store, or enter "All" to store all assets: ')
                if storing == 'All':
                    if len(self.inventory) > self.rig[0].max_assets - len(self.rig[0].removable_drive):
                        print(f'Inventory contains {len(self.inventory)} and {self.rig[0].get_name()} can only store '
                            f'{self.rig[0].max_assets - len(self.rig[0].removable_drive)} more assets.')
                    else:
                        for item in reversed(self.inventory):
                            if item.get_encryption() is False:
                                self.inventory.remove(item)
                                self.rig[0].add_to_drive(item)
                                self.trace_level += 1
                                self.rig[0].time += 1
                                print(f'{item.get_name()} has been moved')

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
                                self.rig[0].time += 1
                                break
                            else:
                                print(f'No decrypted {item.get_name()}\'s found in inventory.')

    def retrieve_asset(self):
        if self.trace_level >= 5:
            print(f'Trace level is at {self.trace_level}. Cannot transfer assets.')
        else:
            if not self.rig:
                print('No rig found.')
            else:
                retrieving = input('Enter type of asset to retrieve, or enter "All" to retrieve all assets: ')
                if retrieving == 'All':
                    for item in reversed(self.rig[0].removable_drive):
                        if item.get_encryption() is False:
                            self.rig[0].removable_drive.remove(item)
                            self.inventory.append(item)
                            self.trace_level += 1
                            self.rig[0].time += 1
                            print(f'{item.get_name()} has been retrieved.')

                else:
                    for item in self.rig[0].removable_drive:
                        if item.get_name() == retrieving and item.get_encryption() is False:
                            self.rig[0].removable_drive.remove(item)
                            self.inventory.append(item)
                            self.trace_level += 1
                            self.rig[0].time += 1
                            print(f'{item.get_name()} has been retrieved.')
                            break
                        else:
                            print(f'No decrypted {retrieving}\'s found in drive.')
                self.check_time()


    def do_encryption(self, location, to_encrypt):
        if location == 'H':
            check = self.inventory
        else:
            check = self.rig[0].removable_drive
        for asst in check:
            if asst.get_name() == to_encrypt and asst.get_encryption() is False:
                asst.encrypt()
                self.scan_inventory('Security Chip')
                self.trace_level += 1
                print(f'{asst.get_name()} has been encrypted.')
                break
        else:
            print(f'No decrypted {to_encrypt}\'s found in inventory.')


    def encrypt_asset(self):
        if self.trace_level >= 5:
            print(f'Trace level is at {self.trace_level}. Cannot encrypt assets.')
        else:
            if not self.check_inventory('Security Chip'):
                print('No Security Chip found.')
            else:
                to_encrypt = input('Enter the name of the asset to encrypt: ')
                location = input('Enter the location of the asset- H for hacker inventory, R for rig drive: ')
                if location == 'H':
                    self.do_encryption(location, to_encrypt)
                elif location == 'R':
                    if not self.rig:
                        print('No rig found.')
                    else:
                        self.do_encryption(location, to_encrypt)
                else:
                    print('Location not found.')

    def do_decryption(self, location, to_decrypt):
        if location == 'H':
            check = self.inventory
        else:
            check = self.rig[0].removable_drive
        for asst in check:
            if asst.get_name() == to_decrypt and asst.get_encryption() is True:
                asst.encrypt()
                self.scan_inventory('Security Chip')
                self.trace_level += 1
                print(f'{asst.get_name()} has been decrypted.')
                break
        else:
            print(f'No encrypted {to_decrypt}\'s found in inventory.')



    def decrypt_asset(self):
        if self.trace_level >= 5:
            print(f'Trace level is at {self.trace_level}. Cannot decrypt assets.')
        else:
            if not self.check_inventory('Security Chip'):
                print('No Security Chip found.')
            else:
                to_decrypt = input('Enter the name of the asset to decrypt: ')
                location = input('Enter the location of the asset- H for hacker inventory, R for rig drive: ')
                if location == 'H':
                    self.do_decryption(location, to_decrypt)
                elif location == 'R':
                    if self.rig == []:
                        print('No rig found.')
                    else:
                        self.do_decryption(location, to_decrypt)
                else:
                    print('Location not found')


    def launch_dataspike(self, target):
        if self.trace_level >= 5:
            print('Trace level too high. Cannot launch dataspike.')
        else:
            if not self.check_inventory('Data Spike'):
                print('No data spike found in hacker inventory, checking rig')
                if not self.rig:
                    print('No rig found.')
                else:
                    if not self.rig[0].check_drive('Data Spike'):
                        print('No data spike found in rig drive- cannot launch')
                    else:
                        if type(target)== Hacker:
                            target.rig[0].damage_counter += target.rig[0].damage_value
                            self.trace_level += 1
                            print(f'{target.name}\'s rig has been hit. Current damage = {target.rig[0].damage_counter}')
                            if target.rig[0].damage_counter == 2:
                                for item in reversed(target.rig[0].removable_drive):
                                    if item.get_encryption() is False:
                                        target.rig[0].removable_drive.remove(item)
                                        self.inventory.append(item)
                                        print(f'{item.get_name()} has been acquired.')
                        else:
                            print(f'Cannot find rig.')
            else:
                if type(target)== Hacker:
                    target.rig[0].damage_counter += target.rig[0].damage_value
                    self.trace_level += 1
                    print(f'{target.name}\'s rig has been hit. Current damage = {target.rig[0].damage_counter}')
                    if target.rig[0].damage_counter == 2:
                        for item in reversed(target.rig[0].removable_drive):
                            if item.get_encryption() is False:
                                target.rig[0].removable_drive.remove(item)
                                self.inventory.append(item)
                                print(f'{item.get_name()} has been acquired.')
                else:
                    print('Cannot find rig.')




    def check_time(self):
        if self.rig[0].time >= 2:
            new_asset = self.rig[0].generate_asset()
            self.inventory.append(new_asset)
            print(f'{self.rig[0].get_name()} has generated a {new_asset.name} and added to '
                  f'{self.name}\'s inventory.')
            self.rig[0].time = 0


