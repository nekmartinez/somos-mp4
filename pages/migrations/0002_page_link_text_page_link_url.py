from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='link_text',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Texto del enlace'),
        ),
        migrations.AddField(
            model_name='page',
            name='link_url',
            field=models.URLField(blank=True, null=True, verbose_name='Enlace (opcional)'),
        ),
    ]
