import time
import json

from home_server.src.device_gateway import DeviceGateway
from home_server.src.g_bridge import GBridge


class IotGateway:
    running = True

    def __init__(self):
        device_list = ["light_switch_001"]

        self.device_gateway = DeviceGateway()
        self.device_gateway.start()
        self.g_bridge = GBridge(device_list)

        self.run()

    def __del__(self):
        del self.g_bridge
        self.device_gateway.join()

    def run(self):
        while self.running:
            self.device_to_cloud_communication()
            self.cloud_to_device_communication()
            time.sleep(1)

    def device_to_cloud_communication(self):
        # Take oldest message from device_gateway gueue and poss it to the Gbridge
        message = self.device_gateway.get_last_message()
        if message is not None:
            device = message[0]
            data = "light_state: " + message[1]
            event = message[2]
            self.g_bridge.publish_data(device, event, data)

    def cloud_to_device_communication(self):
        message = self.g_bridge.get_last_message()
        if message is not None:
            json_key = 'light_state'
            json_string = message[1]
            device = message[0]
            data = decode_json(json_string, json_key)
            if data is not None:
                self.device_gateway.publish_control_message(device, data)


def decode_json(json_string, key):
    try:
        data = json.loads(json_string)
        if key in data:
            return data[key]
        else:
            return None
    except ValueError as e:
        return None


if __name__ == '__main__':
    iotGateway = IotGateway()