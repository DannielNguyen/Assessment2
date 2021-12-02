import re
# java language
from enum import Enum

class Classifier(Enum):
    BLOCK_COMMENT = "(/\\*.*?\\*/).*"
    LINE_COMMENT = "(//(.*?)[\r$]?\n).*"
    SPACE = "( ).*"
    OPEN_PAREN = "(\\().*"
    CLOSE_PAREN = "(\\)).*"
    SEMICOLON = "(;).*"
    COMMA = "(,).*"
    OPEN_CURLY_BRACE = "(\\{).*"
    CLOSE_CURLY_BRACE = "(\\}).*"
    OPEN_BRACE = "(\\[).*"
    CLOSE_BRACE = "(\\]).*"
    DOUBLE_CONSTANT = "\\b(\\d{1,9}\\.\\d{1,32})\\b.*"
    INT_CONSTANT = "\\b(\\d{1,9})\\b.*"
    VOID = "\\b(void)\\b.*"
    INT = "\\b(int)\\b.*"
    DOUBLE = "\\b(int|double)\\b.*"
    TAB = "(\\t).*"
    NEW_LINE = "(\\n).*"
    PUBLIC = "\\b(public)\\b.*"
    PRIVATE = "\\b(private)\\b.*"
    FALSE = "\\b(false)\\b.*"
    TRUE = "\\b(true)\\b.*"
    NULL = "\\b(null)\\b.*"
    RETURN = "\\b(return)\\b.*"
    NEW = "\\b(new)\\b.*"
    CLASS = "\\b(class)\\b.*"
    IF = "\\b(if)\\b.*"
    ELSE = "\\b(else)\\b.*"
    WHILE = "\\b(while)\\b.*"
    STATIC = "\\b(static)\\b.*"
    STRING = "\\b(String)\\b.*"
    CHAR = "\\b(char)\\b.*"
    FINAL = "\\b(final)\\b.*"
    ABSTRACT = "\\b(abstract)\\b.*"
    CONTINUE = "\\b(continue)\\b.*"
    FOR = "\\b(for)\\b.*"
    SWITCH = "\\b(switch)\\b.*"
    ASSERT = "\\b(assert)\\b.*"
    DO = "\\b(do)\\b.*"
    BREAK = "\\b(break)\\b.*"
    IMPLEMENTS = "\\b(implements)\\b.*"
    CASE = "\\b(case)\\b.*"
    CATCH = "\\b(catch)\\b.*"
    EXTENDS = "\\b(extends)\\b.*"
    TRY = "\\b(try)\\b.*"
    INTERFACE = "\\b(INTERFACE)\\b.*"
    LONG = "\\b(LONG)\\b.*"
    CONST = "\\b(const)\\b.*"
    FLOAT = "\\b(float)\\b.*"
    NATIVE = "\\b(native)\\b.*"
    super = "\\b(super)\\b.*"
    POINT = "(\\.).*"
    PLUS = "(\\+{1}).*"
    MINUS = "(\\-{1}).*"
    MULTIPLY = "(\\*).*"
    DIVIDE = "(/).*"
    EQUAL = "(==).*"
    ASSIGNMENT = "(=).*"
    NOT_EQUAL = "(\\!=).*"
    CLOSE_CARET = "(>).*"
    OPEN_CARET = "(<).*"
    IDENTIFIER = "\\b([a-zA-Z]{1}[0-9a-zA-Z_]{0,31})\\b.*"
    STRING_LITERAL = '\"(\\.|[^\\"])*\"'
    CHARACTER_LITERAL = r"\'(\\.|[^\\'])*\'"
#switch
# foreach
# for
# while
# do-while
# block
# if
# assignment
# return
class LexicalError(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class Token:

    def __init__(self, begin, end, value, type):
        self.begin = begin
        self.end = end
        self.value = value
        self.type = type

    def __str__(self):
        return self.type.name + '\t' + self.value

def lex_source(file):
    with open(file, 'r') as sample:
        return lex_source_string(sample.read())



def lex_source_string(string):
    
    tokens = list()
    index = 0
    while index < len(string):
        token = token_seperator(string, index)
        if token is None:
            break
        index = token.end
        tokens.append(token)
    if index != len(string):
        raise LexicalError('error at position ' + str(index))
    return tokens


def token_seperator(string, begin):
    
    for type in Classifier:
        pattern = r'.{' + str(begin) + '}' + type.value
        match = re.match(pattern, string, re.DOTALL)
        if match:
            end = match.end(1)
            if type == Classifier.STRING_LITERAL or type == Classifier.CHARACTER_LITERAL:
                end += 1
            return Token(begin, end, string[begin:end], type)
    return None

#main 
tokens = lex_source('example.txt')
def paren_check():
    paren_counter = 0
    for token in tokens:
            if token.type is Classifier.OPEN_PAREN:
                 paren_counter +=1


            if token.type is Classifier.CLOSE_PAREN:
                paren_counter = paren_counter - 1


    if paren_counter != 0:
        print('PAREN SYNTAX ERROR')
                
def all_correct():
    for token in tokens:
        if token.type not in [Classifier.SPACE, Classifier.NEW_LINE]:
            print(token)

def print_error():
    print('Syntax Error')

def switch_check():
    for token in tokens:
            if token.type is Classifier.SWITCH:
                print('Switch statement found')
                return True
    
def case_check():
    for token in tokens:
            if token.type is Classifier.CASE:
                print('case statement found')
                return True

def if_check():
    for token in tokens:
        if token.type is Classifier.IF:
             print('if statement found')  
    
def while_check():
    for token in tokens:
        print(token)
        if token.type is Classifier.WHILE:
             print('While statement found')
             
             return True    
     
def do_while():
    for token in tokens:
        if token.type is Classifier.DO:
             print('Do statement found')
                 
             return True   
    

    for token in tokens:
        if token.type not in [Classifier.SPACE, Classifier.NEW_LINE]:
            print(token)
def block_check():
    block_counter = 0
    for token in tokens:
        if token.type not in [Classifier.SPACE, Classifier.NEW_LINE]:

        
            if token.type is Classifier.OPEN_CURLY_BRACE:
                 block_counter +=1


            if token.type is Classifier.CLOSE_CURLY_BRACE:
                block_counter = block_counter -1


    if block_counter != 0:
        print('BLOCK SYNTAX ERROR')

all_correct()