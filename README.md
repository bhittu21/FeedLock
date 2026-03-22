<!-- Project FeedLock - RSS Feed Aggregator -->

<div align="center">

# Project FeedLock

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()

*A powerful RSS feed aggregator that fetches and displays news from multiple sources with search and pagination capabilities.*

</div>

---

## 📰 Project Overview

Project FeedLock is a Flask-based web application that aggregates RSS feeds from multiple prominent news sources into a single, user-friendly interface. It provides real-time fetching of articles from leading financial and technology news outlets, enabling users to stay updated with the latest news across different platforms without visiting each site individually.

### What It Does

- **Multi-Source Aggregation**: Fetches articles from Yahoo Finance, Hacker News, Wall Street Journal, and CNBC
- **Smart Sorting**: Automatically sorts articles by publication date (newest first)
- **Search Functionality**: Full-text search across all article titles
- **Pagination**: Easy navigation through large collections of articles
- **Responsive Design**: Clean, accessible interface that works on all devices

---

## ✨ Features

### Core Features

| Feature | Description |
|---------|-------------|
| **Real-time RSS Fetching** | Dynamically fetches articles from multiple RSS feed sources on each request |
| **Article Search** | Search through article titles with case-insensitive query matching |
| **Pagination** | Browse through articles with easy-to-use pagination (10 articles per page) |
| **Date-based Sorting** | Articles automatically sorted by publication date (newest first) |
| **Multiple Source Support** | Aggregates from Yahoo Finance, Hacker News, Wall Street Journal, and CNBC |

### Additional Features

- **Accessibility Support**: ARIA labels and screen reader-friendly HTML
- **Skip Navigation**: Keyboard-accessible skip links
- **Error Handling**: Graceful handling of empty search results and feed parsing errors
- **Responsive Layout**: Mobile-friendly CSS Grid/Flexbox design

---

## � Prerequisites

Before running this application, ensure you have the following installed:

| Requirement | Version | Description |
|-------------|---------|-------------|
| **Python** | 3.8 or higher | Programming language |
| **pip** | Latest version | Package installer for Python |
| **Flask** | 2.3+ | Web framework |
| **feedparser** | Latest version | RSS/Atom feed parser |

### Required Dependencies

```
Flask>=2.3.0
feedparser>=6.0.0
```

---

## 🚀 Installation Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/bhittu21/project-feedlock.git
cd project-feedlock
```

### Step 2: Create a Virtual Environment

**On Windows:**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note**: If you don't have a `requirements.txt`, install dependencies manually:
```bash
pip install Flask feedparser
```

### Step 4: Run the Application

```bash
python main.py
```

The application will start on `http://127.0.0.1:5000`

---

## 📖 Usage Examples

### Running the Application

After installation, run:

```bash
python main.py
```

Open your browser and navigate to: **http://127.0.0.1:5000**

---

### API Usage Examples

#### 1. Home Page - View Latest Articles

```bash
curl http://127.0.0.1:5000/
```

**Expected Response:** HTML page with paginated articles (10 per page)

---

#### 2. Browse Specific Page

```bash
curl "http://127.0.0.1:5000/?page=2"
```

**Response:** Page 2 of articles with navigation links

---

#### 3. Search with Query Parameter

```bash
curl "http://127.0.0.1:5000/search?query=oil"
```

**Expected Response:**
```html
<!-- HTML page showing search results for "oil" -->
<!-- Example: 5 results found -->
```

---

#### 4. Search Without Parameters

```bash
curl http://127.0.0.1:5000/search
```

**Expected Response:** Returns "0 results found" (empty query returns no results)

---

#### 5. Search with No Results

```bash
curl "http://127.0.0.1:5000/search?query=nonexistentkeyword123"
```

**Expected Response:** "No Results Found" page

---

## 📡 API Endpoints Documentation

### Endpoint 1: Home Page (`/`)

**Description:** Displays aggregated articles from all RSS feeds with pagination.

| Component | Details |
|-----------|---------|
| **URL** | `/` |
| **Method** | `GET` |
| **Parameters** | `page` (optional, default: 1) |

**Example Request:**
```
GET http://127.0.0.1:5000/
GET http://127.0.0.1:5000/?page=3
```

**Response Format:**
```html
<!DOCTYPE html>
<html>
    <head><title>Latest News - Project FeedLock</title></head>
    <body>
        <div class="articles">
            <article class="article-card">
                <h2><a href="...">Article Title</a></h2>
                <div class="article-meta">
                    <span class="article-source">Source Name</span>
                    <span class="article-date">2026-03-22T16:00:00Z</span>
                </div>
            </article>
        </div>
        <nav class="pagination">
            <span class="current-page">Page 1 of 13</span>
            <a href="/?page=2">Next</a>
        </nav>
    </body>
</html>
```

---

### Endpoint 2: Search (`/search`)

**Description:** Search articles by query string.

| Component | Details |
|-----------|---------|
| **URL** | `/search` |
| **Method** | `GET` |
| **Parameters** | `query` (optional, default: empty string) |

**Example Requests:**
```
GET http://127.0.0.1:5000/search?query=technology
GET http://127.0.0.1:5000/search?query=stocks
```

