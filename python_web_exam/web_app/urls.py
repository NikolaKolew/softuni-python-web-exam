# •	http://localhost:8000/ - home page
# •	http://localhost:8000/album/add/ - add album page
# •	http://localhost:8000/album/details/<id>/ - album details page
# •	http://localhost:8000/album/edit/<id>/ - edit album page
# •	http://localhost:8000/album/delete/<id>/ - delete album page
# •	http://localhost:8000/profile/details/ - profile details page
# •	http://localhost:8000/profile/delete/ - delete profile page
from django.urls import path

from python_web_exam.web_app.views import show_home, add_album, album_details, album_edit, album_delete, \
    profile_details, profile_delete, create_profile

urlpatterns = (
    path('', show_home, name='index'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', album_edit, name='album edit'),
    path('album/delete/<int:pk>/', album_delete, name='album delete'),
    path('profile/deteils/', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='profile delete'),
    path('createuser/', create_profile, name='profile create'),
)