"""
File: main.py
Description: Module for testing the "Into the Grid" game.
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import Hacker
import Rig
import Asset

def test1():
    ### Creates a hacker, acquires a rig, retrieves asset(s) from rig to hacker inventory.
    # These actions will make enough time pass that the rig will generate a random asset for itself
    hack1 = Hacker.Hacker('HackMan')
    hack1.acquire_rig()
    hack1.retrieve_asset()
    # either retrieve All to take 2 data spikes, or choose single data spike to transfer


def test2():
    ### Creates a hacker, acquires a rig, attempts to acquire a 2nd rig. Will not allow hacker to own more than 1 rig
    hack2 = Hacker.Hacker('Hackerino')
    hack2.acquire_rig()
    hack2.acquire_rig()

def test3():
    ### Creates 2 hackers, acquires rigs for each. 1st hacker launches 2 x data spikes at 2nd hacker, breaking their
    ### rig and transferring all un-encrypted assets to 1st hacker's inventory
    hack3 = Hacker.Hacker('HackInTheBox')
    hack3.acquire_rig()
    hack4 = Hacker.Hacker('HackAndTheBeanstalk')
    hack4.acquire_rig()
    hack3.launch_dataspike(hack4)
    hack3.launch_dataspike(hack4)
    print(hack3)
    print(hack4)


def test4():
    ### Creates hacker and attempts to encrypt their crypto token. Since no security chip is in their inventory,
    ### cannot achieve
    hack5 = Hacker.Hacker('HackSkellington')
    hack5.encrypt_asset()

def test5():
    ### creates hacker and attempts to upgrade their rig. hacker has no rig, cannot upgrade.
    ### then, acquires a rig and attempts to upgrade, hacker has no hardware patch, cannot upgrade
    hack6 = Hacker.Hacker('HackBeNimble')
    hack6.upgrade_rig()
    hack6.acquire_rig()
    hack6.upgrade_rig()


def test6():
    ### Creates a hacker and attempts to retrieve an asset from the rig. Since hacker has no rig, cannot retrieve.
    ### Then acquires rig and can retrieve asset(s)
    hack7 = Hacker.Hacker('HackInBlack')
    hack7.retrieve_asset()
    hack7.acquire_rig()
    hack7.retrieve_asset()

def test7():
    ### creates hacker, acquires rig. transfers assets from rig to hacker and back until trace level
    ### reaches threshold and will not allow any further transfers
    hack8 = Hacker.Hacker('HackySack')
    hack8.acquire_rig()
    hack8.retrieve_asset()
    hack8.store_asset()
    hack8.retrieve_asset()


test7()

