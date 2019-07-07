import jwt
from django.conf import settings
import base64
from datetime import datetime, timedelta

def get_new_json_web_token(data, expiry_time_in_secs=settings.JWT_EXPIRY_TIME):
    secret = settings.JWT_SIGN_SECRET
    payload = {
        'exp': datetime.utcnow() + timedelta(seconds=expiry_time_in_secs),
        'data': data
    }
    token = jwt.encode(payload, secret, algorithm="HS256").decode('utf8')
    print("PAYLOAD - ", data)
    print('JWT - ', token)
    return token

def get_new_refresh_token(token):
    part3 = token.split('.')[2][::-1]
    refresh_token = base64.b64encode(base64.b64encode(part3.encode('utf8')).decode('utf8')[::-1].encode('utf8')).decode('utf8')[::-1]
    print('REFRESH TOKEN - ', refresh_token)
    return refresh_token

def json_web_token_is_valid(token):
    is_valid, status, payload, message = False, 600, None, 'JWT has been successfully validated'

    try:
        payload = jwt.decode(token, settings.JWT_SIGN_SECRET, algorithms=['HS256'])
        is_valid = True
        status = 200
    except jwt.exceptions.InvalidSignatureError as error:
        """
        If secret is invalid or
        jwt.decode(enc + 'o', 'sec', algorithms=['HS256'])
        --------------------------------------------------
        >>> enc = jwt.encode({'ok': 1, 'exp': datetime.utcnow() + timedelta(minutes=5)}, 'sec', algorithm='HS256')
        >>> enc
        b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvayI6MSwiZXhwIjoxNTYwMjY2MjI0fQ.1-6ClPMT_R80EcE1b18qZ2bz6Q2FFkNUusqIDYY8HUs'
        >>> 
        >>> enc = enc.decode('utf-8')
        >>> enc
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvayI6MSwiZXhwIjoxNTYwMjY2MjI0fQ.1-6ClPMT_R80EcE1b18qZ2bz6Q2FFkNUusqIDYY8HUs'
        >>> 
        >>> d = jwt.decode(enc, 'secret')
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/jwt/api_jwt.py", line 92, in decode
            jwt, key=key, algorithms=algorithms, options=options, **kwargs
          File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/jwt/api_jws.py", line 156, in decode
            key, algorithms)
          File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/jwt/api_jws.py", line 223, in _verify_signature
            raise InvalidSignatureError('Signature verification failed')
        jwt.exceptions.InvalidSignatureError: Signature verification failed
        >>> 
        >>> d = jwt.decode(enc, 'sec')
        >>> d
        {'ok': 1, 'exp': 1560266224}
        >>> 
        """
        message = f'Invalid JWT/secret, {error}' 
    except jwt.exceptions.DecodeError as error:
        # jwt.decode(enc[:-2], 'sec', algorithms=['HS256'])
        message = f"Invalid JWT, {error}"
    except jwt.exceptions.ExpiredSignatureError as error:
        """
        >>> d = jwt.decode(enc, 'sec')
        >>> d
        {'ok': 1, 'exp': 1560266224}
        >>> 
        >>> d = jwt.decode(enc, 'sec')
        >>> d
        {'ok': 1, 'exp': 1560266224}
        >>> 
        >>> d = jwt.decode(enc, 'sec')
        >>> d
        {'ok': 1, 'exp': 1560266224}
        >>> 
        >>> # ----- After 5 minutes ------
        ...
        >>>
        >>> d = jwt.decode(enc, 'sec')
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/jwt/api_jwt.py", line 104, in decode
            self._validate_claims(payload, merged_options, **kwargs)
          File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/jwt/api_jwt.py", line 134, in _validate_claims
            self._validate_exp(payload, now, leeway)
          File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/jwt/api_jwt.py", line 175, in _validate_exp
            raise ExpiredSignatureError('Signature has expired')
        jwt.exceptions.ExpiredSignatureError: Signature has expired
        >>> 
        """
        message = f'JWT is expried so you will need to refresh the token, {error}'
        status = 601
        is_valid = True
    except Exception as error:
        message = f"{error}"

    return is_valid, status, message, payload


if __name__ == "__main__":
    token = get_new_json_web_token({'username': 'RR', 'password': 'RR@123'})
    print(token)
