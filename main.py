from website import create_app

app = create_app()

# only if this file is ran does the webserver get started
if __name__ == '__main__':
    app.run(debug=True)