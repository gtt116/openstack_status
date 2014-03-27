# Installation

    git clone git://github.com/gtt116/openstack_status
    cd openstack_status
    pip install .
    python manage.py syncdb

# start checker

    python openstack_status/checker/__init__.py

# start web
    
    python manage.py runserver
