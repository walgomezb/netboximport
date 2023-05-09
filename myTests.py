import pynetbox
import pprint


NETBOX_URL = "http://127.0.0.1:8000/"
NETBOX_TOKEN = "a6f36aa90e0ff46c19c011a8bfec942ba62d6b02"
nb = pynetbox.api(NETBOX_URL, token=NETBOX_TOKEN)

ips = list(nb.ipam.ip_addresses.all())
print("aqui")
for Mipv4 in ips:
    print(Mipv4.address)
    print(Mipv4.id)

nb.ipam.ip_addresses.delete(ips)

devices = list(nb.dcim.devices.all())
nb.dcim.devices.delete(devices)

ipDevice = nb.ipam.ip_addresses.create(
    address="10.0.10.1/24",
    status="active"
)

#sites = list(nb.dcim.sites.all())
#print("aqui")
#for site in sites:
#    print(site.name)
#    print(site.id)

device = nb.dcim.devices.create(
    name='r3',
    site=nb.dcim.sites.get(name='Site1').id,
    device_type=nb.dcim.device_types.get(slug='cisco-asr-9006').id,
    device_role=nb.dcim.device_roles.get(name="role1").id,
    status='active',
   
    )

moduleBayTarget = nb.dcim.module_bays.get(name = "Slot 0", device_id = device.id)
moduleTypeTarget = nb.dcim.module_types.get(model="A9K-RSP440-SE")



module = nb.dcim.modules.create(
    device = device.id,
    module_type=moduleTypeTarget.id,
    module_bay = moduleBayTarget.id

)

devices = list(nb.dcim.devices.all())
for device in devices:
    print(device.name)
    print(device.id)


