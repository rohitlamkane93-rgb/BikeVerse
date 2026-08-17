import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bikeverseproject.settings")
django.setup()

from bikeverse.models import Bike


yamaha_specs = {

    "Yamaha MT-15 v2": {
        "price": "₹1.70 Lakh",
        "engine": "155 cc",
        "mileage": "48 kmpl",
        "power": "18.4 PS",
        "torque": "14.1 Nm",
        "top_speed": "130 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Sporty design, performance | Cons: Firm ride",
    },

    "FZ-FI": {
        "price": "₹1.18 Lakh",
        "engine": "149 cc",
        "mileage": "49 kmpl",
        "power": "12.4 PS",
        "torque": "13.3 Nm",
        "top_speed": "115 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Comfortable, reliable | Cons: Moderate power",
    },

    "FZS-FI": {
        "price": "₹1.22 Lakh",
        "engine": "149 cc",
        "mileage": "49 kmpl",
        "power": "12.4 PS",
        "torque": "13.3 Nm",
        "top_speed": "115 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Styling, comfort | Cons: Moderate performance",
    },

    "FZ-X": {
        "price": "₹1.38 Lakh",
        "engine": "149 cc",
        "mileage": "48 kmpl",
        "power": "12.4 PS",
        "torque": "13.3 Nm",
        "top_speed": "115 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Retro styling, comfort | Cons: Low power",
    },

    "FZ-S Hybrid": {
        "price": "₹1.45 Lakh",
        "engine": "149 cc",
        "mileage": "55 kmpl",
        "power": "12.4 PS",
        "torque": "13.3 Nm",
        "top_speed": "115 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Hybrid efficiency, features | Cons: Moderate performance",
    },

    "MT-15": {
        "price": "₹1.70 Lakh",
        "engine": "155 cc",
        "mileage": "48 kmpl",
        "power": "18.4 PS",
        "torque": "14.1 Nm",
        "top_speed": "130 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Performance, handling | Cons: Compact seat",
    },

    "MT-15 V2": {
        "price": "₹1.70 - ₹1.75 Lakh",
        "engine": "155 cc",
        "mileage": "48 kmpl",
        "power": "18.4 PS",
        "torque": "14.1 Nm",
        "top_speed": "130 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Aggressive design, performance | Cons: Firm suspension",
    },

    "R15 V4": {
        "price": "₹1.83 - ₹2.10 Lakh",
        "engine": "155 cc",
        "mileage": "47 kmpl",
        "power": "18.4 PS",
        "torque": "14.2 Nm",
        "top_speed": "140 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Sporty performance, handling | Cons: Riding position",
    },

    "R15M": {
        "price": "₹2.00 Lakh",
        "engine": "155 cc",
        "mileage": "45 kmpl",
        "power": "18.4 PS",
        "torque": "14.2 Nm",
        "top_speed": "140 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Premium features, performance | Cons: Expensive",
    },

    "R3": {
        "price": "₹4.65 Lakh",
        "engine": "321 cc",
        "mileage": "25 kmpl",
        "power": "42 PS",
        "torque": "29.6 Nm",
        "top_speed": "190 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Smooth twin-cylinder engine | Cons: Premium price",
    },

    "R7": {
        "price": "₹10.80 Lakh",
        "engine": "689 cc",
        "mileage": "20 kmpl",
        "power": "73.4 PS",
        "torque": "67 Nm",
        "top_speed": "230 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Strong performance, lightweight | Cons: Expensive",
    },

    "R1": {
        "price": "₹20.39 Lakh",
        "engine": "998 cc",
        "mileage": "15 kmpl",
        "power": "200 PS",
        "torque": "113 Nm",
        "top_speed": "299 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Extreme performance | Cons: Very expensive",
    },

    "R1M": {
        "price": "₹22.50 Lakh",
        "engine": "998 cc",
        "mileage": "15 kmpl",
        "power": "200 PS",
        "torque": "113 Nm",
        "top_speed": "299 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.9/5 | Pros: Track performance, premium electronics | Cons: Very expensive",
    },

    "Fascino 125": {
        "price": "₹79,900 - ₹92,000",
        "engine": "125 cc",
        "mileage": "50 kmpl",
        "power": "8.2 PS",
        "torque": "10.3 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Drum/Disc Brakes",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Stylish, practical | Cons: Limited performance",
    },

    "RayZR 125": {
        "price": "₹85,000 - ₹95,000",
        "engine": "125 cc",
        "mileage": "49 kmpl",
        "power": "8.2 PS",
        "torque": "10.3 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Drum/Disc Brakes",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Lightweight, mileage | Cons: Small storage",
    },

    "RayZR Street Rally": {
        "price": "₹92,000",
        "engine": "125 cc",
        "mileage": "49 kmpl",
        "power": "8.2 PS",
        "torque": "10.3 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Disc/Drum Brakes",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Sporty styling, lightweight | Cons: Basic equipment",
    },

    "Aerox 155": {
        "price": "₹1.50 Lakh",
        "engine": "155 cc",
        "mileage": "40 kmpl",
        "power": "15 PS",
        "torque": "13.9 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Performance, sporty design | Cons: Premium scooter",
    },

    "XSR155": {
        "price": "₹1.40 Lakh",
        "engine": "155 cc",
        "mileage": "45 kmpl",
        "power": "19 PS",
        "torque": "14.7 Nm",
        "top_speed": "135 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Retro design, performance | Cons: Limited availability",
    },

    "Tenere 700": {
        "price": "₹12.00 Lakh",
        "engine": "689 cc",
        "mileage": "22 kmpl",
        "power": "73.4 PS",
        "torque": "68 Nm",
        "top_speed": "200 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Excellent adventure ability | Cons: Expensive",
    },

    "Tracer 9": {
        "price": "₹12.00 Lakh",
        "engine": "890 cc",
        "mileage": "20 kmpl",
        "power": "119 PS",
        "torque": "93 Nm",
        "top_speed": "230 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Touring comfort, powerful engine | Cons: Expensive",
    },

    "MT-09": {
        "price": "₹12.00 Lakh",
        "engine": "890 cc",
        "mileage": "20 kmpl",
        "power": "119 PS",
        "torque": "93 Nm",
        "top_speed": "240 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Powerful engine, agile handling | Cons: Premium price",
    },

    "MT-07": {
        "price": "₹8.00 Lakh",
        "engine": "689 cc",
        "mileage": "24 kmpl",
        "power": "73.4 PS",
        "torque": "67 Nm",
        "top_speed": "214 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Fun performance, lightweight | Cons: Limited features",
    },

    "MT-10": {
        "price": "₹16.00 Lakh",
        "engine": "998 cc",
        "mileage": "18 kmpl",
        "power": "166 PS",
        "torque": "112 Nm",
        "top_speed": "250 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Superbike performance | Cons: Expensive",
    },

    "R6": {
        "price": "₹15.00 Lakh",
        "engine": "599 cc",
        "mileage": "18 kmpl",
        "power": "117 PS",
        "torque": "61.7 Nm",
        "top_speed": "260 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Track performance, handling | Cons: Not practical for daily use",
    },

    "R9": {
        "price": "₹12.00 Lakh",
        "engine": "890 cc",
        "mileage": "20 kmpl",
        "power": "119 PS",
        "torque": "93 Nm",
        "top_speed": "240 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Sport performance, electronics | Cons: Premium price",
    },

    "Tracer 7": {
        "price": "₹9.50 Lakh",
        "engine": "689 cc",
        "mileage": "23 kmpl",
        "power": "73.4 PS",
        "torque": "67 Nm",
        "top_speed": "210 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Touring comfort, versatile | Cons: Expensive",
    },

    "YZF-R125": {
        "price": "₹5.00 Lakh",
        "engine": "125 cc",
        "mileage": "45 kmpl",
        "power": "15 PS",
        "torque": "11.5 Nm",
        "top_speed": "130 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Sporty design, handling | Cons: Small engine",
    },

    "YZF-R1": {
        "price": "₹20.39 Lakh",
        "engine": "998 cc",
        "mileage": "15 kmpl",
        "power": "200 PS",
        "torque": "113 Nm",
        "top_speed": "299 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Extreme performance | Cons: Very expensive",
    },

    "YZF-R1M": {
        "price": "₹22.50 Lakh",
        "engine": "998 cc",
        "mileage": "15 kmpl",
        "power": "200 PS",
        "torque": "113 Nm",
        "top_speed": "299 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.9/5 | Pros: Track-focused performance | Cons: Very expensive",
    },

    "XSR700": {
        "price": "₹8.50 Lakh",
        "engine": "689 cc",
        "mileage": "23 kmpl",
        "power": "73.4 PS",
        "torque": "67 Nm",
        "top_speed": "200 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Retro styling, performance | Cons: Premium price",
    },
}


for bike_name, specs in yamaha_specs.items():

    try:
        bike = Bike.objects.get(name=bike_name)

        for field, value in specs.items():
            setattr(bike, field, value)

        bike.save()

        print(f"✅ {bike_name} updated successfully!")

    except Bike.DoesNotExist:
        print(f"❌ {bike_name} not found in database.")


print("\n🏍️ All Yamaha bike information updated!")