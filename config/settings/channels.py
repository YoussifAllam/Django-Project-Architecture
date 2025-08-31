from config.env import env

REDIS_HOSTNAME = env("REDIS_HOSTNAME")

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(REDIS_HOSTNAME, 6379)],
        },
    },
}
