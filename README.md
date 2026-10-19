# Payment Gateway Application (Django & Vanilla JavaScript)

A simulation of a payment gateway integration using Django, Razorpay API, and Vanilla JavaScript.

## Features
- Order creation on server side using Razorpay client
- Seamless checkout modal powered by Razorpay Checkout JS
- Server-side signature verification and automatic payment capture
- Payment transaction status tracking in database (Created, Success, Failed)
- Environment variable protection for credentials and secret keys

## Tech Stack
- **Backend:** Python, Django 6.1
- **Payment Gateway:** Razorpay Python SDK
- **Frontend:** Vanilla JavaScript, HTML5, CSS3
- **Configuration:** Python-dotenv

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/LIKHIT123498/Payment-Gateway-Application.git
cd Payment-Gateway-Application
```

### 2. Set up virtual environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Inside the `dj_razorpay/` directory, copy `.env.example` to `.env`:
```bash
cp dj_razorpay/.env.example dj_razorpay/.env
```
Open `dj_razorpay/.env` and insert your credentials:
```ini
DJANGO_SECRET_KEY=your-django-secret-key
RAZOR_KEY_ID=your-razorpay-key-id
RAZOR_KEY_SECRET=your-razorpay-key-secret
```

### 5. Run Migrations & Start Server
```bash
python dj_razorpay/manage.py migrate
python dj_razorpay/manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.
