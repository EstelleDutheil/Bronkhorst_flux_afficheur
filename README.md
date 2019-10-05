Python program on Raspberry PI 3 Model B+ for Bronkhorst's MFC control.

Afficheur_flux, an example, is the main program as a GUI for displaying a Bronkhorst's MFC.

Based on tkinter Afficheur_flux also needs modules :
 - creation_serial_port => to get a (or several) serial communication with MFC
 - trames_fonctions => working with "convertisseurs" modules can generate the communication
   for some specific parameters and read and write the values.

The way to make your program :
 - Take modules : from tkinter import*
                  from tkinter.messagebox import*
                  (already standard and welknown)
                  from creation_serial_port import*
                  from trames_fonctions import*
                  (two additionnal modules in the repository, trames_fonctions already integrats several
                   "convertisseur" modules for reading and writing the values needed)
 - class instrument has to be used
                  Created with several function (def ...) can question the MFC or sending instructions.
                  Each requested parameter can be integrated as the program needs
 - with tkinter the window for a graphic user interface can be program for MFC control.
