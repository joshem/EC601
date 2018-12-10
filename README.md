# E601 Mini Project 3
This project builds off of the first project, of which this is a branch of.  To explain, the original project used the Twitter API and Google Vission API to grab pictures off of a feed, convert them to a slideshow and then create descriptions of them.  This branch implements a mongoDB and mySQL implementation as well.

## Setup
Please refer to the master branch for instructions on how to setup a working prototype.

## Installation and Running

### SQL
```
sudo apt update
sudo apt remove --purge mysql*
sudo apt install mysql-server mysql-common mysql-client
pip3 install mysql-connector-python
```
You may have to install python3 or pip3. There are plenty of helpful tutorials online for this.
If you had an instance/setup of MySQL already installed, I would not recommend the first instruction, as it may get rid of all your data.  User experience may vary.

I also had the encounter of consistantly forgetting my password, as I had at some point 
used a secure installation, which implemented various security measures.  This prevented some commands like 
```sudo mysql``` 
as you needed to have a password running.  I personally found this guide to be helpful, please refer to it.
https://help.ubuntu.com/community/MysqlPasswordReset

To initialize and/or clean your databse:
```
python3 init_sql.py
```
You will be given an input instruction, and enter the one you would like to do.

To run a series of executions of suggested API implementations, run the following:
```
python3 mysql_run.py
```
This utilizes an API implemented, entitled simply sqlAPI.py.  To utilize this in your projects, you may copy the file into your directory and have ```import sqlAPI``` into your python program.  You may of course change the title, but do always keep a record of where you got this from :)



### MongoDB

```
sudo apt update
sudo apt install mongodb
pip3 install pymongo
```
If you run into connection problems while running anything, this link may be of assistance.  I personally encounterred trouble with simple pymongo application: https://askubuntu.com/questions/884541/cant-start-mongodb-service. Note that to undo installation, run ```sudo apt purge mongodb*```.  This will remove any instances, and then simply follow those instructions.



###### I requested an extension for this project due to computer problems (it was in the shop getting fixed for some unfortunate damage)..Professor Osama never specified a date, but I will be done by Saturday. Please email me if this needs to be discussed, at joshe@bu.edu



