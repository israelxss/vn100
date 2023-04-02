import serial

ser = serial.Serial("/dev/serial/by-id/usb-FTDI_USB-RS232_Cable_FT420XL8-if00-port0", 115200, timeout=1)

def read_gyro_accel():
    ser.write(b'VNRRG,10\r\n') # Request the current gyro and accelerometer measurements
    response = ser.readline().decode().strip() # Read the response from the VN-100
    values = response.split(",") # Split the response into individual values
    gyro = [float(values[1]), float(values[2]), float(values[3])] # Extract the gyro measurements
    accel = [float(values[4]), float(values[5]), float(values[6])] # Extract the accelerometer measurements
    return gyro, accel

while True:
    gyro, accel = read_gyro_accel()
    gx,gy,gz = gyro
    ax,ay,az = accel
    print("Gyro: ",gx,gy,gz)
    print("Accelerometer: ",ax,ay,az)