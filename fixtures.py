"""Setup mock data for database."""
import pytz
import json
import random


from faker import Faker
from datetime import datetime

fake = Faker()

# Set the IST timezone
ist = pytz.timezone("Asia/Kolkata")


num_fixtures = 50
appointment_data = []
staff_data = []
service_data = []
feedback_data = []
product_data = []
purchase_data = []
gallery_data = []
attendance_data = []


for pk in range(1, num_fixtures + 1):
    current_time = datetime.now().astimezone(ist).isoformat()
    phone_number = fake.numerify(text="##########")

    staff_fixture = {
        "model": "myuser.staff",
        "pk": pk,
        "fields": {
            "user": random.randint(1, 10),
            "profile": None,
            "name": fake.first_name(),
            "surname": fake.last_name(),
            "phone": phone_number,
            "email": fake.email(),
            "specialization": fake.job(),
            "created_at": current_time,
            "updated_at": current_time,
        },
    }

    staff_data.append(staff_fixture)

    service_fixture = {
        "model": "myuser.service",
        "pk": pk,
        "fields": {
            "user": random.randint(1, 10),
            "img": None,  # Replace with the image file path
            "name": fake.word(),
            "cost": random.randint(10, 100),
            "text": fake.text(max_nb_chars=50),
            "created_at": current_time,
            "updated_at": current_time,
        },
    }
    service_data.append(service_fixture)

    service_ids = random.sample(
        range(1, 20), 3
    )  # Generate a list of 3 unique service IDs
    appointment_fixture = {
        "model": "myuser.appointment",
        "pk": pk,
        "fields": {
            "user": random.randint(1, 10),
            "name": fake.first_name(),
            "surname": fake.last_name(),
            "phone": phone_number,
            "app_date": fake.date_this_year().strftime("%Y-%m-%d"),
            "app_time": fake.time_object().strftime("%H:%M:%S"),
            "service": service_ids,
            "provided": random.randint(1, 20),
            "created_at": current_time,
            "updated_at": current_time,
        },
    }

    appointment_data.append(appointment_fixture)

    feedback_fixture = {
        "model": "myuser.feedback",
        "pk": pk,
        "fields": {
            "user": random.randint(1, 10),
            "name": fake.first_name(),
            "phone": phone_number,
            "feedback": fake.text(max_nb_chars=1200),
            "created_at": current_time,
            "updated_at": current_time,
        },
    }

    feedback_data.append(feedback_fixture)

    product_fixture = {
        "model": "myuser.product",
        "pk": pk,
        "fields": {
            "user": random.randint(1, 10),
            "img": None,
            "name": fake.word(),
            "price": random.randint(10, 100),
            "stock": random.randint(1, 100),
            "note": fake.sentence(),
            "created_at": current_time,
            "updated_at": current_time,
        },
    }
    product_data.append(product_fixture)

    purchase_fixture = {
        "model": "myuser.purchase",
        "pk": pk,
        "fields": {
            "user": random.randint(1, 10),
            "product": random.randint(1, 10),
            "name": fake.first_name(),
            "phone": phone_number,
            "qty": random.randint(1, 10),
            "created_at": current_time,
            "updated_at": current_time,
        },
    }

    purchase_data.append(purchase_fixture)

    gallery_fixture = {
        "model": "myuser.gallery",
        "pk": pk,
        "fields": {
            "user": random.randint(1, 10),
            "name": fake.word(),
            "img": None,
            "file": None,
            "about": fake.paragraph(),
            "created_at": current_time,
            "updated_at": current_time,
        },
    }
    gallery_data.append(gallery_fixture)

    attendance_fixture = {
        "model": "myuser.attendance",
        "pk": pk,
        "fields": {
            "user": random.randint(1, 10),
            "staff": random.randint(1, 25),
            "date": fake.date_this_year().strftime("%Y-%m-%d"),
            "is_present": fake.boolean(),
            "created_at": current_time,
            "updated_at": current_time,
        },
    }
    attendance_data.append(attendance_fixture)

with open("fixtures/appointment.json", "w") as appointment_file:
    json.dump(appointment_data, appointment_file, indent=2)

with open("fixtures/staff.json", "w") as staff_file:
    json.dump(staff_data, staff_file, indent=2)

with open("fixtures/service.json", "w") as service_file:
    json.dump(service_data, service_file, indent=2)

with open("fixtures/feedback.json", "w") as feedback_file:
    json.dump(feedback_data, feedback_file, indent=2)

with open("fixtures/product.json", "w") as product_file:
    json.dump(product_data, product_file, indent=2)

with open("fixtures/purchase.json", "w") as purchase_file:
    json.dump(purchase_data, purchase_file, indent=2)

with open("fixtures/gallery.json", "w") as gallery_file:
    json.dump(gallery_data, gallery_file, indent=2)

with open("fixtures/attendance.json", "w") as attendance_file:
    json.dump(attendance_data, attendance_file, indent=2)
