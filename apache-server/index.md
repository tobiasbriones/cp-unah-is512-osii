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

## Install Apache

Start with these commands:

`sudo apt-get update`

`sudo apt-get install apache2`

Create the public directory for the website:

`sudo mkdir -p /var/www/operatingsystems.website/public`

Where "operatingsystems.website" is the name of our website to deploy.

Change ownership for the normal user (you have to be logged as the new user 
you created):

`sudo chown -R $USER:$USER /var/www/operatingsystems.website/public`

`sudo chmod -R 755 /var/www`

## Clone the Website

We're going to use my example project website as said above. Clone the 
repository first:

`git clone https://github.com/tobiasbriones/ep-coniestica.git`

And install node with NVM, get the latest script version
from https://github.com/nvm-sh/nvm#installing-and-updating

`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash`

`source ~/.bashrc`

Check the Node versions with `nvm list-remote` and install the latest (LTS 
or normal) version:

`nvm install v16.14.2`

`nvm list`

Now go into the project directory `cd ep-coniestica` to build the project:

`npm i`

`npm run build:prod`

Then you'll have a "dist" directory that contains the production-ready website.
That is what has to be copied to the public directory to be deployed.

`mv -v dist/* /var/www/operatingsystems.website/public`

## Create the Virtual Host File

Virtual Hosts are individual entities in the Apache web server, this way you can
have several websites on the same machine for example. The default is the
file `000-default.conf` that we'll use as a basis for adding the others.

`sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/operatingsystems.website.conf`

`cd /etc/apache2/sites-available/`

`sudo nano operatingsystems.website.conf`

Recall that, the default port is port 80. So first, we need to configure the 
domain for this website.

Set the `ServerAdmin` directive to an admin email you can use.

Set the `DocumentRoot` directive to `var/www/operatingsystems.website/public`.

Add two more directives, `ServerName operatingsystems.website` and 
`ServerAlias www.operatingsystems.website`. 

It'll look like this:

![PuTTY Main Virtual Host](screenshots/putty-main-virtual-host.png)

Now enable the virtual host file:

`sudo a2ensite operatingsystems.website.conf`

Disable the default with `sudo a2dissite 000-default.conf`, and reload the 
server `sudo systemctl restart apache2`.

This exercise is to be repeated for creating more virtual host files.

Now by enabling the port 80 via `sudo ufw allow 80` you will be able to open 
the page at http://operatingsystems.website (your own domain).

## Set Up the Domain Name

Go to Porkbun to your domain DNS Record config. Add the following config 
with your VM's IP address.

![Porkbun Set Up DNS Records](screenshots/porkbun-set-up-dns-records.png)

Add another for "www" too.

That's it. The domain name will respond with the website.

There's another way to add domains to DO, by going to your VM and clicking 
on the "More" menu, then "Add a domain". We used the apache virtual host to 
set up out web server this time.

## Install Let's Encrypt SSL Certificate

We need to install certbot and python3-certbot-apache
first `sudo apt install certbot python3-certbot-apache`. Now we already have 
the virtual host configured with the `ServerName` and `ServerAlias` directives.

Check the state of the virtual host file with `sudo apache2ctl configtest`, 
and reload the server `sudo systemctl reload apache2`.

### Allow HTTPS

Run `sudo ufw status` to check your current config, then 
`sudo ufw allow 'Apache Full'`, and `sudo ufw delete allow 80` or
`sudo ufw delete allow 'Apache'` depending on your current config.

### Obtain the SSL Certificate

Use `sudo certbot --apache`, and enter a valid email address, then accept 
the information that will be asked to you.

Great! Reload the page and you will have HTTPS enabled.

## Add Users with Password

We'll need three users to access the website with a password.

Install `apache2-utils` if not installed yet, so we can store our credentials:

`sudo apt-get update`

`sudo apt-get install apache2-utils`

Store an "admin" user with password "sistemasoperativos" by creating the 
next file. Use the "-c" argument the firsts time to create the file.

`sudo htpasswd -c /etc/apache2/.htpasswd admin`

Then enter the user password.

And add two more users as desired:

`sudo htpasswd /etc/apache2/.htpasswd { other-user }`

Just to mention, I added the example users "tobi:tobiasbriones", and 
"do:digitalocean" (username:password).

Check the ".htpasswd" file with `cat /etc/apache2/.htpasswd` that will show 
the encrypted passwords for each user. My users look like this:

![Website Users](website-users.png)

Go to the host file to add the following child:

`sudo nano /etc/apache2/sites-enabled/operatingsystems.website.conf`

If you are using SSL (you should) then edit the
`operatingsystems.website-le-ssl.conf` file instead.

```
<Directory "/var/www/operatingsystems.website/public">
    AuthType Basic
    AuthName "Proyecto de Sistemas Operativos II"
    AuthUserFile /etc/apache2/.htpasswd
    Require valid-user
</Directory>
```

It'll look like this:

![PuTTY Auth VirtualHost Config](screenshots/putty-auth-virtualhost-config.png)

Restart `sudo service apache2 restart`.

Then, the client will ask you for user and password:

![MS Edge Prompt enter Credentials](screenshots/ms-edge-prompt-enter-credentials.png)

## Add more Sites on Different Ports

This will deploy more websites to different ports. They'll be 4 websites on 
ports 8081-8084.

The procedure will be done for one website, and then this has to be copied 
for the others.

Make a new directory for the new site
with `sudo mkdir /var/www/operatingsystems.website.8081`, create an "index.html"
file into its "public" directory to add some content. Now copy the normal (80
HTTP) virtual host with
`sudo cp /etc/apache2/sites-available/operatingsystems.website.conf /etc/apache2/sites-available/operatingsystems.website.8081.conf`.

Open the file and make the respective changes:

`sudo nano /etc/apache2/sites-available/operatingsystems.website.8081.conf`

Changing the port from 80 to 8081, the `DocumentRoot` directive would be 
enough. We'll leave the same password file for authentication, create other 
password file with other users if needed.

Enable the new site with 

`cd /etc/apache2/sites-available/`

`sudo a2ensite operatingsystems.website.8081.conf`

`systemctl reload apache2`

Add the port 8081 to the Apache config `sudo nano /etc/apache2/ports.conf` 
by adding "Listen 8081" to that file.

Now to make the outside world access that port on our machine we need to 
allow it on the firewall rules:

`sudo ufw allow 8081`

![MS Edge Port 8081](screenshots/ms-edge-port-8081.png)

To add the other sites, replicate this section again.

Make sure to access as HTTP because the HTTPS connection is only for the secure 
port 443.
