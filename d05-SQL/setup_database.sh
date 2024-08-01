#!/bin/bash

# Variables
DB_NAME="formationdjango"
DB_USER="djangouser"
DB_PASS="secret"


# Step 0: Install PostgreSQL
sudo apt-get update
sudo apt-get install -y postgresql postgresql-contrib
systemctl start postgresql
systemctl status postgresql

# Step 1: Create PostgreSQL database and user
sudo -u postgres psql <<EOF
CREATE DATABASE $DB_NAME;
CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOF

# DROP DATABASE formationdjango;