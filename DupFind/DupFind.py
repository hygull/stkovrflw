"""
%%
% This is a simple example file used in conjunction with merge2latex,
% a tool to merge the results from an m-file with a latex documentation
% file.
%
% This file is planned to be used with the merge2lates documentation file
% introduction.tex.
%
% (c) Paul O'Leary and Matthew harker 2013
%
clear all;
close all;
publishFigureFormat;
%%
% \cellName{Cell1}
a=1:10;
b = a.^2;
for k = 1:5
    c(k) = a(k) * b(k)
end;
%%
% \cellName{Cell2}
h = figure;
plot( a,b,'k');
% \caption{Plot of $a$ vs $b$.}
%%
% \cellName{Cell3}
figure
plot(a,b,'h');
xlabel('Hier');
ylabel('there');
% \caption{Plot of $a$ vs $b$ with markers.}
%
"""

def duplicate_finder2(word):
    word1 = word.lower();
    w = list(word1);
    w1 = '';
    for i in range(0, len(word1)):
        if ([v in word1.replace(w[i], '') for v in w[i]]==[True]):
            w1 += ')';    
        else:
            w1 += '(';
    return (w1)

# dup by )
# org by (
# not caps
print duplicate_finder2('dgdggde7gdfsfs')


# def duplicate_finder(word):
#     word1 = word.lower();
#     new_word = ''

#     for ch in word:

# dup by )
# org by (
# not caps
# print duplicate_finder('dgdggde7gdfsfs')


def duplicate_finder3(word):
    word1 = word.lower();
    for c in word1:
        # If more that one occurence of c
        if 1 != word1.count(c):
            # Replace all c with (
            word1 = word1.replace(c, '(')
        # Only one occurence
        else:
            word1 = word1.replace(c, ')')
    return word1

print duplicate_finder3('abaccccsgfsyetgdggdh')

#................................
from collections import Counter

def duplicate_finder4(word):
	word = word.lower()
	for ch, count in Counter(word).items():
		print 'After, ', ch, count
		if count == 1:
			word = word.replace(ch, '(')	
		else:
			word = word.replace(ch, ')')
	return word

print 'abaccccsgfsyetgdggdh'
print duplicate_finder4('abaccccsgfsyetgdggdh'), " :(New1)"
print "...................."

# Code
def duplicate_finder5(word):
	word = word.lower()
	i = 1;

	for ch, count in Counter(word).items():
		print '(', i, ') Original character: \'', ch, '\'with', count - 1, 'more occurence(s)'
		if count == 1:
			word = word.replace(ch, '(')	
		else:
			l = list(word)
			l[word.find(ch)] = '('
			word = ''.join(l) 
			word = word.replace(ch, ')')

		print 1, 'occurence of \'', ch, '\' replaced with \'(\' and remaining ', count - 1, ' occurence(s) with \')\''
		print 'Iteration ', i, ' gives: ', word, '\n'
		i += 1
	return word

# Testing

s = '\nINPUT STRING : abaccccsgfsyetgdggdh' 
s = s + "\nOUTPUT STRING: "
print s + duplicate_finder5('abaccccsgfsyetgdggdh')

# print s + duplicate_finder5('AAABBBCCC34519543absd67das1729')
# AAABBBCCC34519543absd67das1729
# ())())())((((()))))(((()))))()
"""
%%
% This is a simple example file used in conjunction with merge2latex,
% a tool to merge the results from an m-file with a latex documentation
% file.
%
% This file is planned to be used with the merge2lates documentation file
% introduction.tex.
%
% (c) Paul O'Leary and Matthew harker 2013
%
clear all;
close all;
publishFigureFormat;
%%
% \cellName{Cell1}
a=1:10;
b = a.^2;
for k = 1:5
    c(k) = a(k) * b(k)
end;
%%
% \cellName{Cell2}
h = figure;
plot( a,b,'k');
% \caption{Plot of $a$ vs $b$.}
%%
% \cellName{Cell3}
figure
plot(a,b,'h');
xlabel('Hier');
ylabel('there');
% \caption{Plot of $a$ vs $b$ with markers.}
%
"""