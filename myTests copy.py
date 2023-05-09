import pynetbox


NETBOX_URL = "http://127.0.0.1:8000/"
NETBOX_TOKEN = "a6f36aa90e0ff46c19c011a8bfec942ba62d6b02"
nb = pynetbox.api(NETBOX_URL, token=NETBOX_TOKEN)






device = nb.dcim.devices.create(
    name='r3',
    site=nb.dcim.sites.get(name='Site1').id,
    device_type=nb.dcim.device_types.get(slug='cisco-asr-9006').id,
    device_role=nb.dcim.device_roles.get(name="role1").id,
    status='active',
    )



devices = list(nb.dcim.devices.all())
for device in devices:
    print(device.name)
    print(device.id)


