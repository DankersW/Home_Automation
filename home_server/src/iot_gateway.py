from src.device_gateway import DeviceGateway
#from src.g_bridge import GBridge


class IotGateway:
    def __init__(self):
        device_list = ["light_switch_001"]
        # start listing for connected devices
        device_gateway = DeviceGateway()
        #g_bridge = GBridge(device_list)


if __name__ == '__main__':
    iotGateway = IotGateway()
