#!/bin/bash

# Define paths to the Python scripts
SERVER_SCRIPT="tcp_stub.py"
MAIN_SCRIPT="main.py"
TEST_SCRIPT="tests/test_tcp_protocol.py"

# Function to clean up by killing any running Python processes
cleanup() {
    echo "Cleaning up..."
    pkill -f "python.*$SERVER_SCRIPT"
    pkill -f "python.*$MAIN_SCRIPT"
    pkill -f "python.*$TEST_SCRIPT"
}

# Trap script exit to ensure cleanup is called
trap cleanup EXIT

# Set PYTHONPATH to the project directory
export PYTHONPATH=$(pwd)

# Start the TCP/IP server in the background
echo "Starting TCP/IP server..."
python $SERVER_SCRIPT &
SERVER_PID=$!

# Wait for a short period to ensure the server starts
sleep 2

# Run the main program in the background
echo "Running main program..."
python $MAIN_SCRIPT &
MAIN_PID=$!

# Wait for the main program to finish
wait $MAIN_PID

# Run unit tests
echo "Running unit tests..."
python $TEST_SCRIPT

# Cleanup
cleanup
