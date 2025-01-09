# 🛒EcommerceWebsite
A professional and scalable e-commerce platform built with Django following a simplified Clean Architecture approach.

This project demonstrates a modular and maintainable structure, complete with robust documentation, including use-case diagrams, ER diagrams, and a detailed functional requirements table.


# 🚀About the Project
EcommerceWebsite serves as a fully functional online store, designed with scalability, clean code principles, and separation of concerns in mind. The platform features user account management, admin controls, real-time chat, and seamless order and payment workflows.

<img src="https://github.com/user-attachments/assets/9cdd1d9a-25c0-47eb-ae4c-827fe24294a8" alt="Home " >

# 🌐Why This Project Stands Out
**Simplified Clean Architecture**

+ Clear separation into modules (domain, application, interface, infrastructure).
+ Professional Documentation: Use-case diagrams, ER diagrams, and requirement analysis tables.
+ Scalable Infrastructure: PostgreSQL, AWS S3, Redis, and WebSockets integration.
+ Real-Time Interactivity: WebSocket-based chat and live order updates.
# 📚 Documentation
+ Use-Case Diagrams
Admin Panel Use-Cases: [link](https://miro.com/app/board/uXjVLFDsZIw=/?share_link_id=486442718649)

  *Detailed workflows for managing products, users, and orders.*


+ Client Use-Cases: [link](https://miro.com/app/board/uXjVLFMSWmw=/?share_link_id=364783148560)
  
  *Customer functionalities like checkout, order tracking, and account management.*

+ ER Diagram: [link](https://miro.com/app/board/uXjVLFfztEY=/?share_link_id=13656592557)
  
  *A visual representation of the database structure and relationships between entities like Users, Orders, Products, and Payments.*

+ Functional Requirements Table: [link](https://docs.google.com/spreadsheets/d/1C8ueSmLesP9aJSpkPhJmyz85gJ8oASZDgeh0eb0EDaQ/edit?gid=0#gid=0)
  
  *A comprehensive table mapping system functionalities to inputs and outputs, ensuring clarity and traceability.*

***All documentation is hosted on Miro and Google Sheets, emphasizing project clarity and pre-development planning.***

# 🛠️ Architecture Overview
The project follows a simplified Clean Architecture pattern adapted to the Django MVT (Model-View-Template) structure. Below is an explanation of how Clean Architecture concepts map onto Django's MVT:

**Domain**
 + Core business logic and domain entities.
 + Defined in Django models and custom services where necessary.
 
**Application**
 + Orchestrates use-cases, coordinating domain and interface logic.
 + Includes service layers and utility functions to handle specific tasks.
 
**Interface**
 + Views and forms serve as controllers.
 + User-facing interaction logic resides here.


**Infrastructure**
 + ORM models handle database interactions.
 + Integration with external services (e.g., AWS S3, Redis).
 + Configuration and environment management.
___
**This structure ensures:**


✅ Separation of Concerns: Clear boundaries between business logic, presentation, and data management.

✅ Scalability: Easy to extend functionality without introducing tight coupling.

✅ Testability: Individual layers can be tested independently.


Even though the project follows Django's MVT structure, the principles of Clean Architecture are applied consistently to maintain clarity and modularity.


# 💡Key Features


### 1. Account Management
- Custom user model with `AbstractBaseUser` and `CustomUserManager`.
- User authentication: login, registration, and email verification.
- Password reset functionality.
- User groups with role-specific permissions (Client, Agent, Manager).
<img src="https://github.com/user-attachments/assets/abf43e6d-58f7-4a8d-aa50-1d43f521c859" alt="Account Management" width="400">

### 2. Admin Panel
- Custom admin panel for managing products, categories, users, and orders.
- CRUD operations on products, users, and orders.
- Order status management with tracking of payment status.
- Live chat management with customers
- Pagination, search, and filtering for effective data management.
<img src="https://github.com/user-attachments/assets/f5fcd681-038e-4aa8-816d-8df9f8969a50" alt="Admin Dashboard" width="400">
<img src="https://github.com/user-attachments/assets/4cadb713-ede1-4b42-8f4b-6a972957fb21" alt="Admin Management" width="400">
<img src="https://github.com/user-attachments/assets/4d4b7ae7-7cf6-4f42-8ea9-8bb6fc8869b0" alt="Admin Management" width="400">
<img src="https://github.com/user-attachments/assets/ad953ffc-9c35-4571-9007-478b3ca64416" alt="Admin Management" width="400">
<img src="https://github.com/user-attachments/assets/3e5a6573-6ab0-4f18-9469-f65075b750ad" alt="Admin chat" width="400">


### 3. Shopping Cart
- Add/remove products to/from the cart and update quantities.
- Persistent cart data across sessions using context processors.
<img src="https://github.com/user-attachments/assets/2e957610-34a5-4a08-9386-c39e1a15d17a" alt="Admin chat" width="400">

### 4. Real-Time Chat
- WebSocket-based live chat for real-time communication.
- Admin and client chat interface powered by Django Channels, Daphne and Redis.
- Client-side JavaScript and WebSocket integration for smooth communication.
<img src="https://github.com/user-attachments/assets/c21387d8-7504-40e8-b93e-301d482f7f64" alt="Client chat" width="200">
<img src="https://github.com/user-attachments/assets/56fac25c-48b2-4a7f-8567-93f45a767290" alt="Admin chat" width="400">


### 5. Client Area
- User profile management: update addresses, view order history, and manage account.
- Checkout process with address autofill from saved addresses.
<img src="https://github.com/user-attachments/assets/41bfbab7-0f17-4c01-9ce9-9060975a3fcb" alt="account profile" width="400">
<img src="https://github.com/user-attachments/assets/f1b3fd51-df99-43d2-bbca-3b11dec73080" alt="account address" width="400">
<img src="https://github.com/user-attachments/assets/421cb908-18bd-4ca8-ab8f-c37a0674183c" alt="account orders" width="400">
<img src="https://github.com/user-attachments/assets/f0f6aed4-7609-450a-b4dd-58dde9aa005f" alt="account change password" width="400">


### 6. Core
- Basic pages: Home, Contact, etc.
- Custom decorators for role-based access control.
- Site configuration to enable or disable customer chat
<img src="https://github.com/user-attachments/assets/9cdd1d9a-25c0-47eb-ae4c-827fe24294a8" alt="Home " width="400">
<img src="https://github.com/user-attachments/assets/47c05bbf-1953-44c7-8e29-389ee0fec947" alt="Contact" width="400">


### 7. Orders and Payments
- Order management with order status and tracking.
- PayPal integration for online payments (sandbox mode supported).
- Signals for real-time payment status updates.
<img src="https://github.com/user-attachments/assets/67d43a4a-23de-4e54-9232-3df81d29a84a" alt="Contact" width="400">
<img src="https://github.com/user-attachments/assets/3d3c0bb3-aaac-4d90-bc23-68478caeb348" alt="Contact" width="400">

### 8. Shop
- Product listing with category filters and search functionality.
- Product detail pages with review options for purchased products.
<img src="https://github.com/user-attachments/assets/d5200af3-afd1-4022-86c0-b6f50d47084e" alt="Contact" width="400">
<img src="https://github.com/user-attachments/assets/9cd6ca5b-22d2-46f8-a0e3-696993c85810" alt="Contact entert" width="400">


###📦 AWS S3 Integration
The platform uses AWS S3 for efficient and scalable storage of static and media files. A dedicated bucket has been created for the IPN user, ensuring secure and seamless management of uploaded content.

Key Benefits:

Reliability: Highly durable and available storage.
Cost-Effectiveness: Pay-as-you-go pricing for flexibility.
Security: Fine-grained access controls for enhanced data protection.


### ⚙️Technologies Used
- **Backend:** Django, Django Channels, PostgreSQL, Redis.
- **Frontend:** Tailwind CSS, JavaScript.
-  **Storage:**  AWS S3
- **Others:** Django Environ, Whitenoise, WebSockets.


## 🌍Live Demo

The project is hosted on Render and can be accessed at the following link: [Live Demo](https://ecommercewebsite-zcj7.onrender.com).

*Please note:* The website might take a few moments to load initially, as it is hosted on Render’s free tier, which requires the server to "wake up" from an idle state.


## 🚀Getting Started

### Prerequisites
- Python, Node.js, PostgreSQL, Redis.

### Installation
1. Clone the repository and set up the virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
