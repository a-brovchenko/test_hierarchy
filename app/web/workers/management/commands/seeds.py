from faker import Faker
from workers.models import Workers
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        fake = Faker()

        boss = Workers.objects.create(
            name=fake.name(),
            position='CEO',
            email=fake.email(),
            employment_date=fake.date_this_decade(),
        )
        workers_num = 10

        for i in range(1, workers_num):
            # random choice parent
            if i == 1:
                parent = boss
            else:
                descendants = parent.get_descendants(include_self=True)
                parent = Workers.objects.filter(id__in=descendants).order_by('?').first()

            # Create employee with specified parent
            employee = Workers.objects.create(
                name=fake.name(),
                position=fake.job()[0:20],
                email=fake.email(),
                employment_date=fake.date_this_decade(),
                parent=parent
            )

        # boss = Workers.objects.create(name=fake.name(), position='CEO', email=fake.email(), employment_date=fake.date_this_decade(),)

        # for i in range(3):
        #     child = Workers.objects.create(name=fake.name(), position=fake.job()[0:20], email=fake.email(), employment_date=fake.date_this_decade(), parent=boss)

        #     for j in range(3):
        #         child_child = Workers.objects.create(name=fake.name(), position=fake.job()[0:20], email=fake.email(), employment_date=fake.date_this_decade(), parent=child)

        #         for k in range(3):
        #             child_child_child = Workers.objects.create(name=fake.name(), position=fake.job()[0:20], email=fake.email(), employment_date=fake.date_this_decade(), parent=child_child)