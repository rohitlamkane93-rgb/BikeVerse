import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bikeverseproject.settings")
django.setup()

from bikeverse.models import Bike


bajaj_specs = {

    "Bajaj Pulsar 220F": {
        "price": "₹1.40 Lakh",
        "engine": "220 cc",
        "mileage": "40 kmpl",
        "power": "20.4 PS",
        "torque": "18.55 Nm",
        "top_speed": "134 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Powerful, comfortable | Cons: Older design",
    },

    "Platina 100": {
        "price": "₹65,000",
        "engine": "102 cc",
        "mileage": "70 kmpl",
        "power": "7.9 PS",
        "torque": "8.3 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.2/5 | Pros: Excellent mileage, comfortable | Cons: Low power",
    },

    "Platina 110": {
        "price": "₹70,000",
        "engine": "115.45 cc",
        "mileage": "70 kmpl",
        "power": "8.6 PS",
        "torque": "9.81 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Disc/Drum Brakes with ABS",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Mileage, comfort | Cons: Basic performance",
    },

    "CT 100": {
        "price": "₹60,000",
        "engine": "102 cc",
        "mileage": "75 kmpl",
        "power": "7.9 PS",
        "torque": "8.34 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.1/5 | Pros: Excellent mileage, affordable | Cons: Basic features",
    },

    "CT 110": {
        "price": "₹70,000",
        "engine": "115 cc",
        "mileage": "70 kmpl",
        "power": "8.48 PS",
        "torque": "9.81 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.2/5 | Pros: Mileage, rugged | Cons: Low performance",
    },

    "Pulsar 125": {
        "price": "₹90,000",
        "engine": "124.4 cc",
        "mileage": "51 kmpl",
        "power": "11.8 PS",
        "torque": "10.8 Nm",
        "top_speed": "105 km/h",
        "brakes_abs": "Disc/Drum Brakes",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Sporty, efficient | Cons: Limited highway performance",
    },

    "Pulsar 150": {
        "price": "₹1.12 Lakh",
        "engine": "149.5 cc",
        "mileage": "47 kmpl",
        "power": "14 PS",
        "torque": "13.6 Nm",
        "top_speed": "110 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Reliable, sporty | Cons: Older platform",
    },

    "Pulsar 160 NS": {
        "price": "₹1.25 Lakh",
        "engine": "160.3 cc",
        "mileage": "52 kmpl",
        "power": "17.2 PS",
        "torque": "14.6 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Performance, handling | Cons: Firm ride",
    },

    "Pulsar N160": {
        "price": "₹1.23 Lakh",
        "engine": "164.82 cc",
        "mileage": "51 kmpl",
        "power": "16 PS",
        "torque": "14.65 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Smooth engine, handling | Cons: Moderate power",
    },

    "Pulsar NS160": {
        "price": "₹1.25 Lakh",
        "engine": "160.3 cc",
        "mileage": "52 kmpl",
        "power": "17.2 PS",
        "torque": "14.6 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Sporty, powerful | Cons: Firm suspension",
    },

    "Pulsar NS200": {
        "price": "₹1.59 Lakh",
        "engine": "199.5 cc",
        "mileage": "40 kmpl",
        "power": "24.5 PS",
        "torque": "18.74 Nm",
        "top_speed": "136 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Powerful, sporty | Cons: Vibrations at high rpm",
    },

    "Pulsar N250": {
        "price": "₹1.51 Lakh",
        "engine": "249.07 cc",
        "mileage": "39 kmpl",
        "power": "24.5 PS",
        "torque": "21.5 Nm",
        "top_speed": "132 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Strong torque, comfortable | Cons: Heavy",
    },

    "Pulsar NS400Z": {
        "price": "₹1.86 Lakh",
        "engine": "373 cc",
        "mileage": "34 kmpl",
        "power": "40 PS",
        "torque": "35 Nm",
        "top_speed": "174 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Excellent performance, features | Cons: Firm ride",
    },

    "Pulsar RS200": {
        "price": "₹1.75 Lakh",
        "engine": "199.5 cc",
        "mileage": "35 kmpl",
        "power": "24.5 PS",
        "torque": "18.7 Nm",
        "top_speed": "140 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Sporty design, performance | Cons: Aggressive riding position",
    },

    "Dominar 250": {
        "price": "₹1.85 Lakh",
        "engine": "248.77 cc",
        "mileage": "32 kmpl",
        "power": "27 PS",
        "torque": "23.5 Nm",
        "top_speed": "132 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Touring comfort, performance | Cons: Heavy",
    },

    "Dominar 400": {
        "price": "₹2.40 Lakh",
        "engine": "373.3 cc",
        "mileage": "30 kmpl",
        "power": "40 PS",
        "torque": "35 Nm",
        "top_speed": "148 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Excellent touring bike, powerful | Cons: Heavy",
    },

    "Avenger 160 Street": {
        "price": "₹1.20 Lakh",
        "engine": "160 cc",
        "mileage": "45 kmpl",
        "power": "15 PS",
        "torque": "13.7 Nm",
        "top_speed": "105 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Comfortable cruiser | Cons: Limited performance",
    },

    "Avenger 220 Cruise": {
        "price": "₹1.50 Lakh",
        "engine": "220 cc",
        "mileage": "40 kmpl",
        "power": "19 PS",
        "torque": "17.55 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Cruiser comfort, styling | Cons: Low ground clearance",
    },

    "Freedom 125": {
        "price": "₹90,000",
        "engine": "125 cc CNG + Petrol",
        "mileage": "102 km/kg (CNG)",
        "power": "9.5 PS",
        "torque": "9.7 Nm",
        "top_speed": "93 km/h",
        "brakes_abs": "Disc/Drum Brakes",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Very economical, CNG option | Cons: Limited CNG availability",
    },

    "Chetak 3501": {
        "price": "₹2.00 Lakh",
        "engine": "Electric",
        "mileage": "153 km range",
        "power": "Electric Motor",
        "torque": "Not specified",
        "top_speed": "73 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Premium design, good range | Cons: Charging time",
    },

    "Chetak 3502": {
        "price": "₹1.50 Lakh",
        "engine": "Electric",
        "mileage": "153 km range",
        "power": "Electric Motor",
        "torque": "Not specified",
        "top_speed": "73 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Comfortable, practical | Cons: Charging infrastructure",
    },

    "Pulsar RS400": {
        "price": "₹2.20 Lakh",
        "engine": "373 cc",
        "mileage": "30 kmpl",
        "power": "40 PS",
        "torque": "35 Nm",
        "top_speed": "170 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Sporty, powerful | Cons: Premium price",
    },

    "Pulsar N400": {
        "price": "₹2.00 Lakh",
        "engine": "373 cc",
        "mileage": "32 kmpl",
        "power": "40 PS",
        "torque": "35 Nm",
        "top_speed": "170 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Strong performance, sporty | Cons: Heavy",
    },

    "Pulsar 250": {
        "price": "₹1.51 Lakh",
        "engine": "249 cc",
        "mileage": "39 kmpl",
        "power": "24.5 PS",
        "torque": "21.5 Nm",
        "top_speed": "132 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Performance, comfort | Cons: Moderate top speed",
    },

    "Pulsar NS250": {
        "price": "₹1.60 Lakh",
        "engine": "249 cc",
        "mileage": "38 kmpl",
        "power": "24.5 PS",
        "torque": "21.5 Nm",
        "top_speed": "140 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Sporty, powerful | Cons: Firm ride",
    },

    "Dominar 450": {
        "price": "₹2.60 Lakh",
        "engine": "450 cc",
        "mileage": "28 kmpl",
        "power": "45 PS",
        "torque": "40 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Touring, powerful | Cons: Heavy",
    },

    "Avenger 400": {
        "price": "₹2.20 Lakh",
        "engine": "373 cc",
        "mileage": "30 kmpl",
        "power": "40 PS",
        "torque": "35 Nm",
        "top_speed": "145 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Cruiser styling, power | Cons: Heavy",
    },

    "Pulsar 400 GT": {
        "price": "₹2.50 Lakh",
        "engine": "373 cc",
        "mileage": "30 kmpl",
        "power": "40 PS",
        "torque": "35 Nm",
        "top_speed": "170 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Sporty touring, powerful | Cons: Premium price",
    },

    "Pulsar 400 SS": {
        "price": "₹2.50 Lakh",
        "engine": "373 cc",
        "mileage": "30 kmpl",
        "power": "40 PS",
        "torque": "35 Nm",
        "top_speed": "170 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Sportbike styling, performance | Cons: Aggressive riding position",
    },

    "Bajaj GT 400": {
        "price": "₹2.40 Lakh",
        "engine": "373 cc",
        "mileage": "30 kmpl",
        "power": "40 PS",
        "torque": "35 Nm",
        "top_speed": "165 km/h",
        "brakes_abs": "Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Performance, sporty design | Cons: Heavy",
    },
}


for bike_name, specs in bajaj_specs.items():

    try:
        bike = Bike.objects.get(name=bike_name)

        for field, value in specs.items():
            setattr(bike, field, value)

        bike.save()

        print(f"✅ {bike_name} updated successfully!")

    except Bike.DoesNotExist:
        print(f"❌ {bike_name} not found in database.")


print("\n🏍️ All Bajaj bike information updated!")