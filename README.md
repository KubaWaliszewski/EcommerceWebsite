# EcommerceWebsite

EcommerceWebsite is a fully-featured e-commerce platform built using Django. The project is designed as a versatile and scalable online store, including user accounts, product management, order processing, and real-time chat functionality. It uses AWS S3 for static and media file storage, PostgreSQL as a database, Redis and WebSockets for live chat, and Tailwind CSS for responsive UI.
![Uploading image.png…]()

## Features

### 1. Account Management
- Custom user model with `AbstractBaseUser` and `CustomUserManager`.
- User authentication: login, registration, and email verification.
- Password reset functionality.
- User groups with role-specific permissions (Client, Agent, Manager).

### 2. Admin Panel
- Custom admin panel for managing products, categories, users, and orders.
- CRUD operations on products, users, and orders.
- Order status management with tracking of payment status.
- Chat management for customer interactions.
- Pagination, search, and filtering for effective data management.

### 3. Shopping Cart
- Add/remove products to/from the cart and update quantities.
- Persistent cart data across sessions using context processors.

### 4. Real-Time Chat
- WebSocket-based live chat for real-time communication.
- Admin and client chat interface powered by Django Channels, Daphne and Redis.
- Client-side JavaScript and WebSocket integration for smooth communication.

### 5. Client Area
- User profile management: update addresses, view order history, and manage account.
- Checkout process with address autofill from saved addresses.

### 6. Core
- Basic pages: Home, Contact, etc.
- Custom decorators for role-based access control.
- Site configuration to enable or disable customer chat

### 7. Orders and Payments
- Order management with order status and tracking.
- PayPal integration for online payments (sandbox mode supported).
- Signals for real-time payment status updates.

### 8. Shop
- Product listing with category filters and search functionality.
- Product detail pages with review options for purchased products.

### Technologies Used
- **Backend:** Django, Django Channels, PostgreSQL, Redis, AWS S3.
- **Frontend:** Tailwind CSS, JavaScript.
- **Others:** Django Environ, Whitenoise, crispy-tailwind, WebSockets.

## Getting Started

### Prerequisites
- Python, Node.js, PostgreSQL, Redis.

### Installation
1. Clone the repository and set up the virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
