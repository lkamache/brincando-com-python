from time import sleep
import paho.mqtt.client as mqtt

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)

def on_connect(client, userdata, flags, rc):
    client.subscribe("buzzer")

def on_message(client, userdata, msg):
    mensagem = str(msg.payload)
    if mensagem == "1":
    	GPIO.output(21, True)
    	sleep(0.06)
    	GPIO.output(21, False)
    else:
    	GPIO.cleanup()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.0.0.254", 1883, 60)

client.loop_forever()

def buzzer_on(interval_on):
    GPIO.output(21, True)
    sleep(interval_on)

def buzzer_off(interval_off):
    GPIO.output(21, False)
    sleep(interval_off)

# try:
#     while True:
#         buzzer_on(0.06)
#         buzzer_off(1)

# except KeyboardInterrupt:
#     GPIO.cleanup()
