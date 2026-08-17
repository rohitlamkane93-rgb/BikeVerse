import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bikeverseproject.settings")
django.setup()

from bikeverse.models import Bike


ktm_specs = {

    "KTM Duke": {
        "price": "₹1.80 Lakh",
        "engine": "200 cc",
        "mileage": "35 kmpl",
        "power": "25 PS",
        "torque": "19.3 Nm",
        "top_speed": "135 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Performance, handling | Cons: Firm ride",
    },

    "125 Duke": {
        "price": "₹1.80 Lakh",
        "engine": "124.7 cc",
        "mileage": "40 kmpl",
        "power": "15 PS",
        "torque": "11.5 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Lightweight, sporty | Cons: Expensive for 125cc",
    },

    "160 Duke": {
        "price": "₹1.80 Lakh",
        "engine": "160 cc",
        "mileage": "40 kmpl",
        "power": "19 PS",
        "torque": "15 Nm",
        "top_speed": "125 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Agile handling | Cons: Limited touring comfort",
    },

    "200 Duke": {
        "price": "₹2.05 Lakh",
        "engine": "199.5 cc",
        "mileage": "35 kmpl",
        "power": "25 PS",
        "torque": "19.3 Nm",
        "top_speed": "135 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Strong performance, handling | Cons: Firm suspension",
    },

    "250 Duke": {
        "price": "₹2.45 Lakh",
        "engine": "249 cc",
        "mileage": "32 kmpl",
        "power": "31 PS",
        "torque": "25 Nm",
        "top_speed": "150 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Performance, features | Cons: Premium price",
    },

    "390 Duke": {
        "price": "₹2.95 Lakh",
        "engine": "399 cc",
        "mileage": "28 kmpl",
        "power": "46 PS",
        "torque": "39 Nm",
        "top_speed": "167 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Excellent performance, electronics | Cons: Firm ride",
    },

    "790 Duke": {
        "price": "₹8.50 Lakh",
        "engine": "799 cc",
        "mileage": "20 kmpl",
        "power": "105 PS",
        "torque": "86 Nm",
        "top_speed": "220 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Powerful twin-cylinder engine | Cons: Expensive",
    },

    "890 Duke R": {
        "price": "₹14.00 Lakh",
        "engine": "889 cc",
        "mileage": "18 kmpl",
        "power": "121 PS",
        "torque": "99 Nm",
        "top_speed": "240 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Track performance, premium brakes | Cons: Very expensive",
    },

    "1290 Super Duke R": {
        "price": "₹18.50 Lakh",
        "engine": "1301 cc",
        "mileage": "15 kmpl",
        "power": "180 PS",
        "torque": "140 Nm",
        "top_speed": "250 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.9/5 | Pros: Extreme performance | Cons: Very expensive",
    },

    "RC 125": {
        "price": "₹1.90 Lakh",
        "engine": "124.7 cc",
        "mileage": "38 kmpl",
        "power": "15 PS",
        "torque": "12 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Sporty design, handling | Cons: Riding position",
    },

    "RC 200": {
        "price": "₹2.18 Lakh",
        "engine": "199.5 cc",
        "mileage": "35 kmpl",
        "power": "25 PS",
        "torque": "19.2 Nm",
        "top_speed": "140 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Performance, sharp handling | Cons: Aggressive riding position",
    },

    "RC 390": {
        "price": "₹3.21 Lakh",
        "engine": "373 cc",
        "mileage": "25 kmpl",
        "power": "43 PS",
        "torque": "37 Nm",
        "top_speed": "170 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Performance, electronics | Cons: Firm ride",
    },

    "RC 8C": {
        "price": "₹35.00 Lakh",
        "engine": "889 cc",
        "mileage": "Not applicable",
        "power": "128 PS",
        "torque": "101 Nm",
        "top_speed": "260 km/h",
        "brakes_abs": "Race-spec braking system",
        "pros_cons_rating": "Rating: 4.9/5 | Pros: Track-focused performance | Cons: Very expensive",
    },

    "Adventure 250": {
        "price": "₹2.50 Lakh",
        "engine": "248.8 cc",
        "mileage": "30 kmpl",
        "power": "30 PS",
        "torque": "24 Nm",
        "top_speed": "140 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Adventure capability, comfort | Cons: Heavy",
    },

    "Adventure 390": {
        "price": "₹3.40 Lakh",
        "engine": "373 cc",
        "mileage": "28 kmpl",
        "power": "43 PS",
        "torque": "37 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Off-road ability, performance | Cons: Expensive",
    },

    "Adventure 390 X": {
        "price": "₹2.90 Lakh",
        "engine": "373 cc",
        "mileage": "28 kmpl",
        "power": "43 PS",
        "torque": "37 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Adventure touring | Cons: Fewer premium features",
    },

    "890 Adventure": {
        "price": "₹14.00 Lakh",
        "engine": "889 cc",
        "mileage": "20 kmpl",
        "power": "105 PS",
        "torque": "100 Nm",
        "top_speed": "210 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Excellent adventure performance | Cons: Expensive",
    },

    "1290 Super Adventure": {
        "price": "₹22.00 Lakh",
        "engine": "1301 cc",
        "mileage": "15 kmpl",
        "power": "160 PS",
        "torque": "138 Nm",
        "top_speed": "250 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Long-distance adventure, power | Cons: Very heavy and expensive",
    },

    "450 Rally": {
        "price": "₹12.00 Lakh",
        "engine": "450 cc",
        "mileage": "20 kmpl",
        "power": "70 PS",
        "torque": "45 Nm",
        "top_speed": "170 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Rally performance, off-road ability | Cons: Expensive",
    },

    "500 EXC": {
        "price": "₹12.50 Lakh",
        "engine": "510.9 cc",
        "mileage": "18 kmpl",
        "power": "45 PS",
        "torque": "40 Nm",
        "top_speed": "150 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Off-road capability | Cons: Expensive",
    },

    "690 Enduro R": {
        "price": "₹12.00 Lakh",
        "engine": "692.7 cc",
        "mileage": "22 kmpl",
        "power": "74 PS",
        "torque": "73.5 Nm",
        "top_speed": "180 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Powerful off-road performance | Cons: Expensive",
    },

    "990 Duke": {
        "price": "₹18.00 Lakh",
        "engine": "947 cc",
        "mileage": "18 kmpl",
        "power": "123 PS",
        "torque": "103 Nm",
        "top_speed": "230 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Powerful engine, aggressive handling | Cons: Premium price",
    },

    "1390 Super Duke R": {
        "price": "₹22.00 Lakh",
        "engine": "1350 cc",
        "mileage": "15 kmpl",
        "power": "190 PS",
        "torque": "145 Nm",
        "top_speed": "280 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.9/5 | Pros: Extreme performance | Cons: Very expensive",
    },

    "390 Adventure R": {
        "price": "₹3.40 Lakh",
        "engine": "399 cc",
        "mileage": "28 kmpl",
        "power": "46 PS",
        "torque": "39 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Off-road ability, performance | Cons: Premium price",
    },

    "250 Adventure": {
        "price": "₹2.60 Lakh",
        "engine": "249 cc",
        "mileage": "30 kmpl",
        "power": "30 PS",
        "torque": "25 Nm",
        "top_speed": "140 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Touring, manageable size | Cons: Moderate power",
    },

    "RC 390 GP": {
        "price": "₹3.50 Lakh",
        "engine": "373 cc",
        "mileage": "25 kmpl",
        "power": "43 PS",
        "torque": "37 Nm",
        "top_speed": "170 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Sporty performance, racing style | Cons: Aggressive ergonomics",
    },

    "450 SMR": {
        "price": "₹12.00 Lakh",
        "engine": "449.9 cc",
        "mileage": "18 kmpl",
        "power": "63 PS",
        "torque": "44 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Supermoto handling, performance | Cons: Expensive",
    },

    "350 EXC-F": {
        "price": "₹11.50 Lakh",
        "engine": "349.7 cc",
        "mileage": "20 kmpl",
        "power": "45 PS",
        "torque": "35 Nm",
        "top_speed": "145 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Lightweight, off-road performance | Cons: Expensive",
    },

    "500 EXC-F": {
        "price": "₹12.50 Lakh",
        "engine": "510.9 cc",
        "mileage": "18 kmpl",
        "power": "45 PS",
        "torque": "40 Nm",
        "top_speed": "150 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Strong off-road performance | Cons: Expensive",
    },

    "690 SMC R": {
        "price": "₹13.00 Lakh",
        "engine": "692.7 cc",
        "mileage": "22 kmpl",
        "power": "74 PS",
        "torque": "73.5 Nm",
        "top_speed": "180 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Supermoto performance, lightweight | Cons: Expensive",
    },
}


for bike_name, specs in ktm_specs.items():

    try:
        bike = Bike.objects.get(name=bike_name)

        for field, value in specs.items():
            setattr(bike, field, value)

        bike.save()

        print(f"✅ {bike_name} updated successfully!")

    except Bike.DoesNotExist:
        print(f"❌ {bike_name} not found in database.")


print("\n🏍️ All KTM bike information updated!")