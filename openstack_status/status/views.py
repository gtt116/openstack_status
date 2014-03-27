from django.shortcuts import render_to_response

from openstack_status.status import models
from openstack_status import checkers


def overall(request):
    results = []
    for checker in checkers.all_checker_names():
        x = models.CheckResult.objects.\
                filter(check_name=checker).\
                order_by('-updated_at').\
                first()
        results.append(x)

    aggregate = models.CheckAggregation.objects.\
            order_by('-updated_at').\
            first()
    return render_to_response('overall.html', {'results': results,
                                               'aggregate': aggregate})
