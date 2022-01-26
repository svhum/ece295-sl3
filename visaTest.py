# This program makes sure that libraries are all installed correctly
# by Ian Bennett
import pyvisa as visa
rm = visa.ResourceManager(r'C:\WINDOWS\system32\visa64.dll')
print(rm)
print(rm.list_resources('TCPIP0::?*'))
