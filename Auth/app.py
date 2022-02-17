import connexion
import requests

data = requests.get('http://localhost:')

def auth(username, password):
    if username and password !='root':
        return False
    else:
        return True


app = connexion.FlaskApp(__name__, specification_dir='')
if __name__ == "__main__":
    app.run(port=8080)