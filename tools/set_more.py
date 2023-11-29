import os

path = './source/_posts/'

for filename in os.listdir(path):
    # read file content
    with open(os.path.join(path, filename), 'r+', encoding='UTF-8') as f:
        content = f.read()
        if (content.find('<!-- more -->') != -1):
            print('find more in ' + filename)
