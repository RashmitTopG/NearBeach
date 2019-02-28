# Generated by Django 2.1.5 on 2019-02-27 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NearBeach', '0009_permission_set_request_for_change'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request_for_change',
            old_name='request_for_change_id',
            new_name='rfc_id',
        ),
        migrations.RenameField(
            model_name='request_for_change',
            old_name='request_for_change_impact',
            new_name='rfc_impact',
        ),
        migrations.RenameField(
            model_name='request_for_change',
            old_name='request_for_change_implementation_end_date',
            new_name='rfc_implementation_end_date',
        ),
        migrations.RenameField(
            model_name='request_for_change',
            old_name='request_for_change_implementation_release_date',
            new_name='rfc_implementation_release_date',
        ),
        migrations.RenameField(
            model_name='request_for_change',
            old_name='request_for_change_implementation_start_date',
            new_name='rfc_implementation_start_date',
        ),
        migrations.RenameField(
            model_name='request_for_change',
            old_name='request_for_change_priority',
            new_name='rfc_priority',
        ),
        migrations.RenameField(
            model_name='request_for_change',
            old_name='request_for_change_risk',
            new_name='rfc_risk',
        ),
        migrations.RenameField(
            model_name='request_for_change',
            old_name='request_for_change_status',
            new_name='rfc_status',
        ),
        migrations.RenameField(
            model_name='request_for_change',
            old_name='request_for_change_title',
            new_name='rfc_title',
        ),
        migrations.RenameField(
            model_name='request_for_change',
            old_name='request_for_change_type',
            new_name='rfc_type',
        ),
        migrations.RenameField(
            model_name='request_for_change',
            old_name='request_for_change_version_number',
            new_name='rfc_version_number',
        ),
        migrations.RemoveField(
            model_name='request_for_change',
            name='request_for_change_backout_plan',
        ),
        migrations.RemoveField(
            model_name='request_for_change',
            name='request_for_change_implementation_plan',
        ),
        migrations.RemoveField(
            model_name='request_for_change',
            name='request_for_change_lead',
        ),
        migrations.RemoveField(
            model_name='request_for_change',
            name='request_for_change_risk_and_impact_analysis',
        ),
        migrations.RemoveField(
            model_name='request_for_change',
            name='request_for_change_summary',
        ),
        migrations.RemoveField(
            model_name='request_for_change',
            name='request_for_change_test_plan',
        ),
        migrations.AddField(
            model_name='request_for_change',
            name='rfc_backout_plan',
            field=tinymce.models.HTMLField(default='', verbose_name='rfc_backout_plan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request_for_change',
            name='rfc_implementation_plan',
            field=tinymce.models.HTMLField(default='', verbose_name='rfc_implementation_plan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request_for_change',
            name='rfc_lead',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='rfc_lead', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request_for_change',
            name='rfc_risk_and_impact_analysis',
            field=tinymce.models.HTMLField(default='', verbose_name='rfc_risk_and_impact_analysis'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request_for_change',
            name='rfc_summary',
            field=tinymce.models.HTMLField(default='', verbose_name='rfc_summary'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request_for_change',
            name='rfc_test_plan',
            field=tinymce.models.HTMLField(default='', verbose_name='rfc_test_plan'),
            preserve_default=False,
        ),
    ]
