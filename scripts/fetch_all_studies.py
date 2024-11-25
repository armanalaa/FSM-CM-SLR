from scholarly import scholarly, ProxyGenerator
import os
import pickle

# Proxy and Scholar ID setup
pg = ProxyGenerator()
scholar_id = 'scholar_id'

# Ensure proper directory structure
file_path = '../data/raw/1137_CachedPapers.pkl'
os.makedirs('./data/raw', exist_ok=True)

# Check and load or initialize the cached paper dictionary
if os.path.exists(file_path):
    with open(file_path, 'rb') as fp:
        try:
            paper_diz = pickle.load(fp)
            if len(paper_diz) == 0:
                print("The paper_diz dictionary is empty. Starting fresh.")
            else:
                print(f"Loaded {len(paper_diz)} papers from the file.")
        except EOFError:
            print("The file exists but is empty or corrupted. Starting with an empty dictionary.")
            paper_diz = {}
else:
    print("File not found. Creating a new one.")
    paper_diz = {}

# Function to create Excel (TSV file)
def creaExcel(nome, diz_titles, keys, bibkeys, titles, dropped, dropNoVenue):
    f = open(nome + '.tsv', 'w', encoding='UTF8')
    firstRow = 'searchStrings'
    for k in keys:
        firstRow += '\t' + k
    for k in bibkeys:
        firstRow += '\t' + "['bib']" + k

    titles = list(diz_titles.keys())
    titles.sort()
    print(firstRow, file=f)
    for p in titles:
        index = len(diz_titles[p]) - 1
        if diz_titles[p][index]['bib']['venue'] == 'NA' and dropNoVenue:
            dropped.add(p)
            continue
        row = str(diz_titles[p][0])
        for k in keys:
            if k in diz_titles[p][index].keys():
                row += '\t' + str(diz_titles[p][index][k])
            else:
                row += '\tNA'
        for k in bibkeys:
            if k in diz_titles[p][index]['bib'].keys():
                row += '\t' + str(diz_titles[p][index]['bib'][k])
            else:
                row += '\tNA'
        print(row, file=f)
    f.close()

#41 query strings
s=['"software estimation" AND "conceptual model" AND "function point"',
'"software estimation" AND "conceptual model" AND "FPA"',
'"software estimation" AND "conceptual model" AND "COSMIC"',
'"software estimation" AND "UML" AND "function point"',
'"software estimation" AND "UML" AND "FPA"',
'"software estimation" AND "UML" AND "COSMIC"',
'"software estimation" AND "BPMN" AND "function point"',
'"software estimation" AND "BPMN" AND "FPA"',
'"software estimation" AND "BPMN" AND "COSMIC"',
'"software estimation" AND "Entity-Relationship" AND "function point"',
'"software estimation" AND "Entity-Relationship" AND "FPA"',
'"software estimation" AND "Entity-Relationship" AND "COSMIC"',
'"software estimation" AND "Data Flow Diagram" AND "function point"',
'"software estimation" AND "Data Flow Diagram" AND "FPA"',
'"software estimation" AND "Data Flow Diagram" AND "COSMIC"',
'"early sizing" AND "conceptual model" AND "function point"',
'"early sizing" AND "conceptual model" AND "FPA"',
'"early sizing" AND "conceptual model" AND "COSMIC"',
'"early sizing" AND "UML" AND "function point"',
'"early sizing" AND "UML" AND "FPA"',
'"early sizing" AND "UML" AND "COSMIC"',
'"early sizing" AND "BPMN" AND "function point"',
'"early sizing" AND "BPMN" AND "FPA"',
'"early sizing" AND "BPMN" AND "COSMIC"',
'"early sizing" AND "Entity-Relationship" AND "function point"',
'"early sizing" AND "Entity-Relationship" AND "FPA"',
'"early sizing" AND "Entity-Relationship" AND "COSMIC"',
'"early sizing" AND "Data Flow Diagram" AND "function point"',
'"early sizing" AND "Data Flow Diagram" AND "FPA"',
'"early sizing" AND "Data Flow Diagram" AND "COSMIC"',
'"FSM" AND "UML" AND "COSMIC"',
'"software estimation" AND "conceptual model" AND "Functional Size Measurement"',
'"software estimation" AND "UML" AND "Functional Size Measurement"',
'"software estimation" AND "BPMN" AND "Functional Size Measurement"',
'"software estimation" AND "Entity-Relationship" AND "Functional Size Measurement"',
'"software estimation" AND "Data Flow Diagram" AND "Functional Size Measurement"',
'"early sizing" AND "conceptual model" AND "Functional Size Measurement"',
'"early sizing" AND "UML" AND "Functional Size Measurement"',
'"early sizing" AND "BPMN" AND "Functional Size Measurement"',
'"early sizing" AND "Entity-Relationship" AND "Functional Size Measurement"',
'"early sizing" AND "Data Flow Diagram" AND "Functional Size Measurement"']

# Log initialization
f = open('log.txt', 'a', encoding='UTF8')
print('---------------------------------------', file=f)
f.close()

# Sorting and processing the existing papers
ll = list(paper_diz.keys())
ll.sort()

if len(ll) > 0:
    print(paper_diz[ll[0]][1].keys())
else:
    print("No existing papers to process. Starting fresh.")

# Main loop for querying or loading data
fromData = False
newPapers = set()

for q in range(1, len(s) + 1):
    queryPapers = []
    query = s[q - 1]
    if fromData:
        with open(f'../data/raw/queryCachedPapers/titles{q}.pkl', 'rb') as fp:
            queryPapers = pickle.load(fp)
    else:
        search_results = scholarly.search_pubs(query)
        print(q + 1000, query, search_results.total_results)
        f = open('log.txt', 'a', encoding='UTF8')
        print(q + 1000, query, search_results.total_results, file=f)
        f.close()

        for i, result in enumerate(search_results):
            print(i, result['bib']['title'])
            print('.', end='')
            queryPapers.append(result)

        results = []
        for i in range(len(queryPapers)):
            print('+++', i, queryPapers[i]['bib']['title'])
            newPapers.add(queryPapers[i]['bib']['title'])
            if queryPapers[i]['bib']['title'] not in paper_diz:
                ris1 = scholarly.search_single_pub(queryPapers[i]['bib']['title'])
            else:
                ris1 = paper_diz[queryPapers[i]['bib']['title']][1]
            results.append(ris1)

        filledQueryPapers = []
        for i in range(len(results)):
            if results[i]['bib']['title'] not in paper_diz:
                paper_diz[results[i]['bib']['title']] = [[]]
                try:
                    paper_diz[results[i]['bib']['title']].append(scholarly.fill(results[i]))
                except:
                    paper_diz[results[i]['bib']['title']].append(results[i])

            paper_diz[results[i]['bib']['title']][0].append(q)
            pf = paper_diz[results[i]['bib']['title']][1]
            filledQueryPapers.append(pf)

# Save the updated paper_diz dictionary
if not fromData:
    with open(file_path, 'wb') as fp:
        pickle.dump(paper_diz, fp)

# Generate the final Excel file
keys = set()
bibkeys = set()
for e in paper_diz:
    index = len(paper_diz[e]) - 1
    keys = keys.union(paper_diz[e][index].keys())
    bibkeys = bibkeys.union(paper_diz[e][index]['bib'].keys())
if 'bib' in keys:
    keys.remove('bib')

bibkeys = list(bibkeys)
keys = list(keys)
bibkeys.sort()
keys.sort()
dropped = set()

creaExcel('../data/raw/allPapers', paper_diz, keys, bibkeys, ll, dropped, True)
