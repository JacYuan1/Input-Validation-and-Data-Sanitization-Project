# Input Validation and Data Sanitization Project

## Table of Contents

- [Introduction](#Introduction)
- [Inputs Requirements](#Inputs-Requirements)
- [Get Started](#Get-Started)
- [Example Inputs](#Example-Inputs)
- [Example Outputs](#Example-Outputs)
- [References](#References)

<h2 id="#Introduction">Introduction</h2>

The objective of this project is to check and remove unwanted input ensuring that data conforms to security-related requirements.

<h2 id="#Get-Started">Get Started</h2>

Here are some steps to get started:

1. Create a text or csv file anywhere on your pc and name it
2. In the file open() function (Line 4) provide the location of that text file you've created in step 1
3. Paste in samples (you can use the sample inputs provided [here](#Example-Inputs)
4. Run the code!

<h2 id="#Inputs-Requirements">Inputs Requirements</h2>

Here are all the valid input requirements:

1. **Student:** 9 digits. acceptable formats: 000000000, 000 000 000
2. **Password:** a-z, A-Z, 0-9, ascii printable special characters, minimum 12 characters
3. **Username:** a-z, A-Z, 0-9, minimum 3 characters, maximum 20 characters
4. **Email:** username@domain.TLD, username, domain and TLD will conform to the rules above for a “username” field. There will only be one TLD (i.e. no multiples like domain.co.uk)
5. **Previous:** Confirm that this data field is identical to the previous line’s data field (excluding whitespace)
6. **Phone:** A North American phone number. Possible formats: 1234567890, 123.456.7890, 123-456-7890, (123) 456-7890
7. **Postal:** A Canadian postal code. Possible formats: A0A0A0, A0A 0A0
8. **Address:** A string field containing a-z, A-Z, 0-9, periods and dashes.
9. **Binary:** A single binary string, must contain only 1s and 0s with no breaks between digits
10. **Biography:** A generic string field. Report “no” only if the field contains any html tags.

<h2 id="#Example-Intputs">Example Inputs</h2>

Here are some example inputs:

student,999999999

password,abcd1234

username,user123

email,testuser@testdomain.com

previous,testuse@testdomain.com 

phone,123-456-7890

postal,M86 72Z

address,123 street blvd.

binary,11110000

bio,  hello world

student,9999 9999

student,   111111111

password,123456abcdef!!

username,stevedave

previous,stevedave

phone,((416-111-1234

postal,H1R3T7

bio,Hello<script>World</script>

<h2 id="#Example-Outputs">Example Outputs</h2>

The output will be a simple “yes” or “no” string. Here is what the example output would look like (based on the provided input in the above section):

yes

no

yes

yes

no

yes

no

yes

yes

yes

no

yes

yes

yes

yes

no

yes

no

## References

[Reference Link](https://github.com/JacYuan1/Input-Validation-and-Data-Sanitization-Project/blob/536a1bd0f0cf73fc16dda56914658a45de1e837b/Reference.pdf)
