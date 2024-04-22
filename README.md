
# AmmaRental - Django Web Application

Welcome to AmmaRental! This Django-based web application provides a platform for managing car rentals, user registrations, and bookings. With its intuitive interface and robust backend, AmmaRental simplifies the process of renting cars and keeping track of bookings.

## Overview

AmmaRental is built using Django 4.2.5 and MySQL database for storing car rental information, user data, and booking details. The application offers the following features:

### Features

1. **User Authentication and Registration**:
   - Secure user authentication system with password hashing for user login.
   - User registration functionality with email verification for new accounts.

2. **Car Rental Management**:
   - View available cars for rent with details such as car number, model, and price.
   - Book cars for specific pickup and return dates, calculating the total price based on the rental duration.

3. **Dashboard and User Profile**:
   - User-specific dashboard displaying booking history and current bookings.
   - Update user profile information including email and contact details.

4. **Admin Panel**:
   - Separate admin interface for managing cars, users, and bookings.
   - CRUD (Create, Read, Update, Delete) operations for car rental listings and user accounts.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/AmmaRental.git
   ```

2. **Set Up the Database**:
   - Create a MySQL database named `ammarental`.
   - Update the database settings in `settings.py` with your MySQL credentials.

3. **Install Dependencies**:
   - Navigate to the project directory and install Python dependencies using pip:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run Migrations**:
   - Apply database migrations to create tables in the database:
     ```bash
     python manage.py migrate
     ```

5. **Start the Development Server**:
   - Launch the Django development server to run the application locally:
     ```bash
     python manage.py runserver
     ```

6. **Access the Application**:
   - Open a web browser and navigate to `http://localhost:8000` to access the application.

## Usage

1. **User Registration and Login**:
   - Register a new account with a valid email address and password.
   - Log in using your registered credentials to access the dashboard.

2. **View Available Cars**:
   - Browse through the list of available cars for rent, displayed with relevant details.
   - Click on a car to view more information and proceed with booking.

3. **Book a Car**:
   - Select a car and choose the pickup and return dates for your rental.
   - Confirm the booking details and proceed with the reservation.

4. **Manage Bookings**:
   - View your booking history and current bookings on the dashboard.
   - Cancel or modify existing bookings as needed.

## Contributing

Contributions to AmmaRental are welcome! Whether it's fixing bugs, adding new features, or improving documentation, your contributions are appreciated. Here's how you can contribute:

- Fork the repository and create a new branch for your changes.
- Make your modifications and submit a pull request for review.
- Participate in discussions, code reviews, and issue tracking.

## License

This project is licensed under the ISC License. See the [LICENSE](LICENSE.txt) file for details.

## Support

For support, feedback, or inquiries, please contact the project maintainer(s) at [ranjitheggadi@gmail.com]. We're here to assist you and welcome any questions or suggestions you may have!

