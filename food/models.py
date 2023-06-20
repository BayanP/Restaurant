from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created At')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Menu')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Category', null=True)
    image = models.ImageField(upload_to='food/', verbose_name='Image')
    price = models.PositiveIntegerField(verbose_name='Price')
    description = models.TextField(max_length=500 ,verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created At')

    def __str__(self):
        return f'{self.title} - {self.category}'
    
    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"

class Events(models.Model):
    image = models.ImageField(upload_to='events/', verbose_name='Image')
    title = models.CharField(max_length=100, verbose_name='title')
    price = models.PositiveIntegerField(verbose_name='Price')
    description = models.TextField(max_length=500 ,verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created At')

    def __str__(self):
        return f'{self.title} - {self.price} - {self.created_at}'
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

class Reservation(models.Model):
    full_name = models.ImageField(upload_to='events/', verbose_name='Name')
    email = models.EmailField(max_length=100 ,verbose_name='email')
    phone = models.CharField(max_length=13, verbose_name='phone')
    date = models.DateField(verbose_name='date')
    time = models.TimeField(verbose_name='time')
    persons = models.PositiveIntegerField(verbose_name='persons')
    message = models.TextField(max_length=500 ,verbose_name='message')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created At')

    def __str__(self):
        return f'{self.full_name} - {self.phone} - {self.date} - {self.time} - {self.persons}'
    
    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

class Testimonials(models.Model):
    image = models.ImageField(upload_to="testimonials/", 
        verbose_name="Изображение", blank=True, null=True)
    first_name = models.CharField(verbose_name="Имя", max_length=120)
    last_name = models.CharField(verbose_name="Фамилия", max_length=120)
    description = models.TextField(verbose_name="Тематика", max_length=120)
    profession = models.CharField(verbose_name="Профессия", max_length=120)
    created_at = models.DateTimeField(auto_now_add=True,
        verbose_name="Дата создания")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} | Профессия: {self.profession} | {self.created_at}"

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/", 
        verbose_name="Изображение", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,
        verbose_name="Дата создания")
    
    def __str__(self):
        return f'photo has been uploaded to {self.created_at}'
    
    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

class Role(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    created_at = models.DateTimeField(auto_now_add=True,
        verbose_name="Дата создания")
    
    def __str__(self):
        return f'{self.title} | {self.created_at}'
    
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

class Chefs(models.Model):
    image = models.ImageField(upload_to="shefs/", 
        verbose_name="Изображение", blank=True, null=True)
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, 
        verbose_name="Роль повара")
    twitter  = models.URLField(blank=True, null=True, unique=True, 
        verbose_name="twitter Url", max_length=300)
    facebook = models.URLField(blank=True, null=True, unique=True, 
        verbose_name="facebook Url", max_length=300)
    instagram = models.URLField(blank=True, null=True, unique=True,
        verbose_name="instagram Url", max_length=300)
    linkedin = models.URLField(blank=True, null=True, unique=True, 
        verbose_name="linkedin Url", max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, 
        verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.full_name} | {self.role} | {self.created_at}"
    
    class Meta:
        verbose_name = "Повар"
        verbose_name_plural = "Повара"

class Contact(models.Model):
    full_name=models.CharField(verbose_name="ФИО",max_length=120)
    email=models.EmailField(verbose_name="Email",max_length=120)
    subject=models.TextField(verbose_name="Сообщение", max_length=120)
    message=models.TextField(verbose_name="Cooбщение",max_length=400)
    created_at = models.DateTimeField(auto_now_add=True, 
        verbose_name="Дата создания")

    def str(self) -> str:
        return f"{self.full_name} | {self.subject} |{self.message} | {self.created_at}"
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"







