# Generated by Django 3.1.7 on 2021-03-12 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0001_initial'),
        ('cmp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='u_c',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmp_proveedor_creation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='u_m',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmp_proveedor_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comprasenc',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.proveedor'),
        ),
        migrations.AddField(
            model_name='comprasenc',
            name='u_c',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmp_comprasenc_creation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comprasenc',
            name='u_m',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmp_comprasenc_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comprasdet',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.comprasenc'),
        ),
        migrations.AddField(
            model_name='comprasdet',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.producto'),
        ),
        migrations.AddField(
            model_name='comprasdet',
            name='u_c',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmp_comprasdet_creation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comprasdet',
            name='u_m',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmp_comprasdet_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
