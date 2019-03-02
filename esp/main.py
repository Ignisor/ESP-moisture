import time

import ubinascii
import machine
from umqtt.simple import MQTTClient

from data import conf
from utils.pins import MOISTURE


CLIENT_ID = ubinascii.hexlify(machine.unique_id()).decode()
mqtt = MQTTClient(CLIENT_ID, conf.MQTT_SERVER, **conf.MQTT_CONF)
mqtt.connect()


def main():
    time.sleep(1)
    value = MOISTURE.read()

    print('Publishing {}'.format(value))
    mqtt.publish('sensors/moisture/{}'.format(CLIENT_ID).encode(), str(value).encode(), qos=1)

retries = 5
while retries:
    try:
        main()
        break
    except Exception as e:
        with open('errors.txt', 'a') as err_file:
            err_file.write(str(e))
            err_file.write('\n')
        mqtt.publish('errors/{}'.format(CLIENT_ID).encode(), str(e).encode(), qos=2)
        retries -= 1

mqtt.disconnect()

rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
rtc.alarm(rtc.ALARM0, 60 * 60 * 1000)

machine.deepsleep()
