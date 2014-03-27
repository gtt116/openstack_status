from django.db import models

# Create your models here.

check_result_status = ['init', 'running', 'finished']


class CheckResult(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    elapse = models.FloatField(null=False)
    check_name = models.CharField(max_length=50, null=False, db_index=True)
    check_path = models.CharField(max_length=50, null=False, db_index=True)
    status = models.CharField(max_length=10)
    failed = models.BooleanField(default=False)
    exception = models.CharField(max_length=255, null=True)

    def __repr__(self):
        return "%s.%s" % (self.check_name, self.status)


check_aggregation_status = ['green', 'yellow', 'red']


class CheckAggregation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10)
    description = models.CharField(max_length=255)

    def __repr__(self):
        return "%s: %s" % (self.updated_at, self.status)
