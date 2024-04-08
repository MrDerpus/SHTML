'''
Author: MrDerpus


Version: 0.0.1


Dev conditions:
Windows 10 / Fedora 38
Python 3.12.2


Tested Compatible OS's:
Windows 10
Fedora  38


Description: 
Simple HTML (SHTML)
'''




from rich.traceback import install; install(show_locals = True) # type: ignore
from rich.console   import Console; c = Console() # type: ignore

import click # type: ignore

import sys
import os

from settings import HASH


# custom function to test if a string is wrapped in a specific char
def isWrapped(string:str, char:str='"'):
	if(string[0] and string[len(string)-1] != char):
		return False
	else:
		return True


@click.group()
def cli():
	pass



# python3 main.py convert_to_html --input_file 'script.txt' --output_file 'index.html'
# python3 main.py build --input_file 'script.txt' --output_file 'index.html'
# shtml build --input_file 'script.txt' --output_file 'index.html'
# shtml build -i 'script.txt' -o 'index.html'

@click.command()
@click.option('--input_file',  '-i',  default = HASH.NO_INPUT_FILE)
@click.option('--output_file', '-o',  default = HASH.NO_OUTPUT_FILE)
@click.option('--error_debug', '-d0', default = False)
def build(input_file:str, output_file:str, error_debug:bool):

	# the separator character that can be changed using the $sep command.
	syntax_sep = '|'
	innerText = ''
	tag_args = ''
	kill = 0
	line_count = 1
	
	
	if(input_file == HASH.NO_INPUT_FILE):
		c.print(' There was no input SHTML script defined. \n', style = '#ff0000')
		sys.exit(0)
	elif(output_file == HASH.NO_OUTPUT_FILE):
		c.print(' There was no output HTML file defined.   \n', style = '#ff0000')
		sys.exit(0)
	
	
	
	
	if(os.path.exists(output_file)):
		os.remove(output_file)

	c.print(f' Building output: {output_file}', style = '#ffff00')
	
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

				case str(HASH.IGNORE): # ignore line
					pass

				case 'h1':
					converted_line = f'<h1 {tag_args}>{innerText}</h1>'

				case '$exit':
					converted_line = '</body>\n</html>'
					kill = 1
					
				case '$sep':
					converted_line = ''
					syntax_sep = line.split('"')[1]

				case _:
					#print(line.split())
					converted_line = ''



			#output to output_file
			with open(output_file, 'a') as outfile:
				outfile.write(converted_line + '\n')

			
			line_count += 1

			if kill >= 1:
				#c.print(' Exiting . . .', style = '#ffff00')
				sys.exit()




cli.add_command(build)


if __name__ == '__main__':
	cli()
	#build()
 





# Read file line by line, edit the line and then and output to the output_file
