# 🏦 Sistema Multiagente – Backend Django

Este proyecto implementa un sistema real para controlar:

- Trámites RENIEC
- Pagos (BN, BBVA, Interbank, KasNet)
- Fotografías (digitales / impresas)
- Múltiples sucursales
- Dashboard

## 🚀 Instalación (modo simple)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend disponible en: http://localhost:8000/api/
Admin: http://localhost:8000/admin/

## 🐳 Ejecución con Docker (recomendado)

```
docker-compose up --build
```

## 📡 Endpoints principales

- `GET /api/sucursales/`
- `POST /api/tramites/`
- `POST /api/pagos/`
- `POST /api/fotos/`
- `GET /api/dashboard/`

## 🤝 Autenticación

Usa el login de Django (`/admin/` o `/api-auth/login/`)
