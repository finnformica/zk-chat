# zkChat

A privacy application developed as part of my MSc Fintech with Data Science research project to allow users to interact with third party services (and specifically ChatGPT) in a pseudonymous and unlinkable manner.

The `client.py` file contains an example of how the proxy can be used to interact with a third party service.

The `third_party_service.py` file contains a mock API for a third party service like ChatGPT.

The `proxy_server.py` file contains the proxy server which handles the interaction between the client and the third party service. This was later adapted from a FastAPI application to a Next.js full-stack application.

The `zkchat-app` directory contains the Next.js app including the backend proxy service handling authentication and proxy functionality and front-end pages. The app is structured using the Next.js 13 App Router and Route Handlers.

## Getting Started

### Prerequisites

- npm
- Docker (for Keycloak)
- [BC Wallet](https://www2.gov.bc.ca/gov/content/governments/government-id/bc-wallet) from BCGov (for Verifiable Credential)
- [Email verification credential](https://email-verification.vonx.io/)

### Installation

1. Clone the repo
   ```sh
   git clone && cd /zk-chat
    ```
2. Install dependencies
    ```sh
    cd /zk-chat-app && npm install
    ```
3. Start dev server
    ```sh
    npm run dev
    ```
4. From the root directory run the mock chatbot service
    ```sh
    scripts/run_tps.sh
    ```
5. Navigate to `localhost:3000` in your browser

### Setting up local Keycloak instance

1. Run command in terminal:
    ```sh
    docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:22.0.1 start-dev
    ```

2. Navigate to `localhost:8080` and log in using `admin` as both the username and password.

3. Create a new realm called `vc-authn`

4. Create a new client called `zk-chat` and add a valid redirect URI as `localhost:3000`

### Testing

1. Run the tests
    ```sh
    pytest
    ```