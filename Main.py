"""
File: main.py
Description: Module for testing the "Into the Grid" game.
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import Hacker




def test1():
    """
    Creates a hacker, acquires a rig, retrieves asset(s) from rig to hacker inventory.
    These actions will make enough time pass that the rig will generate a random asset for itself
    """
    hack1 = Hacker.Hacker('HackMan')
    hack1.acquire_rig()
    hack1.retrieve_asset()
    print(hack1)



def test2():
    """
    Creates a hacker, acquires a rig, attempts to acquire 2nd rig.
    Will not allow hacker to own more than 1 rig.
    """

    ### Creates a hacker, acquires a rig, attempts to acquire a 2nd rig. Will not allow hacker to own more than 1 rig
    hack2 = Hacker.Hacker('Hackerino')
    hack2.acquire_rig()
    hack2.acquire_rig()

def test3():
    """
    Creates 2 hackers, acquires each a rig. 1st hacker launches DataSpike at 2nd Hacker.
    2nd hacker's rig is broken. All un-encrypted assets in broken rig transferred to 1st Hacker's inventory
    """
    hack3 = Hacker.Hacker('HackInTheBox')
    hack3.acquire_rig()
    hack4 = Hacker.Hacker('HackAndTheBeanstalk')
    hack4.acquire_rig()
    hack3.launch_dataspike(hack4)
    hack3.launch_dataspike(hack4)
    print(hack3)
    print(hack4)


def test4():
    """
    Creates hacker and attempts to encrypt an asset. Since hacker has no security chip, cannot be done.

    """

    ### Creates hacker and attempts to encrypt their crypto token. Since no security chip is in their inventory,
    ### cannot achieve
    hack5 = Hacker.Hacker('HackSkellington')
    hack5.encrypt_asset()

def test5():
    """
    Creates hacker and attempts to upgrade their rig. Hacker has no rig, cannot upgrade.
    Acquires rig for hacker, attempts to upgrade. Hacker has no hardware patch. cannot upgrade

    """

    hack6 = Hacker.Hacker('HackBeNimble')
    hack6.upgrade_rig()
    hack6.acquire_rig()
    hack6.upgrade_rig()


def test6():
    """
    Creates a hacker and attempts to retrieve an asset from the rig. Hacker has no rig, cannot retrieve.
    Acquires rig, retrieves asset(s)

    """

    ### Creates a hacker and attempts to retrieve an asset from the rig. Since hacker has no rig, cannot retrieve.
    ### Then acquires rig and can retrieve asset(s)
    hack7 = Hacker.Hacker('HackInBlack')
    hack7.retrieve_asset()
    hack7.acquire_rig()
    hack7.retrieve_asset()

def test7():
    """
    Creates hacker, acquires rig. Transfers assets from rig to hacker inventory and back again until trace level
    reaches threshold. Will not allow further transfers.
    """
    ### creates hacker, acquires rig. transfers assets from rig to hacker and back until trace level
    ### reaches threshold and will not allow any further transfers
    hack8 = Hacker.Hacker('HackySack')
    hack8.acquire_rig()
    hack8.retrieve_asset()
    print(hack8)
    hack8.store_asset()
    hack8.retrieve_asset()



test3()

