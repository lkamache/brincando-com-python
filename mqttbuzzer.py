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
	
	if isinstance(msg.payload,int):

		beeps = int(msg.payload)

		if beeps > 10:
			GPIO.output(21, True)
			sleep(0.06)
			GPIO.output(21, False)
			sleep(0.06)
			GPIO.output(21, True)
			sleep(0.06)
			GPIO.output(21, False)

		else:
			for x in range(int(beeps)):
				GPIO.output(21, True)
				sleep(0.06)
				GPIO.output(21, False)
				sleep(0.5)

	else:
		GPIO.output(21, True)
		sleep(0.06)
		GPIO.output(21, False)
		sleep(0.5)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.0.0.254", 1883, 60)

try:
	client.loop_forever()

except KeyboardInterrupt:
	GPIO.cleanup()
