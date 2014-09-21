import sys
from os.path import isfile

import argparse

from antlr4 import *
from ProtoLexer import ProtoLexer
from ProtoParser import ProtoParser, ProtoParserListener
from os.path import split, join, realpath


class BaseListener(ProtoParserListener):
    _processed_files = []
    def __init__(self, targeted_dir, import_dirs, ostream):
        self._targeted_dir = targeted_dir
        self._import_dirs = import_dirs
        self._ostream = ostream
             
#    def exitProto(self, ctx):         
#        print("Oh, a proto!")
    def give_me_some_import_file(self, import_file_name):
        
        realpath_import_file_name = realpath(join(self._targeted_dir, import_file_name))
        if isfile(realpath_import_file_name):
            return realpath_import_file_name

        realpath_import_file_name = realpath(import_file_name)
        if isfile(realpath_import_file_name):
            return realpath_import_file_name
        
        for d in self._import_dirs:
            realpath_import_file_name = realpath(join(d, import_file_name))
            #print ('?: %s' % realpath_import_file_name, file=sys.stderr)
            if isfile(realpath_import_file_name):
                return realpath_import_file_name
        raise Exception("Can't find any file as for '%s'. You may want to specify -I dir for a import search path" % import_file_name)

    def exitImport_file_name(self, ctx):
        # print("oh, a file name...")
        # print(dir(ctx))
        import_file_name = ctx.getText()[1:]
        import_file_name = import_file_name[:(len(import_file_name) - 1)]
        pathname = self.give_me_some_import_file(import_file_name)
        if len(list(ctx.parentCtx.getChildren())) != 2:
            raise Exception('This form of import is not supported yet, sorry.')
        if pathname not in self._processed_files:
            self._processed_files.append(pathname)
            FileToTreeParser(pathname, self._import_dirs, ostream=self._ostream)

class DotListener(BaseListener):
    _basic_types = ['double', 'float', 'int32', 'int64', 'uint32', 'uint64', 'sint32', 'sint64',
                   'fixed32', 'fixed64', 'sfixed32', 'sfixed64', 'bool', 'string', 'bytes']
    _prologue = '''digraph G {
    fontname = "Bitstream Vera Sans"
    fontsize = 8

    node [
            fontname = "Bitstream Vera Sans"
            fontsize = 8
            shape = "record"
    ]

    edge [
            fontname = "Bitstream Vera Sans"
            fontsize = 8
            arrowhead = diamond
            labeldistance = 2
    ]

'''
    _epilogue = '\n}\n'
    _attribute_fmt = '+ %(attribute_name)s : %(attribute_type)s\l'
    _node_prologue_fmt = '''
    %(class_name)s [
        label = "{%(class_name)s|'''
    _node_epilogue_fmt = '|}"\n        ]'
    
    def __init__(self, targeted_dir, import_dirs, ostream):
        super().__init__(targeted_dir, import_dirs, ostream)
        self._aggregations = []
        
    def enterMessage_def(self, ctx):
        class_name = ctx.getChild(1).getText()
        print(self._node_prologue_fmt % { 
                                 'class_name' : class_name
                                 }, file=self._ostream)
        self._curr_message = class_name
        
    def exitMessage_def(self, ctx):
        print(self._node_epilogue_fmt, file=self._ostream)
        
    def exitMessage_item_def(self, ctx):
        qualifier = ctx.getChild(0).getText().lower()
        attribute_type = ctx.getChild(1).getText()
        attribute_name = ctx.getChild(2).getText()
        if attribute_type in self._basic_types:
            print(self._attribute_fmt % {'attribute_name' : attribute_name,
                                         'attribute_type' : attribute_type},
                  file=self._ostream)
        else:
            if qualifier == 'optional':
                quantifier = '"0..1"' 
            if qualifier == 'required':
                quantifier = '"1"'
            if qualifier == 'repeated':
                quantifier = '"0..*"' 
 
            self._aggregations.append((attribute_type, 
                                       self._curr_message, 
                                       "1", 
                                       attribute_name, 
                                       quantifier))
            
    def exitProto(self, ctx):
        # from pprint import pprint
        # pprint(self._aggregations)
        for edge in self._aggregations:
            # print('E: %s' % str(edge))
            print('        edge[headlabel=%s, label=%s, taillabel=%s]\n' % edge[2:], file=self._ostream)
            print('        %s -> %s\n' % edge[:2], file=self._ostream)    

class FileToTreeParser(object):
    def __init__(self, pathname, import_dirs, ostream):
        self._pathname = pathname
        self._dir, self._filename = split(pathname)
        input = FileStream(pathname)
        lexer = ProtoLexer(input)
        stream = CommonTokenStream(lexer)        
        parser = ProtoParser(stream)
        self._tree = parser.proto()
        printer = DotListener(targeted_dir=self._dir, import_dirs = import_dirs, ostream=ostream)
        walker = ParseTreeWalker()
        walker.walk(printer, self._tree)    

def non_cli_main(pathname_protobuf_ifile, import_dirs, ostream=sys.stdout):
    print(DotListener._prologue, file=ostream)
    file_to_tree_parser = FileToTreeParser(pathname_protobuf_ifile, 
                                           import_dirs=import_dirs, 
                                           ostream=ostream)
    print(DotListener._epilogue, file=ostream)
    # print (file_to_tree_parser._tree.toStringTree())
    # print('------')

def cli_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-I', '--proto_path', help='search also this colon-separated list of directories for proto imports')
    parser.add_argument('proto_file')
    args = parser.parse_args()
    
    import_dirs = args.proto_path.split(':') if args.proto_path else []
    non_cli_main(pathname_protobuf_ifile = args.proto_file, 
                 import_dirs = import_dirs, 
                 ostream=sys.stdout)
 
if __name__ == '__main__':
    cli_main()

