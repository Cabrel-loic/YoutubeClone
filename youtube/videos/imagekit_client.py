import os
from imagekitio import ImageKit
from django.conf import settings

# Set environment variables for ImageKit
os.environ['IMAGEKIT_PRIVATE_KEY'] = settings.IMAGEKIT_PRIVATE_KEY
os.environ['IMAGEKIT_PUBLIC_KEY'] = settings.IMAGEKIT_PUBLIC_KEY


def get_imagekit_client():
    return ImageKit()

def get_optimized_url(base_url: str) -> str:
    """
    Return the original URL for videos.

    The previous implementation added ImageKit transformation parameters like
    `?tr=q-50,w-200,h-150,fo-auto`, which can cause 403 errors depending on
    your ImageKit configuration and plan. For video files, it's safer to use
    the direct URL returned by ImageKit.
    """
    return base_url

def get_streaming_url(base_url: str) -> str:
    """Use the video URL directly - ImageKit will handle streaming"""
    return base_url

def get_thumbnail_url(base_url: str, width: int = 480, height: int = 270) -> str:
    """
    For video URLs, extract a frame by appending video-to-image transformation.
    ImageKit supports frame extraction using the 'epage' parameter for video files.
    """
    # Use epage-0 to extract the cover/first frame of the video
    if '?' in base_url:
        return f"{base_url}&tr=epage-0,w-{width},h-{height},c-at,q-80"
    return f"{base_url}?tr=epage-0,w-{width},h-{height},c-at,q-80"


def upload_video(file_data: bytes, file_name:str, folder: str = 'videos') -> dict:
    client = get_imagekit_client()

    response = client.files.upload(
        file=file_data,
        file_name=file_name,
        folder=folder,
    )
    return {
        "file_id": response.file_id,
        "url": response.url,
    }

def upload_thumbnail(
        file_data: bytes,
        file_name: str,
        folder: str = 'thumbnails'
) -> dict:
    import base64

    if file_data.startswith('data:'):
        base64_data = file_data.split(',', 1)[1]
        image_bytes = base64.b64decode(base64_data)
    else:
        image_bytes = base64.b64decode(file_data)

    client = get_imagekit_client()

    response = client.files.upload(
        file=image_bytes,
        file_name=file_name,
        folder=folder,
    )

    return {
        "file_id": response.file_id,
        "url": response.url,
    }

def delete_video(file_id: str) -> bool:
    client = get_imagekit_client()
    client.files.delete(file_id=file_id)
    return True