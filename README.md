# YouTube Clone

A Django-based video sharing platform that mimics core YouTube functionality. Built with Python, Django, and ImageKit for video processing and storage.

## Repository

**GitHub**: [Cabrel-loic/YoutubeClone](https://github.com/Cabrel-loic/YoutubeClone)

**Clone Options:**
- **HTTPS**: `https://github.com/Cabrel-loic/YoutubeClone.git`
- **SSH**: `git@github.com:Cabrel-loic/YoutubeClone.git`

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

**Using HTTPS:**
```bash
git clone https://github.com/Cabrel-loic/YoutubeClone.git
cd YoutubeClone
```

**Using SSH:**
```bash
git clone git@github.com:Cabrel-loic/YoutubeClone.git
cd YoutubeClone
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
uv add -r requirements.txt
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


### Upload Size Limits

- Maximum video file size: **100 MB**
- Configured in Django settings:
  - `DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600` (100 MB)
  - `FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600` (100 MB)

## Running the Project

### 1. Apply Database Migrations

```bash
cd youtube
uv run manage.py migrate
```

### 2. Create Superuser (Admin Account)

```bash
uv run manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 3. Run Development Server

```bash
python manage.py runserver
```

The server will start at `http://localhost:8000`

## Database Models

### User Model
Uses Django's built-in `User` model with extensions:
- username
- email
- password (hashed)
- first_name, last_name (optional)

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

### ImageKit Upload Error

**Error**: `IMAGEKIT_PRIVATE_KEY or IMAGEKIT_PUBLIC_KEY not found`

**Solution**:
1. Sign up at https://imagekit.io
2. Get keys from dashboard
3. Add to `.env` file
4. Restart Django server

### Port Already in Use

**Error**: `OSError: [Errno 48] Address already in use`

**Solution**:
```bash
python manage.py runserver 8001  # Use different port
```
### Static Files Not Loading

**Error**: CSS/JS files returning 404

**Solution**:
```bash
uv run manage.py collectstatic
```

## Development Notes

### Adding a New Feature

1. Create models in appropriate app (`models.py`)
2. Create forms if needed (`forms.py`)
3. Create views (`views.py`)
4. Create/update templates
5. Add URLs to `urls.py`
6. Create migrations: `uv run manage.py makemigrations`
7. Apply migrations: `uv run manage.py migrate`
8. Test thoroughly
9. Update this README

### Running Tests

```bash
uv run manage.py test
```
