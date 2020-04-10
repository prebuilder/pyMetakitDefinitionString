# Generated from grammar.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,54,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,3,5,39,8,5,1,6,1,6,1,7,1,7,
        1,8,1,8,1,9,1,9,3,9,49,8,9,1,10,1,10,1,11,1,11,0,0,12,1,1,3,2,5,
        3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,1,0,5,2,0,48,57,
        95,95,7,0,65,65,67,67,69,69,71,72,74,76,78,82,84,90,7,0,97,97,99,
        99,101,101,103,104,106,108,110,114,116,122,6,0,66,66,68,68,70,70,
        73,73,77,77,83,83,6,0,98,98,100,100,102,102,105,105,109,109,115,
        115,56,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,27,1,0,0,0,5,29,1,0,0,
        0,7,31,1,0,0,0,9,33,1,0,0,0,11,38,1,0,0,0,13,40,1,0,0,0,15,42,1,
        0,0,0,17,44,1,0,0,0,19,48,1,0,0,0,21,50,1,0,0,0,23,52,1,0,0,0,25,
        26,5,91,0,0,26,2,1,0,0,0,27,28,5,93,0,0,28,4,1,0,0,0,29,30,5,58,
        0,0,30,6,1,0,0,0,31,32,5,44,0,0,32,8,1,0,0,0,33,34,5,94,0,0,34,10,
        1,0,0,0,35,39,3,13,6,0,36,39,3,15,7,0,37,39,3,17,8,0,38,35,1,0,0,
        0,38,36,1,0,0,0,38,37,1,0,0,0,39,12,1,0,0,0,40,41,7,0,0,0,41,14,
        1,0,0,0,42,43,7,1,0,0,43,16,1,0,0,0,44,45,7,2,0,0,45,18,1,0,0,0,
        46,49,3,21,10,0,47,49,3,23,11,0,48,46,1,0,0,0,48,47,1,0,0,0,49,20,
        1,0,0,0,50,51,7,3,0,0,51,22,1,0,0,0,52,53,7,4,0,0,53,24,1,0,0,0,
        3,0,38,48,0
    ]

class metakit4_definition_stringLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SubFieldsStart = 1
    SubFieldsEnd = 2
    Colon = 3
    OptionsSeparator = 4
    IndirectMarker = 5
    OtherWordChars = 6
    OtherWordCharsOther = 7
    OtherWordCharsUpper = 8
    OtherWordCharsLower = 9
    TypeSpecifier = 10
    TypeSpecifierUpper = 11
    TypeSpecifierLower = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "':'", "','", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "SubFieldsStart", "SubFieldsEnd", "Colon", "OptionsSeparator", 
            "IndirectMarker", "OtherWordChars", "OtherWordCharsOther", "OtherWordCharsUpper", 
            "OtherWordCharsLower", "TypeSpecifier", "TypeSpecifierUpper", 
            "TypeSpecifierLower" ]

    ruleNames = [ "SubFieldsStart", "SubFieldsEnd", "Colon", "OptionsSeparator", 
                  "IndirectMarker", "OtherWordChars", "OtherWordCharsOther", 
                  "OtherWordCharsUpper", "OtherWordCharsLower", "TypeSpecifier", 
                  "TypeSpecifierUpper", "TypeSpecifierLower" ]

    grammarFileName = "grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


