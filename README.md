# zkChat

A privacy application developed as part of my MSc Fintech with Data Science research project to allow users to interact with third party services (and specifically ChatGPT) in a pseudonymous and unlinkable manner.

## Getting Started

### Prerequisites

- Python 3.8
- pip

### Installation

1. Clone the repo
   ```sh
   git clone
    ```
3. Create a virtual environment
    ```sh
    python3 -m venv venv && source venv/bin/activate
    ```
2. Install requirements
    ```sh
    pip3 install -r requirements.txt
    ```
3. Run the proxy
    ```sh
    scripts/run_proxy.sh
    ```

4. Run the mock third party service
    ```sh
    scripts/run_tps.sh
    ```

5. Run the client
    ```sh
    python3 client.py
    ```

### Testing

1. Run the tests
    ```sh
    pytest
    ```