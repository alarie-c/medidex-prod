from flask import Flask, redirect, request, url_for, render_template
import backend

app = Flask(__name__)

N = 4

@app.route('/search/<param>', methods=['GET', 'POST'])
def search(param):
    results = []
    n = 0

    if request.method == 'POST':
        # Get search parameter from form data
        search_param = request.form.get('search-box')
        name_results = backend.search_for(search_param)

        # Check if search results are valid
        if name_results.unwrap() != 0:
            # Process each name in search results
            for name in name_results.unwrap():
                d = backend.get_dict_from_name(name)
                if d is not None:
                    d['namelower'] = d['name'].lower()
                    results.append(d)

            # Set `n` to the length of results
            n = name_results.len()
        else:
            return 'There was an error'

    # Render the template with results, count `n`, and search parameter `param`
    return render_template('search.html', results=results, n=n, param=param)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        param = request.form.get('search-box')
        return search(param)
    else:
        return render_template('home.html', n=N)
    
@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        param = request.form.get('search-box')
        return search(param)
    else:
        return render_template('about.html', n=N)

@app.route('/<name>', methods=['GET', 'POST'])
def entry(name):
    if request.method == 'POST':
        param = request.form.get('search-box')
        return search(param)
    else:
        data = backend.get_dict_from_name(name)
        tags = backend.split_tags(data)
        print(tags)
        
        if data != None:
            return render_template(
                'entry.html',
                n=N,
                tags=tags,
                name=data['name'],
                clas=data['clas'],
                use=data['use'],
                func=data['func'],
                routes=data['routes'],
                effects=data['effects'],
                serious_effects=data['serious_effects'],
                other=data['other'],
                brands=data['brands'],
                citations=data['citations']
            )
        else:
            print("TODO: No results found")
            return '404'

# @app.route('/admin')
# def redir():
#     return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()