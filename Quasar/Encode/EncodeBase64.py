import base64

texte = "seck_live_q7S36B1e4Ha6E1yBbQJhzqq0U0QgMyBb"
encoded = base64.b64encode(texte.encode('utf-8'))
print(encoded.decode('utf-8'))
