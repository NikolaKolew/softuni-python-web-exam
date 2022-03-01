from django.shortcuts import render, redirect

from python_web_exam.web_app.forms import CreateProfile, CreateAlbum, EditAlbum, DeleteAlbum, DeleteProfile
from python_web_exam.web_app.models import Profile, Album


def get_user():
    profile = Profile.objects.first()
    return profile


def show_home(request):
    profile = get_user()
    if not profile:
        return redirect('profile create')

    album = Album.objects.all()
    context = {
        'album': album,
    }

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfile()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = CreateAlbum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateAlbum()

    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }

    return render(request, 'album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbum(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditAlbum(instance=album)

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbum(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteAlbum(instance=album)

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_user()
    album = Album.objects.all()
    all_albums = len(album)
    context = {
        'profile': profile,
        'all_albums': all_albums,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_user()
    if request.method == 'POST':
        form = DeleteProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfile(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
