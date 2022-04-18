<!--
  ~ Copyright (c) 2022 Tobias Briones. All rights reserved.
  ~ SPDX-License-Identifier: MIT
  ~
  ~ This source code is part of
  ~ https://github.com/tobiasbriones/cp-unah-is512-osii and is
  ~ licensed under the MIT License found in the LICENSE file in the root
  ~ directory of this source tree or at https://opensource.org/licenses/MIT
  -->

# Apache Server

## Get Started

For this project, there are the following requirements:

- Domain Name.
- VM.
- Website to Deploy.

I chose to use Porkbun for acquiring the domain name, Digital Ocean for the VM,
and [Coniestica](https://github.com/tobiasbriones/ep-coniestica) (an EP I use to
use for these scenarios).

I opted for this config because I want to make some test to those platforms, I
have expertise on domain names, and Porkbun has super cheap prices. Digital
Ocean is more mature now, and I've seen they have managed databases, so it is a
good chance to check out over there.

### Get the Domain Name

You need a domain name to set up the web server. I'll lead you through this
on [Porkbun](https://porkbun.com). As you can see, there are many cheap
[registration prices](https://porkbun.com/products/domains), you can also go to
other registrars like [Namecheap](https://namecheap.com) (most popular),
[Google Domains](https://domains.google), [Name.com](https://name.com), or many
others. I was able to find domain registration as low as about $1 in Porkbun,
and bought this one:

![Porkbub Buy Domain](screenshots/porkbun-buy-domain.png)

A .website domain for about $1.11. The process is always simple, select your
domain name, and go to checkout to pay with your account. Make sure your account
is secure as it contains your personal information and your domain names, this
is sensitive information, or else imagine someone stealing your domain name,
that would be a nightmare. I leave you
this [scary story](https://www.namepros.com/threads/domains-got-stolen-from-my-namesilo-recovered.1097787)
you can read.

## Get the VM

I'll lead you to Digital Ocean on this endeavour. There are many other options
like Linode, Azure, AWS, or Google Cloud too.

Head to "Droplets" on the "Manage" navigation, and click on "Create Droplet".

I chose an Ubuntu 20.04 (LTS) x64, Basic plan, Regular with SSD $5/mo CPU
(1GB, 1 vCPU, 25GB SSD, 1000GB transfer) configuration.

The datacenter might be "New York (1)" for this test, and the VPC as default.

![DigitalOcean Create Droplet](screenshots/digitalocean-create-droplet.jpeg)

For authentication, use SSH which is more secure. Now a key pair is to be
created. Click on "New SSH Key", to create a new key you can
read [How-to Add SSH Keys to New or Existing Droplets \| DigitalOcean 
Documentation](https://docs.digitalocean.com/products/droplets/how-to/add-ssh-keys)
to add the public key to the public field. SSH keys are automatically 
generated in other platforms like AWS or Azure when creating them, that's a 
downside of DO.

Then, set a hostname like "ubuntu-do". 

Click on "Create Droplet" and wait until the machine is deployed.

You will have created a droplet like this:

![DigitalOcean Droplets](screenshots/digitalocean-droplets.png)

## Get the VM Started

First, log into your VM. You can use PuTTY following
[this guide](https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/putty)
to enter your server as root user.

Once you are into your machine, execute basic maintenance commands:

`sudo apt update`

![PuTTY Log into VM](screenshots/putty-log-into-vm.png)

It is highly recommended creating a different user to avoid using the root user
as [detailed here](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04).

Run `adduser { username }` and set the user's password and other information.
Then add root privileges to that user as follows:

`usermod -aG sudo { username }`

That will add your new user to the sudo group. In this case, my username is
"tobi".

Then generate another key pair for giving SSH access to the new user.

Add the public key next, first enter as root to then change to the new user:

`su - { username }`

`mkdir ~/.ssh`

`chmod 700 ~/.ssh`

`cd ~/.ssh`

`nano authorized_keys`

And paste your public key.

`chmod 600 ~/.ssh/authorized_keys`

`exit`

Now disable password authentication:

`sudo nano /etc/ssh/sshd_config`

Find this property, and make sure it is uncommented and set to "no", that
is, `PasswordAuthentication no`. For my case, this was already configured that
way.

Other attributes that we have by default are `PubkeyAuthentication yes` and
`ChallengeResponseAuthentication no`.

Finally, reload the SSH daemon with `sudo systemctl reload sshd`.

Now you can log with the new user created.

![PuTTY Log as tobi](screenshots/putty-log-as-tobi.png)

### Set Up the Firewall

Make sure the firewall will allow you to connect via SSH, this is a common 
problem when playing with this.

`sudo ufw app list`

It'll show `OpenSSH` as available applications.

And make sure to allow your connection:

`sudo ufw allow OpenSSH`

Now run:

`sudo ufw enable`

`sudo ufw status`

![PuTTY Firewall Config](screenshots/putty-firewall-config.png)

