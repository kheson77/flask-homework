from flask import Flask
from .models import User, Product, db
from flask_migrate import Migrate
from flask import Flask, request, render_template, url_for, redirect

def create_app():
    app = Flask(__name__)
    
    app.config.update(
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{app.instance_path}/flask-example.db",
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
    
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    
    
    @app.route("/")
    def index():
        data = Product.query.all()
        return render_template("products/products.html", data = data)
    
    # @app.route("/delete/<int:id>")
    # def delete(id):
    #     user = User.query.filter_by(id = id).first()
    #     db.session.delete(user)
    #     db.session.commit()
    #     return redirect(url_for('index'))

    # @app.route("/add-user/<int:id>", methods=["GET", "POST"])
    # def add_user(id):
    #     if request.method == "GET":
    #         data = {"id": id}
    #         if id > 0: 
    #             data = User.query.filter_by(id = id).first()
    #         return render_template("auth/login.html", data = data)
    #     elif request.method == "POST":
    #         if int(request.form["id"]) == 0:
    #             user = User(name=request.form["name"])
    #             db.session.add(user)
    #         else: 
    #            user = User.query.filter_by(id = int(request.form["id"])).first()
    #            user.name = request.form["name"]
            
    #         db.session.commit()
    #         return  redirect(url_for('index'))
    
    # @app.route("/user/<int:id>", methods=["GET"])
    # def user(id):
    #     return f"Sản phẩm {id}"
    
    #List product
    @app.route("/products", methods=["GET"])
    def get_all_products():
        data = Product.query.all()
        return render_template("products/products.html", data = data)
    
    #Detail product
    @app.route("/products/<int:id>", methods=["GET"])
    def get_product_by_id(id):
        data = Product.query.all()
        product = Product.query.filter_by(id = id).first()
        print(product)
        return render_template("products/product_detail.html", product = product)

    #Add product
    @app.route("/add-product", methods=["GET", "POST"])
    def add_product():
        if request.method == "GET":
            return render_template("products/add_product.html")
        elif request.method == "POST":
            product = Product(name=request.form["name"], desciption=request.form["desciption"], price=request.form["price"])
            db.session.add(product)
            db.session.commit()
        return redirect(url_for('get_all_products'))
    
    #Delete product
    @app.route("/delete-product/<int:id>")
    def delete_product(id):
        product = Product.query.filter_by(id = id).first()
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('get_all_products'))
    
    #Update product
    @app.route("/update-product/<int:id>", methods=["GET", "POST"])
    def update_product(id):
        if request.method == "GET":
            data = Product.query.filter_by(id = id).first()
            return render_template("products/update_product.html", data=data)
        elif request.method == "POST":
            user = Product.query.filter_by(id = int(request.form["id"])).first()
            user.name = request.form["name"]
            user.desciption = request.form["desciption"]
            user.price = request.form["price"]
            db.session.commit()
        return redirect(url_for('get_all_products'))
    
    @app.errorhandler(404)
    def not_found(e):
        return "<center><h1>404 Not found</h1></center>"
    return app