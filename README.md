# OLEDSteamLauncher
A script to turn on your LG OLED TV, switch the image source to your PC, and launch Steam for a seamless gaming experience.

## Features

* Wake up the TV using Wake-on-LAN.
* Turn on the LG TV.
* Change the TV's input source.
* Change the computer's display output to the TV.
* Change the computer's audio output to the TV.
* Launch Steam in Big Picture mode.

## Requirements

    Python 3.x
    pywebostv library
    wakeonlan library
    configparser library (standard with Python)
    nircmd utility
    Steam installed on your computer

## Installation

Clone the repository:

``` bash

git clone https://github.com/yourusername/tv-automation-script.git
cd tv-automation-script
```
Install the required Python packages:

```bash

    pip install pywebostv wakeonlan

    Download and place the nircmd utility in the specified path.

    Ensure Steam is installed in the specified path.
```
## Configuration

Create a config.ini file in the root directory of the repository with the following structure:

ini
```
[TV]
MAC_ADDRESS = xx:xx:xx:xx:xx:xx
IP_ADDRESS = 192.168.1.x
CLIENT_KEY = your_client_key
SOURCE_INDEX = 0

[PATHS]
NIRCMD_PATH = C:\Path\To\NirCmd
STEAM_PATH = C:\Path\To\Steam

[AUDIO]
SOURCE_NAME = your_tv_source_name
```

## Usage

Run the script with Python:

```bash
python tv_automation.py
```

## The script will:

* Send a Wake-on-LAN packet to wake up the TV.
* Connect to the TV and set the input source.
* Change the display output to the TV.
* Change the audio output to the TV.
* Launch Steam in Big Picture mode.

## Creating an Executable with PyInstaller (Recommended)

To create an executable file for this script using PyInstaller, follow these steps:

Install PyInstaller:

```bash
pip install pyinstaller
```

Create the executable:

```bash
pyinstaller --onefile tv_automation.py
```

This command will generate a dist folder containing the tv_automation.exe file.

Move the config.ini file to the same directory as the executable (dist folder).

Ensure that all paths specified in the config.ini file are absolute paths.

## Troubleshooting

* Ensure that the TV is connected to the same network as the computer running the script.
* Verify that the MAC address, IP address, and client key are correct in the config.ini file.
* Make sure nircmd and Steam paths are correct.
* Check for any errors in the terminal output for additional troubleshooting information.

License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

### pywebostv https://pypi.org/project/pywebostv/
### wakeonlan https://pypi.org/project/wakeonlan/
### NirCmd https://www.nirsoft.net/utils/nircmd.html