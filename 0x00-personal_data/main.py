#!/usr/bin/env python3
"""
Main file
"""

import logging

get_logger = __import__('filtered_logger').get_logger
PII_FIELDS = __import__('filtered_logger').PII_FIELDS

logger = get_logger()
msg = '''name=Marlene Wood;email=hwestiii@att.net;phone=(473) 401-4253;ssn=261-72-6780;password=K5?BMNv;ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea;last_login=20
19-11-14 06:14:24;user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36; '''
lg = logging.LogRecord("user_d", logging.INFO, None, None, msg, None, None)
logger.handle(lg)
print("PII_FIELDS: {}".format(len(PII_FIELDS)))