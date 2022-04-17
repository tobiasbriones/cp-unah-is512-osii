# Exam

## Introduction

You need to test your virtual machines created in VirtualBox to perform some 
system administration.

The virtual machines are two Ubuntu Server images like the picture below:

![VirtualBox VMs](screenshots/virtualbox-vms.png)

You should run maintenance commands like:

`sudo apt update`

Then install a remote desktop to control the server via GUI, setting up 
commands like these:

`sudo apt install xrdp`

`sudo apt install xubuntu-desktop`

`sudo systemctl status xrdp`

Or any other GUI you like.

`sudo ufw allow 3389`

To allow the remote connection port.

Make sure to connect the VM to the internet via Bridge Adapter so your 
Windows machine can access their IP addresses.

Then you should be able to do something like this:

![Windows RDC](screenshots/windows-rdc.png)

To enter your username and password to log into the machine.

Other tasks involved are firewall configurations using the `ufw` command.

This introduction gave an insight about the administration given to the VMs.
