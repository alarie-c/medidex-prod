from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# TEMPORARY
ondansetron = {
    "name": "Ondansetron",
    "clas": "(Anti-emetic)",
    "tags": [],
    "use": "Ondansetron is used to prevent vomiting and naseau, commonly paired with chemotherapy treatment for cancer.",
    "func": "Ondansetron antagonizes serotonin receptors in the brain and Vagus nerve, preventing nausea and vomiting triggers in the body from reaching the brain.",
    "routes": "Oral (PO), Intramuscular (IM), Intravenous (IV)",
    "effects": "headaches, fatigue, dry mouth, malaise, constipation",
    "brands": "Zofran",
    "citations": [
            {
                "uid": "1",
                "title": "Ondansetron",
                "source": "National Library of Medicine",
                "link": "https://medlineplus.gov/druginfo/meds/a601209.html"
            }
        ]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<name>')
def entry(name):
    # GRAB JSON FILE FOR NAME
    if name == 'ondansetron':
        return render_template(
            'entry.html', 
            name='ondansetron',
            clas=ondansetron["clas"],
            use=ondansetron["use"],
            func=ondansetron["func"],
            routes=ondansetron["routes"],
            effects=ondansetron["effects"],
            brands=ondansetron["brands"],
            citations=ondansetron['citations'],
        )
    else:
        return f'Displaying page for {name}'
        
# @app.route('/admin')
# def redir():
#     return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()