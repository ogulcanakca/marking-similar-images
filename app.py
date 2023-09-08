from flask import Flask, render_template, request, g, redirect, url_for, flash, session
import random
import sqlite3
import secrets
import os
import shutil
import pyodbc
from passlib.hash import pbkdf2_sha256

server = 'similarimages.database.windows.net'
database = 'similarimages'
username = 'adminsimilarimages'
password = 'qhuzjPvmSnB7BZQaKCm/TW2qSuYx4I3w1CqCwwxNBF+ACRAXXAMZ'   
driver= '{ODBC Driver 17 for SQL Server}'
connection = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = connection.cursor()

app = Flask(__name__, static_folder= "static")
app.secret_key = secrets.token_hex(16)
db_username=""
downloaded_folders_name = 'Trendyol Resimler'

#def create_users_table():
#    with sqlite3.connect('users.db') as conn:
#        cursor = conn.cursor()
#        cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

def add_user(username, password):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))

#def get_user(username):
#    with sqlite3.connect('users.db') as conn:
#        cursor = conn.cursor()
#        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
#        return cursor.fetchone()
        
def get_user(username):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        return cursor.fetchone()

def is_user_authenticated():
    return 'username' in session

@app.route('/login', methods=['GET', 'POST'])
def login():
    global db_username
    if is_user_authenticated():
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user(username)
        db_username = username
        if user is None or not pbkdf2_sha256.verify(password, user[1]):
            flash('Kullanıcı adı veya şifre hatalı. Lütfen tekrar deneyin.', 'error')
        else:
            session['username'] = username
            flash('Giriş başarılı!', 'success')
            return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if is_user_authenticated():
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user(username)
        if user is not None:
            flash('Bu kullanıcı adı zaten alınmış. Lütfen farklı bir kullanıcı adı seçin.', 'error')
        else:
            hashed_password = pbkdf2_sha256.hash(password)
            add_user(username, hashed_password)
            flash('Kayıt başarılı! Şimdi giriş yapabilirsiniz.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')


source_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), downloaded_folders_name)
static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
                             
def replace_spaces_with_underscore(directory):
    items = os.listdir(directory)
    for item in items:
        item_path = os.path.join(directory, item)
        
        if os.path.isdir(item_path):
            new_name = item.replace(" ", "_")
            if new_name != item:
                new_path = os.path.join(directory, new_name)
                try:
                    shutil.copytree(item_path, new_path)
                    shutil.rmtree(item_path)
                    print(f"{item_path} klasörü {new_path} olarak taşındı ve eski klasör silindi.")
                except FileExistsError:
                    print(f"{new_path} adı zaten mevcut, atlanıyor.")
        else:
            print(f"{item_path} bir klasör değil, atlanıyor.")
            
replace_spaces_with_underscore(source_folder)

def move_folders(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        print(f"{source_dir} klasör yolu mevcut değil, hiçbir işlem yapılmıyor.")
        return
    
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"{destination_dir} klasör yolu oluşturuldu.")
    
    items = os.listdir(source_dir)
    
    if not items:
        print(f"{source_dir} klasörü boş, hiçbir işlem yapılmıyor.")
        return
    
    for item in items:
        source_item_path = os.path.join(source_dir, item)
        destination_item_path = os.path.join(destination_dir, item)
        
        if os.path.exists(destination_item_path):
            print(f"{destination_item_path} hedef dizinde zaten var, atlanıyor.")
            continue
        
        if os.path.isdir(source_item_path):
            shutil.move(source_item_path, destination_item_path)
            print(f"{source_item_path} klasörü taşındı.")
        else:
            print(f"{source_item_path} bir klasör değil, atlanıyor.")

move_folders(source_folder, static_folder)

def get_subfolder_names(directory):
    subfolder_names = []
    items = os.listdir(directory)
    
    for item in items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            subfolder_names.append(item)
    
    return subfolder_names
subfolder_names = get_subfolder_names('/app/static')
'''subfolder_names = get_subfolder_names(static_folder)'''

def extract_file_names(selected_images):
    extracted_file_names = []

    for image_path in selected_images:
        parts = image_path.split("\\")
        file_name = parts[-1]
        extracted_file_names.append(file_name)
    
    return extracted_file_names

folderPath = static_folder

folder_name = "Bej_kaşmir_hırka"

file_paths = []
for folder, subs, files in os.walk('/app/static'):
    folder = folder[folder.rfind("/") + 1:]
    for filename in files:
        if folder_name == folder:
            file_paths.append('static/' + folder + '/' + filename)
            
