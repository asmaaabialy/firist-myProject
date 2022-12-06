import re
import six
_WHITESPACE_RE=re.compile(r'\s')
def pre_process(input, marker='@@IGNORE@@'):
    if len(input) != 0:
        #if not isinstance(input, six.string_types):
        #bidi_text1=re.fullmatch('\s+\d', input)    
        #input= re.compile('\،\؟\:\؛'.input)
        for sent in input.split('،'):
            print(sent)
            
            for word in sent.split(' '):
                print(word)
            #re.match(r'{}\S+', word)
    else:
        raise ValueError("من فضلك: أدخل النص")
    
#test= ''
        #re.UNICODE|re.MULTILINE

test = "الحمد لله رب العالمين ، الرحمن الرحيم، مالك يوم الدين"

pre_process(test)

