'''
Container:
- Namespaces
- Chroot
- Cgroups

docker run --rm -it ubuntu /bin/bash
hostname
ps
'''
import subprocess 
import sys
import argparse

# docker run image <cmd> <params>
# py main.py run    <cmd> <params>

'''
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('package_name', help='Name of your new python package', nargs="?", default='mypackage')
    parser.add_argument('description', help='Description of the package purpose', nargs="?", default='')
    parser.add_argument('git_url', help='Url of the github repo', nargs="?", default='')
    return parser.parse_args()
'''


# print(sys.argv)
def run():
    print('Running',*sys.argv[2:],sep=" ", end='\n')
    cmd = subprocess.run(sys.argv[2:], shell=True)
    subprocess.CREATE_NEW_PROCESS_GROUP
def main():
    switch={
        'run': run()
    }
    switch.get(sys.argv[1],"Bad command")

main()