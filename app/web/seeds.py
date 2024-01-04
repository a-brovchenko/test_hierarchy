from faker import Faker
from workers.models import Workers

fake = Faker()

# create CEO
ceo = Workers.objects.create(
    name=fake.name(),
    position='CEO',
    email=fake.email(),
    employment_date=fake.date_this_decade(),
)

workers_num = 200

# Create other workers
for i in range(1, workers_num):
    employee = Workers.objects.create(
        name=fake.name(),
        position=fake.job()[0:20],
        email=fake.email(),
        employment_date=fake.date_this_decade(),
    )

    # random choice parent
    if i == 1:
        parent = ceo
    else:
        descendants = employee.get_ancestors(include_self=True)
        parent = Workers.objects.exclude(id__in=descendants).order_by('?').first()

    # parent for worker
    employee.parent = parent
    employee.save()