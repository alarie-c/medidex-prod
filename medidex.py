from flask import Flask, redirect, request, url_for, render_template
import backend

app = Flask(__name__)

# # TEMPORARY
# ondansetron = {
#     "name": "Ondansetron",
#     "clas": "(Anti-emetic)",
#     "tags": [],
#     "use": "Ondansetron is used to prevent vomiting and naseau, commonly paired with chemotherapy treatment for cancer.",
#     "func": "Ondansetron antagonizes serotonin receptors in the brain and Vagus nerve, preventing nausea and vomiting triggers in the body from reaching the brain.",
#     "routes": "Oral (PO), Intramuscular (IM), Intravenous (IV)",
#     "effects": "headaches, fatigue, dry mouth, malaise, constipation",
#     "brands": "Zofran",
#     "citations": [
#             {
#                 "uid": "1",
#                 "title": "Ondansetron",
#                 "source": "National Library of Medicine",
#                 "link": "https://medlineplus.gov/druginfo/meds/a601209.html"
#             }
#         ]
# }

# do a search
# result = backend.search_for('ondans')
# print(result.unwrap())
n = 150
def entry(data):
    print(data['name'])

@app.route('/search/<param>')
def search(param, results, n: int):
    print(param)
    print(results)
    return render_template('search.html', results=results, n=n, param=param)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_param = request.form.get('search-box')
        name_results: backend.SearchResult = backend.search_for(search_param)

        if name_results.unwrap() != 0:
            results = []
            for name in name_results.unwrap():
                d = backend.get_dict_from_name(name)
                if d != None:
                    results.append(d)
                continue
            return search(search_param, results, name_results.len())
        else:
            return 'There was an error'

    return render_template('home.html', n=backend.get_len())

# @app.route('/<name>')
# def entry(name):
#     # GRAB JSON FILE FOR NAME
#     if name == 'ondansetron':
#         return render_template(
#             'entry.html', 
#             name='ondansetron',
#             clas=ondansetron["clas"],
#             use=ondansetron["use"],
#             func=ondansetron["func"],
#             routes=ondansetron["routes"],
#             effects=ondansetron["effects"],
#             brands=ondansetron["brands"],
#             citations=ondansetron['citations'],
#         )
#     else:
#         return f'Displaying page for {name}'
        
# @app.route('/admin')
# def redir():
#     return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()