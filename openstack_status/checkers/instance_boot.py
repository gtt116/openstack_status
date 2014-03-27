import time

from openstack_status.checkers import opsclient
from openstack_status.checkers import base


image_id = 'c720fee1-91de-4a81-a066-34d3ec1dbdec'
flavor_id = '1'


class InstanceBoot(base.CheckerBase, opsclient.NovaMixin):
    name = 'Instance Boot'
    timeout = 20

    def _prepare(self):
        self.novaclient

    def _run(self):
        image = self.novaclient.images.get(image_id)
        flavor = self.novaclient.flavors.get(flavor_id)
        vm = self.novaclient.servers.create('openstack_status',
                                            image,
                                            flavor)
        print 'Booting instance with image: %s, flavor: %s' % (image, flavor)
        while True:
            vm.get()
            if vm.status == 'ACTIVE':
                break
            time.sleep(0.01)

        vm.delete()
