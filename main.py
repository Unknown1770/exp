from flask import Flask,request

app = Flask(__name__)
# GET requests will be blocked
# GET requests will be blocked
@app.route('/')
def hello():
    return 'Hello There'


@app.route('/profile-example', methods=['POST'])
def profile_example():
    request_data = request.get_json()

    city = None
    email = None
    name = None
    mobile = None
    gender = None
    dob = None
    nationality = None
    dob_month = None
    dob_year = None

    if request_data:
        if 'city' in request_data:
            city = request_data['city']

        if 'email' in request_data:
            email = request_data['email']

        if 'dob' in request_data:
            dob = request_data['dob']
            dob_year = dob[0:4]
            dob_month = dob[5:7]
            

        if 'mobile' in request_data:
            mobile = request_data['mobile']

        if 'gender' in request_data:
            gender = request_data['gender']
        
        if 'nationality' in request_data:
            nationality = request_data['nationality']
            
        if 'name' in request_data:
            name = request_data['name']

    return '''
           Name: {}
           City: {}
           Email: {}
           Mobile: {}
           Date_of_birth: {}
           Birth_month: {}
           Birth_year: {}
           Gender: {}'''.format(name, city, email, mobile, dob, dob_month, dob_year, gender)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.0', port=8080, debug=True)
