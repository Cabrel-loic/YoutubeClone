import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube.settings')
django.setup()

from videos.models import Video
from videos.imagekit_client import get_thumbnail_url

# Get a video without custom thumbnail
videos = Video.objects.filter(thumbnail_url__isnull=True)

if videos.exists():
    video = videos.first()
    print(f"Video: {video.title}")
    print(f"Video URL: {video.video_url}")
    print(f"Thumbnail URL (DB): {video.thumbnail_url}")
    print(f"Generated Thumbnail URL: {video.generated_thumbnail_url}")
    print(f"Display Thumbnail URL: {video.display_thumbnail_url}")
else:
    print("No videos without custom thumbnails found")
