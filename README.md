# Quasar-sanic-template

A Sanic & Quasar Project

## Clone this repo, rename it and update to your remote

```bash
git clone https://github.com/lalondesteve/quasar-sanic-template.git
mv quasar-sanic-template your-awesome-new-app
cd your-awesome-new-app
(Create your new github repo)
git remote set-url origin git@github.com:YOURNAME/your-awesome-new-app.git
git push
```

## Install the dependencies

```bash
yarn
# or
npm install
```

## create the virtual environment and install python modules

```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements
```

### Start the frontend in development mode (hot-code reloading, error reporting, etc.)

```bash
quasar dev
```

### Activate the virtual environment and start the api in development mode

```bash
source ./venv/bin/activate
./run dev
```

### Then click on the Hellow World! text at the top right to check the connection between front and backend

### Lint the frontend files

```bash
yarn lint
# or
npm run lint
```

### Build the app for production

```bash
quasar build
```

### run the server with the built frontend

```bash
(venv)# ./run
```

The production server is available at http://0.0.0.0:8000 and the api at http://0.0.0.0:8000/api
