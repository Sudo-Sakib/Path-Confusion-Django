# Django Path Confusion Demo 🚀

This is a **simple Django web application** demonstrating **Path Confusion vulnerabilities**.

## 🛠 Features:
✅ Allows accessing `/profile/` dynamically with extra path segments.  
✅ Demonstrates how cache & web servers interpret paths differently.  
✅ Useful for security research on **Web Cache Deception (WCD)**.

## ⚠️ Vulnerability:
- The `/profile/` route improperly accepts **extra path segments**.
- This allows **path confusion attacks**, where `/profile.css` still serves private data.

## 🚀 Setup & Run:
```bash
git clone https://github.com/yourusername/Django-Path-Confusion-Demo.git
cd Django-Path-Confusion-Demo
python manage.py runserver
