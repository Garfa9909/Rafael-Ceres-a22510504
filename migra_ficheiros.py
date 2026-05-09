import os
from django.core.files import File
from portfolio.models import Technology, MakingOf, Subject
from django.conf import settings

for obj in Technology.objects.all():
    if obj.image and obj.image.name:  
        local_path = os.path.join(settings.MEDIA_ROOT, obj.image.name)  

        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.image.save(                         # adequar
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print(f"Migrado: {obj}")

for obj in MakingOf.objects.all():
    if obj.picture and obj.picture.name:  
        local_path = os.path.join(settings.MEDIA_ROOT, obj.picture.name)   

        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.picture.save(                         # adequar
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print(f"Migrado: {obj}")

for obj in Subject.objects.all():
    if obj.image and obj.image.name:  
        local_path = os.path.join(settings.MEDIA_ROOT, obj.image.name) 

        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.image.save(                         # adequar
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print(f"Migrado: {obj}")

            