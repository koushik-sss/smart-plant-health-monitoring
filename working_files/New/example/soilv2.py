def soilID():
    import RPi.GPIO as GPIO

     
    #GPIO SETUP
    channel = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)


    if (GPIO.input(channel)==GPIO.LOW):
        print("Water")
        status = "water present"
    else:
        print("No Water")
        status = "Not present"

    return status
       