**Query Parameter Handling:**
- **Case-insensitive**: Search is performed on lowercase converted strings
- **Title-only**: Searches article titles only
- **Empty query**: Returns 0 results (no articles returned)
- **Whitespace handling**: Leading/trailing whitespace is trimmed

**Response Format:**
```html
<!DOCTYPE html>
<html>
    <head><title>Search Results - Project FeedLock</title></head>
    <body>
        <div class="search-results-header">
            <h1>Search Results For: <span class="search-query">oil</span></h1>
            <p class="results-count">5 result(s) found</p>
        </div>
        <div class="articles">
            <article class="article-card">
                <h2><a href="...">Article Title</a></h2>
                <div class="article-meta">
                    <span class="article-source">Yahoo Finance</span>
                    <span class="article-date">2026-03-22T16:33:00Z</span>
                </div>
            </article>
        </div>
    </body>
</html>
```

**Response Structure:**

| Field | Type | Description |
|-------|------|-------------|
| `search-query` | string | The search query entered by user |
| `results-count` | string | Number of articles found (e.g., "5 result(s) found") |
| `articles` | array | List of article objects |
| `article.title` | string | Article headline |
| `article.link` | string | URL to full article |
| `article.source` | string | News source name |
| `article.date` | string | Publication date (ISO 8601 format) |

---

## ⚙️ Configuration Details

### Customizing RSS Feed Sources

To modify the RSS feed sources, edit the `RSS_FEEDS` dictionary in `main.py`:

```python
RSS_FEEDS = {
    'Source Name': 'https://example.com/rss/feed.xml',
    'Another Source': 'https://another.com/feed.rss',
    # Add more feeds here...
}
```

### Configuration Options

| Setting | Location | Description | Default |
|---------|----------|-------------|---------|
| **RSS Feeds** | `main.py` line 6-11 | Dictionary of source names and URLs | Yahoo Finance, Hacker News, WSJ, CNBC |
| **Articles per page** | `main.py` line 29 | Number of articles per page | 10 |
| **Debug mode** | `main.py` line 55 | Flask debug setting | True |
| **App host** | `main.py` line 55 | Server binding | 127.0.0.1 |
| **App port** | `main.py` line 55 | Server port | 5000 |

### Adding New RSS Feeds

1. Open `main.py`
2. Locate the `RSS_FEEDS` dictionary (lines 6-11)
3. Add a new entry:
   ```python
   'Your Source Name': 'https://your-feed-url.com/rss',
   ```
4. Save the file
5. The new feed will be automatically included on the next page refresh

---

## 🧪 Testing Information

### Testing the Application

#### 1. Verify Application Starts

```bash
python main.py
```

Expected output:
```
 * Serving Flask app 'main'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

#### 2. Test Home Page

Open browser to `http://127.0.0.1:5000`

**Verification:**
- [ ] Page loads successfully
- [ ] Articles are displayed
- [ ] Articles are sorted by date (newest first)
- [ ] Pagination is visible

#### 3. Test Pagination

Navigate to `http://127.0.0.1:5000/?page=2`

**Verification:**
- [ ] Different set of articles displayed
- [ ] Previous/Next links work

#### 4. Test Search Functionality

Navigate to `http://127.0.0.1:5000/search?query=technology`

**Verification:**
- [ ] Search results page loads
- [ ] Only matching articles shown
- [ ] Result count is accurate

#### 5. Test Empty Search

Navigate to `http://127.0.0.1:5000/search`

**Verification:**
- [ ] "No Results Found" message displayed

#### 6. Test with curl (Command Line)

```bash
# Test home page
curl -s http://127.0.0.1:5000/ | findstr "article-card"

# Test search
curl -s "http://127.0.0.1:5000/search?query=stocks" | findstr "results-count"

# Test pagination
curl -s "http://127.0.0.1:5000/?page=2" | findstr "Page"
```

---

## 🤝 Contributing Guidelines

We welcome contributions to Project FeedLock! Here's how you can help:

### How to Contribute

1. **Fork the Repository**
   Click the "Fork" button on the GitHub repository page.

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/project-feedlock.git
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**
   Implement your feature or bug fix.

5. **Test Your Changes**
   Ensure all tests pass and the application runs correctly.

6. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

7. **Push to GitHub**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create Pull Request**
   Open a pull request on the original repository.

### Coding Standards

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Test edge cases

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026 Project FeedLock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👤 Author

### Sheikh Abir Ali

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-bhittu21-181717?style=for-the-badge&logo=github)](https://github.com/bhittu21)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-sheikhabirali-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/sheikhabirali)
[![Portfolio](https://img.shields.io/badge/Portfolio-sheikhabirali.netlify.app-FF5722?style=for-the-badge&logo=netlify)](https://sheikhabirali.netlify.app/)
[![Email](https://img.shields.io/badge/Email-contact@sheikhabirali.netlify.app-D14836?style=for-the-badge&logo=gmail)](mailto:contact@sheikhabirali.netlify.app)

</div>

---

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [feedparser](https://feedparser.readthedocs.io/) - RSS parsing library
- [Python](https://www.python.org/) - Programming language
- All RSS feed providers: Yahoo Finance, Hacker News, Wall Street Journal, CNBC

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

*Made with ❤️ by [Sheikh Abir Ali](https://github.com/bhittu21)*

</div>
