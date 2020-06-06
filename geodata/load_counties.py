import os

from django.contrib.gis.utils import LayerMapping

from geodata.models import County


county_mapping = {
    'objectid': 'OBJECTID',
    'unit_area': 'UNIT_AREA',
    'unit_perim': 'UNIT_PERIM',
    'district': 'DISTRICT',
    'count_field': 'COUNT_',
    'county_nam': 'COUNTY_NAM',
    'code': 'CODE',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'counties', 'County.shp'))


def load_data(verbose=True):
    lm = LayerMapping(County, shp, county_mapping, encoding='iso-8859-1', transform=False)
    lm.save(verbose=verbose, strict=True)
