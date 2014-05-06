from django.core.urlresolvers import reverse
from django.db import models
from bsct.models import BSCTModelMixin

class Company(BSCTModelMixin, models.Model ):
	company = models.CharField(max_length=255)
	link = models.CharField(max_length=255)
	income = models.CharField(max_length=8)
	phone = models.CharField(max_length=60)
	email = models.CharField(max_length=150)

	def __unicode__( self ):
		return '%s' % ( self.company )

	class Meta:
		verbose_name = "Company"
		verbose_name_plural = "Companies"
 
 