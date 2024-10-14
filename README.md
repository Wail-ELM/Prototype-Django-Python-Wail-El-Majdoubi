# Wail El Majdoubi

# Python/Django Web Prototype: Blog with Authentication

This project is a prototype of a simple blog web application developed with Python and the Django framework. It was created for the purpose of experimenting and learning the fundamentals of web development with Python and Django.

## Features

*   **Authentication system:**
    *   User login and signup.
    *   Password management with hashing and confirmation.
    *   Feedback messages for login and signup actions.
    *   Redirection to the appropriate page after login and signup.
*   **Blog post management:**
    *   Create, read, update, and delete (CRUD) blog posts.
    *   Display all posts and posts by the logged-in user.
    *   Restrict editing and deleting posts to their authors.


## Project Structure

```
myproject_python/
├── myproject_python/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/
│   ├── migrations/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── registration/
│   │   ├── login.html
│   │   └── signup.html
│   └── blog/
│       ├── all_articles.html
│       ├── my_articles.html
│       ├── article_detail.html
│       ├── add_article.html
│       ├── edit_article.html
│       └── delete_article.html
└── manage.py
```

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    ```bash
    # Windows (cmd)
    venv\Scripts\activate

    # Windows (PowerShell)
    .\venv\Scripts\activate

    # macOS/Linux
    source venv/bin/activate
    ```

4.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

1.  **Access the application:** Open your web browser and go to the address `http://127.0.0.1:8000/`.

2.  **Log in or sign up:** Use the links in the navigation bar to log in or sign up.

3.  **Manage articles:** Once logged in, you can add, edit, and delete articles.

## Technologies Used

*   Python 3
*   Django 5.1.1
*   Bootstrap 4.5.2
*   SQLite

## Resources

*   **Django documentation:** [https://docs.djangoproject.com/en/5.1/](https://docs.djangoproject.com/en/5.1/)
*   **Django tutorial:** [https://docs.djangoproject.com/en/5.1/intro/tutorial01/](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)
*   **Bootstrap documentation:** [https://getbootstrap.com/docs/4.5/getting-started/introduction/](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
*   **Python documentation:** [https://docs.python.org/3/](https://docs.python.org/3/)
*   **SQLite documentation:** [https://www.sqlite.org/docs.html](https://www.sqlite.org/docs.html)
*   **W3Schools Python tutorial:** [https://www.w3schools.com/python/](https://www.w3schools.com/python/)
*   **ChatGPT:** [https://chat.openai.com/](https://chat.openai.com/)


