from rst2.parser.rst2Parser import rst2Parser as rst2ParserBase
from rst2.parser.rst2Semantics import rst2Semantics

class rst2Parser(rst2ParserBase):

    def  parse(self, text, **kwargs):
        return super(rst2Parser, self).parse(text, 
                'document', 
                **kwargs)

def main(filename):
    parser = rst2Parser()
    with open(filename) as f:
        text = f.read()
        semantics = rst2Semantics()
        model = parser.parse(text,
                filename=filename,
                semantics=semantics,
                whitespace='',
                trace=True)
        print model

if __name__ == '__main__':
    main('tests/test.rst')
    

