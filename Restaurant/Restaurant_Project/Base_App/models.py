from django.db import models

# Create your models here.
class ItemList(models.Model):
    Category_name=models.CharField(max_length=15)

    def __str__(self) :
        return self.Category_name

class Items(models.Model):
    Item_name= models.CharField( max_length=50)
    description = models.TextField(blank=False)
    Price = models.IntegerField() 
    Category = models.ForeignKey(ItemList,related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='media/items')

        

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

    

class Feedback(models.Model):
    User_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()


    
    

class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()






