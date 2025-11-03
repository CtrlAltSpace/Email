# Get user input for email details
sender = input("Enter your email: ")
recipient = input("Enter the recipient's email: ")

# Check if sender and recipient are the same
if sender == recipient:
    print("Error: Sender and recipient email addresses cannot be the same.")
else:
    subject = input("Enter the subject: ")
    body = input("Enter the body: ")

    # Create the email content
    email_message = f"From: {sender}\nTo: {recipient}\nSubject: {subject}\n\n{body}"

    # Print the email content
    print("----------------------")
    print(email_message)
