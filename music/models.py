from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return '{} - {} ({})'.format(self.name, self.artist.name, self.year)


class Track(models.Model):
    name = models.CharField(max_length=196)
    play_time = models.FloatField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'

    def __str__(self):
        return '{} - [{}][{}] ({})'.format(self.name, self.album.name, self.album.artist.name, self.float_to_time())

    @property
    def float_to_time(self):
        minutes = int(self.play_time)
        seconds = int((self.play_time - minutes) * 100)
        if seconds < 10:
            seconds = '0{}'.format(seconds)

        return '{}:{}'.format(minutes, seconds)
