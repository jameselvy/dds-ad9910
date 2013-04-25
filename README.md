
# dds-ad9910

This is a Python program that enables a user to control the [dds-ad9910](http://www.gempillar.com/dds-ad9910.html) board that I built from a graphical user interface via USB. 

## Dependencies

Besides Python, you will need the following python packages:

+ python-gtk
+ shutil
+ gnomevfs

### Running the program

Once you have installed the necessary dependencies and downloaded the code from the repository, go into the top directory and execute ddscontrol:

`$ ./ddscontrol`


#### TODO

This program is not yet finished but here are some of the major items that still need to be addressed:

+ Hook up ftdi interface code to ftdi commands
+ Package up the code with distutils
+ ...



