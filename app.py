from flask import Flask ,render_template, url_for ,request, Blueprint,flash, redirect
from forms import RegistrationForm , LoginForm
import urllib.request , json

app = Flask(__name__)

app.config['SECRET_KEY'] = '29e8bdb6c50357715c9c10489a9c89b8'
source = urllib.request.urlopen('http://api.coinlayer.com/api/live?access_key=7ada23db733a48bfc93fb28b039112e5').read()
res_crypto = json.loads(source)
data = {
			
			"btc": str(res_crypto['rates']['BTC']),
			"eth": str(res_crypto['rates']['ETH']),
			"bnb": str(res_crypto['rates']['BNB']),
			"xrp": str(res_crypto['rates']['XRP']),

			"ant": str(res_crypto['rates']['ANT']),
			"mana": str(res_crypto['rates']['MANA']),
			"steem": str(res_crypto['rates']['STEEM']),

            "dgb": str(res_crypto['rates']['DGB']),
			"doge": str(res_crypto['rates']['DOGE']),
			"gbyte": str(res_crypto['rates']['GBYTE']),

             "ltc": str(res_crypto['rates']['LTC']),
			
			"tnt": str(res_crypto['rates']['TNT']),
            
			
		}



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', data = data)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/cryptoandworld")
def cryptoandworld():
    return render_template('cryptoandworld.html', title='Crypto & World')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)