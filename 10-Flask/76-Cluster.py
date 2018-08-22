from rediscluster import StrictRedisCluster


def user_cluster():
    try:
        cluster_nodes = [
            {"host": "192.168.68.91", "port": 7000},
            {"host": "192.168.68.91", "port": 7001},
            {"host": "192.168.68.91", "port": 7002},
        ]
        cluster = StrictRedisCluster(startup_nodes=cluster_nodes, decode_responses=True)
        cluster.set("name", "laowang")
        print(cluster.get("name"))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    user_cluster()
