from django.contrib import admin

from .models import Artist, Album, Track


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_of_albums', 'count_of_tracks')
    search_fields = ("name__contains",)

    def count_of_albums(self, obj):
        return obj.album_set.count()

    def count_of_tracks(self, obj):
        return Track.objects.filter(album__artist=obj).count()


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'artist', 'count_of_tracks')
    list_filter = ('artist', 'year')
    search_fields = ("name__contains",)

    def count_of_tracks(self, obj):
        return obj.track_set.count()


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'float_to_time', 'album')
    list_filter = ('album__artist', 'album')
    search_fields = ("name__contains",)
