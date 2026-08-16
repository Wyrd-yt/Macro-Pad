import win32com.client
import serial.tools.list_ports
from communication import connectVerif, send
from logique import presets, ID
import time



def showCurrentDevices():
    for port in serial.tools.list_ports.comports():
        print(port.device)
        print(port.description)
        print(port.hwid)
        print(port.serial_number)
        print()



wmi = win32com.client.GetObject("winmgmts:")

watcher = wmi.ExecNotificationQuery(
    "SELECT * FROM Win32_DeviceChangeEvent"
)

if connectVerif():
    send(presets)

while True:
    event = watcher.NextEvent()

    if event:
        print("Appareil connecté/déconnecté")
        if connectVerif():
            send(presets)



    