# Steam Shared Library Fix

This script is designed to fix a niche issue for users who store their game library on external drive or partition other than the primary linux OS partition. Though, the specific situation this tool aims to solve is for a partition/drive that is exFAT formatted. 

## Justification: 
With proton in theory we should be able to install a Windows-only game once on our exFAT partition and then launch it from either a Windows or Linux OS. This is useful when dual booting to save space. Especially if you are a Windows user considering switching to linux but not ready to remove windows from your system entirely.

## Pre-requisites:

On Windows:
* format a partition or drive to be exFAT
* using steam install or move games to the exFAT partition

On Linux:
* python3 installed
* the exFAT partition or drive is mounted with the following options: ```nosuid,nodev,nofail,x-gvfs-show,exec,uid=1000,gid=1000,umask=000```
* proton is enabled in steam
* add the following to your .bashrc replacing the paths with appropriate ones for your system:
     ```
     export STEAM_EXT_LIB=/path/to/your/exFAT/SteamLibrary/steamapps/
     export STEAM_LOC_LIB=/path/to/your/local/default/steamapps/
     fix_steam(){
         python3 /path/to/your/steam_library_fix.py
     }
     ```

Now, once you start a fresh terminal session you should be able to invoke ```fix_steam ``` and the tool should take care of everything else.

## Notes
* I am running Regolith Linux based on ubuntu 21.04 LTS dual booting with Windows 10, as much as I would like to say this should work for all linux distros I will warn that this is the only configuration I have tested this on and have no plans on testing it with other distros.

* this tool will need to be re-run any time you add more games to your shared library and also requires that you install games only with windows, kinda crummy but hey, it works. This is due to the nature of the solution being to use symlinks to "trick" linux into thinking your game is stored locally allowing it to utilize all the linux-specific proton magics.