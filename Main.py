"""
File: main.py
Description: Module for testing the "Into the Grid" game.
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import Asset
import Hacker




def test1():
    """
    Creates a hacker, acquires a rig, retrieves asset(s) from rig to hacker inventory.
    These actions will make enough time pass that the rig will generate a random asset for itself
    """
    print('****TEST 1**** \n')
    hack1 = Hacker.Hacker('HackMan')
    hack1.acquire_rig()
    hack1.retrieve_asset()
    print(hack1)



def test2():
    """
    Creates a hacker, acquires a rig, attempts to acquire 2nd rig.
    Will not allow hacker to own more than 1 rig.
    """
    print('****TEST 2**** \n')
    hack2 = Hacker.Hacker('Hackerino')
    hack2.acquire_rig()
    hack2.acquire_rig()

def test3():
    """
    Creates 2 hackers, acquires each a rig. 1st hacker launches DataSpike at 2nd Hacker.
    2nd hacker's rig is broken. All un-encrypted assets in broken rig transferred to 1st Hacker's inventory
    """
    print('****TEST 3**** \n')
    hack3 = Hacker.Hacker('HackInTheBox')
    hack3.acquire_rig()
    hack4 = Hacker.Hacker('HackAndTheBeanstalk')
    hack4.acquire_rig()
    hack3.launch_dataspike(hack4)
    hack3.launch_dataspike(hack4)
    print(hack3)
    print(hack4)


def test4():
    print('****TEST 4**** \n')
    """
    Creates hacker and attempts to encrypt an asset. Since hacker has no security chip, cannot be done.
    Adds security chip to hacker's inventory.
    Encrypts asset
    """
    hack5 = Hacker.Hacker('HackSkellington')
    hack5.encrypt_asset()
    hack5.inventory.append(Asset.Asset('Security Chip', 'used for encrypting and decrypting'))
    hack5.encrypt_asset()

def test5():
    """
    Creates hacker and attempts to upgrade their rig. Hacker has no rig, cannot upgrade.
    Acquires rig for hacker, attempts to upgrade. Hacker has no hardware patch. cannot upgrade

    """
    print('****TEST 5**** \n')
    hack6 = Hacker.Hacker('HackBeNimble')
    hack6.upgrade_rig()
    hack6.acquire_rig()
    hack6.upgrade_rig()


def test6():
    """
    Creates a hacker and attempts to retrieve an asset from the rig. Hacker has no rig, cannot retrieve.
    Acquires rig, retrieves asset(s)

    """
    print('****TEST 6**** \n')
    hack7 = Hacker.Hacker('HackInBlack')
    hack7.retrieve_asset()
    hack7.acquire_rig()
    hack7.retrieve_asset()

def test7():
    """
    Creates hacker, acquires rig. Transfers assets from rig to hacker inventory and back again until trace level
    reaches threshold. Will not allow further transfers.
    """
    print('****TEST 7**** \n')
    hack8 = Hacker.Hacker('HackySack')
    hack8.acquire_rig()
    hack8.retrieve_asset()
    print(hack8)
    hack8.store_asset()
    hack8.retrieve_asset()


test1()
print('------------\n')
test2()
print('------------\n')
test3()
print('------------\n')
test4()
print('------------\n')
test5()
print('------------\n')
test6()
print('------------\n')
test7()


