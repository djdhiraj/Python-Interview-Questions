 payload = {
        'username': username,
        'usertype': usertype,
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + timedelta(days=365)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token.decode('unicode_escape')
