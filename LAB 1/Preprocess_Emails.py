import re, os

os.chdir(r'C:\Users\bholu\OneDrive\Documents\Python\IR\LAB 1\mails')

def preprocess_email(email):
    header_pattern = r"^(From:|To:|Subject:|Date:|Cc:|Bcc:|X-.*:|Received:|Return-Path:|Message-ID:|Reply-To:|In-Reply-To:|References:|Content-Type:)"
    signature_pattern = r"^(--|__|-{2,}|==|Sent from|Best regards|Sincerely|Yours truly|Cheers|Thanks|Regard|Author:|Unsubscribe |Sent by|wrote:|writes:|On .* wrote:|On .*,.*wrote:|On .* .* .* wrote:)"
    
    lines = email.split('\n')
    
    inside_email_body = False
    
    cleaned_lines = []
    
    for line in lines:
        if re.match(header_pattern, line):
            continue
        elif re.match(signature_pattern, line):
            inside_email_body = False
            continue
        elif inside_email_body:
            cleaned_lines.append(line)
        else:
            inside_email_body = True
            cleaned_lines.append(line)
    
    cleaned_email = '\n'.join(cleaned_lines)
    return cleaned_email


with open('Happy Diwali.txt', 'r') as file:
    email = file.read()

cleaned_email = preprocess_email(email)

print(cleaned_email)
