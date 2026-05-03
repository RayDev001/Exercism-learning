def response(hey_bob):
    response = "Whatever."
    if hey_bob.strip().endswith('?'):
        response = "Sure."

    if hey_bob.isupper():
        response = "Whoa, chill out!"

    if hey_bob.isupper() and hey_bob.endswith('?'):
        response = "Calm down, I know what I'm doing!"

    if hey_bob.strip() == '':
        response = "Fine. Be that way!"

    return response