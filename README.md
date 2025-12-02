# Baby-Led Weaning Tracker (BLW Tracker)
### CIDM 6325 – Final Project by Alexis Lopez

A Django + Bootstrap web app designed to help parents track Baby-Led Weaning (BLW) progress.  
Users can log **Babies**, **Foods**, **Meals**, and **Reactions**, including images, notes, and allergen details.  
The system supports a simple user interface, media uploads, and Django Admin management tools.

---

## 🚀 Features Overview

- **Babies:** Add and manage baby profiles with photo and notes  
- **Foods:** Track foods, categories, allergen status, and upload images  
- **Meals:** Record what a baby ate, link multiple foods to one meal  
- **Reactions:** Track potential allergic or negative reactions  
- **Authentication:** Login/logout system with role-based access  
- **Bootstrap Styling:** Clean, responsive UI with consistent navigation  
- **Admin Customization:** Search, filters, inlines, and list displays for efficiency  
- **Static & Media Files:** Supports file uploads and static styling  

---

## 🧠 Business Use Case
Parents or caregivers can easily track a baby’s weaning progress and reactions to specific foods.  
This helps identify allergens early and document feeding history — all within a secure, easy-to-use web app.

---

## 🧩 Rubric Mapping

| Rubric Area | Implementation Summary |
|--------------|------------------------|
| **Part A – Django Admin** | Configured for Baby, Food, Meal, and Reaction models with search, filters, and list displays |
| **Part B – Authentication** | Enabled login/logout and restricted access for certain pages |
| **Part C – Peer Review** | Code and UI structured for readability and security evaluation |
| **Part D – Blog Post: Productivity vs Security** | Posted on project blog to discuss Django admin usability |
| **Part E – Static/Media** | Enabled image uploads and Bootstrap for layout styling |

---

## ⚙️ Installation & Setup

```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate  # (Windows)

# 2. Install dependencies
python -m pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Create a superuser
python manage.py createsuperuser

# 5. Start the server
python manage.py runserver
Open your browser and visit:
- **App:** http://127.0.0.1:8000/blw/
- **Admin:** http://127.0.0.1:8000/admin/

---

## 🧰 Project Structure

cidm6325_blog/
├── blogproject/urls.py
├── blw/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   └── templates/blw/
│       ├── base.html
│       ├── foods/
│       ├── meals/
│       └── reactions/
├── static/
├── media/
├── requirements.txt
├── manage.py
└── README.md

---

## 💡 Notes
- This project is for educational purposes (CIDM 6325).  
- `DEBUG=True` for development; disable in production.  
- Uploaded images are stored in the `/media/` directory.  
- Bootstrap 5 CDN used for layout and styling.  

---

## 👩‍💻 Author
**Alexis Lopez**  
West Texas A&M University  
Master’s in Computer Information Systems & Business Analytics  
