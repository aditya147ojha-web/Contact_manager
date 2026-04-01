# Basic test file

from contact_manager import validate_phone, validate_email

print("Phone Test:", validate_phone("1234567890"))
print("Phone Test (invalid):", validate_phone("123"))

print("Email Test:", validate_email("test@example.com"))
print("Email Test (invalid):", validate_email("test@com"))