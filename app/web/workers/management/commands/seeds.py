from faker import Faker
from workers.models import Workers
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
    numb = 3

    def handle(self, *args, **options):
        fake = Faker()

        # boss = Workers.objects.create(
        #     name=fake.name(),
        #     position='CEO',
        #     email=fake.email(),
        #     employment_date=fake.date_this_decade(),
        # )
        # workers_num = 50

        # for i in range(1, workers_num):
        #     # random choice parent
        #     if i == 1:
        #         parent = boss
        #     else:
        #         descendants = parent.get_descendants(include_self=True)
        #         parent = Workers.objects.filter(id__in=descendants).order_by('?').first()

        #     # Create employee with specified parent
        #     employee = Workers.objects.create(
        #         name=fake.name(),
        #         position=fake.job()[0:20],
        #         email=fake.email(),
        #         employment_date=fake.date_this_decade(),
        #         parent=parent
        #     )

        boss = Workers.objects.create(name=fake.name(), position='CEO', email=fake.email(), employment_date=fake.date_this_decade(),)

        for q in range(self.numb):
            child_1 = Workers.objects.create(name=fake.name(), position=fake.job()[0:20], email=fake.email(), employment_date=fake.date_this_decade(), parent=boss)

            for w in range(self.numb):
                child_2 = Workers.objects.create(name=fake.name(), position=fake.job()[0:20], email=fake.email(), employment_date=fake.date_this_decade(), parent=child_1)

                for e in range(self.numb):
                    child_3 = Workers.objects.create(name=fake.name(), position=fake.job()[0:20], email=fake.email(), employment_date=fake.date_this_decade(), parent=child_2)    

                    for r in range(self.numb):
                        child_4 = Workers.objects.create(name=fake.name(), position=fake.job()[0:20], email=fake.email(), employment_date=fake.date_this_decade(), parent=child_3)  

                        for t in range(self.numb):
                            child_5 = Workers.objects.create(name=fake.name(), position=fake.job()[0:20], email=fake.email(), employment_date=fake.date_this_decade(), parent=child_4)  

                            for y in range(self.numb):
                                child_6 = Workers.objects.create(name=fake.name(), position=fake.job()[0:20], email=fake.email(), employment_date=fake.date_this_decade(), parent=child_5)
                                
                                for u in range(self.numb):
                                    child_7 = Workers.objects.create(name=fake.name(), position=fake.job()[0:20], email=fake.email(), employment_date=fake.date_this_decade(), parent=child_6)