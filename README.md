
# SiHTML (Simple HTML)

### SiHTML is a custom programming language designed to streamline the process of creating webpages by offering a simplified syntax reminiscent of the popular EMMET plugin syntax found in various code editors. SiHTML aims to empower developers of all experience levels by eliminating the need for manually closing tags and ensuring correct tag order, thus enabling rapid webpage development without sacrificing flexibility or control.


## Key Features:
- **Simplified Syntax:** SiHTML employs a concise and intuitive syntax inspired by the EMMET plugin, allowing developers to write HTML markup quickly and efficiently. With SiHTML, developers can write markup in shorthand without worrying about closing tags or maintaining the correct tag order.

- **Automatic Tag Closure:** One of the standout features of SiHTML is its ability to automatically close HTML tags, sparing developers the need to manually close tags. SiHTML intelligently detects tag nesting and automatically inserts closing tags where necessary, reducing the likelihood of syntax errors and streamlining the coding process.

- **Intuitive Tag Nesting:** SiHTML encourages a clear and logical structure by enforcing intuitive tag nesting. Developers can easily create complex nested structures without the need for meticulous attention to detail, allowing for faster prototyping and development iterations.

- **Familiarity for EMMET Users:** SiHTML's syntax closely mirrors that of the EMMET plugin, making it instantly familiar to developers who are accustomed to using EMMET for code expansion and shorthand notation. This familiarity promotes rapid adoption and minimizes the learning curve for developers transitioning to SiHTML.

- **Accessibility and Versatility:** SiHTML is designed to be accessible to developers of all skill levels, from beginners to seasoned professionals. Its simplicity and flexibility make it well-suited for a wide range of web development projects, from simple landing pages to complex web applications.

- **Variable Declaration:** SiHTML introduces a straightforward mechanism for declaring variables within HTML markup, enhancing the language's flexibility and expressiveness. Variables in SiHTML follow a simple syntax and can be used to dynamically insert values into the generated HTML output. 

**Example Usage:**

Below is an example of SiHTML code compared to traditional HTML:

Traditional HTML:
```html
<!DOCTYPE HTML>
<html>
	<head>
		<title>TITLE GOES HERE</title>
		<link rel="stylesheet" href="stylesheet.css" />
	</head>
	
	<body>
		<h1 id="idName" class="className">Hello World!</h1>
		<h1 style="color:#f00;">Greetings!</h1>
		<h2>Variable string!</h2>
	</body>
</html>
```

SiHTML syntax:
```html
html
	head
		title | TITLE GOES HERE
		stylesheet | stylesheet.css

	@var | string variable_name = "Variable string!"

	body
		h1 #idName .className | Hello World!
		h1 | Greetings ~% style="color:#f00;"
		h2 | $variable_name
```
