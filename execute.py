import os
import json

prefix = 'anchor'

def extract_json(lines):
    outputs = []
    for line in lines:
        try:
            blob = json.loads(line)
            name, age = blob['name'], blob['prop']['age']
            if name != "" and age != "":
                outputs = outputs + [str(name) + ' ' + str(age)]
        except:
            pass

    return outputs

outputs = []
try:
    os.chdir('/srv/runme')

    print('Directory changed.')
    for file in os.listdir('.'):
        if file.startswith(prefix):
            try:
                with open(file) as txt_file:
                    openned_file = txt_file.readlines()
                    outputs = outputs + extract_json(openned_file)
            except:
                print file, ': error in JSON'
except:
    print 'Sorry, this directoy does not exist.'
print '\n'.join(outputs)