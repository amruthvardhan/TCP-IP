# TCP-IP

# TCP/IP Communication Program

This project demonstrates TCP/IP communication using Python's `asyncio` module. It includes a TCP server, a client application, and unit tests for validating the communication protocol.

## Project Structure

cpip/
│
├── main.py # Main application that connects to the TCP server and communicates
├── tcp_stub.py # TCP server stub that echoes messages back to the client
├── tcp_protocol.py # TCP protocol handler with methods for connecting, reading, and writing
└── tests/
└── test_tcp_protocol.py # Unit tests for the TCP protocol handler


## Getting Started

Make sure you have the necessary modules and version of python available.

## Running the TCP Server and Client

To run the TCP server, the main application, and unit tests, use the provided shell script:

``` ./run.sh```

This script performs the following tasks:

    Starts the TCP server (tcp_stub.py).
    Runs the main application (main.py).
    Executes the unit tests (tests/test_tcp_protocol.py).
    Cleans up any remaining processes.
