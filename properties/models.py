import uuid

from django.contrib.gis.db import models as geo_models
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from accounts.models import Profile
from geodata.models import County

def generate_uuid():
	val = uuid.uuid4()
	exists = Property.objects.filter(uuid=val)
	if exists:
		generate_uuid()

	return val


class Facility(models.Model):
	name = models.CharField(max_length=15)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'facilities'

	def __str__(self):
		return self.name

	@property
	def property_count(self):
		return self.property_set.count()


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    @property
    def property_count(self):
    	return self.property_set.count()

    def get_absolute_url(self):
    	return reverse('properties:property_list')

    def save(self, *args, **kwargs):
    	self.slug = slugify(self.name)
    	super(Category, self).save(*args, **kwargs)


class Property(geo_models.Model):
	uuid = models.UUIDField(default=generate_uuid, unique=True, editable=False)
	realtor = geo_models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
	categories = geo_models.ManyToManyField(Category)
	facilities = geo_models.ManyToManyField(Facility)

	name = geo_models.CharField(max_length=100, db_index=True)
	slug = geo_models.SlugField(max_length=200, db_index=True)
	description = geo_models.TextField()
	price_min = geo_models.PositiveIntegerField()
	price_max = geo_models.PositiveIntegerField()
	is_available = geo_models.BooleanField(default=True)

	location = geo_models.PointField(geography=True, extent=(33.951521, -4.699269, 41.888351, 5.383732), srid=4326)
	
	created = geo_models.DateTimeField(auto_now_add=True)
	updated = geo_models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created',)
		index_together = (('id', 'slug'),)
		verbose_name_plural = 'properties'

	def __str__(self):
		return self.name

	@property
	def county(self):
		qs = County.objects.filter(geom__contains=self.location)
		if qs:
			return qs.first().county_nam
		return None

	@property
	def image_list(self):
		return [photo.image.url for photo in self.photo_set.all()]

	@property
	def category_list(self):
		return [i.name for i in self.categories.all()]	

	@property
	def facility_list(self):
		return [i.name for i in self.facilities.all()]

	def get_absolute_url(self):
		return reverse('properties:property_detail', args=[self.pk])

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Property, self).save(*args, **kwargs)


class Photo(models.Model):
    property_item = models.ForeignKey(Property, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='properties', verbose_name='Property Image')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return 'Image for %s' % self.property_item.name

    @property
    def property_name(self):
    	return self.property_item.name

    @property
    def url(self):
    	return self.image.url    
    