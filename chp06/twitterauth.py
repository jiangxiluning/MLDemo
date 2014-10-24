# This code is supporting material for the book
# Building Machine Learning Systems with Python
# by Willi Richert and Luis Pedro Coelho
# published by PACKT Publishing
#
# It is made available under the MIT License

import sys

CONSUMER_KEY = 'aSikTMEgibXwLJzPqg5MzNpOa'
CONSUMER_SECRET = 'gMT84SIHlhlLoWdDzVRU4VlRBqg7M8hqCdNQqLGaMttZmSxtCk'

ACCESS_TOKEN_KEY = '116327181-wS3Qg6jHoTpjfTa7Cky23Zd0VtGkiVz9oe1PvzlD'
ACCESS_TOKEN_SECRET = 'S0TG7vQSFw16I5CiVTguSlvpojX7xkl0aF9H9CZHJRAeL'

if CONSUMER_KEY is None or CONSUMER_SECRET is None or ACCESS_TOKEN_KEY is None or ACCESS_TOKEN_SECRET is None:
    print("""\
When doing last code sanity checks for the book, Twitter
was using the API 1.0, which did not require authentication.
With its switch to version 1.1, this has now changed.

It seems that you don't have already created your personal Twitter
access keys and tokens. Please do so at
https://dev.twitter.com/docs/auth/tokens-devtwittercom
and paste the keys/secrets into twitterauth.py

Sorry for the inconvenience,
The authors.""")

    sys.exit(1)
