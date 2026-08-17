import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bikeverseproject.settings")
django.setup()

from bikeverse.models import Bike


re_specs = {

    "Royal Enfield Standard 350": {
        "price": "₹1.93 Lakh",
        "engine": "349 cc",
        "mileage": "41 kmpl",
        "power": "20.2 PS",
        "torque": "27 Nm",
        "top_speed": "114 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Comfortable, classic design | Cons: Moderate performance",
    },

    "Hunter 350": {
        "price": "₹1.50 Lakh",
        "engine": "349 cc",
        "mileage": "36 kmpl",
        "power": "20.2 PS",
        "torque": "27 Nm",
        "top_speed": "114 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Compact, stylish | Cons: Firm ride",
    },

    "Classic 350": {
        "price": "₹1.95 Lakh",
        "engine": "349 cc",
        "mileage": "41 kmpl",
        "power": "20.2 PS",
        "torque": "27 Nm",
        "top_speed": "114 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Classic styling, comfort | Cons: Heavy",
    },

    "Bullet 350": {
        "price": "₹1.75 Lakh",
        "engine": "349 cc",
        "mileage": "37 kmpl",
        "power": "20.2 PS",
        "torque": "27 Nm",
        "top_speed": "110 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Classic design, road presence | Cons: Heavy",
    },

    "Meteor 350": {
        "price": "₹2.10 Lakh",
        "engine": "349 cc",
        "mileage": "41 kmpl",
        "power": "20.2 PS",
        "torque": "27 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Comfortable cruiser, touring | Cons: Heavy",
    },

    "Goan Classic 350": {
        "price": "₹2.35 Lakh",
        "engine": "349 cc",
        "mileage": "36 kmpl",
        "power": "20.2 PS",
        "torque": "27 Nm",
        "top_speed": "115 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Unique styling, comfort | Cons: Premium price",
    },

    "Himalayan 450": {
        "price": "₹2.85 Lakh",
        "engine": "452 cc",
        "mileage": "30 kmpl",
        "power": "40 PS",
        "torque": "40 Nm",
        "top_speed": "150 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Adventure capability, performance | Cons: Tall seat",
    },

    "Scram 411": {
        "price": "₹2.11 Lakh",
        "engine": "411 cc",
        "mileage": "29 kmpl",
        "power": "24.3 PS",
        "torque": "32 Nm",
        "top_speed": "140 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Comfortable, versatile | Cons: Heavy",
    },

    "Scram 440": {
        "price": "₹2.08 Lakh",
        "engine": "443 cc",
        "mileage": "30 kmpl",
        "power": "25.4 PS",
        "torque": "34 Nm",
        "top_speed": "140 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Adventure ability, torque | Cons: Heavy",
    },

    "Guerrilla 450": {
        "price": "₹2.39 Lakh",
        "engine": "452 cc",
        "mileage": "29 kmpl",
        "power": "40 PS",
        "torque": "40 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Powerful engine, handling | Cons: Firm ride",
    },

    "Interceptor 650": {
        "price": "₹3.03 Lakh",
        "engine": "648 cc",
        "mileage": "23 kmpl",
        "power": "47 PS",
        "torque": "52 Nm",
        "top_speed": "170 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Smooth twin-cylinder, touring | Cons: Heavy",
    },

    "Continental GT 650": {
        "price": "₹3.19 Lakh",
        "engine": "648 cc",
        "mileage": "23 kmpl",
        "power": "47 PS",
        "torque": "52 Nm",
        "top_speed": "170 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Café racer styling, performance | Cons: Aggressive riding position",
    },

    "Super Meteor 650": {
        "price": "₹3.64 Lakh",
        "engine": "648 cc",
        "mileage": "23 kmpl",
        "power": "47 PS",
        "torque": "52 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Cruiser comfort, powerful engine | Cons: Heavy",
    },

    "Shotgun 650": {
        "price": "₹3.60 Lakh",
        "engine": "648 cc",
        "mileage": "22 kmpl",
        "power": "47 PS",
        "torque": "52 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Custom styling, twin-cylinder | Cons: Heavy",
    },

    "Bear 650": {
        "price": "₹3.39 Lakh",
        "engine": "648 cc",
        "mileage": "23 kmpl",
        "power": "47 PS",
        "torque": "56.5 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Scrambler styling, torque | Cons: Heavy",
    },

    "Classic 650": {
        "price": "₹3.37 Lakh",
        "engine": "648 cc",
        "mileage": "23 kmpl",
        "power": "47 PS",
        "torque": "52 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Premium classic design, twin-cylinder | Cons: Heavy",
    },

    "Bullet 650": {
        "price": "₹3.40 Lakh",
        "engine": "648 cc",
        "mileage": "23 kmpl",
        "power": "47 PS",
        "torque": "52 Nm",
        "top_speed": "160 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.6/5 | Pros: Classic design, strong engine | Cons: Heavy",
    },

    "Himalayan 650": {
        "price": "₹4.50 Lakh",
        "engine": "648 cc",
        "mileage": "22 kmpl",
        "power": "47 PS",
        "torque": "52 Nm",
        "top_speed": "170 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Adventure touring, twin-cylinder | Cons: Heavy",
    },

    "Flying Flea C6": {
        "price": "₹3.00 Lakh",
        "engine": "Electric",
        "mileage": "150 km range",
        "power": "Electric Motor",
        "torque": "Not specified",
        "top_speed": "Not specified",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Electric, lightweight design | Cons: Range depends on riding",
    },

    "Flying Flea S6": {
        "price": "₹3.50 Lakh",
        "engine": "Electric",
        "mileage": "150 km range",
        "power": "Electric Motor",
        "torque": "Not specified",
        "top_speed": "Not specified",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.5/5 | Pros: Electric, modern design | Cons: Charging infrastructure",
    },

    "650 Twin": {
        "price": "₹3.00 Lakh",
        "engine": "648 cc",
        "mileage": "23 kmpl",
        "power": "47 PS",
        "torque": "52 Nm",
        "top_speed": "170 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Smooth twin-cylinder | Cons: Heavy",
    },

    "Interceptor 750": {
        "price": "₹4.50 Lakh",
        "engine": "750 cc",
        "mileage": "22 kmpl",
        "power": "60 PS",
        "torque": "65 Nm",
        "top_speed": "180 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Strong performance, touring | Cons: Heavy",
    },

    "Continental GT 750": {
        "price": "₹4.70 Lakh",
        "engine": "750 cc",
        "mileage": "21 kmpl",
        "power": "60 PS",
        "torque": "65 Nm",
        "top_speed": "185 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.7/5 | Pros: Café racer design, performance | Cons: Aggressive position",
    },

    "Himalayan 750": {
        "price": "₹5.00 Lakh",
        "engine": "750 cc",
        "mileage": "22 kmpl",
        "power": "60 PS",
        "torque": "65 Nm",
        "top_speed": "180 km/h",
        "brakes_abs": "Disc Brakes with Dual-Channel ABS",
        "pros_cons_rating": "Rating: 4.8/5 | Pros: Adventure touring, power | Cons: Heavy",
    },

    "Classic 500": {
        "price": "₹2.10 Lakh",
        "engine": "499 cc",
        "mileage": "32 kmpl",
        "power": "27.2 PS",
        "torque": "41.3 Nm",
        "top_speed": "130 km/h",
        "brakes_abs": "Disc Brakes with ABS",
        "pros_cons_rating": "Rating: 4.4/5 | Pros: Strong torque, classic styling | Cons: Discontinued",
    },

    "Thunderbird 350": {
        "price": "₹1.60 Lakh",
        "engine": "346 cc",
        "mileage": "40 kmpl",
        "power": "19.8 PS",
        "torque": "28 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Comfortable cruiser | Cons: Discontinued",
    },

    "Thunderbird X": {
        "price": "₹1.70 Lakh",
        "engine": "346 cc",
        "mileage": "40 kmpl",
        "power": "19.8 PS",
        "torque": "28 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Stylish, cruiser comfort | Cons: Discontinued",
    },

    "Electra 350": {
        "price": "₹1.60 Lakh",
        "engine": "346 cc",
        "mileage": "40 kmpl",
        "power": "19.8 PS",
        "torque": "28 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Classic styling, comfortable | Cons: Discontinued",
    },

    "Machismo 500": {
        "price": "₹1.80 Lakh",
        "engine": "499 cc",
        "mileage": "30 kmpl",
        "power": "27.2 PS",
        "torque": "41.3 Nm",
        "top_speed": "130 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.2/5 | Pros: Strong torque, classic feel | Cons: Discontinued",
    },

    "Bullet Trials 350": {
        "price": "₹1.65 Lakh",
        "engine": "346 cc",
        "mileage": "38 kmpl",
        "power": "19.8 PS",
        "torque": "28 Nm",
        "top_speed": "120 km/h",
        "brakes_abs": "Disc Brakes",
        "pros_cons_rating": "Rating: 4.3/5 | Pros: Scrambler styling, rugged | Cons: Discontinued",
    },
}


for bike_name, specs in re_specs.items():

    try:
        bike = Bike.objects.get(name=bike_name)

        for field, value in specs.items():
            setattr(bike, field, value)

        bike.save()

        print(f"✅ {bike_name} updated successfully!")

    except Bike.DoesNotExist:
        print(f"❌ {bike_name} not found in database.")


print("\n🏍️ All Royal Enfield bike information updated!")