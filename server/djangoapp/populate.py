from .models import CarMake, CarModel


def initiate():
    makes = [
        ("NISSAN", "Great cars. Japanese technology"),
        ("Mercedes", "Great cars. German technology"),
        ("Audi", "Great cars. German technology"),
        ("Kia", "Great cars. Korean technology"),
        ("Toyota", "Great cars. Japanese technology"),
    ]
    objs = [CarMake.objects.create(name=n, description=d) for n, d in makes]
    models_data = [
        ("Pathfinder", "SUV", 2023, 0), ("Qashqai", "SUV", 2023, 0),
        ("XTRAIL", "SUV", 2023, 0),
        ("A-Class", "SUV", 2023, 1), ("C-Class", "SUV", 2023, 1),
        ("E-Class", "SUV", 2023, 1),
        ("A4", "SUV", 2023, 2), ("A5", "SUV", 2023, 2),
        ("A6", "SUV", 2023, 2),
        ("Sorrento", "SUV", 2023, 3), ("Carnival", "SUV", 2023, 3),
        ("Cerato", "SEDAN", 2023, 3),
        ("Corolla", "SEDAN", 2023, 4), ("Camry", "SEDAN", 2023, 4),
        ("Kluger", "SUV", 2023, 4),
    ]
    for name, t, y, i in models_data:
        CarModel.objects.create(name=name, type=t, year=y,
                                car_make=objs[i], dealer_id=1)
