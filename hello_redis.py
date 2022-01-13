import redis


r = redis.Redis("127.0.0.1", "6379", db=0)


r.set("user:name", "mapsa", ex=30)
r.hmset("mapsa", {"name": "ashkan"})