'''
Created on Sep 20, 2014

@author: vak
'''
from os.path import join, dirname, realpath
from os import walk, makedirs
from shutil import rmtree
from protobuf.main import non_cli_main
from time import time
import sys
import os

TEST_PROTO_DIR = join(dirname(realpath(__file__)), 'protos')
OUTPUT_DIR = '/tmp/protobuf2uml_tests'

import unittest
import traceback

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_all_files(self):
        rmtree(OUTPUT_DIR, ignore_errors=True)
        makedirs(OUTPUT_DIR)
        for root, dirs, files in walk(TEST_PROTO_DIR):
            # print(root)
            # print([join(root, name) for name in files])
            for f in files:
                if f.endswith('.proto'):
                    iproto_pathname = join(root, f)
                    output_dot_pathname = '%s.dot' % join(OUTPUT_DIR, f)
                    print('testing on %s ...' % iproto_pathname, end=' ', file=sys.stderr)
                    sys.stderr.flush()
                    start_time = time()
                    with open(output_dot_pathname, 'wt') as ofile:
                        try:
                            non_cli_main(iproto_pathname,
                                         import_dirs=[TEST_PROTO_DIR],
                                         ostream=ofile)
                            generation_time = time() - start_time
                            start_time = time()
                        except Exception as e:
                            print(' FAIL', file=sys.stderr)
                            print('Exception: %s ' % e, file=sys.stderr)
                            traceback.print_exc()
                            continue
                        
                    output_png_pathname = '%s.png' % output_dot_pathname
                    cmd = 'dot -Tpng <%s >%s' % (output_dot_pathname, output_png_pathname)
                    # cmd = 'which dot >%s' % output_png_pathname
                    exit_code = os.system(cmd)
                    assert 0 == exit_code, 'dot crashed with exit code: %d' % exit_code
                    print(' OK [generation-to-dot time:%.1f, dot time: %.1f]' % (generation_time,
                                                                                 time() - start_time),
                          file=sys.stderr)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
