# Setting up flask on DreamHost for web app deployment
Step by step guidance for setting up the flask on DreamHost for web app deployment.

These steps are valid for both Shared Website Hosting and Virtual Private Server.

## Enable Passenger for your domain
DreamHost uses Passenger to simplify the deployment of Flask web apps. The process of enabling Passenger for a site/domain/subdomain can be found in the DreamHost documentation https://help.dreamhost.com/hc/en-us/articles/216385637-How-do-I-enable-Passenger-on-my-domain-. The easiest way might be to select Passenger in the process of creating a domain/subdomain instead of changing it after the creation of the domain.

## Install Python3
DreamHost has Python2 installed by default, but it also allows users to install a custom version of Python3. The installation of python or any other related libraries requires the use of SSH (or Secure Shell). 

### Connection of SSH to the server
There are a large range of SSH clients that you can choose to connect to the server, on systems including MacOS X, Unix/Linux, Windows, Chrome, IOS (iphone), and Android. Here is a quick list in the DreamHost documentation https://help.dreamhost.com/hc/en-us/articles/215360828-SSH-client-software.

There are two ways to connect the SSH to the server:
```
[server]$ ssh username@example.com
```
or
```
[server]$ ssh username@server.dreamhost.com
```

followed by inputting the password upon pressing "Enter".

The `username` and `password` can be easily found in the **DreamHost Panel** - **Websites** - **FTP Users & Files**.

The `server` in the second option varies depending on the plan you have with DreamHost. More information can be found in the DreamHost documentation https://help.dreamhost.com/hc/en-us/articles/216041267-SSH-overview. To make it easier, we recommand using the first option whenever possible.

### Python3 installation
After logged into the server via SSH, run the below command one by one to install a custom version of Python3. Below example installs Python 3.9.2. You can change this based on your own needs.
```
[server]$ cd ~
[server]$ mkdir py3_tmp
[server]$ cd py3_tmp
[server]$ wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
[server]$ tar zxvf Python-3.9.2.tgz 
[server]$ cd Python-3.9.2 
[server]$ ./configure --prefix=$HOME/opt/python-3.9.2
[server]$ make
[server]$ make install
[server]$ echo 'export PATH=$HOME/opt/python-3.9.2/bin:$PATH' >> ~/.bash_profile
[server]$ . ~/.bash_profile
```
The last two commands set this version of Python as the default for the user, and then reload the file to activate it.
Now we can delete the temporary folder `py3_tmp` using the command below:
```
[server]$ cd ~
[server]$ rm -r py3_tmp
```

