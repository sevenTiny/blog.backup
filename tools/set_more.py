import os

path = './source/_posts/'

for filename in os.listdir(path):
    # read file content
    with open(os.path.join(path, filename), 'r+', encoding='UTF-8') as f:
        content = f.read()

        # get content length
        length = len(content)

        if (length < 500):
            continue

        # if <!-- more --> exists, then skip
        if (content.find('<!-- more -->') != -1):
            continue

        # find the first \n after 300
        index = 300
        while (content[index] != '\n'):
            index += 1

        # if the first \n is after 300, then add <!-- more -->
        if (index > 300 and index < length-1):
            content = content[:index] + '\n\n<!-- more -->' + content[index:]
            print(filename + ' added <!-- more --> at ' + str(index))
            # print(content)

        # write file
        f.seek(0)
        f.truncate()
        f.write(content)
