# Generated by Django 3.0.5 on 2020-05-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0048_taskstate_finished_by'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='workflowstate',
            name='unique_in_progress_workflow',
        ),
        migrations.AlterField(
            model_name='workflowstate',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In progress'), ('approved', 'Approved'), ('needs_changes', 'Needs changes'), ('cancelled', 'Cancelled')], default='in_progress', max_length=50, verbose_name='status'),
        ),
        migrations.AddConstraint(
            model_name='workflowstate',
            constraint=models.UniqueConstraint(condition=models.Q(('status', 'in_progress'), ('status', 'needs_changes'), _connector='OR'), fields=('page',), name='unique_in_progress_workflow'),
        ),
    ]
