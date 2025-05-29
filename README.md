# UPCSG Backend

## Overview
This repository contains the backend for the University of the Philippines (Cebu) Computer Science Guild (UPCSG) system. It is a Django-based RESTful API server that manages users, content, merchandise, orders, helpdesk, and officer board functionalities. The backend is designed for scalability, security, and ease of deployment, supporting both local and cloud-based (AWS) environments.

## Technology Stack
- **Language:** Python 3.12
- **Framework:** Django 5.1, Django REST Framework
- **Authentication:** JWT (SimpleJWT), dj-rest-auth, django-allauth
- **Database:** PostgreSQL (via dj-database-url)
- **Containerization:** Docker, Gunicorn
- **Cloud/Infra:** AWS (EC2, VPC, IAM, ECR), Terraform, cloud-init

## Directory Structure
```
├── main/         # Django project settings, URLs, WSGI/ASGI
├── user/         # User management (custom user model, auth, registration)
├── cms/          # Content management system
├── merch/        # Merchandise management
├── order/        # Order processing
├── help/         # Helpdesk and support
├── officers/     # Officer board management
├── scripts/      # Utility scripts
├── requirements.txt
├── Dockerfile
├── main.tf       # Terraform infrastructure
├── cloud-init.sh # Cloud deployment script
├── bootstrap.py  # Local setup script
└── manage.py
```

## Setup & Installation

### Prerequisites
- Python 3.12+
- PostgreSQL database
- Docker (optional, for containerized deployment)
- AWS CLI & Terraform (for cloud deployment)

### Local Development
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd upcsg-backend
   ```
2. **Install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Set environment variables:**
   - Create a `.env` file in the root directory with:
     ```env
     SUPABASE_DB_CONNECTION_STRING=postgres://<user>:<password>@<host>:<port>/<db>
     DJANGO_SECRET_KEY=your-secret-key
     ```
4. **Run migrations and collect static files:**
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```
5. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

### Using Docker
1. **Build and run the container:**
   ```bash
   docker build -t upcsg-backend .
   docker run -d -p 8080:8080 --env-file .env upcsg-backend
   ```
   The app will be available at `http://localhost:8080`.

## API Endpoints
- `api/user/`     – User registration, login, profile
- `api/cms/`      – Content management
- `api/help/`     – Helpdesk and support
- `api/merch/`    – Merchandise catalog
- `api/order/`    – Order management
- `api/board/`    – Officer board
- `admin/`        – Django admin panel

Authentication is via JWT. See the `user` app for custom serializers and authentication logic.

## Deployment

### AWS & Terraform
- Infrastructure is defined in `main.tf` (VPC, EC2, IAM, Security Groups, etc.).
- Use `terraform init` and `terraform apply` to provision resources.
- The EC2 instance uses `cloud-init.sh` to install Docker, pull the backend image from ECR, and configure Nginx as a reverse proxy with SSL (Let's Encrypt).

### cloud-init
- `cloud-init.sh` automates server setup, Docker image deployment, Nginx configuration, and SSL certificate issuance.
- Ensure your domain DNS points to the EC2 instance before running certbot.

## Environment Variables
- `SUPABASE_DB_CONNECTION_STRING` – PostgreSQL connection string
- `DJANGO_SECRET_KEY` – Django secret key
- (Other variables as needed for third-party integrations)

## Running Tests
```bash
python manage.py test
```

## Contribution Guidelines
- Fork the repository and create a feature branch.
- Follow PEP8 and Django best practices.
- Write tests for new features.
- Submit a pull request with a clear description.

## License
This project is for academic and organizational use by UPCSG.

---
For more details, see the code in each app directory and the inline documentation.
