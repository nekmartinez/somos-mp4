from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.deletion.CASCADE, related_name='replies', to='messaging.comment'),
        ),
    ]
