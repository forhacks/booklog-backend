import re, pickle

tags_regex = re.compile('(<.*?>)')
escape_regex = re.compile('([^a-zA-Z\.\, ]*)')

def harvest(k):
    j = k.split(',')
    return {
        "book_name" : j[0],
        "author" : j[1],
        "rating" : j[2],
        "votes" : j[3],
        "description" : re.sub(escape_regex, '', re.sub(tags_regex, '', ','.join(j[4:-6]))).strip(),
        "link" : j[-1],
        "genre" : j[-2],
        "isbn13" : j[-3],
        "first_published" : j[-4],
        "no_of_pages" : j[-5],
        "book_type" : j[-6]
    }


props = file("goodreads_list_props.csv").read().splitlines()
output = []

for i, p in enumerate(props):
    h = harvest(p)

    genre = h["genre"]
    desc = h["description"]
    rating = h["rating"]

    output.append((genre, desc, rating))
with open("data.pkl", "w") as f:
    pickle.dump(output, f)




