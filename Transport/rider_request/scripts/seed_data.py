# سكريبت لإضافة بيانات تجريبية للأحياء وأيام الأسبوع
# شغله عبر: python manage.py shell < Transport/rider_request/scripts/seed_data.py

from rider_request.models import Neighborhood
from main.models import City, Day
from main.models import City

# إضافة أحياء تجريبية
city_neighborhoods = {
    "Riyadh": [
        "Olaya", "Malaz", "Nakheel", "Sahafa", "Rawdah", "Morooj", "Suwaidi",
        "King Fahd", "Al Yasmin", "Al Waha", "Al Munsiyah", "Al Shifa", "Al Rabwa", "Al Sulimaniyah", "Al Nahda", "Al Uraija", "Al Qirawan",
    "Al Mughrizat", "Al Manar", "Al Shuhada", "Al Yarmouk", "Al Falah", "Al Quds", "Al Mursalat", "Al Wizarat", "Al Batha", "Al Diriyah", "Al Urayriyah"
    ],
    "Jeddah": [
        "Al Hamra", "Al Rawdah", "Al Shati", "Al Salamah", "Al Safa", "Al Naeem", "Al Faisaliyah",
        "Al Mohammadiyah", "Al Basateen", "Al Zahraa", "Al Andalus", "Al Ruwais", "Al Bawadi", "Al Samer", "Al Marwah", "Al Naseem", "Al Aziziyah", "Al Rehab", "Al Hamdaniyah",
        "Al Rabwa", "Al Nuzha", "Al Mushrifah", "Al Hindawiyah", "Al Baghdadiyah", "Al Balad", "Al Jamiah", "Al Safa 2", "Al Safa 3", "Al Safa 4"
    ],
    "Dammam": [
        "Al Faisaliyah", "Al Shati", "Al Mazruiyah", "Al Badiyah", "Al Khalij", "Al Rakah", "Al Anoud", "Al Shulah", "Al Rayyan",
        "Al Jamiyin", "Al Manar", "Al Tubaishi", "Al Adamah", "Al Shati Al Gharbi", "Al Firdaws", "Al Nakheel", "Al Rayan", "Al Khalidiyah", "Al Shulah Al Jadidah"
    ],
    "Al Khobar": [
        "Al Thuqbah", "Al Rakah", "Al Aziziyah", "Al Quds", "Al Shamalia", "Al Corniche", "Al Rawabi", "Al Aqrabiyah", "Al Bandariyah",
        "Al Jawhara", "Al Khuzama", "Al Dhahran", "Al Firdaws", "Al Salam", "Al Yarmouk", "Al Taawun", "Al Nahda", "Al Shatea", "Al Qiblah"
    ]
}
for city_name, neighborhoods in city_neighborhoods.items():
    city, _ = City.objects.get_or_create(name=city_name)
    for n_name in neighborhoods:
        Neighborhood.objects.get_or_create(name=n_name, city=city)

days = [
    ("Sunday", "sun"),
    ("Monday", "mon"),
    ("Tuesday", "tue"),
    ("Wednesday", "wed"),
    ("Thursday", "thu"),
    ("Friday", "fri"),
    ("Saturday", "sat"),
]
for name, code in days:
    Day.objects.get_or_create(name=name, code=code)

print("Neighborhoods and days of week added in English!")
