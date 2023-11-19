"""Checks that the cofundable package installs correctly"""
import cofundable

def test_package_name():
    """The package name should be cofundable"""
    assert cofundable.__name__ == "cofundable"
