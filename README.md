# Arduino-Radar
Arduino-Radar Project

This project runs an ultrasonic sensor and servo motor on a arduino uno.
Than python reads the data from the arduino and create a polar plot for radar.

The code to flash onto the arduino is under the radar folder.
Use the Arduino IDE to load the radar.ino file on to the arduino board

<insert diagram of arduino setup>

<add in assembly code and commands to flash it onto the arduino>

The python code for reading the data and creating the polar plot is under python

pull repo with 
```git clone https://github.com/Jacob5585/Arduino-Radar```

Install the nessary python packages.
```
python -m venv python/.env
source python/.env/bin/activate
pip install -r python/requirements.txt
```

run the python code with
```
source python/.env/bin/activate
python python/main.py
```

The radar graph can be run on its own, since it creates its own data to work with when run directly
```
python python/radar_graph.py
```

https://github.com/user-attachments/assets/9d452c04-90c3-42a6-aefe-05f801773178
