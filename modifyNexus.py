import pynetbox
import pprint


NETBOX_URL = "http://127.0.0.1:8000/"
NETBOX_TOKEN = "c7f629dc647e859d43bdb37831d36eff7501b11a"
SDNET_MANAGEMENT_INTERFACE = "mgmtsdnet"
MEGACABLE_TENANT = "megacable"

targetDeviceType = "cisco-n9k-c9508"
targetDeviceIp = "10.0.20.2/24"
targetDeviceName = "Nexusc9508-test3"
targetModuleType = "N9K-X97160YC-EX"
slotTarget = "Slot 1"
targetSite = "Site1"
targetRole = "Agregacion"


nb = pynetbox.api(NETBOX_URL, token=NETBOX_TOKEN)


targetDevice = nb.dcim.devices.get(name="Nexusc9508-test3")

print(targetDevice.name)
print(targetDevice.id)

targetDevice.serial = "abc123"
targetDevice.save()


