# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


D_ZONA_CHOICES = (('UR', 'Urbano'), ('RU', 'Rural'), ('SE', 'Semiurbano'))

C_TIPO_ASENTA_CHOICES = (('32', 'Villa'), ('37', 'Zona industrial'), ('27', 'Poblado comunal'), ('20', 'Finca'), ('09', 'Colonia'), ('38', 'Ampliación'), ('10', 'Condominio'), ('34', 'Zona federal'), ('18', 'Exhacienda'), ('30', 'Residencial'), ('02', 'Barrio'), ('47', 'Zona militar'), ('12', 'Conjunto habitacional'), ('46', 'Zona naval'), ('23', 'Granja'), ('40', 'Puerto'), ('01', 'Aeropuerto'), ('15', 'Ejido'), ('04', 'Campamento'), ('45', 'Paraje'), ('29', 'Ranchería'), ('31', 'Unidad habitacional'), ('24', 'Hacienda'), ('28', 'Pueblo'), ('11', 'Congregación'), ('33', 'Zona comercial'), ('22', 'Gran usuario'), ('16', 'Estación'), ('26', 'Parque industrial'), ('48', 'Rancho'), ('21', 'Fraccionamiento'), ('17', 'Equipamiento'))


C_ESTADO_CHOICES = (('26', 'Sonora'), ('10', 'Durango'), ('03', 'Baja California Sur'), ('04', 'Campeche'), ('16', 'Michoacán de Ocampo'), ('31', 'Yucatán'), ('19', 'Nuevo León'), ('12', 'Guerrero'), ('11', 'Guanajuato'), ('25', 'Sinaloa'), ('15', 'México'), ('29', 'Tlaxcala'), ('13', 'Hidalgo'), ('08', 'Chihuahua'), ('24', 'San Luis Potosí'), ('27', 'Tabasco'), ('23', 'Quintana Roo'), ('28', 'Tamaulipas'), ('14', 'Jalisco'), ('05', 'Coahuila de Zaragoza'), ('09', 'Ciudad de México'), ('21', 'Puebla'), ('06', 'Colima'), ('02', 'Baja California'), ('32', 'Zacatecas'), ('01', 'Aguascalientes'), ('22', 'Querétaro'), ('30', 'Veracruz de Ignacio de la Llave'), ('20', 'Oaxaca'), ('17', 'Morelos'), ('18', 'Nayarit'), ('07', 'Chiapas'))



class PostalCode(TimeStampedModel):
    d_codigo=models.CharField(_('Codigo Postal'), max_length=5)
    d_asenta = models.CharField(_('Asentamiento'), max_length=128)
    D_mnpio = models.CharField(_('Municipio'), max_length=128)
    d_ciudad = models.CharField(_('Ciudad'), max_length=128, blank=True, null=True)
    d_CP = models.CharField(_('Código postal'), max_length=128, blank=True, null=True)
    c_estado = models.CharField(_('Código de estado'), max_length=2, choices=C_ESTADO_CHOICES)
    c_oficina = models.CharField(_('Código de oficina'), max_length=5)
    c_tipo_asenta = models.CharField(_('Código de tipo de asentamiento'), max_length=2, choices=C_TIPO_ASENTA_CHOICES)
    c_mnpio = models.CharField(_('Código de municipio'), max_length=3)
    id_asenta_cpcons = models.CharField(_('Id Asentamiento'), max_length=4)
    d_zona = models.CharField(_('Tipo de Zona'), max_length=2, choices=D_ZONA_CHOICES)
    c_cve_ciudad = models.CharField(_('Asentamiento'), max_length=2, blank=True, null=True)

    @property
    def c_CP(self):
        return None

    @property
    def d_estado(self):
        return self.get_c_estado_display()

    @property
    def d_tipo_asenta(self):
        return self.get_c_tipo_asenta_display()


    def __str__(self):
        return '{} {} {}'.format(d_codigo, D_mnpio, d_estado)





