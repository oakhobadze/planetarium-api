🌌 Planetarium Ticket Booking System
Are you fascinated by the wonders of stars and planets? If so, this project is perfect for you! 🌠

This system allows visitors to book tickets online for their favorite sessions at the local planetarium, making the experience smooth and enjoyable. No more waiting in lines—just pick a show, reserve your seat, and get ready to explore the universe!

✨ **Features**

✅ Easy Online Booking – Choose your session and book tickets effortlessly.

✅ Real-Time Availability – Check seat availability for different shows.

✅ User-Friendly Interface – Simple and intuitive design for all users.

✅ Secure Payments – Hassle-free and safe transaction options.

![Monosnap Study _ Mate academy - Google Chrome 2025](https://github.com/user-attachments/assets/652aae78-4079-480e-91df-bf7413eaad62)

**Project Setup and Running Instructions**

This project uses **Docke**r and **Docker Compose** to set up the development environment. Follow the steps below to get the project up and running.

Use: docker-compose up --build The application will be running on http://localhost:8888

The **Swagger documentation** is available at: http://localhost:8888/api/swagger/

**JWT Authentication**

Create User: POST /api/planetarium/create_user/

Login: POST /api/planetarium/login/

After creating a user, you need to log in to receive a JWT token:

Go to /api/planetarium/login/

Include the JWT token in the Authorization header as follows: Authorization: Bearer <your_jwt_token>

