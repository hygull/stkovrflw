/*
unction [matchedSymbols, symbolsT] = matchSymbols( symbolsM, symbolsT )
%
% Purpose : This function matches the symbols from th .tex and m-files and
% collates the necessary line numbers form the files
%
% Use (syntax):
%   [matchedSymbols, symbolsT] = matchSymbols( symbolsM, symbolsT )
%
% Input Parameters :
%   symbolsM, symbolsT: the m-file and .tex file symbol tables
%
% Return Parameters :
%   matchedSymbols: symbol table with matched symbols and th enecessary
%   file-line information
%
% Description and algorithms:
%
% References : 
%
% Author :  Matther Harker and Paul O'Leary
% Date :    29. Jan 2013
% Version : 1.0
%
% (c) 2013 Matther Harker and Paul O'Leary
% url: www.harkeroleary.org
% email: office@harkeroleary.org
%
% History:
%   Date:           Comment:
%
fullFilePath = mfilename('fullpath')
path = getFileName(fullFilePath)
fprintf('%s: %s...\n', path{:}, 'Just enetered matchSymbols()');
disp(symbolsM)
disp(symbolsT)

noTexSymbols = length( symbolsT );
%
matchedSymbols = [];
*/
var objs = [ 
    { id: 'X82ns', name: 'james', presence: 'online'     },
    { id: '8YSHJ',    name: 'mary', presence: 'offline'   },
    { id: '7XHSK', name: 'rene', presence: 'online' }
];

/*
unction [matchedSymbols, symbolsT] = matchSymbols( symbolsM, symbolsT )
%
% Purpose : This function matches the symbols from th .tex and m-files and
% collates the necessary line numbers form the files
%
% Use (syntax):
%   [matchedSymbols, symbolsT] = matchSymbols( symbolsM, symbolsT )
%
% Input Parameters :
%   symbolsM, symbolsT: the m-file and .tex file symbol tables
%
% Return Parameters :
%   matchedSymbols: symbol table with matched symbols and th enecessary
%   file-line information
%
% Description and algorithms:
%
% References : 
%
% Author :  Matther Harker and Paul O'Leary
% Date :    29. Jan 2013
% Version : 1.0
%
% (c) 2013 Matther Harker and Paul O'Leary
% url: www.harkeroleary.org
% email: office@harkeroleary.org
%
% History:
%   Date:           Comment:
%
fullFilePath = mfilename('fullpath')
path = getFileName(fullFilePath)
fprintf('%s: %s...\n', path{:}, 'Just enetered matchSymbols()');
disp(symbolsM)
disp(symbolsT)

noTexSymbols = length( symbolsT );
%
matchedSymbols = [];
*/