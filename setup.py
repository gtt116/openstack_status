import setuptools


requires = [
    'django',
    'python-novaclient',
    'south',
]


setuptools.setup(
    name='openstack_status',
    version='0.0.0',
    url='https://github.com/gtt116/openstack_status/',
    license='Apache 2.0',
    description="openstack status",
    author='gtt116',
    author_email='gtt116@gmali.com',
    packages=setuptools.find_packages(),
    install_requires=requires,
    include_package_data=True,
    py_modules=[],
)
