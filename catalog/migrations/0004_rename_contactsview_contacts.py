# Generated by Django 5.0.4 on 2024-07-17 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_contactsview_remove_product_manufactured_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactsView',
            new_name='Contacts',
        ),
    ]