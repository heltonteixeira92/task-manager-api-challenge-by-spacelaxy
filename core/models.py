from django.db import models


class Task(models.Model):
    CHOICES = [
        ('pending', 'pendente'),
        ('in progress', 'em andamento'),
        ('concluded', 'concluída')
    ]
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=CHOICES, default='pending')
    description = models.TextField()

    class Meta:
        ordering = ['status']

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'status': self.status,
            'description': self.description
        }
