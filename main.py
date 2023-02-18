import sys

try:
    if sys.argv[1][sys.argv[1].index('.')+1:] != 'hanpy':
        raise RuntimeError('이 파일이 아니야!')

    with open(sys.argv[1], encoding='UTF-8') as f:
        src = '\n'.join(f.readlines())

    toreplace = {'거짓':'False', 'ㅇ벗다':'None', '참':'True', '그리고':'and', '와 같은':'as', '옹호하다':'assert',
                '비동기':'async', '기다려':'await', '부수다':'break', '안돼 돌아가':'continue', '함수':'def', '없애다':'del',
                '아니고 만약':'elif', '아니면':'else', '그러나 그거시 실제로 이러나씁니다':'except', '결국':'finally', '위하여':'for',
                '세계적인':'global', '만약':'if', '있다':'in', '똑같다':'is', '무명 함수':'lambda', '지역적이지 않은':'nonlocal',
                '아니다':'not', '또는':'or', '알빠임?':'pass', '기르다':'raise', '유턴':'return', '어디 해봐':'try', '하는 동안':'while',
                '양보하다':'yield'}

    toreplace2 = {'적용': 'isalpha', '정리': 'PendingDeprecationWarning', '셋째': '__str__', '소속': 'getattr', '금년': 'ModuleNotFoundError',
                '둘째': 'UnboundLocalError', '연합': 'ImportWarning', '깜짝': '__getstate__', '마누라': '__iter__', '약속하다': 'find',
                '침묵': 'encode', '실로': 'endswith', '아무튼': 'FileExistsError', '원고': 'delattr', '두렵다': 'list', '담임': 'KeyboardInterrupt',
                '보관하다': 'abs', '요즈음': 'expandtabs', '꼭': 'SyntaxError', '발견': 'zfill', '닮다': '__package__', '제작': 'format',
                '후기': 'ArithmeticError', '내지': 'ExceptionGroup', '웃기다': 'IndexError', '물기': 'Exception', '덥다': 'min',
                '대충': 'setattr', '잠깐': 'aiter', '전달하다': '__rmod__', '전해지다': 'format_map',
                '이상': 'float', '완전': 'AssertionError', '한복': '__build_class__', '힘쓰다': '__getitem__',
                '다치다': 'join', '년도': 'ascii', '그쪽': 'ConnectionResetError', '간부': 'EOFError', '향': '__init__',
                '찌르다': 'ResourceWarning', '향상': 'MemoryError', '만지다': 'RecursionError', '제법': 'ConnectionRefusedError',
                '심정': 'bool', '진단': 'any', '정해지다': 'upper', '자랑하다': 'compile', '주머니': 'dict', '안전하다': 'callable',
                '검은색': 'slice', '잃어버리다': '__class__', '목사': 'OSError', '왠지': 'staticmethod', '완성': 'tuple', '군사': 'isprintable',
                '카드': 'swapcase', '도구': 'bin', '용돈': 'issubclass', '기타': 'ord', '낚시': 'ConnectionError', '디자인': 'UserWarning',
                '예방': 'open', '조심하다': 'RuntimeWarning', '물결': 'NotImplemented', '요청하다': 'UnicodeTranslateError', '성립되다': 'property',
                '배우': 'DeprecationWarning', '사귀다': 'help', '고생하다': '__contains__', '그나마': 'hex', '후배': 'StopIteration', '풍경': 'SystemError',
                '두드리다': 'index', '비롯되다': 'copyright', '희곡': 'map', '교류': 'classmethod', '전부': 'id', '동일하다': '__setattr__',
                '지식인': 'NameError', '비극': 'IOError', '증상': 'BaseException', '어색하다': 'TabError', '유난히': 'maketrans', '논의하다': 'hash',
                '바로잡다': 'IndentationError', '우리말': 'LookupError', '우승': 'WindowsError', '당황하다': 'memoryview', '멀어지다': '__reduce_ex__',
                '만남': 'removeprefix', '흥미': '__format__', '지출': 'lstrip', '귀하다': 'enumerate', '헤아리다': 'splitlines', '더럽다': '__len__',
                '지적되다': 'TimeoutError', '이불': 'UnicodeDecodeError', '세워지다': 'isdecimal', '불러일으키다': 'center', '말리다': '__dir__',
                '코너': 'Ellipsis', '라면': 'PermissionError', '쫓다': 'replace', '야채': 'isinstance', '버티다': '__subclasshook__', '그다음': 'TypeError',
                '제거하다': 'casefold', '보고': 'ZeroDivisionError', '범인': 'ConnectionAbortedError', '바위': 'ChildProcessError', '전자': 'BlockingIOError',
                '쥐': 'strip', '의무': 'sorted', '화학': 'rindex', '출발': 'SystemExit', '돌아보다': '__name__', '상': 'super', '창밖': '__repr__',
                '킬로그램': '__mul__', '실패하다': 'NotADirectoryError', '무려': '__import__', '축제': 'vars', '머릿속': 'isspace',
                '자동': 'zip', '문서': 'split', '경계': '__ne__', '정식': 'IsADirectoryError', '하긴': 'removesuffix', '뒤지다': 'credits',
                '당연히': '__le__', '비난': 'isnumeric', '최선': 'partition', '비닐': 'islower', '쏘다': 'InterruptedError', '대신하다': '__doc__', 
                '호텔': '__add__', '정치적': '__sizeof__', '귀국하다': 'title', '환경오염': 'KeyError', '말기': 'eval', '일치하다': 'complex',
                '전개': 'ReferenceError', '주의': 'ValueError', '박수': 'UnicodeError', '음료': '__gt__', '함부로': 'isdigit', '크다': '__rmul__',
                '교과서': 'chr', '생산되다': 'istitle', '다방': 'int', '자율': '__delattr__', '깔다': 'Warning', '최대한': 'divmod', 
                '세계관': 'EnvironmentError', '극장': 'isalnum', '나침반': '__debug__', '궁극적': 'input',
                '생산력': 'SyntaxWarning', '창조': 'bytearray', '신고': '__reduce__', '생활하다': 'RuntimeError', '절반': '__lt__',
                '웬': 'rfind', '구경': '__getnewargs__', '차': 'exit', '석유': 'ImportError', '점심': 'quit', '그토록': 'FloatingPointError',
                '미처': 'object', '마음대로': 'breakpoint', '떨어뜨리다': 'StopAsyncIteration', '변호사': 'bytes', '국어': 'EncodingWarning',
                '본성': '__eq__', '많아지다': 'dir', '바늘': 'license', '자연환경': 'FileNotFoundError', '출연하다': 'UnicodeEncodeError',
                '개선하다': 'BytesWarning', '근무하다': 'all', '설탕': 'exec', '바깥': 'sum', '굳어지다': 'range', '학기': 'translate',
                '들': '__getattribute__', '짐작하다': 'pow', '추다': 'rjust', '털다': '__mod__', '자 존심': '__ge__', '무덤': 'locals',
                '적당히': 'round', '밀가루': 'ljust', '정비': 'frozenset', '수십': '__init_subclass__', '접촉': 'isascii', '거짓말': 'GeneratorExit',
                '바치다': 'isidentifier', '익다': 'BufferError', '해석': 'rstrip', '외교': 'UnicodeWarning', '등장': '__spec__', '증명하다': 'oct',
                '모래': 'len', '안경': 'globals', '나란히': 'set', '답하다': 'iter', '해석 하다': 'BrokenPipeError', '망하다': 'FutureWarning',
                '겉': 'capitalize', '하천': 'ProcessLookupError', '종업원': 'reversed', '검토': 'type', '부처': '__hash__', '보고서': 'str',
                '햇빛': 'lower', '먼지': 'filter', '공개하다': 'rpartition', '각기': 'max', '학부모': 'NotImplementedError', '의자': 'isupper',
                '골목': 'next', '위반': 'OverflowError', '적용하다': 'hasattr', '내내': '__loader__', '삶다': 'print', '중요성': '__new__',
                '안타깝다': 'AttributeError', '특정하다': 'rsplit', '현지': 'anext', '깨지다': 'repr', '초원': 'count', '미디어': 'BaseExceptionGroup'}

    thatsnono = ['import', 'from', 'match']

    def main(src:str):
        for v in thatsnono:
            src = src.replace(v, '')
        for k, v in toreplace.items():
            src = src.replace(k, v)
        for k, v in toreplace2.items():
            src = src.replace(k, v)
        return src

    exec(main(src))
    input()
except Exception as e:
    print(e)
    input()