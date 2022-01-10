from flask import Blueprint, render_template, send_file

auth = Blueprint('auth', __name__)

@auth.route('/games')
def games():
    return render_template("games.html")

@auth.route('/games/horrorwords')
def horrorwords():
    return send_file("games/HorrorWords.exe", as_attachment=True)