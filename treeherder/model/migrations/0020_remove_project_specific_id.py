# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 22:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0019_remove_job_duration'),
    ]
    operations = [
        migrations.RunSQL(
            sql="""
ALTER TABLE `job` DROP INDEX `job_repository_id_project_specific_id_7883a5e8_uniq`;
            """,
            reverse_sql="""
CREATE UNIQUE INDEX `job_repository_id_project_specific_id_7883a5e8_uni` ON `job` (`repository_id`,`project_specific_id`);
            """,
            state_operations=[
                migrations.AlterUniqueTogether(
                    name='job',
                    unique_together=set([]),
                ),
            ]
        )
    ]
