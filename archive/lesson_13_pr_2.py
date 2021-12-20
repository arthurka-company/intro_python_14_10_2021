import pickle


with open('../category_links.pkl', 'rb') as f:
    data = pickle.load(f)

print(type(data))
print(len(data))
print(data[:2])
