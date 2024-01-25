from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Function to search in the CSV file
def search_csv(query):
    results = []
    with open('Movies_list.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            for key, value in row.items():
                if query.lower() in value.lower():
                    results.append(row)
                    break  # break to avoid duplicates in results
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        results = search_csv(query)
        return render_template('index.html', results=results, query=query)

    return render_template('index.html', results=None, query=None)

if __name__ == '__main__':
    app.run(debug=True)
