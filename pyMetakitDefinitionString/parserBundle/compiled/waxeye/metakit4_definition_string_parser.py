# Generated by the Waxeye Parser Generator - version 0.8.1
# www.waxeye.org

from waxeye import Edge, State, FA, WaxeyeParser

class Metakit4_definition_stringParser (WaxeyeParser):
    start = 0
    eof_check = True
    automata = [FA("subFields", [State([Edge(1, 1, False)], False),
            State([Edge(5, 2, False)], False),
            State([], True)], FA.LEFT),
        FA("scalarOrView", [State([Edge(3, 1, False),
                Edge(2, 1, False)], False),
            State([], True)], FA.LEFT),
        FA("view", [State([Edge(7, 1, False)], False),
            State([Edge(9, 2, False)], False),
            State([Edge(4, 3, False)], False),
            State([Edge(10, 4, False)], False),
            State([], True)], FA.LEFT),
        FA("scalar", [State([Edge(7, 1, False)], False),
            State([Edge(11, 2, False)], False),
            State([Edge(18, 3, False)], False),
            State([], True)], FA.LEFT),
        FA("body", [State([Edge(0, 1, False),
                Edge(13, 1, False)], False),
            State([], True)], FA.LEFT),
        FA("rest_subFields_with_delF", [State([Edge(6, 0, False)], True)], FA.LEFT),
        FA("rest_subField_with_delF", [State([Edge(12, 1, False)], False),
            State([Edge(1, 2, False)], False),
            State([], True)], FA.LEFT),
        FA("word", [State([Edge(8, 1, False)], False),
            State([Edge(8, 1, False)], True)], FA.LEFT),
        FA("wordPiece", [State([Edge(18, 1, False),
                Edge(14, 2, False)], False),
            State([], True),
            State([Edge(14, 2, False)], True)], FA.LEFT),
        FA("subFieldsStart", [State([Edge("[", 1, False)], False),
            State([], True)], FA.LEFT),
        FA("subFieldsEnd", [State([Edge("]", 1, False)], False),
            State([], True)], FA.LEFT),
        FA("colon", [State([Edge(":", 1, False)], False),
            State([], True)], FA.LEFT),
        FA("optionsSeparator", [State([Edge(",", 1, False)], False),
            State([], True)], FA.LEFT),
        FA("indirectMarker", [State([Edge("^", 1, False)], False),
            State([], True)], FA.LEFT),
        FA("otherWordChars", [State([Edge([(48, 57), "A", "C", "E", (71, 72), (74, 76), (78, 82), (84, 90), "_", "a", "c", "e", (103, 104), (106, 108), (110, 114), (116, 122)], 1, False)], False),
            State([], True)], FA.LEFT),
        FA("otherWordCharsOther", [State([Edge([(48, 57), "_"], 1, False)], False),
            State([], True)], FA.LEFT),
        FA("otherWordCharsUpper", [State([Edge(["A", "C", "E", (71, 72), (74, 76), (78, 82), (84, 90)], 1, False)], False),
            State([], True)], FA.LEFT),
        FA("otherWordCharsLower", [State([Edge(["a", "c", "e", (103, 104), (106, 108), (110, 114), (116, 122)], 1, False)], False),
            State([], True)], FA.LEFT),
        FA("typeSpecifier", [State([Edge(["B", "D", "F", "I", "M", "S", "b", "d", "f", "i", "m", "s"], 1, False)], False),
            State([], True)], FA.LEFT),
        FA("typeSpecifierUpper", [State([Edge(["B", "D", "F", "I", "M", "S"], 1, False)], False),
            State([], True)], FA.LEFT),
        FA("typeSpecifierLower", [State([Edge(["b", "d", "f", "i", "m", "s"], 1, False)], False),
            State([], True)], FA.LEFT)]

    def __init__(self):
        WaxeyeParser.__init__(self, Metakit4_definition_stringParser.start, Metakit4_definition_stringParser.eof_check, Metakit4_definition_stringParser.automata)

