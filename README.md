# FinAPI - Financial Insights REST API

API REST desarrollada con Django y Django REST Framework.
Permite gestionar portfolios, activos financieros y transacciones, con autenticación JWT.

## 🚀 Tecnologías
- Django 5.x
- Django REST Framework
- SimpleJWT
- DRF Spectacular

## 📦 Endpoints principales
- `/api/users/register/` → Registro de usuarios
- `/api/users/token/` → Autenticación JWT
- `/api/portfolios/` → CRUD de portfolios
- `/api/assets/` → CRUD de activos
- `/api/transactions/` → Registro de compras y ventas
- `/api/transactions/summary/{portfolio_id}/` → Resumen de portafolio

## 🧑‍💻 Instalación
```bash
git clone https://github.com/TU_USUARIO/finapi.git
cd finapi
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
