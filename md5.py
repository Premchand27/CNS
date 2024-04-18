import hashlib

def calculate_md5(text):
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()

# Example usage:
text = "This is a sample text."
md5_digest = calculate_md5(text)
print("MD5 Digest:", md5_digest)
