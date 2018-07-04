from time import sleep

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)

def buzzer_on(interval_on):
    GPIO.output(21, True)
    sleep(interval_on)

def buzzer_off(interval_off):
    GPIO.output(21, False)
    sleep(interval_off)

try:
    while True:
        buzzer_on(0.06)
        buzzer_off(1)

except KeyboardInterrupt:
    GPIO.cleanup()
