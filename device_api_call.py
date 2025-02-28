device = CANDevice()
device.parameters['channel'] = 0
device.parameters['bitrate'] = 1234
device.open()
data = 'test data'
device.write(data)
response = device.read()
device.close()
