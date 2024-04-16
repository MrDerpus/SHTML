
class COMMENTS:
	SINGLE_LINE_SCRIPT:str = '/'
	SINGLE_LINE_HTML:str   = '//'




class SYNTAX: # syntax settings that users can change.
	SEPARATOR:str = '|'
	CLOSE:str = '~;' # Squiggle

	CLASS:str = '.'
	ID:str = '#'



class HASH: # Hashes, because it's very unlikely for a person to type in a full hash.
	NO_INPUT_FILE:str  = '509bb0bcae3e762ece6891ce4d34a841'
	NO_OUTPUT_FILE:str = 'f4d6cc0dc0dd99d177b8253bf1e43c6f'
	NO_USER_INPUT:str  = '75e2c40ffa5b937511e96840b56a4a7a'
	NON_EXISTENT_FILE:str = '948861a776811a7fd34ae2e73ee2adee'

	IGNORE:str  = 'a2e843feab94ef623fea888f07c28696'

	COMMENT:str = 'f2cd320b55767434dd48d81b165ea956'
	MULTI_LINE_COMMENT_START:str = '741e8dedeff3fda6a9183224ad3eab44'
	MULTI_LINE_COMMENT_END:str   = '11672c1086f8b351a09d6bbcc8915e43'



class VALID: # Valid HTML tags and language commands.
	# HTML tags -----------
	# HTML tags that are self closing. Example: <link rel="stylesheet" type="text/css" href="styles.css" /> # everything after 'keygen' is not supported in HTML5.
	HTML_SELF_CLOSING:list = ['area','base','br','col','embed','hr','img','input','meta','param','source','track','wbr','keygen','command','menuitem','frame']

	# HTML tags that are not self closing, but need intervention. Example: <div id="idName">
	HTML_NON_INTERVENTION:list = ['div','span','ul', 'head']

	# HTML tags that are not self closing, but DON'T need intervention. Example: <h1 id="idName">Hello World!</h1>
	HTML_INTERVENTION:list = ['title', 'h1','h2','h3','h4','h5','h6','p','b','s','u', 'a']

	# Blocked HTML tags.
	HTML_BLOCKED:list = ['style']

	#HTML_CUSTOM:dict = {'style':'<link rel="stylesheet" type="text/css" href="{innerText}" />', }
	# Tags that are customised in the main.py file
	HTML_CUSTOM:list = ['stylesheet', 'script', 'html', 'body']

	# All valid HTML tags. that are specified above.
	HTML:list = [i for i in HTML_SELF_CLOSING + HTML_NON_INTERVENTION + HTML_INTERVENTION + HTML_CUSTOM]
	# ---------------------
 


	# Valid language commands -----------
	COMMANDS:list = ['$sep', '$exit', '$html', '$end', '$close']
	# -----------------------------------
	
	VALID:list = [i for i in HTML + COMMANDS]