# Generated by Django 4.1.7 on 2023-04-26 19:55

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationMenuSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_items', wagtail.fields.StreamField([('internal_page', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Поумолчанию используется имя страницы.', label='Изменить имя обычного меню', required=False)), ('page', wagtail.blocks.PageChooserBlock(label='Страница')), ('live', wagtail.blocks.BooleanBlock(default=False, help_text='Включение/отключение отображения категории меню', label='Скрыть меню', required=False)), ('anchor', wagtail.blocks.CharBlock(help_text='Для ссылки на определенные элементы страницы, введите текст привязки без символа «#».', label='Якорь', required=False))], default='[]')), ('external_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Имя внешней ссылки', required=True)), ('live', wagtail.blocks.BooleanBlock(default=False, help_text='Включение/отключение отображения меню', label='Скрыть меню', required=False)), ('url', wagtail.blocks.URLBlock(label='Внешняя ссылка')), ('anchor', wagtail.blocks.CharBlock(help_text='Для ссылки на определенные элементы страницы. Введите текст привязки без символа «#».', label='Якорь', required=False))], default='[]')), ('drop_down', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Имя выпадающего меню')), ('live', wagtail.blocks.BooleanBlock(default=False, help_text='Включение/отключение отображения выпадающего меню (субменю не будут отображаться)', label='Скрыть выпадающее меню', required=False)), ('menu_items', wagtail.blocks.StreamBlock([('page', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Поумолчанию используется имя страницы.', label='Изменить имя обычного меню', required=False)), ('page', wagtail.blocks.PageChooserBlock(label='Страница')), ('live', wagtail.blocks.BooleanBlock(default=False, help_text='Включение/отключение отображения категории меню', label='Скрыть меню', required=False)), ('anchor', wagtail.blocks.CharBlock(help_text='Для ссылки на определенные элементы страницы, введите текст привязки без символа «#».', label='Якорь', required=False))])), ('external_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Имя внешней ссылки', required=True)), ('live', wagtail.blocks.BooleanBlock(default=False, help_text='Включение/отключение отображения меню', label='Скрыть меню', required=False)), ('url', wagtail.blocks.URLBlock(label='Внешняя ссылка')), ('anchor', wagtail.blocks.CharBlock(help_text='Для ссылки на определенные элементы страницы. Введите текст привязки без символа «#».', label='Якорь', required=False))]))], collapsed=True, label='Добавить обычное меню или внешнюю ссылку'))], default='[]'))], blank=True, use_json_field=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Меню навигации',
            },
        ),
    ]
