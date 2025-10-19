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

    """
    A class which represents hackers in the game.

    Attributes
    ------------
    name: str
        name of the hacker
    rig: list
        List of rigs owned by hacker (max allowable =1)
    inventory: list
        List of assets owned by hacker
    trace_level: int
        Level of traceability of hacker. When hacker reaches level of 5, they are exposed and cannot
        perform some methods

    Methods
    -------
    acquire_rig:
        Uses CryptoToken to purchase rig for hacker and add to self.rig (if hacker has no rig)
    repair_rig:
        Uses CryptoToken to repair hacker's rig using Rig.repair() method
    upgrade_rig:
        Uses HardwarePatch to upgrade rig using Rig.upgrade() method
    scan_inventory(asset):
        Scans hacker's inventory for asset, if found removes from inventory
    check_inventory(asset):
        Scans hacker's inventory for asset, but does not remove
    store_asset:
        Removes selected asset(s) from hacker's inventory and stores in rig's drive
    retrieve_asset:
        Retrieves selected asset(s) from rig's drive and stores in hacker's inventory
    __do_encryption(location, to_encrypt):
        checks location of asset for asset, if found and un-encrypted, encrypts, otherwise prints msg
    encrypt_asset:
        asks user for location and asset name. uses __do_encryption method to encrypt the asset
    __do_decryption(location, to_decrypt):
        checks the location of asset for asset, if found and encrypted, decrypts, otherwise prints msg
    decrypt_asset:
        asks user for location and asset name. uses __do_decryption method to decrypt the asset
    launch_dataspike(target):
        checks hacker's inventory and rig's drive for dataspike. Launches dataspike at target's rig using
        __ds_launch() method.
    ds_launch(target):
        damages target rig by target damage value. If target rig is broken, transfers unencrypted assets
        from target's rig into hacker's inventory
    check_time:
        checks the internal time of hacker's rig. When time reaches 2, uses Rig.generate_asset() method to
        generate a new asset and add to hacker's inventory.

    """

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
        """
        Max allowable rigs per hacker = 1
        Checks if hacker already owns rig
        Checks for Crypto Token
        Asks user for name of rig
        Instantiates rig
        Checks time
        """
        if self.rig:
            print(f'{self.name} already has a rig.')
        else:
            if not self.check_inventory('Crypto Token'):
                print('No Crypto Token found')
            else:
                self.scan_inventory('Crypto Token')
                name = input('Enter the name of your rig: ')
                self.rig.append(Rig.Rig(name))
                print(f'Rig {name} has been acquired by {self.name}\n')
                self.__check_time()



    def repair_rig(self):
        """
        Checks if hacker has rig
        Checks if rig needs repair
        Checks for Crypto Token
        Repairs rig using Rig.repair()
        Checks time

        """
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
                    print(f'{self.rig[0].get_name()} has been repaired to pristine condition.')
            self.__check_time()



    def upgrade_rig(self):
        """
        Checks if hacker has rig
        Checks if rig can be further upgraded (max upgrade level= 3)
        Checks for hardware patch
        Upgrades rig using Rig.upgrade()
        Checks time

        """
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
            self.__check_time()


    def scan_inventory(self, asset):
        """
        Checks hacker's inventory for asset. If found, removes from inventory
        Parameters:
            asset (string): name of the asset to check for
        Return:
             True if asset found and removed, False if not
        """
        for item in self.inventory:
            if item.get_name() == asset:
                self.inventory.remove(item)
                return True
        else:
            return False


    def check_inventory(self, asset):
        """
        Checks hacker's inventory for asset.
        Parameters:
            asset (string): name of the asset to check for
        Returns:
             True if asset found, False if not
        """
        for item in self.inventory:
            if item.get_name() == asset:
                return True
        else:
            return False

    def store_asset(self):
        """
        Checks hacker's trace level. Cannot transfer assets if trace level at max
        Check hacker has rig
        Asks user for asset name to store or All for all assets
        Transfers all decrypted assets from hacker's inventory to rig's drive
        Checks time

        """
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
                                print(f'{item.get_name()} has been stored in Rig\'s removable drive.')

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
                self.__check_time()

    def retrieve_asset(self):
        """
        Checks hacker's trace level. Cannot transfer assets if trace level at max
        Checks hacker has rig
        Asks user for asset name to retrieve or All for all assets
        Transfers all decrypted assets from rig's drive to hacker's inventory
        Checks time
        """

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
                            self.rig[0].remove_from_drive(item)
                            self.inventory.append(item)
                            self.trace_level += 1
                            print(f'{item.get_name()} has been retrieved.')

                else:
                    for item in self.rig[0].removable_drive:
                        if item.get_name() == retrieving and item.get_encryption() is False:
                            self.rig[0].remove_from_drive(item)
                            self.inventory.append(item)
                            self.trace_level += 1
                            print(f'{item.get_name()} has been retrieved.')
                            break
                        else:
                            print(f'No decrypted {retrieving}\'s found in drive.')
                self.__check_time()


    def __do_encryption(self, location, to_encrypt):
        """
        Encrypts asset from hacker's inventory or rig's drive using security chip from hacker's inventory

        Parameters:
        location (string): Location of asset to encrypt- H for hacker, R for rig
        to_encrypt (string): Name of asset to encrypt

        """

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
        """
        Checks hacker's trace level. Cannot encrypt assets if trace level at max
        Checks hacker's inventory for security chip
        Asks user for name and location of asset to encrypt
        Uses __do_encryption method to encrypt
        Checks time

        """
        if self.trace_level >= 5:
            print(f'Trace level is at {self.trace_level}. Cannot encrypt assets.')
        else:
            if not self.check_inventory('Security Chip'):
                print('No Security Chip found.')
            else:
                to_encrypt = input('Enter the name of the asset to encrypt: ')
                location = input('Enter the location of the asset- H for hacker inventory, R for rig drive: ')
                if location == 'H':
                    self.__do_encryption(location, to_encrypt)
                elif location == 'R':
                    if not self.rig:
                        print('No rig found.')
                    else:
                        self.__do_encryption(location, to_encrypt)
                else:
                    print('Location not found.')

    def __do_decryption(self, location, to_decrypt):
        """
        Decrypts asset from hacker's inventory or rig's drive using security chip from hacker's inventory

        Parameters:
        location (string): Location of asset to decrypt- H for hacker, R for rig
        to_decrypt (string): Name of asset to decrypt

        """
        if location == 'H':
            check = self.inventory
        else:
            check = self.rig[0].removable_drive
        for asst in check:
            if asst.get_name() == to_decrypt and asst.get_encryption() is True:
                asst.decrypt()
                self.scan_inventory('Security Chip')
                self.trace_level += 1
                print(f'{asst.get_name()} has been decrypted.')
                break
        else:
            print(f'No encrypted {to_decrypt}\'s found in inventory.')



    def decrypt_asset(self):
        """
        Checks hacker's trace level. Cannot decrypt assets if trace level at max
        Checks hacker's inventory for security chip
        Asks user for name and location of asset to decrypt
        Uses __do_decryption method to decrypt
        Checks time

        """
        if self.trace_level >= 5:
            print(f'Trace level is at {self.trace_level}. Cannot decrypt assets.')
        else:
            if not self.check_inventory('Security Chip'):
                print('No Security Chip found.')
            else:
                to_decrypt = input('Enter the name of the asset to decrypt: ')
                location = input('Enter the location of the asset- H for hacker inventory, R for rig drive: ')
                if location == 'H':
                    self.__do_decryption(location, to_decrypt)
                elif location == 'R':
                    if self.rig == []:
                        print('No rig found.')
                    else:
                        self.__do_decryption(location, to_decrypt)
                else:
                    print('Location not found')


    def launch_dataspike(self, target):
        """
        Checks trace level. Cannot launch dataspike if trace level at max
        Checks hacker has rig
        Checks hacker's inventory and rig's drive for data spike
        Uses __ds_launch method to launch dataspike

        Parameters:
            target (string): Name of hacker whose rig is being attacked

        """
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
                            self.__ds_launch(target)
                        else:
                            print(f'Cannot find hacker')
                    self.__check_time()
            else:
                if type(target)== Hacker:
                    self.__ds_launch(target)
                else:
                    print('Cannot find hacker')

    def __ds_launch(self,target):
        """
        Damages target's rig by target's damage value
        Adds to hacker's trace level
        Checks if target's rig is broken:
        Transfers all decrypted assets to hacker's inventory

        Parameters:
             target (Hacker): Name of hacker whose rig is being attacked
        """
        target.rig[0].damage_counter += target.rig[0].damage_value
        self.trace_level += 1
        print(f'{target.name}\'s rig has been hit. Current damage = {target.rig[0].damage_counter}')
        if target.rig[0].damage_counter == 2:
            print(f'{target.name}\'s rig is broken. Scanning rig drive...\n')
            for item in reversed(target.rig[0].removable_drive):
                if item.get_encryption() is False:
                    target.rig[0].removable_drive.remove(item)
                    self.inventory.append(item)
                    print(f'{item.get_name()} has been acquired.\n')



    def __check_time(self):
        """
        Checks Hacker's rig's internal time.
        When time reaches 2, Rig.generate_asset() us called to generate random new asset.
        Adds new asset to hacker's inventory
        """
        if self.rig[0].time >= 2:
            new_asset = self.rig[0].generate_asset()
            self.inventory.append(new_asset)
            print(f'{self.rig[0].get_name()} has generated a {new_asset.name} and added to '
                  f'{self.name}\'s inventory.')
            self.rig[0].time = 0

