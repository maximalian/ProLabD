from flask import Flask, render_template
from config import Config
from auth_routes import auth, bcrypt
from user_routes import user_bp
from product_routes import product_bp
import logging


# Iestatām žurnālu ierakstīšanu sistēmā
logging.basicConfig(
    level=logging.ERROR,  # Žurnālu līmenis (ERROR, INFO, DEBUG utt.)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formāts: laiks, līmenis un ziņa
    handlers=[
        logging.FileHandler("app.log"),  # Ieraksti tiek glabāti failā app.log
        logging.StreamHandler()  # Ieraksti tiek parādīti konsolē
    ]
)

app = Flask(__name__)
app.config.from_object(Config) 
bcrypt.init_app(app)

app.register_blueprint(auth, url_prefix='/auth')  # Autentifikācijas ceļi
app.register_blueprint(user_bp, url_prefix='/user_bp')  # Lietotāju ceļi
app.register_blueprint(product_bp, url_prefix='/product_bp')  # Produktu pārvaldības ceļi

# Galvenā lapa (mājaslapa)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run("0.0.0.0", port=5001, debug=True)
