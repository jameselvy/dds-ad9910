
# dds-ad9910 

## Quick Start

This is a Python program that enables a user to control the [dds-ad9910 board](http://www.gempillar.com/dds-ad9910.html) that I built from a graphical user interface via USB. 


### Dependencies

On newer Debian based systems the only dependency that is not installed by default is normally just python-gnome2 (which will give you the gnomevfs module).

`$ sudo apt-get install python-gtk2 python-ftdi`

The above command should install all the packages that you will need to run this program.  If `python-ftdi` is not found for your system, at this point you can still run the program but later versions of it do plan on using this package.


### Running the program

Once you have installed the necessary dependencies and downloaded the code from the repository, go into the top directory and execute ddscontrol:

`$ ./ddscontrol`


#### TODO

This program is not yet finished but here are some of the major items that still need to be addressed:

+ Create hooks for GUI and ftdi commands
+ Package up the code with distutils
+ ...



