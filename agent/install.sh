#!/bin/bash

###############################################################################
#
# INNORIX AI Integration
# Agent Bootstrap Installer
#
# This script downloads and installs the latest INNORIX Agent
# for RPM-based Linux distributions.
#
###############################################################################

set -e

###############################################################################
# Configuration
###############################################################################

INNORIX_DOWNLOAD_URL="https://innorix.com/download/agent?os=rpm"
PACKAGE_NAME="innorix-agent.rpm"

###############################################################################
# Environment Check
###############################################################################

echo "============================================================"
echo "           INNORIX AI Integration Installer"
echo "============================================================"
echo

echo "[1/6] Checking operating system..."

if ! command -v rpm >/dev/null 2>&1; then
    echo "ERROR: RPM package manager was not found."
    echo "This installer supports RPM-based Linux distributions only."
    exit 1
fi

###############################################################################
# Download Agent
###############################################################################

echo "[2/6] Downloading the latest INNORIX Agent..."

curl -L "${INNORIX_DOWNLOAD_URL}" \
     -o "${PACKAGE_NAME}"

###############################################################################
# Install Agent
###############################################################################

echo "[3/6] Installing INNORIX Agent..."

sudo rpm -Uvh "${PACKAGE_NAME}"

###############################################################################
# Enable Service
###############################################################################

echo "[4/6] Enabling INNORIX Agent service..."

sudo systemctl enable exacoolaag

###############################################################################
# Start Service
###############################################################################

echo "[5/6] Starting INNORIX Agent..."

sudo systemctl start exacoolaag

###############################################################################
# Verify Installation
###############################################################################

echo "[6/6] Verifying installation..."

chmod +x verify.sh
./verify.sh

echo
echo "============================================================"
echo " INNORIX Agent installation completed successfully."
echo "============================================================"
echo
echo "Next Steps:"
echo
echo "1. Update agent/agent.yaml"
echo "2. Configure config/transfer.example.yaml"
echo "3. Configure config/pipeline.example.yaml"
echo "4. Run an integration example"
echo

###############################################################################
# Future Improvements
#
# TODO:
# - Verify OS version
# - Verify CPU architecture
# - Verify RPM package signature
# - Verify Agent version
# - Automatic upgrade
# - Rollback support
#
###############################################################################
