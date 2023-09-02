python manage.py makemigrations
python manage.py migrate
from app_advertisements.models import Advertisement
adv1 = Advertisement(title = "Заголовок1",description = "Описание1",price = 100,auction = True)
adv1.save()
python manage.py runserver


@admin.display(description="дата создания")
def created_date(self):
    from django.utils import timezone
    from django.utils.html import format_html
    if self.created_at.date() == timezone.now().date():
        created_time = self.created_at.time().strfine("%H:%M:%S")
        return format_html('<span style="color: blue, font-weith: bold">Сегодня в {}</span>', created_time)
    return self.created_at.time().strfine("%H:%M:%S")


@admin.display(description="дата обновления")
def updated_date(self):
    from django.utils import timezone
    from django.utils.html import format_html
    if self.updated_at.date() == timezone.now().date():
        updated_time = self.updated_at.time().strfine("%H:%M:%S")
        return format_html('<span style="color: green, font-weith: bold">Сегодня в {}</span>', updated_time)
    return self.updated_at.time().strfine("%H:%M:%S")