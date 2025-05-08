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

<img width="1123" alt="Screenshot 2025-05-08 at 2 19 56 AM" src="https://github.com/user-attachments/assets/cd7e1fe6-6536-4b8f-afe9-ad0abd1683c3" />

## Licence

This project is open-sourced under MIT License.
