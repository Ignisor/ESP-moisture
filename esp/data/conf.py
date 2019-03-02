SSID = '[ssid]'
PASSWORD = '[pass]'
CONNECT_RETRIES = 10
CONNECTION_TIME = 6.0

MQTT_SERVER = 'm24.cloudmqtt.com'
MQTT_CONF = {
    'port': 27730,
    'user': '[username]',
    'password': '[password]',
    'ssl': True,
}

ERROR_LOG_FILENAME = 'error.log'

try:
    from .local_conf import *
except ImportError:
    pass
