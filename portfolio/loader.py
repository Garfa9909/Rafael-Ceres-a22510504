import json
from portfolio.models import *

with open("data/tfcs.json", "r") as f:
    d = json.load(f)


for i in d:
    title = i["titulo"]
    author = i["autor"]
    year = i["year"]
    description = i["resumen"]
    degree_name = i["grado"].split(".")[0]
    try:
        degree = Degree.objects.get(name=degree_name)
    except:
        print(f"Degree {degree_name} doesn't exist")

    Tfc.objects.create(title=title, author=author, year=year, description=description, degree=degree)