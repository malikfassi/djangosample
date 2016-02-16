from django.db import models

class Application(models.Model):
	description = models.CharField(max_length=300)
	url = models.URLField(max_length=200)
	zipFile = models.FileField()
	PUBLIC = "PU"
	PRIVATE = "PR"
	choices = (
		(PUBLIC, "Public"),
		(PRIVATE, "Private")
		)
	access = models.CharField(max_length=2, choices=choices, default=PUBLIC)


	def __str__(self):
		return self.description
