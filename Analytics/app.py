import connexion



app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("analytics.yaml", strict_validation=True, validate_responses=True)
if __name__ == "__main__":
    app.run(port=8090)