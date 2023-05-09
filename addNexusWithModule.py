import pynetbox
import pprint


NETBOX_URL = "http://127.0.0.1:8000/"
NETBOX_TOKEN = "c7f629dc647e859d43bdb37831d36eff7501b11a"
SDNET_MANAGEMENT_INTERFACE = "mgmtsdnet"
MEGACABLE_TENANT = "megacable"

targetDeviceType = "cisco-n9k-c9508"
targetDeviceIp = "10.0.20.3/24"
targetDeviceName = "Nexusc9508-test4"
targetModuleType = "N9K-X97160YC-EX"
slotTarget = "Slot 1"
targetSite = "Site1"
targetRole = "Agregacion"


nb = pynetbox.api(NETBOX_URL, token=NETBOX_TOKEN)



#ips = list(nb.ipam.ip_addresses.all())
print("aqui")
#for Mipv4 in ips:
#    print(Mipv4.address)
#    print(Mipv4.id)

#nb.ipam.ip_addresses.delete(ips)

#devices = list(nb.dcim.devices.all())
#nb.dcim.devices.delete(devices)



#sites = list(nb.dcim.sites.all())
#print("aqui")
#for site in sites:
#    print(site.name)
#    print(site.id)

device = nb.dcim.devices.create(
    name=targetDeviceName,
    site=nb.dcim.sites.get(name=targetSite).id,
    device_type=nb.dcim.device_types.get(slug=targetDeviceType).id,
    device_role=nb.dcim.device_roles.get(name=targetRole).id,
    serial = "chasisSN12367576",
    status='active',
    )

interfaceSdnet = nb.dcim.interfaces.get(
    name=SDNET_MANAGEMENT_INTERFACE, device=targetDeviceName)

interfaceSdnet.custom_fields["SFP"] = "10Gbase-SR"
interfaceSdnet.save()


ipDevice = nb.ipam.ip_addresses.create(
    address=targetDeviceIp,
    status="active"
)


# assign IP Address to device's network interface
ipDevice.assigned_object = interfaceSdnet
ipDevice.assigned_object_id = interfaceSdnet.id
ipDevice.assigned_object_type = 'dcim.interface'
ipDevice.save()

device.primary_ip4 = ipDevice
device.save()



moduleTypeTarget = nb.dcim.module_types.get(model=targetModuleType)
moduleBayTarget = nb.dcim.module_bays.get(name=slotTarget, device_id=device.id)

module = nb.dcim.modules.create(
    device = device.id,
    module_type=moduleTypeTarget.id,
    module_bay = moduleBayTarget.id,
    serial = "moduleSN12311234123"
)

interfaceEth1 = nb.dcim.interfaces.get(name="Ethernet1/1", device=targetDeviceName)
interfaceEth1.custom_fields["SFP"] = "10Gbase-SR"
interfaceEth1.save()

devices = list(nb.dcim.devices.all())
for device in devices:
    print(device.name)
    print(device.id)


