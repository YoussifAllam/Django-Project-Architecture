from config.env import env, ENVIRONMENT

redis_host = env("REDIS_URL")

if ENVIRONMENT == "TEST":
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.inmemory.InMemoryCache",
        }
    }

else:
    # Chat app with redis layer
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": redis_host,
        }
    }

    CACHE_MIDDLEWARE_ALIAS = "default"
    CACHE_MIDDLEWARE_SECONDS = 60 * 6  # 360 minutes
