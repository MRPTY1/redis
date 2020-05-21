import redis

client = redis.Redis(host="47.103.194.86")
print(client.keys("*"))
client.close()
