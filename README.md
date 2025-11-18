# Django Chatbot Application

A modern Django web application that provides an interactive chatbot interface powered by Google's Gemini AI. Users can ask questions, receive AI-generated responses, and view their conversation history.

## Features

- 🤖 **AI-Powered Chat**: Interact with Google's Gemini 2.5 Flash model
- 💬 **Conversation History**: View all past conversations with pagination
- 🗑️ **History Management**: Delete individual conversation entries
- 💾 **Persistent Storage**: SQLite database to store all Q&A pairs
- 🎨 **Modern UI**: Clean and responsive Bootstrap-based interface
- ⌨️ **Keyboard Support**: Submit questions using Enter key

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- A Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd chatgptApp
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirments.txt
   ```

5. **Set up environment variables**
   
   Create a `.env` file in the project root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

6. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server**
   ```bash
   python manage.py runserver
   ```

9. **Open your browser**
   
   Navigate to `http://127.0.0.1:8000/` to access the application.

## Configuration

### Environment Variables

The application requires the following environment variable:

- `GEMINI_API_KEY`: Your Google Gemini API key

Create a `.env` file in the project root with your API key:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

The application uses `python-dotenv` to load environment variables automatically.

## Usage

### Home Page

1. Navigate to the home page (`/`)
2. Enter your question in the input field
3. Click "Send" or press Enter to submit
4. View the AI-generated response below

### Conversation History

1. Click on "History" in the navigation bar
2. Browse through your past conversations (paginated)
3. Delete individual entries using the delete button

### Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/` to:
- View and manage all conversation records
- Perform administrative tasks

## Project Structure

```
chatgptApp/
├── chatbot/                 # Main application
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   ├── base.html      # Base template
│   │   ├── home.html      # Home page
│   │   ├── history.html   # History page
│   │   └── navbar.html    # Navigation bar
│   ├── models.py          # Database models (Past model)
│   ├── views.py           # View functions
│   └── urls.py            # URL routing
├── chatgptApp/            # Django project settings
│   ├── settings.py        # Project settings
│   └── urls.py            # Root URL configuration
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
├── requirments.txt        # Python dependencies
└── .env                   # Environment variables (create this)
```

## Technologies Used

- **Django 5.2.7**: Web framework
- **Google Gemini API**: AI model integration
- **SQLite**: Database
- **Bootstrap**: Frontend styling
- **python-dotenv**: Environment variable management
- **requests**: HTTP library for API calls

## API Integration

The application uses Google's Gemini 2.5 Flash model via the Generative Language API:

- **Endpoint**: `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent`
- **Method**: POST
- **Authentication**: API key via `x-goog-api-key` header

## Database Model

The `Past` model stores conversation history:
- `question`: CharField (max 250 characters)
- `answer`: TextField (max 5000 characters)
- Auto-generated `id` and timestamps

## Development

### Running Tests
```bash
python manage.py test
```

### Making Migrations
After modifying models:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files (for production)
```bash
python manage.py collectstatic
```

## Security Notes

⚠️ **Important**: Before deploying to production:

1. Change `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS` with your domain
4. Use environment variables for sensitive data
5. Consider using a production database (PostgreSQL, MySQL)
6. Set up proper static file serving
7. Enable HTTPS

## Troubleshooting

### API Key Issues
- Ensure your `.env` file is in the project root
- Verify the API key is correct and active
- Check that `python-dotenv` is installed

### Database Issues
- Run `python manage.py migrate` to apply migrations
- Delete `db.sqlite3` and re-run migrations if needed

### Port Already in Use
- Change the port: `python manage.py runserver 8001`
- Or stop the process using port 8000

---

**Note**: This project uses Google's Gemini API, not OpenAI's ChatGPT, despite the project name. The application is branded as "LinaAI" in the user interface.

