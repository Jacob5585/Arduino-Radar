# Arduino-Radar
Arduino-Radar Project

This project runs an ultrasonic sensor and servo motor on a arduino uno.
Than python reads the data from the arduino and create a polar plot for radar.

The code to flash onto the arduino is under the radar folder.
The python code for reading the data and creating the polar plot is under python

pull repo with 
`git clone clone Jacob5585/Arduino-Radar`

Install the nessary python packages.
```
python -m venv python/.env source
source python/.env/bin/activate
pip install -r requirements.txt
```

run the python code with
```
source python/.env/bin/activate
python python/main.py
```
