# FINANCE - APP  
Financial management software   

## Disclaimer  
All commands are available in the Makefile. Use the following command to see available targets:  
```shell
make help
```  

## Setting Up and Running  

### 1. Prepare Your Environment  
Create a virtual environment and install dependencies:  
```shell
python -m venv venv
source venv/bin/activate  # Use venv\Scripts\activate on Windows
make install # To install dependencies
```  

### 2. Running the Application and Database
```shell
make database # Run PostgreSQL container
make run 
```  

### 3. Access to Django Admin
```shell
python manage.py createsuperuser # Create a super user and access http://localhost:8000/admin/

### Software ##
- Docker
- Python 3.9
- Postgresql
 

### TODO  
- ...
