import phonenumbers
from phonenumbers import carrier,geocoder,timezone
n = ("+8801627704636")
a = phonenumbers.parse(n)
c = carrier.name_for_number(a,"en")
g = geocoder.description_for_number(a, "en")
t = timezone.time_zones_for_number(a)
print(c)
print(g)
print(t)