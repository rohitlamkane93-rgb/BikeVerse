import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bikeverseproject.settings")
django.setup()

from bikeverse.models import Bike


tvs_specs = {

    "TVS Apache RTR 160 4v": {
        "price": "₹1.25 Lakh",
        "engine": "159.7 cc",
        "mileage": "45 kmpl",
        "power": "17.55 PS",
        "torque": "14.73 Nm",
        "top_speed": "114 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Sporty, good performance | Cons: Firm ride",
    },

    "Sport": {
        "price": "₹1.10 Lakh",
        "engine": "109.7 cc",
        "mileage": "50 kmpl",
        "power": "8.08 PS",
        "torque": "8.7 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.1/5 | Pros: Simple, economical | Cons: Basic features",
    },

    "Radeon": {
        "price": "₹75,000",
        "engine": "109.7 cc",
        "mileage": "65 kmpl",
        "power": "8.19 PS",
        "torque": "8.7 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.2/5 | Pros: Excellent mileage, comfortable | Cons: Low power",
    },

    "Star City Plus": {
        "price": "₹75,000",
        "engine": "109.7 cc",
        "mileage": "68 kmpl",
        "power": "8.08 PS",
        "torque": "8.7 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.2/5 | Pros: Mileage, comfort | Cons: Basic performance",
    },

    "Raider 125": {
        "price": "₹85,000",
        "engine": "124.8 cc",
        "mileage": "56 kmpl",
        "power": "11.38 PS",
        "torque": "11.2 Nm",
        "top_speed": "99 km/h",
        "brakes_abs": "Disc/Drum Brakes",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Sporty design, mileage | Cons: Limited highway power",
    },

    "Raider iGO": {
        "price": "₹1.00 Lakh",
        "engine": "124.8 cc",
        "mileage": "55 kmpl",
        "power": "11.38 PS",
        "torque": "11.75 Nm",
        "top_speed": "100 km/h",
        "brakes_abs": "Disc/Drum Brakes",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Performance, features | Cons: Premium price",
    },

    "Apache RTR 160": {
        "price": "₹1.20 Lakh",
        "engine": "159.7 cc",
        "mileage": "45 kmpl",
        "power": "16.04 PS",
        "torque": "13.85 Nm",
        "top_speed": "114 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Performance, handling | Cons: Firm ride",
    },

    "Apache RTR 160 4V": {
        "price": "₹1.25 Lakh",
        "engine": "159.7 cc",
        "mileage": "45 kmpl",
        "power": "17.55 PS",
        "torque": "14.73 Nm",
        "top_speed": "114 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Performance, features | Cons: Vibrations at high rpm",
    },

    "Apache RTR 180": {
        "price": "₹1.35 Lakh",
        "engine": "177.4 cc",
        "mileage": "45 kmpl",
        "power": "17.02 PS",
        "torque": "15.5 Nm",
        "top_speed": "114 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Good performance | Cons: Older platform",
    },

    "Apache RTR 200 4V": {
        "price": "₹1.48 Lakh",
        "engine": "197.75 cc",
        "mileage": "40 kmpl",
        "power": "20.8 PS",
        "torque": "17.25 Nm",
        "top_speed": "127 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Powerful, sporty | Cons: Firm suspension",
    },

    "Apache RTR 310": {
        "price": "₹2.50 Lakh",
        "engine": "312.12 cc",
        "mileage": "30 kmpl",
        "power": "35.6 PS",
        "torque": "28.7 Nm",
        "top_speed": "150 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Performance, electronics | Cons: Premium price",
    },

    "Apache RR 310": {
        "price": "₹2.80 Lakh",
        "engine": "312.12 cc",
        "mileage": "30 kmpl",
        "power": "38 PS",
        "torque": "29 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Sportbike performance | Cons: Aggressive riding position",
    },

    "Ronin": {
        "price": "₹1.35 Lakh",
        "engine": "225.9 cc",
        "mileage": "42 kmpl",
        "power": "20.4 PS",
        "torque": "19.93 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Comfortable, unique styling | Cons: Moderate performance",
    },

    "Ronin 225": {
        "price": "₹1.35 Lakh",
        "engine": "225.9 cc",
        "mileage": "42 kmpl",
        "power": "20.4 PS",
        "torque": "19.93 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Comfortable, stylish | Cons: Limited highway performance",
    },

    "Xtreme 125": {
        "price": "₹95,000",
        "engine": "124.7 cc",
        "mileage": "55 kmpl",
        "power": "11.55 PS",
        "torque": "10.5 Nm",
        "top_speed": "100 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Sporty, efficient | Cons: Moderate power",
    },

    "NTORQ 125": {
        "price": "₹85,000",
        "engine": "124.8 cc",
        "mileage": "45 kmpl",
        "power": "10.2 PS",
        "torque": "10.8 Nm",
        "top_speed": "95 km/h",
        "brakes_abs": "Drum/Disc Brakes",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Features, sporty | Cons: Mileage varies",
    },

    "Jupiter 125": {
        "price": "₹90,000",
        "engine": "124.8 cc",
        "mileage": "50 kmpl",
        "power": "8.2 PS",
        "torque": "10.5 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Disc/Drum Brakes",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Practical, comfortable | Cons: Moderate performance",
    },

    "Scooty Pep Plus": {
        "price": "₹70,000",
        "engine": "87.8 cc",
        "mileage": "50 kmpl",
        "power": "5.4 PS",
        "torque": "6.5 Nm",
        "top_speed": "65 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.2/5 | Pros: Lightweight, easy to ride | Cons: Low power",
    },

    "Zest 110": {
        "price": "₹75,000",
        "engine": "109.7 cc",
        "mileage": "45 kmpl",
        "power": "7.8 PS",
        "torque": "8.8 Nm",
        "top_speed": "80 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.2/5 | Pros: Lightweight, practical | Cons: Basic features",
    },

    "iQube": {
        "price": "₹1.00 Lakh",
        "engine": "Electric",
        "mileage": "Up to 150 km range",
        "power": "Electric Motor",
        "torque": "140 Nm",
        "top_speed": "82 km/h",
        "brakes_abs": "Disc/Drum Brakes",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Electric, quiet, practical | Cons: Charging time",
    },

    "XLS 100": {
        "price": "₹70,000",
        "engine": "100 cc",
        "mileage": "60 kmpl",
        "power": "8 PS",
        "torque": "8.5 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.1/5 | Pros: Mileage, simple | Cons: Basic features",
    },

    "Apache RTX": {
        "price": "₹2.50 Lakh",
        "engine": "299 cc",
        "mileage": "30 kmpl",
        "power": "35 PS",
        "torque": "28 Nm",
        "top_speed": "145 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Adventure styling, performance | Cons: Premium price",
    },

    "Apache RTR 200 Racing": {
        "price": "₹1.55 Lakh",
        "engine": "197.75 cc",
        "mileage": "40 kmpl",
        "power": "20.8 PS",
        "torque": "17.25 Nm",
        "top_speed": "127 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Racing styling, performance | Cons: Firm ride",
    },

    "Apache RR 310 GP": {
        "price": "₹3.00 Lakh",
        "engine": "312.12 cc",
        "mileage": "30 kmpl",
        "power": "38 PS",
        "torque": "29 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Sporty performance, premium design | Cons: Expensive",
    },

    "Apache RTR 310 Racing": {
        "price": "₹2.70 Lakh",
        "engine": "312.12 cc",
        "mileage": "30 kmpl",
        "power": "35.6 PS",
        "torque": "28.7 Nm",
        "top_speed": "150 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Sporty, advanced electronics | Cons: Premium price",
    },

    "Raider 150": {
        "price": "₹1.10 Lakh",
        "engine": "149 cc",
        "mileage": "50 kmpl",
        "power": "15 PS",
        "torque": "13 Nm",
        "top_speed": "115 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Sporty performance | Cons: Limited availability",
    },

    "Radeon 125": {
        "price": "₹80,000",
        "engine": "125 cc",
        "mileage": "55 kmpl",
        "power": "10 PS",
        "torque": "10 Nm",
        "top_speed": "95 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.2/5 | Pros: Mileage, comfort | Cons: Moderate performance",
    },

    "Victor 125": {
        "price": "₹80,000",
        "engine": "125 cc",
        "mileage": "55 kmpl",
        "power": "10 PS",
        "torque": "10 Nm",
        "top_speed": "95 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.1/5 | Pros: Practical, economical | Cons: Older model",
    },

    "Star City 125": {
        "price": "₹80,000",
        "engine": "125 cc",
        "mileage": "60 kmpl",
        "power": "10 PS",
        "torque": "10 Nm",
        "top_speed": "95 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.2/5 | Pros: Mileage, comfort | Cons: Basic features",
    },

    "Fiero 125": {
        "price": "₹90,000",
        "engine": "125 cc",
        "mileage": "55 kmpl",
        "power": "11 PS",
        "torque": "10.5 Nm",
        "top_speed": "100 km/h",
        "brakes_abs": "Disc/Drum Brakes",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Good balance, practical | Cons: Moderate performance",
    },
}


for bike_name, specs in tvs_specs.items():

    try:
        bike = Bike.objects.get(name=bike_name)

        for field, value in specs.items():
            setattr(bike, field, value)

        bike.save()

        print(f"✅ {bike_name} updated successfully!")

    except Bike.DoesNotExist:
        print(f"❌ {bike_name} not found in database.")


print("\n🏍️ All TVS bike information updated!")