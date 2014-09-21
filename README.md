protobuf2uml
============

protobuf2uml - a tool to create an UML diagram from a protobuf files

Description
-----------
protobuf2uml has been written to visualize the architecture of the messages coded in Google Protocol Buffers (protobuf). 

DISCLAIMER: I've spent a weekend to successfully generate UML graph for my project. I'm sorry if this won't work for you.

Install
-------
protobuf2uml is written in Python3, uses ANTLR4 and implies that you have Python3, GraphViz "dot" utility and ANTLR4 run-time files for Python installed:

    sudo apt-get install graphviz python3

as for Python3 antlr runtime, you could use your favorite way to install it from https://pypi.python.org/pypi/antlr4-python3-runtime/ , for example:

    sudo pip3 install antlr4-python3-runtime

Just be sure, that you do install it for python3 and not for python2 ;)

I have no installer yet, so just create some working directory to put protobuf2uml files there:

    mkdir ~/pkg
    cd ~/pkg
    git clone git@github.com:vak/protobuf2uml.git


Usage
-----

    PYTHONPATH=~/pkg/bin/protobuf python3 ~/pkg/protobuf2uml/main.py -I import_path1:import_path2 path/to/my/proto.proto | dot -Tjpg >/tmp/uml.jpg


Your contributions
------------------
Your patches and pull-requests are welcome.
For example, I didn't spent time for some 'exotic' protobuf features that might be important for you:

- import public "protofile"
- trigraph literals
- extend
- ...put your unlucky feature here ;)

So, if you get a non-working case, create an issue for it at least, or even better, fork my repo, make a fix and drop a pull request back on me.

Credits
-------
The antlr grammar & lexer description files were taken from https://github.com/yesme/protobuf-parser/ 
and a bit adjusted to be used with antlr4 and Python.

