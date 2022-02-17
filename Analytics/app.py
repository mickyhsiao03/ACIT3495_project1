import connexion


app = connexion.FlaskApp(__name__, specification_dir='')
if __name__ == "__main__":
    app.run(port=8090)