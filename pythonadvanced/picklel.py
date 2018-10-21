import pickle

l1 = [1,2,43,5,6,6]
pickle.dump(l1,open("save.pkl","wb"))
obj = pickle.load(open("save.pkl","rb"))
for x in obj:
    print(x)