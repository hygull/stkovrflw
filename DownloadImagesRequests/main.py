import requests
import os
# function [preCodeLatex, codeLines, postCodeLatex] = analyzeCellLines( cellLines )
# %
# % Purpose : This function analyses a cell from the m file to determine the
# % pre-m-code text, the m-code and the post-m-code text.
# %
# % Use (syntax):
# %
# % Input Parameters :
# %   cellLines
# %
# % Return Parameters :
# %   preCodeLatex
# %   codeLines
# %   postCodeLatex
# %
# % Author :  Matther Harker and Paul O'Leary
# % Date :    29. Jan 2013
# % Version : 1.0
# %
# % (c) 2013 Matther Harker and Paul O'Leary
# % url: www.harkeroleary.org
# % email: office@harkeroleary.org
# %
# % History:
# %   Date:           Comment:
# %
# noLines = length( cellLines );
# allLines = 1:noLines;
# %
# % the first non-comment is the start of code
# %
# at = 1;
# line = cellLines{at};
# while (strcmp( line(1) , '%' )) && (at < noLines );
#     at = at + 1;
#     line = cellLines{at};
# end;



# {'Content-Length': '1494', 'X-XSS-Protection': '1; mode=block', 'X-Content-Type-Options': 
# 'nosniff', 'Content-Encoding': 'gzip', 'Accept-Ranges': 'bytes', 'Expires': 
# 'Fri, 15 Jun 2018 11:53:18 GMT', 'Vary': 'Accept-Encoding', 'Server': 'sffe', 
# 'Last-Modified': 'Thu, 08 Dec 2016 01:00:57 GMT', 'Cache-Control': 'public, max-age=691200', 
# 'Date': 'Thu, 07 Jun 2018 11:53:18 GMT', 'Alt-Svc': 'quic=":443"; ma=2592000; v="43,42,41,39,35"', 
# 'Content-Type': 'image/x-icon', 'Age': '422916'
# }



# {'X-XSS-Protection': '1; mode=block; report=https://www.google.com/appserve/security-bugs/log/youtube', 'X-Content-Type-Options': 'nosniff', 'Content-Encoding': 'gzip', 'Transfer-Encoding': 'chunked', 'Set-Cookie': 'VISITOR_INFO1_LIVE=AuCsYDSoRGQ; path=/; domain=.youtube.com; expires=Sun, 09-Dec-2018 09:21:58 GMT; httponly, PREF=f1=40000000; path=/; domain=.youtube.com; expires=Sun, 10-Feb-2019 21:14:58 GMT, YSC=fVwjzcmQHvM; path=/; domain=.youtube.com; httponly, GPS=1; path=/; domain=.youtube.com; expires=Tue, 12-Jun-2018 09:51:58 GMT', 'Expires': 'Tue, 27 Apr 1971 19:44:06 EST', 'Server': 'YouTube Frontend Proxy', 'Strict-Transport-Security': 'max-age=31536000', 'Cache-Control': 'no-cache', 'Date': 'Tue, 12 Jun 2018 09:21:58 GMT', 'P3P': 'CP="This is not a P3P policy! See http://support.google.com/accounts/answer/151657?hl=en for more info."', 'Alt-Svc': 'quic=":443"; ma=2592000; v="43,42,41,39,35"', 'Content-Type': 'text/html; charset=utf-8', 'X-Frame-Options': 'SAMEORIGIN'})
def download_file(url, output_dir):
	response = requests.get(url, allow_redirects=True)
	print("HEADERS: ", response.headers);

	file_name = url.split('/')[-1];
	print("FILE NAME: ", file_name);

	print("CONTENT: ", response.content);

	# Write response to the binary file
	with open(os.path.join(os.path.abspath(output_dir), file_name), "wb") as f:
		f.write(response.content);

if __name__ == "__main__":
	download_file("http://google.com/favicon.ico", ".\\downloads");
	download_file('https://www.youtube.com/watch?v=qgGIqRFvFFk', ".\\videos")


# function [preCodeLatex, codeLines, postCodeLatex] = analyzeCellLines( cellLines )
# %
# % Purpose : This function analyses a cell from the m file to determine the
# % pre-m-code text, the m-code and the post-m-code text.
# %
# % Use (syntax):
# %
# % Input Parameters :
# %   cellLines
# %
# % Return Parameters :
# %   preCodeLatex
# %   codeLines
# %   postCodeLatex
# %
# % Author :  Matther Harker and Paul O'Leary
# % Date :    29. Jan 2013
# % Version : 1.0
# %
# % (c) 2013 Matther Harker and Paul O'Leary
# % url: www.harkeroleary.org
# % email: office@harkeroleary.org
# %
# % History:
# %   Date:           Comment:
# %
# noLines = length( cellLines );
# allLines = 1:noLines;
# %
# % the first non-comment is the start of code
# %
# at = 1;
# line = cellLines{at};
# while (strcmp( line(1) , '%' )) && (at < noLines );
#     at = at + 1;
#     line = cellLines{at};
# end;