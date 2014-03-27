from novaclient.v1_1 import client as novaclient

username = 'demo'
password = 'ntse'
tenant_name = 'demo'
keystone_url = 'http://localhost:5000/v2.0'


class NovaMixin(object):

    @property
    def novaclient(self):
        if not hasattr(self, '_novaclient'):
            self._novaclient = novaclient.Client(username,
                                                password,
                                                tenant_name,
                                                keystone_url,
                                                service_type='compute')
        return self._novaclient
