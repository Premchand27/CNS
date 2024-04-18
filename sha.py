import hashlib

def calculate_sha1(text):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(text.encode('utf-8'))
    return sha1_hash.hexdigest()

# Example usage:
text = input("Enter the text::")
sha1_digest = calculate_sha1(text)
print("SHA-1 Digest:", sha1_digest)
