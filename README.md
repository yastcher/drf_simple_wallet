# Wallet Test Project

## Installation

### Local Installation

1. Ensure you have Docker and Docker Compose installed.

2. Clone the repository:
   ```bash
   git clone https://github.com/yastcher/drf_simple_wallet.git
   cd drf_simple_wallet
   ```

3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

4. Set up environment variables. Rename .env.example to .env and set the following variables
   ```env
   SUPERUSER=your_username
   SUPERUSER_PASSWORD=your_password
   ```
5. Start mysql server and apply database migrations:
   ```bash
   docker compose up mysqldb -d --build
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver 127.0.0.1:8000
   ```

8. Access the admin panel at http://127.0.0.1:8000/admin/
Access the API at http://127.0.0.1:8000/api/

9. For run the tests:
   ```bash
   pytest -s -v --cov --cov-report=term
   ```

## Running with Docker

### Installation and Startup
1. Ensure you have Docker and Docker Compose installed.

2. Clone the repository:
   ```bash
   git clone https://github.com/yastcher/drf_simple_wallet.git
   cd drf_simple_wallet
   ```

3. Set up environment variables. Rename .env.example to .env and set the following variables
   ```env
   DB_HOST=mysqldb
   SUPERUSER=your_username
   SUPERUSER_PASSWORD=your_password
   ```

4. Start service in docker:
   ```bash
   docker compose up -d --build
   ```
