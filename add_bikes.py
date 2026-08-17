import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bikeverseproject.settings")
django.setup()

from bikeverse.models import Bike


# प्रत्येक brand साठी unique bikes
# Existing bikes delete होणार नाहीत.
brands = {

    "Hero": [
        "Splendor Plus",
        "Splendor Plus XTEC",
        "HF Deluxe",
        "HF 100",
        "Passion Plus",
        "Passion XTEC",
        "Glamour",
        "Glamour XTEC",
        "Super Splendor",
        "Super Splendor XTEC",
        "Xtreme 125R",
        "Xtreme 160R",
        "Xtreme 160R 4V",
        "Xtreme 250R",
        "Xpulse 125",
        "Xpulse 200 4V",
        "Xpulse 210",
        "Karizma XMR",
        "Mavrick 440",
        "Mavrick 440 Scrambler",
        "Xtreme 250R Pro",
        "Xtreme 160R Stealth",
        "Xpulse 200T",
        "Xpulse 200 Adventure",
        "Hero 450 Rally",
        "Hero GT 250",
        "Hero Xtreme GT",
        "Hero Street 160",
        "Hero Adventure 400",
        "Hero Racing 250",
    ],

    "Honda": [
        "Shine 100",
        "Shine 125",
        "SP 125",
        "SP 160",
        "Unicorn",
        "Hornet 2.0",
        "NX200",
        "CB200X",
        "CB300F",
        "CB300R",
        "Hness CB350",
        "CB350",
        "CB350RS",
        "CB350C",
        "CBR650R",
        "Africa Twin",
        "Gold Wing",
        "Livo",
        "CD 110 Dream",
        "CBR500R",
        "CBR1000RR-R",
        "CB1000 Hornet",
        "CB650R",
        "NX500",
        "XL750 Transalp",
        "Rebel 500",
        "CB500X",
        "CRF300L",
        "CBR250RR",
        "CBR600RR",
    ],

    "Yamaha": [
        "FZ-FI",
        "FZS-FI",
        "FZ-X",
        "FZ-S Hybrid",
        "MT-15",
        "MT-15 V2",
        "R15 V4",
        "R15M",
        "R3",
        "R7",
        "R1",
        "R1M",
        "Fascino 125",
        "RayZR 125",
        "RayZR Street Rally",
        "Aerox 155",
        "XSR155",
        "MT-09",
        "MT-07",
        "MT-10",
        "R6",
        "R9",
        "Tenere 700",
        "Tracer 9",
        "Tracer 7",
        "YZF-R125",
        "YZF-R1",
        "YZF-R1M",
        "XSR700",
        "XSR900",
    ],

    "KTM": [
        "125 Duke",
        "160 Duke",
        "200 Duke",
        "250 Duke",
        "390 Duke",
        "790 Duke",
        "890 Duke R",
        "1290 Super Duke R",
        "RC 125",
        "RC 200",
        "RC 390",
        "RC 8C",
        "Adventure 250",
        "Adventure 390",
        "Adventure 390 X",
        "890 Adventure",
        "1290 Super Adventure",
        "450 Rally",
        "500 EXC",
        "690 Enduro R",
        "990 Duke",
        "1390 Super Duke R",
        "390 Adventure R",
        "250 Adventure",
        "RC 390 GP",
        "450 SMR",
        "350 EXC-F",
        "500 EXC-F",
        "690 SMC R",
        "890 SMT",
    ],

    "Royal Enfield": [
        "Hunter 350",
        "Classic 350",
        "Bullet 350",
        "Meteor 350",
        "Goan Classic 350",
        "Himalayan 450",
        "Scram 411",
        "Scram 440",
        "Guerrilla 450",
        "Interceptor 650",
        "Continental GT 650",
        "Super Meteor 650",
        "Shotgun 650",
        "Bear 650",
        "Classic 650",
        "Bullet 650",
        "Himalayan 650",
        "Flying Flea C6",
        "Flying Flea S6",
        "650 Twin",
        "Interceptor 750",
        "Continental GT 750",
        "Himalayan 750",
        "Classic 500",
        "Thunderbird 350",
        "Thunderbird X",
        "Electra 350",
        "Machismo 500",
        "Bullet Trials 350",
        "Bullet Trials 500",
    ],

    "TVS": [
        "Sport",
        "Radeon",
        "Star City Plus",
        "Raider 125",
        "Raider iGO",
        "Apache RTR 160",
        "Apache RTR 160 4V",
        "Apache RTR 180",
        "Apache RTR 200 4V",
        "Apache RTR 310",
        "Apache RR 310",
        "Ronin",
        "Ronin 225",
        "NTORQ 125",
        "Jupiter 125",
        "Scooty Pep Plus",
        "Zest 110",
        "iQube",
        "Apache RTX",
        "Apache RTR 200 Racing",
        "Apache RR 310 GP",
        "Apache RTR 310 Racing",
        "Raider 150",
        "Radeon 125",
        "Victor 125",
        "Star City 125",
        "Fiero 125",
        "RTR 160 Racing",
        "RTR 200 Racing",
        "Ronin Scrambler",
    ],

    "Bajaj": [
        "Platina 100",
        "Platina 110",
        "CT 100",
        "CT 110",
        "Pulsar 125",
        "Pulsar 150",
        "Pulsar 160 NS",
        "Pulsar N160",
        "Pulsar NS160",
        "Pulsar NS200",
        "Pulsar N250",
        "Pulsar NS400Z",
        "Pulsar RS200",
        "Dominar 250",
        "Dominar 400",
        "Avenger 160 Street",
        "Avenger 220 Cruise",
        "Freedom 125",
        "Chetak 3501",
        "Chetak 3502",
        "Pulsar RS400",
        "Pulsar N400",
        "Pulsar 250",
        "Pulsar NS250",
        "Dominar 450",
        "Avenger 400",
        "Pulsar 400 GT",
        "Pulsar 400 SS",
        "Bajaj GT 400",
        "Bajaj Sports 400",
    ],
}


# Demo specifications
default_data = {
    "price": "₹1,00,000",
    "engine": "125 cc",
    "mileage": "45 km/l",
    "power": "11 PS",
    "torque": "11 Nm",
    "top_speed": "100 km/h",
    "brakes_abs": "Disc / ABS",
    "pros_cons_rating": (
        "Pros: Good performance and stylish design.\n"
        "Cons: Specifications may vary by variant.\n"
        "Rating: 4/5"
    ),
}


for brand, bike_names in brands.items():

    # Case-insensitive existing count.
    # त्यामुळे Hero आणि hero दोन्ही count होतील.
    existing = Bike.objects.filter(brand__iexact=brand).count()

    added = 0

    for bike_name in bike_names:

        # Duplicate name + same brand check
        already_exists = Bike.objects.filter(
            brand__iexact=brand,
            name__iexact=bike_name
        ).exists()

        if already_exists:
            continue

        # 30 पर्यंतच add करायच्या
        if existing + added >= 30:
            break

        Bike.objects.create(
            name=bike_name,
            brand=brand,
            **default_data
        )

        added += 1

    final_count = Bike.objects.filter(brand__iexact=brand).count()

    print(
        f"{brand}: {final_count} bikes "
        f"(newly added: {added})"
    )


print("\n✅ प्रत्येक brand ला 30 पर्यंत unique bikes complete!")
print("🏍️ Existing bikes delete केलेल्या नाहीत.")