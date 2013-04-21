Team Name: apollo
Team Members: Manish Shrestha, Ajaya Maharjan, Nhasala Joshi, Binisha Shrestha, Sajana Maharjan
Team Location: Kathmandu, Nepal, Earth
Virtual Member: Benjamin Pinaya (Bolovia)
Project Name: Pi Powered Arduino
Challenge: Arduiono
InterNational Space Challenge 2013

======
This project is solving the ArduSat challenge.

It address the level 2 hardware challenge related to Ardusat. Here, Linux based computer (RasberryPi) is used as main computer and Arduino Uno & a Freeduino (which can be easily extended to Due/Maple) are used as experiment node.

The first goal of this project is to be able to remotely program the arduino nodes, so that the people from earth or anywhere with internet access can easily program them and test their programs and experiments in the space via the Ardusat.


Assumption:
The web server (apache or any server supporting php)in the Raspberry Pi is hosting our web files at  /var/www/ArduSat. The main server is located at /home/pi/apollo/executer. The startup script is starting the webserver and running the python file at  /home/pi/apollo/executer/executer.py.

The interface for uploading the hex files can be found at http://192.168.5.10/ArduSAT/ , where 192.168.5.10 is the ip address of the Raspberry PI, and should be replaced by the actual IP.


License: GNU General Public License
Source Code: https://github.com/SpaceAppsKtm2013/apollo.git
Project URL: http://spaceappschallenge.org/project/apollo/
