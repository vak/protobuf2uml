# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ProtoParserListener import ProtoParserListener
else:
    from ProtoParserListener import ProtoParserListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3,")
        buf.write("\u0120\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\3\2\3\3")
        buf.write("\3\3\5\3M\n\3\3\4\3\4\3\5\3\5\5\5S\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\7\6\\\n\6\f\6\16\6_\13\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\t\3\t\5\tk\n\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f|\n")
        buf.write("\f\f\f\16\f\177\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\5\16\u0089\n\16\3\17\3\17\7\17\u008d\n\17\f\17\16\17")
        buf.write("\u0090\13\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\7\21\u009d\n\21\f\21\16\21\u00a0\13\21\5")
        buf.write("\21\u00a2\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\7\24\u00ae\n\24\f\24\16\24\u00b1\13\24\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u00b7\n\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u00bf\n\26\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\6\30\u00ca\n\30\r\30\16\30\u00cb\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\5\31\u00d4\n\31\3\31\3\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\5\32\u00dd\n\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\5\33\u00e5\n\33\3\33\3\33\3\34\3\34\3")
        buf.write("\35\3\35\3\35\3\35\6\35\u00ef\n\35\r\35\16\35\u00f0\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u00f7\n\36\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \6 \u00ff\n \r \16 \u0100\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\7!\u010e\n!\f!\16!\u0111\13!\3!\3!\5!\u0115")
        buf.write("\n!\3!\5!\u0118\n!\3\"\3\"\3#\3#\3$\3$\3$\2\2%\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDF\2\4\3\2#$\3\2\37\"\u0121\2H\3\2\2\2\4L\3\2\2\2")
        buf.write("\6N\3\2\2\2\bR\3\2\2\2\n]\3\2\2\2\fb\3\2\2\2\16f\3\2\2")
        buf.write("\2\20h\3\2\2\2\22o\3\2\2\2\24q\3\2\2\2\26w\3\2\2\2\30")
        buf.write("\u0082\3\2\2\2\32\u0088\3\2\2\2\34\u008a\3\2\2\2\36\u0093")
        buf.write("\3\2\2\2 \u00a1\3\2\2\2\"\u00a3\3\2\2\2$\u00a9\3\2\2\2")
        buf.write("&\u00af\3\2\2\2(\u00b2\3\2\2\2*\u00ba\3\2\2\2,\u00c2\3")
        buf.write("\2\2\2.\u00c9\3\2\2\2\60\u00cd\3\2\2\2\62\u00d7\3\2\2")
        buf.write("\2\64\u00e0\3\2\2\2\66\u00e8\3\2\2\28\u00ee\3\2\2\2:\u00f2")
        buf.write("\3\2\2\2<\u00fa\3\2\2\2>\u00fe\3\2\2\2@\u0102\3\2\2\2")
        buf.write("B\u0119\3\2\2\2D\u011b\3\2\2\2F\u011d\3\2\2\2HI\t\2\2")
        buf.write("\2I\3\3\2\2\2JM\7#\2\2KM\5\6\4\2LJ\3\2\2\2LK\3\2\2\2M")
        buf.write("\5\3\2\2\2NO\t\3\2\2O\7\3\2\2\2PS\7\36\2\2QS\5\2\2\2R")
        buf.write("P\3\2\2\2RQ\3\2\2\2S\t\3\2\2\2T\\\5\f\7\2U\\\5\20\t\2")
        buf.write("V\\\5\24\13\2W\\\5\"\22\2X\\\5\64\33\2Y\\\5*\26\2Z\\\5")
        buf.write(":\36\2[T\3\2\2\2[U\3\2\2\2[V\3\2\2\2[W\3\2\2\2[X\3\2\2")
        buf.write("\2[Y\3\2\2\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2")
        buf.write("^`\3\2\2\2_]\3\2\2\2`a\7\2\2\3a\13\3\2\2\2bc\7\7\2\2c")
        buf.write("d\5\16\b\2de\7\34\2\2e\r\3\2\2\2fg\5\2\2\2g\17\3\2\2\2")
        buf.write("hj\7\b\2\2ik\7\6\2\2ji\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\5")
        buf.write("\22\n\2mn\7\34\2\2n\21\3\2\2\2op\7 \2\2p\23\3\2\2\2qr")
        buf.write("\7\t\2\2rs\5 \21\2st\7\31\2\2tu\5\32\16\2uv\7\34\2\2v")
        buf.write("\25\3\2\2\2wx\7\27\2\2x}\5\30\r\2yz\7\33\2\2z|\5\30\r")
        buf.write("\2{y\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0080\3")
        buf.write("\2\2\2\177}\3\2\2\2\u0080\u0081\7\30\2\2\u0081\27\3\2")
        buf.write("\2\2\u0082\u0083\5 \21\2\u0083\u0084\7\31\2\2\u0084\u0085")
        buf.write("\5\32\16\2\u0085\31\3\2\2\2\u0086\u0089\5\4\3\2\u0087")
        buf.write("\u0089\5\34\17\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2")
        buf.write("\2\u0089\33\3\2\2\2\u008a\u008e\7\23\2\2\u008b\u008d\5")
        buf.write("\36\20\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e")
        buf.write("\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3\2\2\2")
        buf.write("\u0090\u008e\3\2\2\2\u0091\u0092\7\24\2\2\u0092\35\3\2")
        buf.write("\2\2\u0093\u0094\7#\2\2\u0094\u0095\7\32\2\2\u0095\u0096")
        buf.write("\5\32\16\2\u0096\37\3\2\2\2\u0097\u00a2\7#\2\2\u0098\u0099")
        buf.write("\7\25\2\2\u0099\u009a\5\2\2\2\u009a\u009e\7\26\2\2\u009b")
        buf.write("\u009d\7%\2\2\u009c\u009b\3\2\2\2\u009d\u00a0\3\2\2\2")
        buf.write("\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a2\3")
        buf.write("\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u0097\3\2\2\2\u00a1\u0098")
        buf.write("\3\2\2\2\u00a2!\3\2\2\2\u00a3\u00a4\7\n\2\2\u00a4\u00a5")
        buf.write("\5$\23\2\u00a5\u00a6\7\23\2\2\u00a6\u00a7\5&\24\2\u00a7")
        buf.write("\u00a8\7\24\2\2\u00a8#\3\2\2\2\u00a9\u00aa\7#\2\2\u00aa")
        buf.write("%\3\2\2\2\u00ab\u00ae\5\24\13\2\u00ac\u00ae\5(\25\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2")
        buf.write("\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\'\3\2\2")
        buf.write("\2\u00b1\u00af\3\2\2\2\u00b2\u00b3\7#\2\2\u00b3\u00b4")
        buf.write("\7\31\2\2\u00b4\u00b6\7\37\2\2\u00b5\u00b7\5\26\f\2\u00b6")
        buf.write("\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2")
        buf.write("\u00b8\u00b9\7\34\2\2\u00b9)\3\2\2\2\u00ba\u00bb\7\13")
        buf.write("\2\2\u00bb\u00bc\5,\27\2\u00bc\u00be\7\23\2\2\u00bd\u00bf")
        buf.write("\5.\30\2\u00be\u00bd\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00c1\7\24\2\2\u00c1+\3\2\2\2\u00c2")
        buf.write("\u00c3\7#\2\2\u00c3-\3\2\2\2\u00c4\u00ca\5\24\13\2\u00c5")
        buf.write("\u00ca\5\60\31\2\u00c6\u00ca\5*\26\2\u00c7\u00ca\5\"\22")
        buf.write("\2\u00c8\u00ca\5\62\32\2\u00c9\u00c4\3\2\2\2\u00c9\u00c5")
        buf.write("\3\2\2\2\u00c9\u00c6\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc/\3\2\2\2\u00cd\u00ce\7\35\2")
        buf.write("\2\u00ce\u00cf\5\b\5\2\u00cf\u00d0\7#\2\2\u00d0\u00d1")
        buf.write("\7\31\2\2\u00d1\u00d3\7\37\2\2\u00d2\u00d4\5\26\f\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5\u00d6\7\34\2\2\u00d6\61\3\2\2\2\u00d7\u00d8\7\r")
        buf.write("\2\2\u00d8\u00d9\7\37\2\2\u00d9\u00dc\7\16\2\2\u00da\u00dd")
        buf.write("\7\37\2\2\u00db\u00dd\7\17\2\2\u00dc\u00da\3\2\2\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\7\34\2")
        buf.write("\2\u00df\63\3\2\2\2\u00e0\u00e1\7\f\2\2\u00e1\u00e2\5")
        buf.write("\66\34\2\u00e2\u00e4\7\23\2\2\u00e3\u00e5\58\35\2\u00e4")
        buf.write("\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\3\2\2\2")
        buf.write("\u00e6\u00e7\7\24\2\2\u00e7\65\3\2\2\2\u00e8\u00e9\5\2")
        buf.write("\2\2\u00e9\67\3\2\2\2\u00ea\u00ef\5\24\13\2\u00eb\u00ef")
        buf.write("\5\60\31\2\u00ec\u00ef\5*\26\2\u00ed\u00ef\5\"\22\2\u00ee")
        buf.write("\u00ea\3\2\2\2\u00ee\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2")
        buf.write("\u00ee\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00ee\3")
        buf.write("\2\2\2\u00f0\u00f1\3\2\2\2\u00f19\3\2\2\2\u00f2\u00f3")
        buf.write("\7\20\2\2\u00f3\u00f4\5<\37\2\u00f4\u00f6\7\23\2\2\u00f5")
        buf.write("\u00f7\5> \2\u00f6\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write("\u00f8\3\2\2\2\u00f8\u00f9\7\24\2\2\u00f9;\3\2\2\2\u00fa")
        buf.write("\u00fb\7#\2\2\u00fb=\3\2\2\2\u00fc\u00ff\5\24\13\2\u00fd")
        buf.write("\u00ff\5@!\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff")
        buf.write("\u0100\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2")
        buf.write("\u0101?\3\2\2\2\u0102\u0103\7\22\2\2\u0103\u0104\5B\"")
        buf.write("\2\u0104\u0105\7\25\2\2\u0105\u0106\5D#\2\u0106\u0107")
        buf.write("\7\26\2\2\u0107\u0108\7\21\2\2\u0108\u0109\7\25\2\2\u0109")
        buf.write("\u010a\5F$\2\u010a\u0117\7\26\2\2\u010b\u010f\7\23\2\2")
        buf.write("\u010c\u010e\5\24\13\2\u010d\u010c\3\2\2\2\u010e\u0111")
        buf.write("\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\u0112\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0114\7\24\2")
        buf.write("\2\u0113\u0115\7\34\2\2\u0114\u0113\3\2\2\2\u0114\u0115")
        buf.write("\3\2\2\2\u0115\u0118\3\2\2\2\u0116\u0118\7\34\2\2\u0117")
        buf.write("\u010b\3\2\2\2\u0117\u0116\3\2\2\2\u0118A\3\2\2\2\u0119")
        buf.write("\u011a\7#\2\2\u011aC\3\2\2\2\u011b\u011c\5\2\2\2\u011c")
        buf.write("E\3\2\2\2\u011d\u011e\5\2\2\2\u011eG\3\2\2\2\35LR[]j}")
        buf.write("\u0088\u008e\u009e\u00a1\u00ad\u00af\u00b6\u00be\u00c9")
        buf.write("\u00cb\u00d3\u00dc\u00e4\u00ee\u00f0\u00f6\u00fe\u0100")
        buf.write("\u010f\u0114\u0117")
        return buf.getvalue()
		

class ProtoParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    BLOCK_OPEN=17
    MESSAGE_LITERAL=9
    SERVICE_LITERAL=14
    PROTOBUF_SCOPE_LITERAL=27
    EXTENSIONS_TO_LITERAL=12
    LINE_COMMENT=1
    PAREN_CLOSE=20
    ITEM_TERMINATOR=26
    OPTION_LITERAL=7
    EXTENSIONS_MAX_LITERAL=13
    WHITESPACE=3
    EQUALS=23
    BOOL_LITERAL=31
    EXTENSIONS_DEF_LITERAL=11
    FLOAT_LITERAL=32
    COLON=24
    QUALIFIED_IDENTIFIER=34
    MULTILINE_COMMENT=2
    STRING_LITERAL=30
    BLOCK_CLOSE=18
    FIELD_IDENTIFIER=35
    PACKAGE_LITERAL=5
    IMPORT_PUBLIC=4
    COMMA=25
    IDENTIFIER=33
    INTEGER_LITERAL=29
    EXTEND_LITERAL=10
    PROTOBUF_TYPE_LITERAL=28
    ENUM_LITERAL=8
    IMPORT_LITERAL=6
    PAREN_OPEN=19
    BRACKET_CLOSE=22
    RPC_LITERAL=16
    RETURNS_LITERAL=15
    BRACKET_OPEN=21
    PROTO=36
    OPTION_PREDEFINED=37
    OPTION_CUSTOMIZED=38
    OPTION_VALUE_ITEM=39
    OPTION_VALUE_OBJECT=40
    ENUM_FIELD=41
    MESSAGE_FIELD=42

    tokenNames = [ "<INVALID>", "LINE_COMMENT", "MULTILINE_COMMENT", "WHITESPACE", 
                   "'public'", "'package'", "'import'", "'option'", "'enum'", 
                   "'message'", "'extend'", "'extensions'", "'to'", "'max'", 
                   "'service'", "'returns'", "'rpc'", "'{'", "'}'", "'('", 
                   "')'", "'['", "']'", "'='", "':'", "','", "';'", "PROTOBUF_SCOPE_LITERAL", 
                   "PROTOBUF_TYPE_LITERAL", "INTEGER_LITERAL", "STRING_LITERAL", 
                   "BOOL_LITERAL", "FLOAT_LITERAL", "IDENTIFIER", "QUALIFIED_IDENTIFIER", 
                   "FIELD_IDENTIFIER", "PROTO", "OPTION_PREDEFINED", "OPTION_CUSTOMIZED", 
                   "OPTION_VALUE_ITEM", "OPTION_VALUE_OBJECT", "ENUM_FIELD", 
                   "MESSAGE_FIELD" ]

    RULE_all_identifier = 0
    RULE_all_value = 1
    RULE_literal_value = 2
    RULE_proto_type = 3
    RULE_proto = 4
    RULE_package_def = 5
    RULE_package_name = 6
    RULE_import_def = 7
    RULE_import_file_name = 8
    RULE_option_line_def = 9
    RULE_option_field_def = 10
    RULE_option_field_item = 11
    RULE_option_all_value = 12
    RULE_option_value_object = 13
    RULE_option_value_item = 14
    RULE_option_name = 15
    RULE_enum_def = 16
    RULE_enum_name = 17
    RULE_enum_content = 18
    RULE_enum_item_def = 19
    RULE_message_def = 20
    RULE_message_name = 21
    RULE_message_content = 22
    RULE_message_item_def = 23
    RULE_message_ext_def = 24
    RULE_ext_def = 25
    RULE_ext_name = 26
    RULE_ext_content = 27
    RULE_service_def = 28
    RULE_service_name = 29
    RULE_service_content = 30
    RULE_rpc_def = 31
    RULE_rpc_name = 32
    RULE_req_name = 33
    RULE_resp_name = 34

    ruleNames =  [ "all_identifier", "all_value", "literal_value", "proto_type", 
                   "proto", "package_def", "package_name", "import_def", 
                   "import_file_name", "option_line_def", "option_field_def", 
                   "option_field_item", "option_all_value", "option_value_object", 
                   "option_value_item", "option_name", "enum_def", "enum_name", 
                   "enum_content", "enum_item_def", "message_def", "message_name", 
                   "message_content", "message_item_def", "message_ext_def", 
                   "ext_def", "ext_name", "ext_content", "service_def", 
                   "service_name", "service_content", "rpc_def", "rpc_name", 
                   "req_name", "resp_name" ]

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class All_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ProtoParser.IDENTIFIER, 0)

        def QUALIFIED_IDENTIFIER(self):
            return self.getToken(ProtoParser.QUALIFIED_IDENTIFIER, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_all_identifier

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterAll_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitAll_identifier(self)




    def all_identifier(self):

        localctx = ProtoParser.All_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_all_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not(_la==ProtoParser.IDENTIFIER or _la==ProtoParser.QUALIFIED_IDENTIFIER):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class All_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ProtoParser.IDENTIFIER, 0)

        def literal_value(self):
            return self.getTypedRuleContext(ProtoParser.Literal_valueContext,0)


        def getRuleIndex(self):
            return ProtoParser.RULE_all_value

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterAll_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitAll_value(self)




    def all_value(self):

        localctx = ProtoParser.All_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_all_value)
        try:
            self.state = 74
            token = self._input.LA(1)
            if token in [self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(self.IDENTIFIER)

            elif token in [self.INTEGER_LITERAL, self.STRING_LITERAL, self.BOOL_LITERAL, self.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73 
                self.literal_value()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LITERAL(self):
            return self.getToken(ProtoParser.FLOAT_LITERAL, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(ProtoParser.INTEGER_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(ProtoParser.STRING_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(ProtoParser.BOOL_LITERAL, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_literal_value

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterLiteral_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitLiteral_value(self)




    def literal_value(self):

        localctx = ProtoParser.Literal_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.INTEGER_LITERAL) | (1 << self.STRING_LITERAL) | (1 << self.BOOL_LITERAL) | (1 << self.FLOAT_LITERAL))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Proto_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROTOBUF_TYPE_LITERAL(self):
            return self.getToken(ProtoParser.PROTOBUF_TYPE_LITERAL, 0)

        def all_identifier(self):
            return self.getTypedRuleContext(ProtoParser.All_identifierContext,0)


        def getRuleIndex(self):
            return ProtoParser.RULE_proto_type

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterProto_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitProto_type(self)




    def proto_type(self):

        localctx = ProtoParser.Proto_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_proto_type)
        try:
            self.state = 80
            token = self._input.LA(1)
            if token in [self.PROTOBUF_TYPE_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(self.PROTOBUF_TYPE_LITERAL)

            elif token in [self.IDENTIFIER, self.QUALIFIED_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79 
                self.all_identifier()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProtoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ProtoParser.EOF, 0)

        def option_line_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Option_line_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Option_line_defContext,i)


        def ext_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Ext_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Ext_defContext,i)


        def import_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Import_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Import_defContext,i)


        def message_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Message_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Message_defContext,i)


        def enum_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Enum_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Enum_defContext,i)


        def service_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Service_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Service_defContext,i)


        def package_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Package_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Package_defContext,i)


        def getRuleIndex(self):
            return ProtoParser.RULE_proto

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterProto(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitProto(self)




    def proto(self):

        localctx = ProtoParser.ProtoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_proto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.PACKAGE_LITERAL) | (1 << self.IMPORT_LITERAL) | (1 << self.OPTION_LITERAL) | (1 << self.ENUM_LITERAL) | (1 << self.MESSAGE_LITERAL) | (1 << self.EXTEND_LITERAL) | (1 << self.SERVICE_LITERAL))) != 0):
                self.state = 89
                token = self._input.LA(1)
                if token in [self.PACKAGE_LITERAL]:
                    self.state = 82 
                    self.package_def()

                elif token in [self.IMPORT_LITERAL]:
                    self.state = 83 
                    self.import_def()

                elif token in [self.OPTION_LITERAL]:
                    self.state = 84 
                    self.option_line_def()

                elif token in [self.ENUM_LITERAL]:
                    self.state = 85 
                    self.enum_def()

                elif token in [self.EXTEND_LITERAL]:
                    self.state = 86 
                    self.ext_def()

                elif token in [self.MESSAGE_LITERAL]:
                    self.state = 87 
                    self.message_def()

                elif token in [self.SERVICE_LITERAL]:
                    self.state = 88 
                    self.service_def()

                else:
                    raise NoViableAltException(self)

                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(self.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Package_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PACKAGE_LITERAL(self):
            return self.getToken(ProtoParser.PACKAGE_LITERAL, 0)

        def package_name(self):
            return self.getTypedRuleContext(ProtoParser.Package_nameContext,0)


        def ITEM_TERMINATOR(self):
            return self.getToken(ProtoParser.ITEM_TERMINATOR, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_package_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterPackage_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitPackage_def(self)




    def package_def(self):

        localctx = ProtoParser.Package_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_package_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(self.PACKAGE_LITERAL)
            self.state = 97 
            self.package_name()
            self.state = 98
            self.match(self.ITEM_TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Package_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_identifier(self):
            return self.getTypedRuleContext(ProtoParser.All_identifierContext,0)


        def getRuleIndex(self):
            return ProtoParser.RULE_package_name

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterPackage_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitPackage_name(self)




    def package_name(self):

        localctx = ProtoParser.Package_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_package_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100 
            self.all_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Import_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT_PUBLIC(self):
            return self.getToken(ProtoParser.IMPORT_PUBLIC, 0)

        def import_file_name(self):
            return self.getTypedRuleContext(ProtoParser.Import_file_nameContext,0)


        def IMPORT_LITERAL(self):
            return self.getToken(ProtoParser.IMPORT_LITERAL, 0)

        def ITEM_TERMINATOR(self):
            return self.getToken(ProtoParser.ITEM_TERMINATOR, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_import_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterImport_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitImport_def(self)




    def import_def(self):

        localctx = ProtoParser.Import_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_import_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(self.IMPORT_LITERAL)
            self.state = 104
            _la = self._input.LA(1)
            if _la==ProtoParser.IMPORT_PUBLIC:
                self.state = 103
                self.match(self.IMPORT_PUBLIC)


            self.state = 106 
            self.import_file_name()
            self.state = 107
            self.match(self.ITEM_TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Import_file_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(ProtoParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_import_file_name

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterImport_file_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitImport_file_name(self)




    def import_file_name(self):

        localctx = ProtoParser.Import_file_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_import_file_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(self.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Option_line_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def option_all_value(self):
            return self.getTypedRuleContext(ProtoParser.Option_all_valueContext,0)


        def EQUALS(self):
            return self.getToken(ProtoParser.EQUALS, 0)

        def ITEM_TERMINATOR(self):
            return self.getToken(ProtoParser.ITEM_TERMINATOR, 0)

        def option_name(self):
            return self.getTypedRuleContext(ProtoParser.Option_nameContext,0)


        def OPTION_LITERAL(self):
            return self.getToken(ProtoParser.OPTION_LITERAL, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_option_line_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterOption_line_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitOption_line_def(self)




    def option_line_def(self):

        localctx = ProtoParser.Option_line_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_option_line_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(self.OPTION_LITERAL)
            self.state = 112 
            self.option_name()
            self.state = 113
            self.match(self.EQUALS)
            self.state = 114 
            self.option_all_value()
            self.state = 115
            self.match(self.ITEM_TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Option_field_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def option_field_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Option_field_itemContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Option_field_itemContext,i)


        def BRACKET_CLOSE(self):
            return self.getToken(ProtoParser.BRACKET_CLOSE, 0)

        def BRACKET_OPEN(self):
            return self.getToken(ProtoParser.BRACKET_OPEN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ProtoParser.COMMA)
            else:
                return self.getToken(ProtoParser.COMMA, i)

        def getRuleIndex(self):
            return ProtoParser.RULE_option_field_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterOption_field_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitOption_field_def(self)




    def option_field_def(self):

        localctx = ProtoParser.Option_field_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_option_field_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(self.BRACKET_OPEN)
            self.state = 118 
            self.option_field_item()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ProtoParser.COMMA:
                self.state = 119
                self.match(self.COMMA)
                self.state = 120 
                self.option_field_item()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(self.BRACKET_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Option_field_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def option_all_value(self):
            return self.getTypedRuleContext(ProtoParser.Option_all_valueContext,0)


        def EQUALS(self):
            return self.getToken(ProtoParser.EQUALS, 0)

        def option_name(self):
            return self.getTypedRuleContext(ProtoParser.Option_nameContext,0)


        def getRuleIndex(self):
            return ProtoParser.RULE_option_field_item

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterOption_field_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitOption_field_item(self)




    def option_field_item(self):

        localctx = ProtoParser.Option_field_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_option_field_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128 
            self.option_name()
            self.state = 129
            self.match(self.EQUALS)
            self.state = 130 
            self.option_all_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Option_all_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def option_value_object(self):
            return self.getTypedRuleContext(ProtoParser.Option_value_objectContext,0)


        def all_value(self):
            return self.getTypedRuleContext(ProtoParser.All_valueContext,0)


        def getRuleIndex(self):
            return ProtoParser.RULE_option_all_value

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterOption_all_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitOption_all_value(self)




    def option_all_value(self):

        localctx = ProtoParser.Option_all_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_option_all_value)
        try:
            self.state = 134
            token = self._input.LA(1)
            if token in [self.INTEGER_LITERAL, self.STRING_LITERAL, self.BOOL_LITERAL, self.FLOAT_LITERAL, self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132 
                self.all_value()

            elif token in [self.BLOCK_OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133 
                self.option_value_object()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Option_value_objectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_OPEN(self):
            return self.getToken(ProtoParser.BLOCK_OPEN, 0)

        def BLOCK_CLOSE(self):
            return self.getToken(ProtoParser.BLOCK_CLOSE, 0)

        def option_value_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Option_value_itemContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Option_value_itemContext,i)


        def getRuleIndex(self):
            return ProtoParser.RULE_option_value_object

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterOption_value_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitOption_value_object(self)




    def option_value_object(self):

        localctx = ProtoParser.Option_value_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_option_value_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(self.BLOCK_OPEN)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ProtoParser.IDENTIFIER:
                self.state = 137 
                self.option_value_item()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(self.BLOCK_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Option_value_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def option_all_value(self):
            return self.getTypedRuleContext(ProtoParser.Option_all_valueContext,0)


        def IDENTIFIER(self):
            return self.getToken(ProtoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(ProtoParser.COLON, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_option_value_item

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterOption_value_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitOption_value_item(self)




    def option_value_item(self):

        localctx = ProtoParser.Option_value_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_option_value_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(self.IDENTIFIER)
            self.state = 146
            self.match(self.COLON)
            self.state = 147 
            self.option_all_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Option_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAREN_CLOSE(self):
            return self.getToken(ProtoParser.PAREN_CLOSE, 0)

        def IDENTIFIER(self):
            return self.getToken(ProtoParser.IDENTIFIER, 0)

        def PAREN_OPEN(self):
            return self.getToken(ProtoParser.PAREN_OPEN, 0)

        def FIELD_IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ProtoParser.FIELD_IDENTIFIER)
            else:
                return self.getToken(ProtoParser.FIELD_IDENTIFIER, i)

        def all_identifier(self):
            return self.getTypedRuleContext(ProtoParser.All_identifierContext,0)


        def getRuleIndex(self):
            return ProtoParser.RULE_option_name

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterOption_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitOption_name(self)




    def option_name(self):

        localctx = ProtoParser.Option_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_option_name)
        self._la = 0 # Token type
        try:
            self.state = 159
            token = self._input.LA(1)
            if token in [self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(self.IDENTIFIER)

            elif token in [self.PAREN_OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(self.PAREN_OPEN)
                self.state = 151 
                self.all_identifier()
                self.state = 152
                self.match(self.PAREN_CLOSE)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ProtoParser.FIELD_IDENTIFIER:
                    self.state = 153
                    self.match(self.FIELD_IDENTIFIER)
                    self.state = 158
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_OPEN(self):
            return self.getToken(ProtoParser.BLOCK_OPEN, 0)

        def BLOCK_CLOSE(self):
            return self.getToken(ProtoParser.BLOCK_CLOSE, 0)

        def enum_content(self):
            return self.getTypedRuleContext(ProtoParser.Enum_contentContext,0)


        def enum_name(self):
            return self.getTypedRuleContext(ProtoParser.Enum_nameContext,0)


        def ENUM_LITERAL(self):
            return self.getToken(ProtoParser.ENUM_LITERAL, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_enum_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterEnum_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitEnum_def(self)




    def enum_def(self):

        localctx = ProtoParser.Enum_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_enum_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(self.ENUM_LITERAL)
            self.state = 162 
            self.enum_name()
            self.state = 163
            self.match(self.BLOCK_OPEN)
            self.state = 164 
            self.enum_content()
            self.state = 165
            self.match(self.BLOCK_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ProtoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_enum_name

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterEnum_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitEnum_name(self)




    def enum_name(self):

        localctx = ProtoParser.Enum_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_enum_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(self.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_contentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def option_line_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Option_line_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Option_line_defContext,i)


        def enum_item_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Enum_item_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Enum_item_defContext,i)


        def getRuleIndex(self):
            return ProtoParser.RULE_enum_content

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterEnum_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitEnum_content(self)




    def enum_content(self):

        localctx = ProtoParser.Enum_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_enum_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ProtoParser.OPTION_LITERAL or _la==ProtoParser.IDENTIFIER:
                self.state = 171
                token = self._input.LA(1)
                if token in [self.OPTION_LITERAL]:
                    self.state = 169 
                    self.option_line_def()

                elif token in [self.IDENTIFIER]:
                    self.state = 170 
                    self.enum_item_def()

                else:
                    raise NoViableAltException(self)

                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_item_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(ProtoParser.INTEGER_LITERAL, 0)

        def option_field_def(self):
            return self.getTypedRuleContext(ProtoParser.Option_field_defContext,0)


        def EQUALS(self):
            return self.getToken(ProtoParser.EQUALS, 0)

        def IDENTIFIER(self):
            return self.getToken(ProtoParser.IDENTIFIER, 0)

        def ITEM_TERMINATOR(self):
            return self.getToken(ProtoParser.ITEM_TERMINATOR, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_enum_item_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterEnum_item_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitEnum_item_def(self)




    def enum_item_def(self):

        localctx = ProtoParser.Enum_item_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_enum_item_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(self.IDENTIFIER)
            self.state = 177
            self.match(self.EQUALS)
            self.state = 178
            self.match(self.INTEGER_LITERAL)
            self.state = 180
            _la = self._input.LA(1)
            if _la==ProtoParser.BRACKET_OPEN:
                self.state = 179 
                self.option_field_def()


            self.state = 182
            self.match(self.ITEM_TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Message_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MESSAGE_LITERAL(self):
            return self.getToken(ProtoParser.MESSAGE_LITERAL, 0)

        def BLOCK_OPEN(self):
            return self.getToken(ProtoParser.BLOCK_OPEN, 0)

        def message_content(self):
            return self.getTypedRuleContext(ProtoParser.Message_contentContext,0)


        def BLOCK_CLOSE(self):
            return self.getToken(ProtoParser.BLOCK_CLOSE, 0)

        def message_name(self):
            return self.getTypedRuleContext(ProtoParser.Message_nameContext,0)


        def getRuleIndex(self):
            return ProtoParser.RULE_message_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterMessage_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitMessage_def(self)




    def message_def(self):

        localctx = ProtoParser.Message_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_message_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(self.MESSAGE_LITERAL)
            self.state = 185 
            self.message_name()
            self.state = 186
            self.match(self.BLOCK_OPEN)
            self.state = 188
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.OPTION_LITERAL) | (1 << self.ENUM_LITERAL) | (1 << self.MESSAGE_LITERAL) | (1 << self.EXTENSIONS_DEF_LITERAL) | (1 << self.PROTOBUF_SCOPE_LITERAL))) != 0):
                self.state = 187 
                self.message_content()


            self.state = 190
            self.match(self.BLOCK_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Message_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ProtoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_message_name

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterMessage_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitMessage_name(self)




    def message_name(self):

        localctx = ProtoParser.Message_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_message_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(self.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Message_contentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def message_ext_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Message_ext_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Message_ext_defContext,i)


        def message_item_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Message_item_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Message_item_defContext,i)


        def option_line_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Option_line_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Option_line_defContext,i)


        def enum_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Enum_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Enum_defContext,i)


        def message_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Message_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Message_defContext,i)


        def getRuleIndex(self):
            return ProtoParser.RULE_message_content

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterMessage_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitMessage_content(self)




    def message_content(self):

        localctx = ProtoParser.Message_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_message_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 199
                token = self._input.LA(1)
                if token in [self.OPTION_LITERAL]:
                    self.state = 194 
                    self.option_line_def()

                elif token in [self.PROTOBUF_SCOPE_LITERAL]:
                    self.state = 195 
                    self.message_item_def()

                elif token in [self.MESSAGE_LITERAL]:
                    self.state = 196 
                    self.message_def()

                elif token in [self.ENUM_LITERAL]:
                    self.state = 197 
                    self.enum_def()

                elif token in [self.EXTENSIONS_DEF_LITERAL]:
                    self.state = 198 
                    self.message_ext_def()

                else:
                    raise NoViableAltException(self)

                self.state = 201 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.OPTION_LITERAL) | (1 << self.ENUM_LITERAL) | (1 << self.MESSAGE_LITERAL) | (1 << self.EXTENSIONS_DEF_LITERAL) | (1 << self.PROTOBUF_SCOPE_LITERAL))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Message_item_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(ProtoParser.INTEGER_LITERAL, 0)

        def proto_type(self):
            return self.getTypedRuleContext(ProtoParser.Proto_typeContext,0)


        def PROTOBUF_SCOPE_LITERAL(self):
            return self.getToken(ProtoParser.PROTOBUF_SCOPE_LITERAL, 0)

        def option_field_def(self):
            return self.getTypedRuleContext(ProtoParser.Option_field_defContext,0)


        def EQUALS(self):
            return self.getToken(ProtoParser.EQUALS, 0)

        def IDENTIFIER(self):
            return self.getToken(ProtoParser.IDENTIFIER, 0)

        def ITEM_TERMINATOR(self):
            return self.getToken(ProtoParser.ITEM_TERMINATOR, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_message_item_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterMessage_item_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitMessage_item_def(self)




    def message_item_def(self):

        localctx = ProtoParser.Message_item_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_message_item_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(self.PROTOBUF_SCOPE_LITERAL)
            self.state = 204 
            self.proto_type()
            self.state = 205
            self.match(self.IDENTIFIER)
            self.state = 206
            self.match(self.EQUALS)
            self.state = 207
            self.match(self.INTEGER_LITERAL)
            self.state = 209
            _la = self._input.LA(1)
            if _la==ProtoParser.BRACKET_OPEN:
                self.state = 208 
                self.option_field_def()


            self.state = 211
            self.match(self.ITEM_TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Message_ext_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None # Token

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(ProtoParser.INTEGER_LITERAL)
            else:
                return self.getToken(ProtoParser.INTEGER_LITERAL, i)

        def EXTENSIONS_MAX_LITERAL(self):
            return self.getToken(ProtoParser.EXTENSIONS_MAX_LITERAL, 0)

        def EXTENSIONS_TO_LITERAL(self):
            return self.getToken(ProtoParser.EXTENSIONS_TO_LITERAL, 0)

        def EXTENSIONS_DEF_LITERAL(self):
            return self.getToken(ProtoParser.EXTENSIONS_DEF_LITERAL, 0)

        def ITEM_TERMINATOR(self):
            return self.getToken(ProtoParser.ITEM_TERMINATOR, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_message_ext_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterMessage_ext_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitMessage_ext_def(self)




    def message_ext_def(self):

        localctx = ProtoParser.Message_ext_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_message_ext_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(self.EXTENSIONS_DEF_LITERAL)
            self.state = 214
            self.match(self.INTEGER_LITERAL)
            self.state = 215
            self.match(self.EXTENSIONS_TO_LITERAL)
            self.state = 218
            token = self._input.LA(1)
            if token in [self.INTEGER_LITERAL]:
                self.state = 216
                localctx.v = self.match(self.INTEGER_LITERAL)

            elif token in [self.EXTENSIONS_MAX_LITERAL]:
                self.state = 217
                localctx.v = self.match(self.EXTENSIONS_MAX_LITERAL)

            else:
                raise NoViableAltException(self)

            self.state = 220
            self.match(self.ITEM_TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ext_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_OPEN(self):
            return self.getToken(ProtoParser.BLOCK_OPEN, 0)

        def ext_name(self):
            return self.getTypedRuleContext(ProtoParser.Ext_nameContext,0)


        def BLOCK_CLOSE(self):
            return self.getToken(ProtoParser.BLOCK_CLOSE, 0)

        def EXTEND_LITERAL(self):
            return self.getToken(ProtoParser.EXTEND_LITERAL, 0)

        def ext_content(self):
            return self.getTypedRuleContext(ProtoParser.Ext_contentContext,0)


        def getRuleIndex(self):
            return ProtoParser.RULE_ext_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterExt_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitExt_def(self)




    def ext_def(self):

        localctx = ProtoParser.Ext_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_ext_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(self.EXTEND_LITERAL)
            self.state = 223 
            self.ext_name()
            self.state = 224
            self.match(self.BLOCK_OPEN)
            self.state = 226
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.OPTION_LITERAL) | (1 << self.ENUM_LITERAL) | (1 << self.MESSAGE_LITERAL) | (1 << self.PROTOBUF_SCOPE_LITERAL))) != 0):
                self.state = 225 
                self.ext_content()


            self.state = 228
            self.match(self.BLOCK_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ext_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_identifier(self):
            return self.getTypedRuleContext(ProtoParser.All_identifierContext,0)


        def getRuleIndex(self):
            return ProtoParser.RULE_ext_name

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterExt_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitExt_name(self)




    def ext_name(self):

        localctx = ProtoParser.Ext_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ext_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230 
            self.all_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ext_contentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def message_item_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Message_item_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Message_item_defContext,i)


        def option_line_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Option_line_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Option_line_defContext,i)


        def enum_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Enum_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Enum_defContext,i)


        def message_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Message_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Message_defContext,i)


        def getRuleIndex(self):
            return ProtoParser.RULE_ext_content

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterExt_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitExt_content(self)




    def ext_content(self):

        localctx = ProtoParser.Ext_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ext_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 236
                token = self._input.LA(1)
                if token in [self.OPTION_LITERAL]:
                    self.state = 232 
                    self.option_line_def()

                elif token in [self.PROTOBUF_SCOPE_LITERAL]:
                    self.state = 233 
                    self.message_item_def()

                elif token in [self.MESSAGE_LITERAL]:
                    self.state = 234 
                    self.message_def()

                elif token in [self.ENUM_LITERAL]:
                    self.state = 235 
                    self.enum_def()

                else:
                    raise NoViableAltException(self)

                self.state = 238 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.OPTION_LITERAL) | (1 << self.ENUM_LITERAL) | (1 << self.MESSAGE_LITERAL) | (1 << self.PROTOBUF_SCOPE_LITERAL))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Service_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def service_content(self):
            return self.getTypedRuleContext(ProtoParser.Service_contentContext,0)


        def service_name(self):
            return self.getTypedRuleContext(ProtoParser.Service_nameContext,0)


        def BLOCK_OPEN(self):
            return self.getToken(ProtoParser.BLOCK_OPEN, 0)

        def SERVICE_LITERAL(self):
            return self.getToken(ProtoParser.SERVICE_LITERAL, 0)

        def BLOCK_CLOSE(self):
            return self.getToken(ProtoParser.BLOCK_CLOSE, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_service_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterService_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitService_def(self)




    def service_def(self):

        localctx = ProtoParser.Service_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_service_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(self.SERVICE_LITERAL)
            self.state = 241 
            self.service_name()
            self.state = 242
            self.match(self.BLOCK_OPEN)
            self.state = 244
            _la = self._input.LA(1)
            if _la==ProtoParser.OPTION_LITERAL or _la==ProtoParser.RPC_LITERAL:
                self.state = 243 
                self.service_content()


            self.state = 246
            self.match(self.BLOCK_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Service_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ProtoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_service_name

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterService_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitService_name(self)




    def service_name(self):

        localctx = ProtoParser.Service_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_service_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(self.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Service_contentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rpc_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Rpc_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Rpc_defContext,i)


        def option_line_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Option_line_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Option_line_defContext,i)


        def getRuleIndex(self):
            return ProtoParser.RULE_service_content

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterService_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitService_content(self)




    def service_content(self):

        localctx = ProtoParser.Service_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_service_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 252
                token = self._input.LA(1)
                if token in [self.OPTION_LITERAL]:
                    self.state = 250 
                    self.option_line_def()

                elif token in [self.RPC_LITERAL]:
                    self.state = 251 
                    self.rpc_def()

                else:
                    raise NoViableAltException(self)

                self.state = 254 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ProtoParser.OPTION_LITERAL or _la==ProtoParser.RPC_LITERAL):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Rpc_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def req_name(self):
            return self.getTypedRuleContext(ProtoParser.Req_nameContext,0)


        def resp_name(self):
            return self.getTypedRuleContext(ProtoParser.Resp_nameContext,0)


        def PAREN_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(ProtoParser.PAREN_OPEN)
            else:
                return self.getToken(ProtoParser.PAREN_OPEN, i)

        def option_line_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoParser.Option_line_defContext)
            else:
                return self.getTypedRuleContext(ProtoParser.Option_line_defContext,i)


        def BLOCK_OPEN(self):
            return self.getToken(ProtoParser.BLOCK_OPEN, 0)

        def rpc_name(self):
            return self.getTypedRuleContext(ProtoParser.Rpc_nameContext,0)


        def RPC_LITERAL(self):
            return self.getToken(ProtoParser.RPC_LITERAL, 0)

        def ITEM_TERMINATOR(self):
            return self.getToken(ProtoParser.ITEM_TERMINATOR, 0)

        def BLOCK_CLOSE(self):
            return self.getToken(ProtoParser.BLOCK_CLOSE, 0)

        def RETURNS_LITERAL(self):
            return self.getToken(ProtoParser.RETURNS_LITERAL, 0)

        def PAREN_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(ProtoParser.PAREN_CLOSE)
            else:
                return self.getToken(ProtoParser.PAREN_CLOSE, i)

        def getRuleIndex(self):
            return ProtoParser.RULE_rpc_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterRpc_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitRpc_def(self)




    def rpc_def(self):

        localctx = ProtoParser.Rpc_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_rpc_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(self.RPC_LITERAL)
            self.state = 257 
            self.rpc_name()
            self.state = 258
            self.match(self.PAREN_OPEN)
            self.state = 259 
            self.req_name()
            self.state = 260
            self.match(self.PAREN_CLOSE)
            self.state = 261
            self.match(self.RETURNS_LITERAL)
            self.state = 262
            self.match(self.PAREN_OPEN)
            self.state = 263 
            self.resp_name()
            self.state = 264
            self.match(self.PAREN_CLOSE)
            self.state = 277
            token = self._input.LA(1)
            if token in [self.BLOCK_OPEN]:
                self.state = 265
                self.match(self.BLOCK_OPEN)
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ProtoParser.OPTION_LITERAL:
                    self.state = 266 
                    self.option_line_def()
                    self.state = 271
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 272
                self.match(self.BLOCK_CLOSE)
                self.state = 274
                _la = self._input.LA(1)
                if _la==ProtoParser.ITEM_TERMINATOR:
                    self.state = 273
                    self.match(self.ITEM_TERMINATOR)



            elif token in [self.ITEM_TERMINATOR]:
                self.state = 276
                self.match(self.ITEM_TERMINATOR)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Rpc_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ProtoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ProtoParser.RULE_rpc_name

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterRpc_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitRpc_name(self)




    def rpc_name(self):

        localctx = ProtoParser.Rpc_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_rpc_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(self.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Req_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_identifier(self):
            return self.getTypedRuleContext(ProtoParser.All_identifierContext,0)


        def getRuleIndex(self):
            return ProtoParser.RULE_req_name

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterReq_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitReq_name(self)




    def req_name(self):

        localctx = ProtoParser.Req_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_req_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281 
            self.all_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Resp_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_identifier(self):
            return self.getTypedRuleContext(ProtoParser.All_identifierContext,0)


        def getRuleIndex(self):
            return ProtoParser.RULE_resp_name

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.enterResp_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ProtoParserListener ):
                listener.exitResp_name(self)




    def resp_name(self):

        localctx = ProtoParser.Resp_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_resp_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283 
            self.all_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




