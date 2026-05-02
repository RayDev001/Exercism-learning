def response(hey_bob):
    bobs_response = "Whatever."
    if hey_bob.strip().endswith("?"):
        bobs_response = "Sure."

    if hey_bob.isupper():
        bobs_response = "Whoa, chill out!"

    if hey_bob.isupper() and hey_bob.endswith("?"):
        bobs_response = "Calm down, I know what I'm doing!"

    if hey_bob.strip() == "":
        bobs_response = "Fine. Be that way!"

    return bobs_response