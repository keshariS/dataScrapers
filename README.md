# Data Scrapers
This is a collection of several data scrapers for popular websites made as part of the Computational Media Lab at UT Austin

Description of each scraper and how it works is documented in the respective folders.

# Note
The scrapers (essentially this repository) are hosted on an Oracle Cloud instance (ubuntu@129.213.41.169) which can be accessed via SSH.
To access the instance from a new device, these steps need to be followed:

1. From the terminal of the new device run this:

>>> $ ssh-keygen -t rsa -b 4096

This will create an SSH pair for the device (private key: id_rsa, public key: id_rsa.pub). Note the directory where these files are stored

2. From the noted directory above, run: 

>>> $ cat id_rsa.pub

This will display the key value something like this: ssh-rsa AAAAB3NzaC......... (a long value) Copy this value

3. For someone/device who/that already has access to the instance: Login to the instance and run:

>>> ubuntu@smscraper:~$ cd .ssh

>>> ubuntu@smscraper:~/.ssh$ echo "<paste the copied public key from step 2 here>" >> authorized_keys

4. To check that the new key has been added to the instance:

>>> ubuntu@smscraper:~/.ssh$ cat authorized_keys

5. Now the new device can access the instance (recommended: use VSCode with Remote SSH extension)


# WinSCP

Use PuTTy to convert the id_rsa.pub file to .ppk file format

Install WinSCP and use the server 129.213.41.169 with username 'ubuntu', SFTP, port 22.
Use the .ppk file for authentication on: Advanced > SSH > Authentication > .ppk file

Then all the data can be viewed on /mnt/smdata/ and the instance can be accessed from /home/ubuntu/
