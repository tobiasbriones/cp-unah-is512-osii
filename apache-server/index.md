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
