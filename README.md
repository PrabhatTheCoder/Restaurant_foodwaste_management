# 🍽️ Restaurant Food Waste Management System

This project provides a web-based system for managing and minimizing food waste in restaurants. The platform helps restaurants track, analyze, and take actionable steps to reduce excess food production and disposal. Built with Django and PostgreSQL, it allows users to log food waste data, view analytics, and generate insights for sustainable decision-making.

---


## 🚀 Features

- 🔐 **Authentication** – Secure login/logout for staff.
- 🍛 **Waste Logging** – Track daily food waste by item, quantity, reason, and date.
- 📊 **Analytics Dashboard** – Visual insights into waste patterns.
- 📅 **Historical Reports** – Filterable views by date, item, or category.
- 📥 **CSV Upload** – Bulk import of historical data.
- 📤 **Export** – Export reports to CSV for offline analysis.
- ⚙️ **Admin Interface** – Manage users, items, categories, and permissions.

---

## 🛠️ Tech Stack

| Layer       | Technology                |
|-------------|---------------------------|
| Backend     | Django (Python)           |
| Database    | PostgreSQL                |
| Frontend    | HTML5, CSS3, Bootstrap    |
| Caching     | Redis                     |
| Task Queue  | Celery                    |
| Web Server  | Nginx                     |
| Deployment  | Docker, AWS (EC2, RDS)    |
| CI/CD       | GitHub Actions


## ⚙️ CI/CD Pipelines

This project includes **end-to-end CI/CD automation** for seamless development and deployment.

### ✅ CI – Continuous Integration
- Run unit tests and migrations on every push
- Linting and code quality checks
- Build Docker images
- Validate environment configuration

### 🚀 CD – Continuous Deployment
- Auto-deploy to AWS (EC2/Elastic Beanstalk/Fargate)
- Push Docker images to AWS ECR
- Restart services on deployment (via SSH or ECS)
- Secure secrets handling using GitHub Actions Secrets / AWS SSM

> Example CI/CD tool used: **GitHub Actions**

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/PrabhatTheCoder/Restaurant_foodwaste_management.git
cd Restaurant_foodwaste_management
