# whatsapp-automation

# WhatsApp Automation Script

This Python script automates sending messages and images to WhatsApp contacts using Selenium WebDriver.

## Description

This script performs the following tasks:
1. Opens WhatsApp Web using Firefox WebDriver
2. Reads contact information from an Excel file
3. For each contact:
   - Opens a new chat
   - Searches for the contact number
   - Sends an image if specified
4. Updates the Excel file with the status of each operation

## Prerequisites

- Python 3.x
- Firefox browser
- Geckodriver (Firefox WebDriver)

## Required Python Libraries

- selenium
- pandas
- openpyxl (for Excel file handling)

Install the required libraries using:

```
pip install selenium pandas openpyxl
```

## Usage

1. Prepare an Excel file named `data.xlsx` with columns:
   - Number: WhatsApp contact numbers
   - Location: File path of images to send (optional)
   - status: Will be updated by the script (1 for success)

2. Run the script:

```
python whatsapp_automation.py
```

3. Scan the QR code to log in to WhatsApp Web when prompted
4. Press Enter to start the automation

## Important Notes

- This script automates WhatsApp Web, which may violate WhatsApp's terms of service. Use responsibly and at your own risk.
- Ensure you have permission to message the contacts in your list.
- The script includes waiting times to handle loading delays. Adjust these if necessary.

## Troubleshooting

- If the script fails to find elements, try increasing the wait times.
- Ensure your WhatsApp Web is up to date and functioning correctly.
- Check that file paths for images are correct and accessible.

## Disclaimer

This script is for educational purposes only. The authors are not responsible for any misuse or any violations of WhatsApp's terms of service.
