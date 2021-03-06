
from django.db import models
from yamlfield.fields import YAMLField


class Document(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    engine = models.CharField(max_length=32, default='dashboard')
    metadata = YAMLField(blank=True, null=True)
    status = models.CharField(max_length=32, default='active')

    def widgets(self):
        return self.metadata.get('widget', {})

    def color(self):
        if self.status == 'active':
            return 'success'
        if self.status == 'error':
            return 'danger'
        if self.status == 'build':
            return 'info'
        else:
            return 'warning'

    def __str__(self):
        return self.name
