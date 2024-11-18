#importar o pyrebase4 no pip
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCB42ADs5t3A6ELhGnjDFQ1x0eAi0VeeWE",
    "authDomain": "diegobm23-05082023.firebaseapp.com",
    "projectId": "diegobm23-05082023",
    "databaseURL": "https://diegobm23-05082023.firebaseio.com",
    "storageBucket": "diegobm23-05082023.appspot.com",
    "messagingSenderId": "264368903509",
    "appId": "1:264368903509:web:50d23d7444324435f1cbdc",
    "measurementId": "G-NLZHWXS879"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

user = input("Digite seu e-mail: ")
password = input("Digite sua senha, com pelo menos 6 caracteres: ")
status = auth.create_user_with_email_and_password(user,password)
print("Resultado: ", status)



