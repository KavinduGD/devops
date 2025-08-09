#!/bin/bash

# =========================================
# Install Required Packages
# =========================================
echo "Installing required packages..."
yum install -y wget unzip httpd > /dev/null

# =========================================
# Prepare Temporary Directory
# =========================================
echo "Creating temporary working directory..."
TMP_DIR="/tmp/myapp"
mkdir -p "$TMP_DIR"
cd "$TMP_DIR" || exit 1

# =========================================
# Download Website Template
# =========================================
echo "Downloading website template..."
wget -O template.zip https://www.tooplate.com/zip-templates/2138_aqua_nova.zip > /dev/null

# =========================================
# Extract Template
# =========================================
echo "Extracting template files..."
unzip -o template.zip > /dev/null

# =========================================
# Deploy to Apache Web Root
# =========================================
echo "Copying files to /var/www/html/..."
cp -rf 2138_aqua_nova/* /var/www/html/

# =========================================
# Start & Enable Apache
# =========================================
echo "Starting Apache HTTPD service..."
systemctl start httpd
systemctl enable httpd

# =========================================
# Cleanup
# =========================================
echo "Cleaning up temporary files..."
rm -rf "$TMP_DIR"

# =========================================
# Done
# =========================================
echo "Deployment completed successfully!"

