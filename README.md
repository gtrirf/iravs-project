# IRAVS Project

Welcome to the **IRAVS Project**! This guide provides step-by-step instructions to set up and run the project on your local machine.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Getting Started](#getting-started)
    - [1. Cloning the Repository](#1-cloning-the-repository)
    - [2. Setting Up the Virtual Environment](#2-setting-up-the-virtual-environment)
    - [3. Installing Dependencies](#3-installing-dependencies)
    - [4. Database Setup](#4-database-setup)
    - [5. Static and Media Directories](#5-static-and-media-directories)
4. [Running the Project](#running-the-project)
5. [Additional Information](#additional-information)

---

## Project Overview

**IRAVS Project** is a Django-based web application designed to provide a streamlined and efficient experience. 

---

## Prerequisites

- Python 3.8+ installed on your local machine
- `virtualenv` for managing virtual environments
- Git for cloning the repository

---

## Getting Started

### 1. Cloning the Repository

First, clone the repository to your local machine and navigate into the project folder:

```bash
git clone https://github.com/gtrirf/iravs-project.git
cd iravs-project
```

### 2. Setting Up the Virtual Environment

1. **Create a virtual environment:**

   ```bash
   virtualenv venv
   ```

2. **Activate the virtual environment:**

   - On **Linux / macOS**:

     ```bash
     source venv/bin/activate
     ```

   - On **Windows**:

     ```bash
     venv\Scripts\activate
     ```

### 3. Installing Dependencies

With the virtual environment active, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Database Setup

Set up the database by running the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Static and Media Directories

Create the directories for static and media files:

```bash
mkdir static
mkdir media
```

After creating these directories, collect static files by running:

```bash
python manage.py collectstatic
```

---

## Running the Project

To start the development server, use:

```bash
python manage.py runserver
```

You can access the project in your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Additional Information

- Ensure the virtual environment is activated whenever you are working on the project.
- For further customization or debugging, refer to Django’s official documentation.

---

Happy coding with **IRAVS Project**! 🎉