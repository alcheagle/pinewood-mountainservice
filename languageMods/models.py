from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_length(value):
    if len(value) != 10:
        raise ValidationError(
            _('%(value)s is bigger or smaller than 10 chars'),
            params={'value': value},
        )

class Language (models.Model):
    id = models.AutoField(primary_key=True)
    language=models.CharField(max_length=5, null=True)#default="")
    campo=models.CharField(max_length=100, null=True)#default="")
    text=models.TextField (max_length=500)#, primary_key=True)

    #class Meta:
    #    unique_together = (('language', 'campo'),)

    def __str__(self):
        return ('\nlanguage: '+self.language+'\ncampo: '+self.campo+"\ntext: "+self.text)

class Report (models.Model):
    id = models.AutoField(primary_key=True)
    KEY = models.CharField (validators=[validate_length], max_length=10, default='')
    description = models.TextField(max_length=400)
    evaluation = models.CharField (max_length=2)
    pathName = models.CharField(max_length=200)

    #class Meta:
    #    unique_together = (('description', 'pathName'),)

    def __str__(self):
        return ('\ndescription: '+self.description+'\nevaluation: '+self.evaluation+"\npathName: "+self.pathName)
