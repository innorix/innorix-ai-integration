#!/bin/bash

###############################################################################
#
# INNORIX AI Integration
# Agent Verification Script
#
# Verifies that the INNORIX Agent has been installed correctly.
#
###############################################################################

set -e

INSTALL_DIR="/opt/innorix"
SERVICE_NAME="exacoolaag"
CONFIG_FILE="${INSTALL_DIR}/agent.yaml"
EXECUTABLE="${INSTALL_DIR}/exacoolaag"

echo "============================================================"
echo "           INNORIX Agent Verification"
echo "============================================================"
echo

###############################################################################
# Check Installation Directory
###############################################################################

echo "[1/5] Checking installation directory..."

if [ -d "${INSTALL_DIR}" ]; then
    echo "✓ Installation directory found"
else
    echo "✗ Installation directory not found"
    exit 1
fi

###############################################################################
# Check Agent Executable
###############################################################################

echo
echo "[2/5] Checking Agent executable..."

if [ -x "${EXECUTABLE}" ]; then
    echo "✓ Agent executable found"
else
    echo "✗ Agent executable not found"
    exit 1
fi

###############################################################################
# Check Agent Service
###############################################################################

echo
echo "[3/5] Checking Agent service..."

if systemctl is-active --quiet "${SERVICE_NAME}"; then
    echo "✓ Agent service is running"
else
    echo "✗ Agent service is not running"
    exit 1
fi

###############################################################################
# Check Configuration
###############################################################################

echo
echo "[4/5] Checking Agent configuration..."

if [ -f "${CONFIG_FILE}" ]; then
    echo "✓ Configuration file found"
else
    echo "✗ Configuration file not found"
    exit 1
fi

###############################################################################
# Platform Connectivity
###############################################################################

echo
echo "[5/5] Checking Platform connectivity..."

echo "⚠ Not implemented (Reference Implementation)"

###############################################################################
# Summary
###############################################################################

echo
echo "============================================================"
echo " Verification completed successfully."
echo "============================================================"
echo
echo "Agent Directory : ${INSTALL_DIR}"
echo "Service         : ${SERVICE_NAME}"
echo "Configuration   : ${CONFIG_FILE}"
echo
echo "The INNORIX Agent is ready for AI Integration."

###############################################################################
# TODO
#
# - Verify Agent version
# - Verify Platform connectivity
# - Verify authentication
# - Verify storage accessibility
# - Verify transfer permissions
#
###############################################################################
