import connexion



def authenticate(body):
    if body['userName'] and body['password'] !='root':
        print('not authenticated')
        return False
    else:
        print('authenticated!')
        return True


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("auth.yaml", strict_validation=True, validate_responses=True)
if __name__ == "__main__":
    app.run(port=8080)