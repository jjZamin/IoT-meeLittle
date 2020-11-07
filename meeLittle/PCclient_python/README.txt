################################# MEE.CHAT #################################
----Written by Ghennadie Mazin----


########## RUN #############
To run the program, you must have python 3.7.x, as "kivy" that was used for the GUI is NOT yet supported for Python 3.8.x! 
Enter your shell or cmd propt and run the meeChat.py file.

This is a piece of software that works as a MQTT client.
Username: jack
Password: 1234

The set-up is simple.
Log in.
Insert the Broker ID.
Insert the Client ID.
Insert the Topic.
Connect.
Send messages!

This is made for the test of the mee.little setup, but it can also be used as a stand alone MQTT client for testing.
If the broker is password protected, the configurations can be made in log_in_dets.txt document in this folder.
Simply change jack to whatever username you need and change 1234 password to whatever password you need.
These same credentials are used to log into the meeChat software! 

### Warning
The software MIGHT crash if you try to connect to a broker IP that does not exist.