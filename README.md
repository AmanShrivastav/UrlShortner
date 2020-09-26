# How it works

Each URL that is submitted goes through a simple check for validity and/or added http:// before it to redirect successful.
After that, a base 64 string is generated and added to a Sqlite database with the corresponding URL that was submitted.
The user is then given a short URL that is formatted as: WEBSITE_DOMAIN/token, the token being the base 64 string.
Whenever this URL is visited the user will get redirected to the tokens corresponding URL in the database.

# Run locally

**Highly encouraged to create a python environment first.**

Clone the repository:

	$ git clone https://github.com/AmanShrivastav/UrlShortner.git

Move into the cloned folder and install the required libraries:

	$ cd UrlShortner
	$ pip install -r requirements.txt

After that run with:

	$ python run.py

Visit the below URL to view the flask app:

	127.0.0.1:5000

**NOTE:** When running locally all redirects will also be local.

# Deploying

If you do not have a dedicated server, I highly recommend using [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python), [PythonAnywhere](https://www.pythonanywhere.com/) or [AWS](https://aws.amazon.com/getting-started/projects/deploy-python-application/) to host your application.

Before deploying, in the file:

	UrlShortner/run.py  

set running in debug mode to False:

	app.run(debug=False)

and change the config file located in the directory below:

	UrlShortner/UrlShortner/config.json
