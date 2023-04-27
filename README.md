# Input Validation and Data Sanitization Project

## Table of Contents

- [Introduction](#Introduction)
- [Inputs Requirements](#Inputs-Requirements)
- [Example Outputs](#Example-Outputs)
- [References](#References)

<h2 id="#Introduction">Introduction</h2>

The objective of this project is to check and remove unwanted input ensuring that data conforms to security-related requirements.

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

<h2 id="#Example-Outputs">Example Outputs</h2>

Here is what the example output would look like:

## References
