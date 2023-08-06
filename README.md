# zkChat

A privacy application developed as part of my MSc Fintech with Data Science research project to allow users to interact with third party services (and specifically ChatGPT) in a pseudonymous and unlinkable manner.

## Getting Started

### Prerequisites

- Python 3.8
- pip
- Docker (for Keycloak)

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

### Setting up local Keycloak instance

If a local keycloak instance is used this should be started BEFORE booting up the proxy server.

1. Run command in terminal:
    ```sh
    docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:22.0.1 start-dev
    ```

2. Navigate to `localhost:8080` and log in using `admin` as both the username and password.

3. Create a new realm called `vc-authn`

4. Create a new client called `fast-api` and add a valid redirect URI as `localhost:10000`

5. Create a new user and set up the password using the credentials tab (ensuring temporary toggle is off).

### Testing

1. Run the tests
    ```sh
    pytest
    ```