from __future__ import unicode_literals

from django.db import models

from team.models import TeamMember

# Create your models here.

class WFH(models.Model):
	teamMember = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
	onDate = models.DateField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	subject = models.CharField(max_length=150,default="<WFH:Today>",blank=True)
	tasks = models.TextField()
	comments = models.CharField(max_length=120,blank=True)

	def __unicode__(self):
		return str(self.teamMember.user) + str(self.onDate)

	def __str__(self):
		return str(self.teamMember.user) + str(self.onDate)

	class Meta:
		ordering = ["teamMember", "-onDate"]

