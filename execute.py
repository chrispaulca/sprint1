import os
import json
import sys

#NOTE 1 : MAKE THIS TAKE AN ARGUMENT FROM SYS
#NOTE 2 : WRITE TO FILE NAMED : prefix.txt > where prefix should be the variable passed from NOTE1

#NOTE 1
prefix = 'anchor'
def extract_keys(d):
    keys = []
    for k,v in d.items():
        if isinstance(v,dict):
            keys = keys + extract_keys(v)
    return list(d.keys()) + keys

def no_dupe_keys(d):
    keys_list = extract_keys(d)
    print('stuff')

    ct = 0
    for i in keys_list:
        if i == 'age' or i == 'name':
            ct += 1
    
    if ct == 2:
        return(True)
    else:
        return(False)

def extract_json(lines):
    outputs = []
    for line in lines:
        try:
            blob = json.loads(line)
            name, age = blob['name'], blob['prop']['age']
            if name != "" and age != "" and no_dupe_keys(blob):
                outputs = outputs + [str(name) + ' ' + str(age)]
        except Exception as e:
            pass

    return outputs

outputs = []

def execute(prefix)
    try:
        os.chdir('./srv/runme')

        print('Directory changed.')
        for file in os.listdir('.'):
            if file.startswith(prefix):
                try:
                    with open(file) as txt_file:
                        openned_file = txt_file.readlines()
                        outputs = outputs + extract_json(openned_file)
                        # NOTE2
                except:
                    print file, ': error in JSON'
    except:
        print 'Sorry, this directoy does not exist.'

    to_print = '\n'.join(outputs)

    with open(prefix+'.txt',w) as f:
        write(to_print)