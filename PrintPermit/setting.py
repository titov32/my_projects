# This file local settings
import redis

USER = {
    'login': '',
    'domain': '',
    'password': ''
}
CONN_REDIS = redis.Redis(host='localhost', port=6379)
