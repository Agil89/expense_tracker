# Expense Tracker API

This project is a Django-based API for managing expenses. The API supports basic CRUD operations, expense filtering by date range, and category-wise summaries. Authentication and authorization are not required.

---

## **Project Setup**

### **Prerequisites**
- Python 3.9+
- Django 4.0+
- Django REST Framework
- PostgreSQL (or any preferred database)

### **Installation Steps**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:
   - Update the database settings in `settings.py`.

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (optional, for admin panel access):
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## **API Endpoints**

### **User Management**
- **Create User**
  - **Endpoint**: `POST /users/`
  - **Body**:
    ```json
    {
        "username": "testuser",
        "email": "testuser@example.com"
    }
    ```

- **List Users**
  - **Endpoint**: `GET /users/`

### **Expense Management**
- **Create Expense**
  - **Endpoint**: `POST /expenses/`
  - **Body**:
    ```json
    {
        "user": 1,
        "title": "Groceries",
        "amount": 50.5,
        "date": "2024-12-12",
        "category": "Food"
    }
    ```

- **List Expenses**
  - **Endpoint**: `GET /expenses/`

- **Retrieve, Update, or Delete Expense**
  - **Endpoint**: `GET /expenses/{id}/`
  - **Methods**: `GET`, `PUT`, `DELETE`

- **List Expenses by Date Range**
  - **Endpoint**: `GET /expenses/by-date-range/`
  - **Query Params**:
    - `user_id` (required)
    - `start_date` (required)
    - `end_date` (required)
  - **Example**:
    ```plaintext
    /expenses/by-date-range/?user_id=1&start_date=2024-12-01&end_date=2024-12-31
    ```

- **Category Summary**
  - **Endpoint**: `GET /expenses/category-summary/`
  - **Query Params**:
    - `user_id` (required)
    - `month` (required)
    - `year` (required)
  - **Example**:
    ```plaintext
    /expenses/category-summary/?user_id=1&month=12&year=2024
    ```

---

## **Validations**
- Expense amount must be positive.
- User must exist before creating an expense.

---

## **Project Structure**

```
project/
├── manage.py
├── requirements.txt
├── users/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── expenses/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

---

## **Testing**

### **Using Postman**
1. Create a user by sending a `POST` request to `/users/`.
2. Use the created user's `id` to create expenses using `POST /expenses/`.
3. Test other endpoints like listing expenses, filtering by date range, and viewing category summaries.

### **Using Django Admin Panel**
1. Access the admin panel at `http://127.0.0.1:8000/admin/`.
2. Manage users and expenses directly.

---

## **Future Enhancements**
- Add authentication and authorization.
- Implement pagination for large datasets.
- Add support for exporting reports (e.g., CSV, PDF).
- Integrate with a frontend framework for a complete user experience.

---
