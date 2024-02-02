from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Function 1: Read the image and show in the navigation
current_dir = os.path.dirname(os.path.abspath(__file__))

@app.route('/images/<filename>')
def serve_image(filename):
    # use os.path.join to find the correct path of the image
    return send_from_directory(os.path.join(current_dir, 'static', 'images'), filename)

# Function 2: Login
# User information is stored in a dictionary in the format {username: password}
users = {
    'user1': 'password1',
    'user2': 'password2',
    # add some more users if needed...
}

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check whether the user name and password match
        if username in users and users[username] == password:
            # Login successful, redirect to home page
            return redirect(url_for('home', username=username))
        else:
            return 'Invalid username or password. Please try again.'
    return render_template("login.html")
@app.route('/home/<username>')
def home(username):
    return render_template('home.html', username=username)

# Function 3: User information profile
users_info_dic = {
    'user1': {'id': 1,
              'avatar': 'bear.jpg',
              'username': 'GloriaBear',
              'phone': '1234566',
              'email': 'u654321@warwick.ac.uk'
              },
    'user2': {'id': 2,
              'avatar': 'cat.jpg',
              'username': 'Tiger',
              'phone': '1234567',
              'email': 'u654322@warwick.ac.uk'
              },
    # add more informartion of users if needed...
}

@app.route('/user_profile/<username>')
def user_profile(username):
    # check if the user is existed
    if username in users_info_dic:
        user_info = users_info_dic[username]
        return render_template('user_profile.html', user_info=user_info)
    else:
        return 'User not found.'


if __name__ == '__main__':
    app.run(debug=True)
