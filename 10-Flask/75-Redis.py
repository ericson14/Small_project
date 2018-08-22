from redis import StrictRedis


def redis_connect():
    try:
        sr = StrictRedis(host="192.168.68.91", decode_responses=True)
        sr.set('sex', 'male')
        result1 = sr.keys()
        result2 = sr.hgetall("class")
        result3 = sr.smembers("gaoyan")
        result4 = sr.zincrby("salary", "eric", 1550)
        print(result1)
        print(result2)
        print(result3)
        print(result4)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    redis_connect()
