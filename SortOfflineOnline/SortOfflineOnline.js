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
    { id: 'X82ns', name: 'james', presence: 'online' },
    { id: '8YSHJ',    name: 'mary', presence: 'offline' },
    { id: '7XHSK', name: 'rene', presence: 'online' }
];

/* Pretty printing objs array*/
console.log(JSON.stringify(objs, null, 4))  // Before modification (sorting)
/*
[
    {
        "id": "X82ns",
        "name": "james",
        "presence": "online"
    },
    {
        "id": "8YSHJ",
        "name": "mary",
        "presence": "offline"
    },
    {
        "id": "7XHSK",
        "name": "rene",
        "presence": "online"
    }
]
*/

objs.map((item, index) => { 
	if(item.presence === 'online') { // online, add to front then remove this item from its current position
		objs.splice(0, 0, item) // add at front
	} else { // offline, push at end then remove this item from its current position
		objs.splice(objs.length, 1, item) // push at end	
	}
	objs.splice(index, 1) // remove
})

/* Pretty printing objs array */
console.log(JSON.stringify(objs, null, 4))  // After modification (sorting)
/*
[
    {
        "id": "X82ns",
        "name": "james",
        "presence": "online"
    },
    {
        "id": "7XHSK",
        "name": "rene",
        "presence": "online"
    },
    {
        "id": "8YSHJ",
        "name": "mary",
        "presence": "offline"
    }
]
*/

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