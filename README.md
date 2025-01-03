# 🛒EcommerceWebsite
A professional and scalable e-commerce platform built with Django following a simplified Clean Architecture approach.

This project demonstrates a modular and maintainable structure, complete with robust documentation, including use-case diagrams, ER diagrams, and a detailed functional requirements table.


# 🚀About the Project
EcommerceWebsite serves as a fully functional online store, designed with scalability, clean code principles, and separation of concerns in mind. The platform features user account management, admin controls, real-time chat, and seamless order and payment workflows.

![Ecommerce Website](https://github.com/user-attachments/assets/9fd1dee8-650d-43d8-b559-2499a2dc7dbb)

# Why This Project Stands Out
Simplified Clean Architecture: Clear separation into modules (domain, application, interface, infrastructure).
Professional Documentation: Use-case diagrams, ER diagrams, and requirement analysis tables.
Scalable Infrastructure: PostgreSQL, AWS S3, Redis, and WebSockets integration.
Real-Time Interactivity: WebSocket-based chat and live order updates.
# 📚 Documentation
1. Use-Case Diagrams
Admin Panel Use-Cases
Detailed workflows for managing products, users, and orders.
[link](https://miro.com/app/board/uXjVLFDsZIw=/?share_link_id=486442718649)

3. Client Use-Cases
Customer functionalities like checkout, order tracking, and account management.
[link](https://miro.com/app/board/uXjVLFMSWmw=/?share_link_id=364783148560)
5. ER Diagram
A visual representation of the database structure and relationships between entities like Users, Orders, Products, and Payments.
[link](https://miro.com/app/board/uXjVLFfztEY=/?share_link_id=13656592557)
7. Functional Requirements Table
A comprehensive table mapping system functionalities to inputs and outputs, ensuring clarity and traceability.
[link](https://docs.google.com/spreadsheets/d/1C8ueSmLesP9aJSpkPhJmyz85gJ8oASZDgeh0eb0EDaQ/edit?gid=0#gid=0)
All documentation is hosted on Miro and Google Sheets, emphasizing project clarity and pre-development planning.

# 🛠️ Architecture Overview
The project follows a simplified Clean Architecture pattern:

Domain: Core business logic and domain entities.
Application: Use-cases coordinating domain and interface logic.
Interface: Controllers, forms, and external-facing APIs.
Infrastructure: ORM models, repositories, and external services (e.g., AWS, Redis).
This structure ensures:

Separation of concerns
Scalability
Testability


# 💡Key Features

🔑 Authentication & Authorization
Custom User Model (AbstractBaseUser)
Email Verification & Password Reset
Role-based Permissions (Client, Agent, Manager)
📊 Admin Panel
User, Product & Order Management
Real-Time Chat Integration
Advanced Filtering & Pagination
🛍️ Shopping Experience
Persistent Shopping Cart
Address Autofill During Checkout
💬 Real-Time Chat
WebSocket-Powered Live Chat
Seamless Admin-Client Communication
💳 Payments & Orders
PayPal Payment Gateway
Order Status Tracking
🧩 Technologies Used
Backend: Django, Django Channels, PostgreSQL, Redis
Frontend: Tailwind CSS, JavaScript
Storage: AWS S3
Other Tools: WebSockets, Django Environ, Whitenoise


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
- **Others:** Django Environ, Whitenoise, WebSockets.


![Example Ecommerce Website](https://github.com/user-attachments/assets/283f5852-abf9-4bcc-a568-e17fa05ce718)

## Live Demo

The project is hosted on Render and can be accessed at the following link: [Live Demo](https://ecommercewebsite-zcj7.onrender.com).

*Please note:* The website might take a few moments to load initially, as it is hosted on Render’s free tier, which requires the server to "wake up" from an idle state.


## Getting Started

### Prerequisites
- Python, Node.js, PostgreSQL, Redis.

### Installation
1. Clone the repository and set up the virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
