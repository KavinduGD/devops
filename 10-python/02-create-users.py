#!/usr/bin/python3

import os
import grp

print('Adding users')
print('##########################################################################################')
users = ['devops', 'dev', 'qa']

for user in users:
    exit_code = os.system('id ' + user)

    if (exit_code != 0):
        print('user do not exit')
        os.system('useradd '+user)
        print('user created successfully')
        print('###################################')
    else:
        print('user already exits')
        print('###################################')


print('Adding jenkins group')
print('##########################################################################################')

exit_code = os.system('grep  jenkins /etc/group')

if exit_code != 0:
    print('jenkins user group do not exits')
    os.system('groupadd jenkins')
    print('group added successfully')
    print('######################################')
else:
    print('Group exits')
    print('######################################')

print('Adding users to the jenkins group')
print('##########################################################################################')

for user in users:
    exit_code = os.system(f"groups {user} | grep -w jenkins")
    if (exit_code != 0):
        print('user is not in the jenkins group')
        os.system(f"usermod -aG jenkins {user}")
        print('user added successfully')
        print('#######################################')
    else:
        print('user already in the jenkins group')
        print('#######################################')


print('creating a directory')
print('#########################################################################################')

path = '/opt/jenkins'

if os.path.isdir(path):
    print('Directory exist')
    print('#######################################')
else:
    os.mkdir(path)
    print('directory created')
    print('#######################################')


print('Give directory ownership to jenkins')
print('#########################################################################################')

ownership_info = os.stat(path)

gid = ownership_info.st_gid()

gname = grp.getgrgid(gid).gr_name

if gname != 'jenkins':
    os.system(f"chgrp -R jenkins {path}")
    print('group ownership changed')
    print('#######################################')
else:
    print('already owned by jenkins group')
    print('#######################################')
