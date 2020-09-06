# json-to-csv-flask

## Overview
This is a simple Flask web application that allows the user to perform the following conversions in their browser:
- JSON string -> CSV string
- CSV string -> JSON string

For a video overview of this web application, please see the following video on YouTube: https://youtu.be/QsJi5qOSZS4.

## Usage
After navigating to the web app, the user is presented with two text boxes, two drop-down fields, and a "Convert" button. In order to convert a string, please follow the below steps:
1. Paste the "source" string into the text box on the left.
2. Select the correct "source" format in the drop down below (either JSON or CSV).
3. The "target" format should auto-populate.
4. Click the "Convert" button. The string will be converted into the target string format, and the output will be shown in the text box on the right.

## Technical details
This project utilizes the following technologies:
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [jQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/)
- Python
- JavaScript
- HTML and CSS

When the user clicks the "Convert" button, the following flow of events occurs:
1. "Source" string value is encoded using base 64 encoding.
2. The base 64 encoded "source" string is sent to the Flask web server using a jQuery AJAX POST request.
3. The Flask web server decodes the base 64 encoded string.
4. The Flask web server converts the string from "source" format into the specified "target" format.
5. The Flask web server encodes the output string once again using base 64 encoding.
6. The Flask web server serializes the response string into a JSON object.
7. the Flask web server returns the JSON response object to the browser.
8. The JSON response object is deserialized using JavaScript in the browser.
9. The base 64 encoded output string is decoded.
10. The output string is displayed in the "target" text box.
