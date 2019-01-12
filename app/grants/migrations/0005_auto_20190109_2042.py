# Generated by Django 2.1.4 on 2019-01-09 20:42

import logging
from django.db import migrations
from grants.models import Grant

logger = logging.getLogger(__name__)

def add_monthly_amount_subscribed(apps, schema_editor):
    for grant in Grant.objects.all().values('subscriptions', 'monthly_amount_subscribed'):
        subscriptions = grant.subscriptions.all()
        for subscription in subscriptions:
            if subscription.active and subscription.num_tx_approved > 1:
                try:
                    grant.monthly_amount_subscribed += subscription.get_converted_monthly_amount()
                    grant.save()

                except Exception as e:
                    logger.info(e)

def backwards(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0004_merge_20190108_2135'),
    ]

    operations = [
            migrations.RunPython(add_monthly_amount_subscribed, backwards),
    ]
