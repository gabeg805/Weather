===========
What is it?
===========

Using the Weather Underground API, this script displays weather information in the
terminal. The user is able to:

    - Print current weather information
    - Print future weather information
            * Displays weather information in 1 hour increments



=============
Documentation
=============

There are two scripts at play in this program:
    
    - weather
    - wuapi.py

The Weather Underground API is accessed by 'wuapi.py'. This gathers a whole lot of 
weather data, and 'weather' uses this information and displays only the 
necessary parts.

For more information on what each script does, check out their headers.



============
Installation
============

To install this program, execute the following:

    $ unzip Linux-Scripts-master.zip
    $ mkdir -p ~/scripts/
    $ mv Linux-Scripts-master/* ~/scripts
    $ rmdir Linux-Scripts-master
    $ cd ~/scripts/programs/weather/src/setup/
    $ ./setup

This will change any harded coded paths in the scripts so that no path errors occur.
In terms of dependencies, I believe the python modules used are included by default, 
in case they are not though, you'll have to research the import module error 
yourself (Sorry!). 



========
Contacts
========

If you have any problems, feel free to email me at 'gabeg@bu.edu'.



==================
Potential Problems
==================

There is one issue, to my knowledge, that may occur when running the weather script.

    - The weather script hangs and doesn't print anything.
            * Just kill the process with Ctrl-C and try again
