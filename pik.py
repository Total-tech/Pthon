import pickle

cars = ["Audi","BMW","Tesla","Mercedees"]
file = "mycar.pkl"
fileobj = open(file, 'wb')
pickle.dump(cars, fileobj)
fileobj.close()