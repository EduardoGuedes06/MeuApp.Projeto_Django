# Generated by Django 3.2.7 on 2022-07-08 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0012_vagaofertada_createdby_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagaofertada',
            name='createdBy_user',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]