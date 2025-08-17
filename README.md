# .MP4 — Blog de música indie argentina

## Rutas principales
- `/home`, `/about/`, `/pages/`, `/accounts/login/`, `/accounts/signup/`, `/accounts/profile/`, `/admin/`

## Paso a paso para no olvidar jeje:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

> Nota: `db.sqlite3` y `media/` están en `.gitignore`.

## Link video: Jam - https://jam.dev/c/5af19cb7-37bb-4fba-b4a4-97e4e4df06a8