from flask import render_template
from UrlShortner import app, db
from UrlShortner.forms import URLForm
from UrlShortner.models import URL
from UrlShortner.token import gen_valid_token
from UrlShortner.config import WEBSITE_DOMAIN

# Index route
@app.route("/", methods=['GET', 'POST'])
def index():
	# Create a instance of the form
	form = URLForm()

	# If the form was valid
	if form.validate_on_submit():

		# If a token was given
		if form.token.data:
			# Add the token and the given url to the database
			db.session.add(URL(token=form.token.data, url=form.url.data))
			db.session.commit()

			# Return the url page with the shortened url
			return render_template("url.html", url=WEBSITE_DOMAIN + "/" + form.token.data)

		# Else if a token was not given
		else:
			# Generate a valid token
			token = gen_valid_token()

			# Add the token and the given url to the database
			db.session.add(URL(token=token, url=form.url.data))
			db.session.commit()

			# Return the url page with the shortened url
			return render_template("url.html", url=WEBSITE_DOMAIN + "/" + token)

	# Else if the form was invalid or not submitted
	else:
		# Return the index page with the form
		return render_template("index.html", form=form)

# Error handling routes
@app.errorhandler(404)
def error_404(error):
	return render_template("error.html", error_code=404, error_message="Not Found"), 404

@app.errorhandler(500)
def error_500(error):
	return render_template("error.html", error_code=500, error_message="Internal Server Error"), 500
