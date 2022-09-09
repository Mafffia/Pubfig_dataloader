import os
def load_files(path='./pubfig'):
    os.chdir(path)
    names = os.listdir()
    ret = {}
    for name in names:
        if(name=='.DS_Store'):
            continue
        os.chdir(name)
        files = os.listdir()
        files = [x for x in files if '.jpg' in x]
        for i in range(len(files)):
            files[i] = path + '/' + name + '/' + files[i]
        ret[name] = files
        os.chdir('..')
    os.chdir('..')
    return ret
