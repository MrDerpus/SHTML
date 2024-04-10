'''
Author: MrDerpus


Version: 0.0.2


Dev conditions:
Windows 10 / Fedora 38
Python 3.12.2


Tested Compatible OS's:
Windows 10
Fedora  38


Description: 
Simple HTML (SHTML).


Added:
+ Comments
	> Single line comments that are only used with in the SHTML script can be defined by '/'.
	> Single line comments that are used in both files can be defined by '//'.

+ Commands
	> $close only exists to close div tags.  This will be removed in later versions.

+ Tags
	> h1, h2, h3, p, br & div


What I want to add next:
	+ Cleaner code.
	+ Better comments.
	+ Multiline comments.
	+ More tags.
	+ More commands.
	- Remove $close command.
'''




from rich.traceback import install; install(show_locals = True)
from rich.console   import Console; c = Console()

import click

import sys
import os

from settings import HASH, COMMENTS


# custom function to test if a string is wrapped in a specific char
def isWrapped(string:str, char:str='"'):
	if(string[0] and string[len(string)-1] != char):
		return False
	else:
		return True


@click.group()
def cli():
	pass




@click.command()
@click.option('--input_file',   '-i',  default = HASH.NO_INPUT_FILE)
@click.option('--output_file',  '-o',  default = HASH.NO_OUTPUT_FILE)
@click.option('--minimal_html', '-m',  default = False)
@click.option('--error_debug', '-d0',  default = False)
def build(input_file:str, output_file:str, minimal_html:bool, error_debug:bool):

	# Var declare 
	syntax_sep:str = '|' # the separator character that can be changed using the $sep command.
	converted_line:str = ''
	innerText:str = ''
	tag_args:str = ''
	kill:int = 0
	line_count:str = 1
	keyword:str = ''
	previous_keyword:str = ''
	minimal_file_output:bool = minimal_html
	
	
	if(input_file == HASH.NO_INPUT_FILE):
		c.print(' There was no input .SHTML script defined. \n', style = '#ff0000')
		sys.exit(1)
	elif(output_file == HASH.NO_OUTPUT_FILE):
		c.print(' There was no output .HTML file defined.   \n', style = '#ff0000')
		sys.exit(1)
	
	
	
	
	if(os.path.exists(output_file)):
		os.remove(output_file)

	c.print(f' Building output: {output_file}', style = '#00ffff')
	
	# Read file line by line
	with open(input_file, 'r') as infile:


		for line in infile:
			#print((str(line_count) + syntax_sep))
			# Cleanse line and grab keyword.
			line = line.lstrip().rstrip()
			keyword = line.split('"')[0].lstrip().rstrip().lower()


			# Grab tag innerText
			try:
				innerText = line.split('"')[1]
				innerText = innerText.replace("/n", '<br>')
			except:
				innerText = ''


			# Grab tag arguments 
			try:
				tag_args = line.split(syntax_sep)[1].lstrip().rstrip()
				tag_args = tag_args.replace('colour', 'color')
			except Exception as err:
				if(error_debug == True):
					c.print(f'{line_count} {err}', style = '#ff0000')
				tag_args = ''




			# is line a comment?
			comment = len(line) >= 1
			if(comment and line[0] == COMMENTS.SINGLE_LINE_SCRIPT):   # comment for script itself.
				keyword = HASH.COMMENT
				converted_line = ''
			
			if(comment and line[0:2] == COMMENTS.SINGLE_LINE_HTML): # html comment
				keyword = HASH.COMMENT
				innerText = line[2:].lstrip().rstrip()
				converted_line = f'<!-- {innerText} -->'



			#print(f'{line_count=}\n{keyword=}\n{comment=}\n{innerText=}\n\n')


			#converted_line = f'<{keyword} {tag_args}>{innerText}</>'

			#sys.exit(f' DEBUG: better line formatting test!\n {converted_line}')

			# keywords and commands
			match keyword:
				case 'html':
					converted_line = '<!DOCTYPE html>\n<html>'

				case 'head':
					converted_line = f'<head {tag_args}>'

				case 'stylesheet':
					converted_line = f'<link rel="stylesheet" type="text/css" href="{innerText}" />'
				
				case 'script':
					converted_line = f'<script src="{innerText}" {tag_args}></script>'

				case 'title':
					converted_line = f'<title>{innerText}</title>'

				case 'body':
					converted_line = f'</head>\n<body {tag_args}>'

				case 'br':
					converted_line = '<br>'

				case str(HASH.COMMENT): # ignore line
					pass


				case 'h1':
					converted_line = f'<h1 {tag_args}>{innerText}</h1>'
				
				case 'h2':
					converted_line = f'<h2 {tag_args}>{innerText}</h2>'

				case 'h3':
					converted_line = f'<h3 {tag_args}>{innerText}</h3>'

				case 'p':
					converted_line = f'<p {tag_args}>{innerText}</p>'

				case 'div':
					converted_line = f'<div {tag_args}>'
					previous_keyword = keyword


				case '$close':
					converted_line = f'</{previous_keyword}>'

				case '$exit':
					converted_line = '</body>\n</html>'
					kill = 1
					
				case '$sep':
					converted_line = ''
					syntax_sep = line.split('"')[1]

				case '$min':
					minimal_file_output = True

				case _:
					if(len(keyword) > 0):
						c.print(f' Unknown keyword @ line {line_count}: {keyword}. ', style = '#ffff00')
						converted_line = f'<!-- Unknown keyword: {keyword} -->'
					else:
						converted_line = ''



			#output to output_file
			if(len(converted_line) > 0): # only print output if changes are made.
				with open(output_file, 'a') as outfile:
					outfile.write(converted_line)
					if(minimal_file_output == False):
						outfile.write('\n')

			
			line_count += 1

			if kill >= 1:
				#c.print(' Exiting . . .', style = '#ffff00')
				sys.exit(0)




cli.add_command(build)


if __name__ == '__main__':
	cli()
	#build()
 





# Read file line by line, edit the line and then and output to the output_file
