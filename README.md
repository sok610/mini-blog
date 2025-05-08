# Mini Blog 📝

A minimalist blogging platform built with Django and Tailwind CSS.

## 🔧 Features

- ✅ User registration, login, and logout using Django's built-in auth system
- ✅ Create, edit, and delete posts (CRUD)
- ✅ Search posts by title or content
- ✅ Only authenticated users can create or edit posts
- ✅ My Page: manage your own posts in one place
- ✅ Clean UI with Tailwind CSS
- ✅ Results count and search type selector

## 🛠️ Tech Stack

- **Backend**: Django 5.2
- **Frontend**: HTML + Tailwind CSS
- **Auth**: Django Sessions
- **Search**: Django ORM with `icontains`
- **Database**: SQLite (default)

## 🚀 Getting Started

Clone the repository and set up a virtual environment:

```zshrc
git clone https://github.com/sok610/mini-blog.git
cd mini-blog
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
