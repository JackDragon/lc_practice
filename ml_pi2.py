class MockFS(object):
    def __init__(self):
        self.files = {
            '1.c': {'mtime': 1, 'content': '''
#include "a.h"
#include "c.h"
// #include "no_such_file.h"
'''},

            'a.h': {'mtime': 1, 'content': '''
#pragma once

#include "b.h"
#include "c.h"
'''},

            'b.h': {'mtime': 1, 'content': '''
#pragma once

#include "d.h"
'''},

            'c.h': {'mtime': 1, 'content': '''
#pragma once
'''},

            'd.h': {'mtime': 11, 'content': '''
#pragma once

#include "a.h"
#include "e.h"
'''},

            'e.h': {'mtime': 1, 'content': '''
#pragma once
'''},

            '2.c': {'mtime': 1, 'content': '''
#include "b.h"
'''},

            '3.c': {'mtime': 1, 'content': '''
#include "g.h"
'''},

            'g.h': {'mtime': 1, 'content': '''
#include "e.h"
'''}
        }

        self.num_calls = {'read': 0, 'stat': 0}

    def __del__(self):
        print('shutting down FS, num calls: {}'.format(list(sorted(self.num_calls.items()))))

    def listdir(self):
        return self.files.keys()

    def read(self, fname):
        self.num_calls['read'] += 1
        return self.files[fname]['content']

    def stat(self, fname):
        self.num_calls['stat'] += 1
        return self.files[fname]['mtime']


fs = MockFS()

"""
No changes above this point
"""
import re


def get_dependent_files(file_content):
    return re.findall('^#include "(.*\.h)', file_content, re.M)


def get_files_to_build(candidate_filenames, last_build_timestamp):
    depend_dict = {}
    time_dict = {}
    for filename, file_dict in fs.files.items():
        # get_dependent_files will go through the content and find which .h files the file includes
        depend_dict[filename] = get_dependent_files(file_dict['content'])
        time_dict[filename] = file_dict['mtime']

    memo = {}

    def traverse(filename, last_build_timestamp, visited=None):
        if filename in memo:
            return memo[filename]
        self_changed = time_dict[filename] >= last_build_timestamp
        if self_changed:
            memo[filename] = True
            return True

        if not visited:
            visited = set([filename])
        elif filename in visited:
            return self_changed
        else:
            visited.add(filename)

        for dependent_file in depend_dict[filename]:
            if traverse(dependent_file, last_build_timestamp, visited):
                memo[filename] = True
                return True
        memo[filename] = self_changed
        return self_changed

    ret_subset = []
    for filename in candidate_filenames:
        if (traverse(filename, last_build_timestamp)):
            ret_subset.append(filename)
    return ret_subset


print(get_files_to_build(['1.c', '2.c'], 10))