'''for folder, subs, files in os.walk(folderPath):
    folder = folder[folder.rfind("\\") + 1:]
    for filename in files:
        if folder_name == folder:
            file_paths.append('static/'+folder+'/'+filename)
'''

def delete_excel_csv_files(directory):
    if not os.path.exists(directory):
        print(f"{directory} klasör yolu mevcut değil, hiçbir işlem yapılmıyor.")
        return
    
    items = os.listdir(directory)
    has_files = False
    
    for item in items:
        item_path = os.path.join(directory, item)
        
        if os.path.isfile(item_path) and (item_path.endswith(".xlsx") or item_path.endswith(".csv")):
            os.remove(item_path)
            print(f"{item_path} dosyası silindi.")
            has_files = True
    
    if not has_files:
        print(f"{directory} klasöründe silinecek dosya bulunamadı.")
    else:
        shutil.rmtree(directory)
        print(f"{directory} klasörü boş, silindi.")
    if not os.path.exists(source_folder):
        os.makedirs(source_folder)


delete_excel_csv_files(source_folder)

#def create_imageSimilarities_table():
#    with sqlite3.connect('database.db') as conn:
#        cursor = conn.cursor()
#        cursor.execute('CREATE TABLE IF NOT EXISTS "imageSimilarities" ( "image" TEXT NOT NULL, "username" TEXT NOT NULL, "positive_images" TEXT, "negative_images" TEXT)')


def list_to_string_with_commas(selected_images):
    file_names = [image_path.split("/")[-1] for image_path in selected_images]
    result_string = ",".join(file_names)
    return result_string

def find_difference(temp_str, positive_images):
    temp_images = temp_str.split(',')
    positive_images_list = positive_images.split(',')

    difference_images = list(set(temp_images) - set(positive_images_list))

    negative_images = ','.join(difference_images)

    return negative_images

def get_db():
    if 'db' not in g:
        g.db = connection
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

temp_selected_images = list()

@app.route('/', methods=['GET', 'POST'])
def home():
    global db_username
    if not is_user_authenticated():
        return redirect(url_for('login'))
    #create_users_table()
    global temp_selected_images
    if request.method == 'POST':
        selected_image = request.form.get('selected_image')
        selected_images = request.form.getlist('selected_image')
        selected_images = extract_file_names(selected_images)
        selected_images.remove(selected_image)
        positive_images = list_to_string_with_commas(selected_images)
        selected_image = selected_image.split("/")[-1]
        temp_selected_images_cb = extract_file_names(temp_selected_images)
        cb_str = list_to_string_with_commas(temp_selected_images_cb)
        negative_images = find_difference(cb_str, positive_images)
        cursor.execute('INSERT INTO tbl_similarimages (image, username, positive_images, negative_images) VALUES (?, ?, ?, ?)', (selected_image, db_username, positive_images, negative_images))
        cursor.commit()
    if len(file_paths) >= 2:
        if len(file_paths) == 2:
            selected_image = random.choice(file_paths)
            file_paths.remove(selected_image)
            selected_images = random.sample(file_paths, 1)
            file_paths.append(selected_image)
            temp_selected_images = selected_images
            return render_template('index.html', folder_header = folder_header, folder_name=folder_name, selected_image=selected_image, other_images=selected_images)
        elif len(file_paths) == 3:
            selected_image = random.choice(file_paths)
            file_paths.remove(selected_image)
            selected_images = random.sample(file_paths, 2)
            file_paths.append(selected_image)
            temp_selected_images = selected_images
            folder_header = folder_name.replace("_", " ")
            return render_template('index.html', folder_header = folder_header, folder_name=folder_name, selected_image=selected_image, other_images=selected_images)
        else:
            selected_image = random.choice(file_paths)
            file_paths.remove(selected_image)
            selected_images = random.sample(file_paths, 3)
            file_paths.append(selected_image)
            temp_selected_images = selected_images
            folder_header = folder_name.replace("_", " ")
            return render_template('index.html', folder_header = folder_header, folder_name=folder_name, selected_image=selected_image, other_images=selected_images)
    else:
        paths = []
        for dizin in file_paths:
            son_kisim = os.path.basename(os.path.dirname(dizin))
            paths.append(son_kisim)
        if len(paths) > 0:
            error_message = "Hata! 2'den az resim sayısı mevcut."
            return render_template('error.html', path = paths[0].replace("_", " ") ,error_message=error_message)
        error_message = "Hata! 2'den az resim sayısı mevcut."
        paths = "boş"
        return render_template('error.html', path = paths ,error_message=error_message)
assets_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')

if __name__ == '__main__':
    #create_users_table()
    #create_imageSimilarities_table()
    app.run(host="0.0.0.0", port=5000)
