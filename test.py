import sounddevice as sd
device = 1
print(sd.query_devices(device, 'input'))
