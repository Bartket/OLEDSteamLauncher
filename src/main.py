import configparser
from pywebostv.discovery import *
from pywebostv.connection import WebOSClient
from pywebostv.controls import SourceControl
from wakeonlan import send_magic_packet
import subprocess
import os
import time

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# TV
TV_MAC_ADDRESS = config['TV']['MAC_ADDRESS']
TV_IP_ADDRESS = config['TV']['IP_ADDRESS']
CLIENT_KEY = config['TV']['CLIENT_KEY']
SOURCE_INDEX = int(config['TV']['SOURCE_INDEX'])
STORE = {'client_key': CLIENT_KEY}
# Applciation Paths
NIRCMD_PATH = config['PATHS']['NIRCMD_PATH']
STEAM_PATH = config['PATHS']['STEAM_PATH']
# Audio Source
AUDIO_SOURCE = config['AUDIO']['SOURCE_NAME']

def wake_up_tv(mac_address):
    """Send magic packet to wake up the TV."""
    send_magic_packet(mac_address)
    print(f"Sent magic packet to {mac_address}")

def connect_to_tv(ip_address, store):
    """Connect to the TV and register the client."""
    client = WebOSClient(ip_address, secure=True)
    client.connect()
    for status in client.register(store):
        if status == WebOSClient.PROMPTED:
            print("Please accept the connection on the TV!")
        elif status == WebOSClient.REGISTERED:
            print("Application login successful")
            return client
    return None

def set_tv_source(client, source_index):
    """Set the TV source to the specified index."""
    source_control = SourceControl(client)
    sources = source_control.list_sources()
    if source_index < len(sources):
        source_control.set_source(sources[source_index])
        print(f"Source set to {sources[source_index]['label']}")
    else:
        print(f"Invalid source index: {source_index}")

def change_display():
    """Change the display to external."""
    subprocess.run([os.path.join(os.getenv('windir'), 'System32', 'DisplaySwitch.exe'), '/external'], check=True)
    time.sleep(3)

def change_audio_source(nircmd_path):
    """Change the audio source to the TV."""
    subprocess.run([os.path.join(nircmd_path, 'nircmd.exe'), 'setdefaultsounddevice', AUDIO_SOURCE, '1'], check=True)
    time.sleep(3)

def open_steam(steam_path):
    """Open Steam in Big Picture mode."""
    subprocess.run([os.path.join(steam_path, 'steam.exe'), 'steam://open/bigpicture'], check=True)
    time.sleep(3)

def main():
    wake_up_tv(TV_MAC_ADDRESS)
    
    client = connect_to_tv(TV_IP_ADDRESS, STORE)
    if client:
        set_tv_source(client, SOURCE_INDEX)

    change_display()
    change_audio_source(NIRCMD_PATH)
    open_steam(STEAM_PATH)

if __name__ == "__main__":
    main()