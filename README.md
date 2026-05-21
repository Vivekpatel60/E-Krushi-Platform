# E-Krushi Data Platform

A Django-based agricultural data management platform that allows farmers to register and submit their agricultural data, while providing administrators with tools to review and approve submissions.

## Features

### For Farmers (Users):
- **Registration**: Farmers can register with their name, username, email, and password
- **Data Entry**: Submit detailed agricultural information including:
  - Personal details (name, phone, location)
  - Crop information (type, land area, dates)
  - Agricultural practices (irrigation, fertilizers, pesticides)
- **Data Management**: View and edit their submitted data
- **Status Tracking**: See approval status of their submissions

### For Administrators:
- **Data Review**: View all submitted agricultural data
- **Approval System**: Approve or manage farmer submissions
- **User Management**: Access Django admin panel for advanced management
- **Data Display**: Approved data is displayed publicly

### Public Features:
- **Public Data View**: Anyone can view approved agricultural data
- **Home Page**: Overview of recent approved submissions

## Installation & Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Create Superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

4. **Run Development Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### For Farmers:
1. Register on the platform with your name and details
2. Login to access your dashboard
3. Add agricultural data using the "Add New Data" button
4. View and edit your submissions from the dashboard
5. Track approval status of your data

### For Administrators:
1. Login to admin panel with superuser credentials
2. Access "Admin Dashboard" to review farmer submissions
3. Approve data submissions to make them publicly visible
4. Use Django admin panel for advanced user and data management

## Form Validation

The platform includes comprehensive form validation:
- **Registration**: Username uniqueness, email validation, password strength
- **Agricultural Data**: Phone number format, land area validation, date consistency
- **Error Display**: Clear error messages with visual indicators

## Database Schema

- **User**: Extended Django user model with first/last name
- **FarmerData**: Agricultural data with approval workflow
- **Admin Interface**: Django admin for data management

## Security Features

- User authentication and authorization
- CSRF protection
- Form validation and sanitization
- Admin-only access to sensitive operations

## Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (default, can be changed)
- **Frontend**: Bootstrap 5.1.3
- **Authentication**: Django built-in auth system