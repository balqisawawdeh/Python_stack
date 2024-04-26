from django.db import models
    
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_movie():
    Movie.objects.create(title="game of throne2",description="test test",release_date="2024-10-10",duration=2)

def update_movie(id):
    movie= Movie.objects.get(id=id) #instanse of movie i want to update.
    movie.title="The lord of the rings."
    movie.description="this is test for update movie description"
    movie.save()
def remove_movie(id):
    movie= Movie.objects.get(id=id) #instanse of movie i want to update.
    movie.delete()
