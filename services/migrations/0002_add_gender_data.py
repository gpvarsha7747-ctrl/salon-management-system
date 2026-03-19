from django.db import migrations

def create_genders(apps, schema_editor):
    Gender = apps.get_model('services', 'Gender')

    if not Gender.objects.filter(name='male').exists():
        Gender.objects.create(name='male')

    if not Gender.objects.filter(name='female').exists():
        Gender.objects.create(name='female')


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_genders),
    ]