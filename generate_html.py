# Define the HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>My HTML Page</title>
</head>
<body>
    <h1>Hello World</h1>
    <div style="text-align: center; color: gold;">
        <p>Let's Get Started!!</p>
    </div>
</body>
</html>
"""

# Write the HTML content to a file
with open("example.html", "w") as html_file:
    html_file.write(html_content)

print("HTML file 'example.html' has been generated.")
