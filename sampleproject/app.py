from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
import io

app = Flask(__name__)


@app.route('/')
def home():
    dataset = pd.read_csv(r"C:\Users\E15\Documents\GitHub\PythonAIBasic\sampleproject\titanic.csv")
    df = dataset[['Name', 'Fare']]
    df_list = df.to_list()
    print(df_list)
    
    
    return render_template('home.html', data=df_list)

@app.route('/m')
def matplt():
    data = {
        'Name':['Mg Mg', 'Aung Aung'],
        'Age':[20,30]
    }
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    df.plot(kind='bar' ,x='Name', y='Age', ax=ax)
    
    img = io.BytesIO()
    plt.savefig(img, format='jpg')
    img.seek(0)
    plt.close(fig)
    return send_file(img, mimetype='image/jpg')
    

if __name__ == '__main__':
    app.run()