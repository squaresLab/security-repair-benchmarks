#! /usr/bin/env3 python3
import subprocess
import json
def main():
   # Opening JSON file
    f = open('bothSan.json')
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    f.close()
    f = open('/workspace/compile_commands.json')
    comp_cs = json.load(f)
    f.close()

    d = {}
    #dictionary with file as the key and compile command as the value
    for c in comp_cs:
        d[c['file']] = c['command']
    compiled = set()
    if data['num_addsan'] > 0:
        for i in data['addsans']:
            for j in i['trace']:
                if j[0] == "" or j[1] == "":
                    continue
                f_name=j[0]
                f_path=j[1]
                cmd = get_llvm_cmd(d, f_name, f_path)
                print(cmd)
                if cmd not in compiled:
                    subprocess.getstatusoutput(cmd)
                    compiled.add(cmd)

    if data['num_ubsan'] > 0:
        for i in data['ubsans']:
            l = i['loc']
            f_name=l[0]
            f_path=l[1] if isinstance(l[1],str) else l[1][0]
            print(str(f_path)+" "+str(type(f_path)))
            cmd = get_llvm_cmd(d, f_name, f_path)
            print(cmd)
            if cmd not in compiled:
                subprocess.getstatusoutput(cmd)
                compiled.add(cmd)

def get_llvm_cmd(d, f_name, f_path):
    llvm_cmd = "clang-11 -emit-llvm -S -g -O0 -c {} {}"
    path ="{}/{}".format(f_path,f_name)
    p = fix_path(path.split('/'))
    try:
        cc = " " + compile_commands(d[p], p)
    except Exception as e:
        raise(e)
    return llvm_cmd.format(p, cc)

def fix_path(p):
    np = []
    for i in range(len(p)-1):
        if p[i] == '..':
            np.pop()
        else:
            np.append(p[i])
    np.append(p[len(p)-1])
    return '/'.join(np)

def compile_commands(c,p):
    #things to remove from the compile flags
    rm = ['-g', 'cc', '-c', '-O2', '-O1',
            '-O2','-O3','-Os','-Ofast','-Og', '-o']
    s = c.split(' ')
    for r in rm:
        if r in s:
            s.remove(r)
    #remove the statement <filelane>.o
    for i in s:
        if i.endswith('.o'):
            s.remove(i)
    c = ' '.join(s)
    c = c.replace(p,'')
    return c

if __name__ == "__main__":
    main()

