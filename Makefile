all: bin/protobuf/ProtoParser.py
	@echo "ok, what's now?.."
bin/protobuf/ProtoParser.py: bin/protobuf/ProtoLexer.py

bin/protobuf/%.py: protobuf/%.g4
	java -jar lib/antlr-4.4-complete.jar -Dlanguage=Python3 -o bin $< -lib bin/protobuf 
