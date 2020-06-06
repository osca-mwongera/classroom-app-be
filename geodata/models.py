from django.contrib.gis.db import models
from django.shortcuts import reverse


class County(models.Model):
    objectid = models.BigIntegerField()
    unit_area = models.FloatField()
    unit_perim = models.FloatField()
    district = models.CharField(max_length=50)
    count_field = models.FloatField()
    county_nam = models.CharField(max_length=50, db_index=True)
    code = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        ordering = ('county_nam',)
        verbose_name = 'county'
        verbose_name_plural = "counties"

    def __str__(self):
        return self.county_nam

    def get_absolute_url(self):
        return reverse('land:parcel_list_by_county', args=[self.county_nam])


class POI(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    location = models.PointField(geography=True, srid=4326)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
