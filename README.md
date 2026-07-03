# CraftsCove

A **Django marketplace** for crafts and handmade goods — user accounts, product listings, and a browsable storefront.

![Django](https://img.shields.io/badge/Django-Python-092E20?style=flat-square&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/DB-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

## Features

- Custom **user model** (`users` app)
- Product / listing management (`mainsite` app)
- SQLite database with bundled `db.sqlite3` for local exploration
- Split Django apps for auth vs. catalog concerns

## Tech stack

- **Django** — MVT
- **SQLite** — local development
- **JavaScript** — frontend interactions

## Quick start

```bash
cd Jeffrey/CraftsCove
pip install django
python manage.py runserver
```

Visit **http://127.0.0.1:8000**

## Project layout

```
Jeffrey/CraftsCove/
  manage.py
  users/         # Custom user accounts
  mainsite/      # Storefront & product logic
  db.sqlite3     # Sample data
```

> **Note:** The Django project lives under `Jeffrey/CraftsCove/` — `cd` there before running management commands.

---

[malimba](https://github.com/malimba)
