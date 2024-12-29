import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

def process_data():
    data = ser.readline()

    try:
        data = data.decode('utf-8')
    except ValueError as e:
        return (False, False)
    
    data = (data.replace('\r','')).replace('\n','')
    
    try:
        angle, distance = int(data.split(',')[0]), float(data.split(',')[1])
    except (ValueError, IndexError) as e:
        return (False, False)
   
    return (angle, distance)


if __name__ == "__main__":
    while True:

        try:
            angle, distance = process_data()
            print(f'Angle: {angle} \nDistance {distance}')
        
        except KeyboardInterrupt:
            break
