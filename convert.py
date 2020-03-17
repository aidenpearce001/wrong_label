import os,glob

path = '.'

ls = []
classes = open('logo.names','r')
for i in classes:
    ls.append(i)
dict_names = {i:ls.index(i) for i in ls}

dict_names = {x.replace('\n', ''): v for x, v in dict_names.items()} 

print(dict_names)

def files_path(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def most_appear(list): 
    return max(set(list), key = list.count) 

files = os.listdir(path)
for name in files:
    print(name)
    for k,v in dict_names.items():
        if k == name.upper() :
            for file in files_path(name):
                if os.stat(name+'/'+file).st_size != 0 and file != 'classes.txt':
                    print(file)
                    with open(name+'/'+file, "r+") as f:
                        old = f.read()
                        print(old)
                        f.seek(0) 
                        new = old.split()
                        new[0] = str(v)
                        if len(new) > 5:
                            new = [sub.replace(most_appear(new), str(v)) for sub in new]
                        f.write(' '.join(new))


