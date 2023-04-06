# python3 manage.py createsuperuser
# python3 manage.py dumpdata -o fixtures/data_dump.json
# python3 manage.py shell
from main.models import *

u1 = User.objects.create(name="u1", surname="s1")
u2 = User.objects.create(name="u2", surname="s2")
u3 = User.objects.create(name="u3", surname="s3")

n1 = Note.objects.create(title="n1", body="b1")
n2 = Note.objects.create(title="n2", body="b2")
n3 = Note.objects.create(title="n3", body="b3")
n4 = Note.objects.create(title="n4", body="b4")
n5 = Note.objects.create(title="n5", body="b5")

a1 = Achievement.objects.create(title="a1", reasons="rrer")
a2 = Achievement.objects.create(title="a2", reasons="rrer")
a3 = Achievement.objects.create(title="a3", reasons="rrer")
a4 = Achievement.objects.create(title="a4", reasons="rrer")
a5 = Achievement.objects.create(title="a5", reasons="rrer")
a6 = Achievement.objects.create(title="a6", reasons="rrer")

ad1 = Ad.objects.create(title="ad1", description="I am an ad", url="ad.com")
ad2 = Ad.objects.create(title="ad2", description="I am an ad", url="ad.com")
ad3 = Ad.objects.create(title="ad3", description="I am an ad", url="ad.com")
ad4 = Ad.objects.create(title="ad4", description="I am an ad", url="ad.com")


u1.add_event(n1)
u1.add_event(n2)
u1.add_event(n3)
u1.add_event(a1)
u1.add_event(a2)
u1.add_event(a3)
u1.add_event(a4)

u2.add_event(n4)
u2.add_event(n5)
u2.add_event(a5)
u2.add_event(a6)

u1.events.all()
