from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.http import FileResponse


from .models import Video, VideoLike
from .forms import VideoUploadForm


from .imagekit_client import upload_video as imagekit_upload_video, upload_thumbnail, delete_video as imagekit_delete_file

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videos/list.html', {'videos': videos})

def video_detail(request, video_id):
    video = get_object_or_404(Video.objects.select_related('user'), id=video_id)

    # Increment views only once per viewer (per session) and never for the owner
    viewed_videos = request.session.get('viewed_videos', [])
    if video.id not in viewed_videos and request.user != video.user:
        video.views += 1
        video.save(update_fields=['views'])
        viewed_videos.append(video.id)
        request.session['viewed_videos'] = viewed_videos

    user_vote = None
    if request.user.is_authenticated:
        like = VideoLike.objects.filter(user = request.user, video = video).first()
        if like:
            user_vote = like.value
    context = {
        'video': video,
        'user_vote': user_vote
    }
    return render(request, 'videos/detail.html', context)

def channel_videos(request, username):
    videos = Video.objects.filter(user__username=username)
    context = {
        'videos': videos,
        'channel_username': username,
    }
    return render(request, 'videos/channel.html', context)

@login_required
@require_POST
def upload_video(request):
    form = VideoUploadForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        video_file = form.cleaned_data['video_file']
        custom_thumbnail = request.POST.get('thumbnail_data', '')

        try:
            result = imagekit_upload_video(
                file_data=video_file.read(),
                file_name=video_file.name,

            )
            thumbnail_url = None
            if custom_thumbnail and custom_thumbnail.startswith('data:'):
                try:
                    base_name = video_file.name.rsplit('.', 1)[0]
                    thumbnail_result = upload_thumbnail(
                        file_data=custom_thumbnail,
                        file_name=f"{base_name}_thumbnail.png"
                    )
                    thumbnail_url = thumbnail_result['url']
                except Exception as e:
                    pass
            video = Video.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                file_id=result['file_id'],
                video_url=result['url'],
                thumbnail_url=thumbnail_url,
            )

            return JsonResponse({
                "success": True,
                "video_id": video.id,
                # "video_url": video.video_url,
                "message": "Your video is uploaded successfully.",

            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "error": str(e),
                # "message": "An error occurred while uploading the video. Please try again.",
            })
    else:
        errors = []
        for field, field_errors in form.errors.items():
            for error in field_errors:
                errors.append(f"{field}: {error}" if field != '__all__' else error)
        return JsonResponse({
            "success": False,
            "errors": ";".join(errors),
        })

@login_required
def video_upload_page(request):
    form = VideoUploadForm()
    return render(request, 'videos/upload.html', {'form': form})


@login_required
@require_POST
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id, user=request.user)

    try: 
        imagekit_delete_file(video.file_id)
    except Exception as e:
        print(e)
        pass
    video.delete()

    return JsonResponse({"success": True, "message": "video deleted"})


@login_required
@require_POST
def video_vote(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    vote_type = request.POST.get('vote')

    if vote_type not in ['like', 'dislike']:
        return JsonResponse({"success": False, "error": "Invalid vote"}, status=400)

    value = VideoLike.LIKE if vote_type == 'like' else VideoLike.DISLIKE

    existing_vote = VideoLike.objects.filter(user=request.user, video=video).first()
    user_vote = None

    if existing_vote:
        # User already voted
        if existing_vote.value == value:
            # Same vote - remove it (toggle off)
            if value == VideoLike.LIKE:
                video.likes -= 1
            else:
                video.dislikes -= 1
            existing_vote.delete()
            user_vote = None
        else:
            # Different vote - switch it
            if existing_vote.value == VideoLike.LIKE:
                video.likes -= 1
                video.dislikes += 1
            else:
                video.dislikes -= 1
                video.likes += 1
            existing_vote.value = value
            existing_vote.save()
            user_vote = value
    else:
        # New vote
        VideoLike.objects.create(user=request.user, video=video, value=value)
        if value == VideoLike.LIKE:
            video.likes += 1
        else:
            video.dislikes += 1
        user_vote = value
    
    video.save(update_fields=['likes', 'dislikes'])
    return JsonResponse({
        'likes': video.likes,
        'dislikes': video.dislikes,
        'user_vote': user_vote
    })
        