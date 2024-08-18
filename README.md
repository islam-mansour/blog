# Django Blog POC

**Version:** 1.0   
**Author:** Islam Mansour

## Table of Contents

- [Django Blog POC](#django-blog-poc)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Project Setup](#project-setup)
  - [Project Structure](#project-structure)
  - [Usage](#usage)
    - [User Registration and Authentication](#user-registration-and-authentication)
    - [Blog Management](#blog-management)
    - [Interaction](#interaction)
    - [Search](#search)
  - [Additional Resources](#additional-resources)
  - [Project Dependencies](#project-dependencies)

## Introduction

Welcome to the Django Blog poc. This project is a feature-rich Django-based blog application that allows users to create, manage, and interact with blog posts. It provides a user-friendly interface for bloggers and readers alike.

## Getting Started

### Installation

Before you begin, make sure you have docker and docker-compose installed on your system. To install, see the following:

https://medium.com/@tomer.klein/step-by-step-tutorial-installing-docker-and-docker-compose-on-ubuntu-a98a1b7aaed0

### Project Setup

1. Clone the project repository from GitHub:

   ```bash
   git clone git@github.com:islam-mansour/blog.git
   ```

2. Navigate to the project directory:

   ```bash
   cd blog
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   docker-compose up --build
   ```

4. Open your web browser and visit [http://localhost:8000/](http://localhost:8000/) to access the project.

## Project Structure

The Django Blog project follows a standard Django project structure, with the following notable components:

- `core/`: The main Django app for managing blog posts and authentication (login, logout, register).
- `*/templates/`: HTML templates for rendering web pages.
- `media/`: Media files (uploaded images) associated with blog posts.

## Usage

### User Registration and Authentication

- To create an account, click the "Register" link in the navigation menu.
- To log in, click the "Login" link in the navigation menu.
- Authenticated users can create their own blogs, comment on blogs, and like/unlike blogs.

### Blog Management

- On the home page, you can view the latest blog posts.
- Use the sorting options to arrange blog posts by date, views, or likes.
- Navigate through multiple pages of blog posts using pagination.

### Interaction

- Authenticated users can like or unlike blog posts without page reload.
- Users can also post comments on their own or other users' blog posts.

### Search

- Utilize the search form in the navigation menu to search for specific blog posts based on title, content, or author name.

## Additional Resources

- [Django](https://docs.djangoproject.com/en/4.2/): Official Django documentation
- [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/): Official Bootstrap documentation
- [Django REST Framework](https://www.django-rest-framework.org/): Official Django REST Framework documentation
- [Postgres](https://www.postgresql.org/): Official Postgresql documentation

## Project Dependencies

The Django Blog project relies on several external frameworks and libraries to enhance its functionality and appearance. Here are the key dependencies used in this project:

1. **Bootstrap and Fontawesome Icon (Frontend)**
2. **Django REST Framework (API)**
3. **Pillow (Media)**
4. **Django Crispy Forms (Form)**

These dependencies significantly contribute to the functionality and aesthetics of the Django Blog project, ensuring a seamless and visually appealing user experience.

Please note that detailed installation instructions for these dependencies can be found in the "Getting Started" section of this documentation.
