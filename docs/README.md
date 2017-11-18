# FacebookTools

This project provide a simple python module for doing batch tasks on your Facebook profile.
Currently the module provide can be used for leaving mulitple Facebook groups using keywords that occur in the name of those groups.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to install Chrome WebDriver for this module to work.
Chrome WebDriver can be found and installed from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). 

### Downloads

You can download the latest release [here](https://github.com/justani98/FacebookTools/releases).

### Installing

**linux**

You can extract the tar.gz file and run (you may be required to give root permission):
```
python3 setup.py install
```
This will install the module facebookTools.
Now open the `python3` terminal and import facebookTools
```
from facebookTools import groups
```

You can now run the leave() function.
```
groups.leave()
```
It will then ask you for your Facebook `username` and `password`.
```
Enter your Facebook username
Password:
Enter the keywords separated by space.
Whenever a group name contain any of these keywords the group will be left.
```

You can enter the keyword in a single line separated by space. The group names which contain the entered keyword will be left.

#TODO
