from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
	print(__name__)
	app.run(port=5555, debug=True)