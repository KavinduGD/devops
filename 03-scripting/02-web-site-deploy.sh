#!/bin/bash
TEMP_DIR="/tmp/myapp"
PACKAGES="wget unzip httpd"
SVC="httpd"
URL="https://www.tooplate.com/zip-templates/2138_aqua_nova.zip"
ART_NAME="2138_aqua_nova"


# =========================================
# Install Required Packages
# =========================================
echo "Installing required packages..."
yum install -y $PACKAGES > /dev/null

# =========================================
# Prepare Temporary Directory
# =========================================
echo "Creating temporary working directory..."
mkdir -p "$TEMP_DIR"
cd "$TEMP_DIR" || exit 1

# =========================================
# Download Website Template
# =========================================
echo "Downloading website template..."
wget -O $ART_NAME.zip $URL &> /dev/null
 

# =========================================
# Extract Template
# =========================================
echo "Extracting template files..."
unzip -o $ART_NAME.zip > /dev/null


# =========================================
# Deploy to Apache Web Root
# =========================================
echo "Copying files to /var/www/html/..."
cp -rf $ART_NAME/* /var/www/html/

# =========================================
# Start & Enable Apache
# =========================================
echo "Starting Apache HTTPD service..."
systemctl start $SVC
systemctl enable $SVC

# =========================================
# Cleanup
# =========================================
echo "Cleaning up temporary files..."
rm -rf "$TEMP_DIR"

# =========================================
# Done
# =========================================
echo "Deployment completed successfully!"



