# YouTube Clone

A Django-based video sharing platform that mimics core YouTube functionality. Built with Python, Django, and ImageKit for video processing and storage.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [Completed Features](#completed-features)
- [Features In Progress / TODO](#features-in-progress--todo)
- [Troubleshooting](#troubleshooting)

## Features

### ✅ Implemented Features

1. **User Authentication**
   - User registration with email
   - Login/Logout functionality
   - Secure password validation

2. **Video Management**
   - Upload videos with title and description
   - Support for multiple video formats (MP4, AVI, MOV, WMV, E-MSVIDEO)
   - Maximum file size: 100 MB
   - Automatic thumbnail generation from video first frame
   - Custom thumbnail upload support
   - Video deletion (owner only)
   - Video metadata storage (title, description, timestamps)

3. **Video Browsing & Discovery**
   - Homepage with video grid listing
   - Video detail page with streaming player
   - View counter (tracks unique viewers per session)
   - Channel/Creator profile page
   - Video metadata display (views, upload date)

4. **Engagement Features**
   - Like/Dislike system with toggle functionality
   - Like/Dislike counts display
   - User vote tracking (prevents duplicate votes)
   - Real-time like/dislike updates via AJAX

5. **User Profiles**
   - Channel pages with creator videos
   - View all videos from a specific creator
   - Upload button on own channel (owner only)

6. **Media Storage & Processing**
   - ImageKit integration for video hosting and processing
   - Automatic thumbnail extraction
   - Video streaming optimization
   - Cloud-based file management

### 🚧 Features In Progress / TODO

1. **Video Search & Filtering**
   - Search functionality for videos
   - Advanced filtering (date, duration, views)
   - Search suggestions/autocomplete

2. **Comments System**
   - Add/Edit/Delete comments on videos
   - Nested reply functionality
   - Comment moderation

3. **Subscriptions**
   - Subscribe to channels
   - Subscriber notifications
   - Subscription feed

4. **Recommendations & Algorithms**
   - Recommended videos sidebar
   - Trending videos section
   - Watch history
   - Algorithm-based suggestions

5. **Playlists**
   - Create custom playlists
   - Add videos to playlists
   - Share playlists

6. **Video Monetization**
   - Ad integration
   - Revenue tracking
   - Creator dashboard analytics

7. **Advanced Features**
   - Video categories/tags
   - Video chapters/segments
   - Subtitles/Captions support
   - Live streaming
   - Video quality options (360p, 720p, 1080p, etc.)
   - Watch time analytics
   - User notifications system
   - Social sharing features

8. **Security & Performance**
   - Rate limiting
   - CSRF protection enhancements
   - CDN integration for faster delivery
   - Database query optimization
   - Caching layer

## Tech Stack

- **Backend Framework**: Django 6.0.1
- **Database**: MySQL 2.2.7
- **Media Management**: ImageKit 5.0.0
- **Python Version**: 3.13+
- **Environment Management**: python-dotenv, python-decouple

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.13 or higher
- MySQL Server (local or remote)
- pip or uv (Python package manager)
- Git

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd "Youtube Clone"
```

### 2. Create Virtual Environment

Using `venv`:
```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows (CMD)**:
  ```bash
  venv\Scripts\activate
  ```
- **Windows (PowerShell)**:
  ```bash
  venv\Scripts\Activate.ps1
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or if using `uv`:
```bash
uv pip install -r requirements.txt
```

### 4. Create Environment Configuration File

Create a `.env` file in the `youtube` directory (same level as `manage.py`):

```env
# Database Configuration
DATABASE_ENGINE=django.db.backends.mysql
DATABASE_NAME=Youtubeclone
DATABASE_USER=root
DATABASE_PASSWORD=your_mysql_password
DATABASE_HOST=localhost
DATABASE_PORT=3306

# ImageKit Configuration
IMAGEKIT_PRIVATE_KEY=your_imagekit_private_key
IMAGEKIT_PUBLIC_KEY=your_imagekit_public_key

# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
```

**Note**: Get your ImageKit credentials from https://imagekit.io/dashboard

### 5. Create MySQL Database

```sql
CREATE DATABASE Youtubeclone;
```

Or run this in MySQL command line:
```bash
mysql -u root -p -e "CREATE DATABASE Youtubeclone;"
```

## Configuration

### Database Configuration

The project uses MySQL for data storage. Configuration is handled via environment variables in `.env`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Youtubeclone',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### ImageKit Setup

1. Sign up at https://imagekit.io
2. Get your Private Key and Public Key from the dashboard
3. Add them to your `.env` file
4. ImageKit provides:
   - Video hosting
   - Automatic thumbnail generation
   - Video streaming optimization
   - URL-based transformations

### Static Files Configuration

Static files (CSS, JS, Images) are stored in:
```
youtube/static/
├── css/
│   ├── auth.css
│   ├── base.css
│   ├── buttons.css
│   ├── forms.css
│   ├── messages.css
│   ├── navbar.css
│   ├── upload.css
│   ├── variables.css
│   ├── videoplayer.css
│   └── videos.css
```

### Upload Size Limits

- Maximum video file size: **100 MB**
- Configured in Django settings:
  - `DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600` (100 MB)
  - `FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600` (100 MB)

## Running the Project

### 1. Apply Database Migrations

```bash
cd youtube
python manage.py migrate
```

### 2. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 3. Run Development Server

```bash
python manage.py runserver
```

The server will start at `http://localhost:8000`

### 4. Access the Application

- **Main Site**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/
- **Register**: http://localhost:8000/accounts/register/
- **Login**: http://localhost:8000/accounts/login/

## Project Structure

```
youtube/
├── manage.py                          # Django management script
├── youtube/                           # Project configuration
│   ├── settings.py                    # Django settings
│   ├── urls.py                        # Main URL configuration
│   ├── asgi.py                        # ASGI configuration
│   └── wsgi.py                        # WSGI configuration
├── accounts/                          # User authentication app
│   ├── models.py                      # User-related models
│   ├── views.py                       # Auth views (Register, Login)
│   ├── forms.py                       # Auth forms (CustomUserCreationForm)
│   ├── urls.py                        # Auth URLs
│   ├── admin.py                       # Admin panel config
│   └── templates/
│       └── accounts/
│           ├── login.html
│           ├── register.html
│           └── logged_out.html
├── videos/                            # Video management app
│   ├── models.py                      # Video & VideoLike models
│   ├── views.py                       # Video views
│   ├── forms.py                       # Video forms (VideoUploadForm)
│   ├── urls.py                        # Video URLs
│   ├── imagekit_client.py             # ImageKit API integration
│   ├── admin.py                       # Admin panel config
│   └── templates/
│       └── videos/
│           ├── list.html              # Homepage - video grid
│           ├── detail.html            # Video detail page
│           ├── upload.html            # Upload form page
│           └── channel.html           # Creator channel page
├── templates/
│   └── base.html                      # Base template
└── static/
    └── css/                           # Stylesheets
```

## API Endpoints

### Video Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|----------------|
| GET | `/` | List all videos | No |
| GET | `/<video_id>/` | Get video details | No |
| GET | `/channel/<username>/` | Get user's videos | No |
| GET | `/upload/` | Upload form page | Yes |
| POST | `/upload/submit/` | Submit video upload | Yes |
| POST | `/<video_id>/delete/` | Delete video | Yes (Owner) |
| POST | `/<video_id>/vote/` | Like/Dislike video | Yes |

### Account Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|----------------|
| GET | `/accounts/register/` | Registration form | No |
| POST | `/accounts/register/` | Submit registration | No |
| GET | `/accounts/login/` | Login form | No |
| POST | `/accounts/login/` | Submit login | No |
| GET | `/accounts/logout/` | Logout | Yes |

## Database Models

### User Model
Uses Django's built-in `User` model with extensions:
- username
- email
- password (hashed)
- first_name, last_name (optional)

### Video Model
```python
Video:
  - user (ForeignKey to User)
  - title (CharField, max 200)
  - description (TextField, optional)
  - file_id (CharField) - ImageKit file ID
  - video_url (URLField) - ImageKit video URL
  - thumbnail_url (URLField, optional)
  - views (PositiveIntegerField, default: 0)
  - likes (PositiveIntegerField, default: 0)
  - dislikes (PositiveIntegerField, default: 0)
  - created_at (DateTimeField, auto)
  - updated_at (DateTimeField, auto)
  
  Properties:
  - display_thumbnail_url: Returns custom or auto-generated thumbnail
  - generated_thumbnail_url: Generates thumbnail from video
  - streaming_url: Returns optimized streaming URL
```

### VideoLike Model
```python
VideoLike:
  - user (ForeignKey to User)
  - video (ForeignKey to Video)
  - value (SmallIntegerField) - LIKE (1) or DISLIKE (-1)
  - created_at (DateTimeField, auto)
  
  Constraints:
  - unique_together: (user, video) - One vote per user per video
```

## Completed Features

### ✅ Authentication System
- [x] User registration with email validation
- [x] Login/Logout functionality
- [x] Password hashing and validation
- [x] Session management
- [x] Logout confirmation page

### ✅ Video Management
- [x] Video upload with validation
- [x] Video metadata (title, description)
- [x] Automatic thumbnail generation
- [x] Custom thumbnail upload
- [x] Video deletion
- [x] File size validation (100 MB max)
- [x] File type validation

### ✅ Video Discovery & Playback
- [x] Homepage with video grid
- [x] Video detail page
- [x] Video streaming via ImageKit
- [x] View counter (unique per session)
- [x] Lazy loading for images
- [x] Video metadata display

### ✅ Creator Channels
- [x] User channel pages
- [x] Channel video listing
- [x] Upload button on own channel
- [x] Channel header with avatar (first letter)

### ✅ Engagement Features
- [x] Like/Dislike system
- [x] Vote counting
- [x] Toggle votes (AJAX)
- [x] Like/Dislike display

### ✅ UI/UX
- [x] Responsive navbar
- [x] CSS styling (videos, forms, auth)
- [x] Base template structure
- [x] Form validation messages
- [x] Empty state handling

## Features In Progress / TODO

### 🚧 High Priority

- [ ] **Search & Filter**
  - [ ] Video search functionality
  - [ ] Filter by date, views, duration
  - [ ] Search API endpoint

- [ ] **Comments**
  - [ ] Comment model
  - [ ] Add/Edit/Delete comments
  - [ ] Comment display on video pages

- [ ] **Video Details**
  - [ ] Video duration
  - [ ] Video categories/tags
  - [ ] Video quality options

### 🚧 Medium Priority

- [ ] **Subscriptions**
  - [ ] Subscribe button
  - [ ] Subscriber count
  - [ ] Subscription feed

- [ ] **Notifications**
  - [ ] New upload notifications
  - [ ] Comment notifications
  - [ ] Reply notifications

- [ ] **Playlists**
  - [ ] Create playlists
  - [ ] Add videos to playlists
  - [ ] Playlist sharing

- [ ] **Watch History**
  - [ ] Store watch history
  - [ ] Display recent videos
  - [ ] Clear history option

### 🚧 Lower Priority

- [ ] **Advanced Features**
  - [ ] Live streaming
  - [ ] Video chapters
  - [ ] Subtitles/Captions
  - [ ] Video reactions
  - [ ] Social sharing

- [ ] **Performance**
  - [ ] Pagination for videos
  - [ ] Database query optimization
  - [ ] Caching layer
  - [ ] CDN integration

- [ ] **Analytics**
  - [ ] View analytics
  - [ ] Engagement analytics
  - [ ] Creator dashboard
  - [ ] Revenue tracking

## Troubleshooting

### Database Connection Error

**Error**: `django.db.utils.OperationalError: (1045, "Access denied for user 'root'@'localhost'"`

**Solution**:
1. Verify MySQL is running
2. Check credentials in `.env` file
3. Ensure database exists: `SHOW DATABASES;`
4. Verify user permissions in MySQL

### ImageKit Upload Error

**Error**: `IMAGEKIT_PRIVATE_KEY or IMAGEKIT_PUBLIC_KEY not found`

**Solution**:
1. Sign up at https://imagekit.io
2. Get keys from dashboard
3. Add to `.env` file
4. Restart Django server

### Migration Error

**Error**: `django.db.utils.ProgrammingError: Table does not exist`

**Solution**:
```bash
python manage.py migrate
```

### Port Already in Use

**Error**: `OSError: [Errno 48] Address already in use`

**Solution**:
```bash
python manage.py runserver 8001  # Use different port
```

### Video Upload Size Limit

**Error**: `Request entity too large`

**Solution**:
- Compress video to under 100 MB
- Check `FILE_UPLOAD_MAX_MEMORY_SIZE` in settings.py

### Static Files Not Loading

**Error**: CSS/JS files returning 404

**Solution**:
```bash
python manage.py collectstatic
```

## Development Notes

### Adding a New Feature

1. Create models in appropriate app (`models.py`)
2. Create forms if needed (`forms.py`)
3. Create views (`views.py`)
4. Create/update templates
5. Add URLs to `urls.py`
6. Create migrations: `python manage.py makemigrations`
7. Apply migrations: `python manage.py migrate`
8. Test thoroughly
9. Update this README

### Running Tests

```bash
python manage.py test
```

### Making Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Admin Panel

Access at `/admin/` to manage:
- Users
- Videos
- Video Likes
- Permissions

---

**Last Updated**: January 12, 2026
**Version**: 0.1.0
**Status**: In Active Development
