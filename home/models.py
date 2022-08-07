
from statistics import mode
from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4 ,editable=False ,primary_key=True)
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Amenities(BaseModel):
    amenity_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.amenity_name

class Fluid(BaseModel):
    fluid_name= models.CharField(max_length=100)
    fluid_price = models.IntegerField()
    description = models.TextField()
    amenities = models.ManyToManyField(Amenities)
    fluid_count= models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.fluid_name

class FluidImages(BaseModel):
    fluid = models.ForeignKey(Fluid, related_name="fluid_images", on_delete= models.CASCADE)
    images = models.ImageField(upload_to="fluid")

class FluidBooking(BaseModel):
    # fluid = models.ForeignKey(Fluid, related_name="fluid_booking", on_delete= models.CASCADE)
    fluid = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="user_booking" , on_delete= models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    
    
    

    
