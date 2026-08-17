import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bikeverseproject.settings")
django.setup()

from bikeverse.models import Bike


honda_specs = {

    "Shine 125": {
        "price": "₹83,251 - ₹87,251",
        "engine": "123.94 cc",
        "mileage": "55 kmpl",
        "power": "10.74 PS",
        "torque": "11 Nm",
        "top_speed": "100 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Good mileage, comfortable | Cons: Basic features",
    },

    "SP 125": {
        "price": "₹91,771 - ₹1.00 Lakh",
        "engine": "123.94 cc",
        "mileage": "60 kmpl",
        "power": "10.87 PS",
        "torque": "10.9 Nm",
        "top_speed": "100 km/h",
        "brakes_abs": "Disc/Drum",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Mileage, refined engine | Cons: Limited premium features",
    },

    "SP 160": {
        "price": "₹1.18 - ₹1.23 Lakh",
        "engine": "162.71 cc",
        "mileage": "48 kmpl",
        "power": "13.46 PS",
        "torque": "14.8 Nm",
        "top_speed": "110 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Performance, styling | Cons: Competition is strong",
    },

    "Hornet 2.0": {
        "price": "₹1.59 Lakh",
        "engine": "184.4 cc",
        "mileage": "42 kmpl",
        "power": "17.26 PS",
        "torque": "15.9 Nm",
        "top_speed": "130 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Sporty design, performance | Cons: Mileage can vary",
    },

    "NX200": {
        "price": "₹1.68 Lakh",
        "engine": "184.4 cc",
        "mileage": "40 kmpl",
        "power": "17.26 PS",
        "torque": "15.9 Nm",
        "top_speed": "127 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Adventure styling, comfort | Cons: Moderate power",
    },

    "CB200X": {
        "price": "₹1.47 Lakh",
        "engine": "184.4 cc",
        "mileage": "40 kmpl",
        "power": "17.26 PS",
        "torque": "15.9 Nm",
        "top_speed": "127 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Touring comfort, design | Cons: Not a hardcore off-roader",
    },

    "CB300F": {
        "price": "₹1.70 - ₹1.75 Lakh",
        "engine": "293.52 cc",
        "mileage": "30 kmpl",
        "power": "24.5 PS",
        "torque": "25.6 Nm",
        "top_speed": "150 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Strong engine, features | Cons: Firm ride",
    },

    "CB300R": {
        "price": "₹2.40 Lakh",
        "engine": "286 cc",
        "mileage": "30 kmpl",
        "power": "31 PS",
        "torque": "27.5 Nm",
        "top_speed": "150 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Lightweight, performance | Cons: Premium price",
    },

    "Hness CB350": {
        "price": "₹2.15 - ₹2.18 Lakh",
        "engine": "348.36 cc",
        "mileage": "35 kmpl",
        "power": "21.07 PS",
        "torque": "30 Nm",
        "top_speed": "125 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Comfortable, refined engine | Cons: Heavy",
    },

    "CB350": {
        "price": "₹2.00 - ₹2.18 Lakh",
        "engine": "348.36 cc",
        "mileage": "35 kmpl",
        "power": "21.07 PS",
        "torque": "30 Nm",
        "top_speed": "125 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Classic design, comfort | Cons: Weight",
    },

    "CB350RS": {
        "price": "₹2.15 - ₹2.18 Lakh",
        "engine": "348.36 cc",
        "mileage": "35 kmpl",
        "power": "21.07 PS",
        "torque": "30 Nm",
        "top_speed": "125 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Scrambler styling, comfort | Cons: Limited off-road ability",
    },

    "CB350C": {
        "price": "₹2.00 Lakh",
        "engine": "348.36 cc",
        "mileage": "35 kmpl",
        "power": "21.07 PS",
        "torque": "30 Nm",
        "top_speed": "125 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Cruiser styling, comfort | Cons: Heavy",
    },

    "CBR650R": {
        "price": "₹9.99 Lakh",
        "engine": "649 cc",
        "mileage": "20 kmpl",
        "power": "95 PS",
        "torque": "63 Nm",
        "top_speed": "240 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Powerful four-cylinder engine | Cons: Expensive",
    },

    "Africa Twin": {
        "price": "₹15.96 Lakh",
        "engine": "1084 cc",
        "mileage": "20 kmpl",
        "power": "99 PS",
        "torque": "112 Nm",
        "top_speed": "200 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Adventure capability, powerful engine | Cons: Expensive and heavy",
    },

    "Gold Wing": {
        "price": "₹39.20 Lakh",
        "engine": "1833 cc",
        "mileage": "14 kmpl",
        "power": "126 PS",
        "torque": "170 Nm",
        "top_speed": "180 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Luxury touring, comfort | Cons: Very expensive and heavy",
    },

    "Livo": {
        "price": "₹83,000 - ₹87,000",
        "engine": "109.51 cc",
        "mileage": "60 kmpl",
        "power": "8.79 PS",
        "torque": "9.30 Nm",
        "top_speed": "90 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.2/5 | Pros: Mileage, easy handling | Cons: Basic features",
    },

    "CD 110 Dream": {
        "price": "₹73,400",
        "engine": "109.51 cc",
        "mileage": "65 kmpl",
        "power": "8.79 PS",
        "torque": "9.30 Nm",
        "top_speed": "86 km/h",
        "brakes_abs": "Drum Brakes",
        "pros_cons_rating": "Rating: 4.2/5 | Pros: Excellent mileage, affordable | Cons: Basic equipment",
    },

    "CB200X Adventure": {
        "price": "₹1.47 Lakh",
        "engine": "184.4 cc",
        "mileage": "40 kmpl",
        "power": "17.26 PS",
        "torque": "15.9 Nm",
        "top_speed": "127 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Touring ability, comfortable | Cons: Limited off-road performance",
    },

    "CBR500R": {
        "price": "₹4.99 Lakh",
        "engine": "471 cc",
        "mileage": "27 kmpl",
        "power": "47 PS",
        "torque": "43 Nm",
        "top_speed": "185 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Smooth twin-cylinder engine | Cons: Expensive",
    },

    "CBR1000RR-R": {
        "price": "₹23.11 Lakh",
        "engine": "999 cc",
        "mileage": "15 kmpl",
        "power": "217 PS",
        "torque": "113 Nm",
        "top_speed": "299 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Extreme performance | Cons: Very expensive",
    },

    "CB1000 Hornet": {
        "price": "₹15.00 Lakh",
        "engine": "999 cc",
        "mileage": "18 kmpl",
        "power": "152 PS",
        "torque": "104 Nm",
        "top_speed": "230 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Strong performance, aggressive design | Cons: Premium price",
    },

    "CB650R": {
        "price": "₹9.60 Lakh",
        "engine": "649 cc",
        "mileage": "20 kmpl",
        "power": "95 PS",
        "torque": "63 Nm",
        "top_speed": "210 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Four-cylinder engine, premium design | Cons: Expensive",
    },

    "NX500": {
        "price": "₹5.90 Lakh",
        "engine": "471 cc",
        "mileage": "28 kmpl",
        "power": "47 PS",
        "torque": "43 Nm",
        "top_speed": "180 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Adventure touring, comfort | Cons: Premium price",
    },

    "XL750 Transalp": {
        "price": "₹11.00 Lakh",
        "engine": "755 cc",
        "mileage": "24 kmpl",
        "power": "91 PS",
        "torque": "75 Nm",
        "top_speed": "195 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Adventure touring, powerful engine | Cons: Expensive",
    },

    "Rebel 500": {
        "price": "₹5.12 Lakh",
        "engine": "471 cc",
        "mileage": "26 kmpl",
        "power": "46.2 PS",
        "torque": "43.3 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Cruiser design, smooth engine | Cons: Expensive",
    },

    "CB500X": {
        "price": "₹5.80 Lakh",
        "engine": "471 cc",
        "mileage": "27 kmpl",
        "power": "47 PS",
        "torque": "43 Nm",
        "top_speed": "170 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Touring comfort, reliable engine | Cons: Premium price",
    },

    "CRF300L": {
        "price": "₹5.50 Lakh",
        "engine": "286 cc",
        "mileage": "30 kmpl",
        "power": "27.3 PS",
        "torque": "26.6 Nm",
        "top_speed": "145 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Off-road capability, lightweight | Cons: Limited availability",
    },

    "Unicorn": {
        "price": "₹1.10 Lakh",
        "engine": "162.7 cc",
        "mileage": "50 kmpl",
        "power": "12.91 PS",
        "torque": "14.58 Nm",
        "top_speed": "106 km/h",
        "brakes_abs": "Disc/Drum",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Comfort, reliability, mileage | Cons: Basic features",
    },
}


for bike_name, specs in honda_specs.items():

    try:
        bike = Bike.objects.get(name=bike_name)

        for field, value in specs.items():
            setattr(bike, field, value)

        bike.save()

        print(f"✅ {bike_name} updated successfully!")

    except Bike.DoesNotExist:
        print(f"❌ {bike_name} not found in database.")


print("\n🏍️ All Honda bike information updated!")