api-replay
==========

An HTTP replay, proxy, routing service with queuing in Python, Flask and Redis

###Installing

`pip install git+https://github.com/easypairings/api-replay.git`

###Configuring

The following environment variables are required:

```
REDIS_URL (e.g. redis://localhost)
DEBUG (defaults to False)
```

###Running

Running the application (for development) requires only Flask and redis

`redis-server & api-replay runserver`

###Contributing

Pull requests are very welcome. In your first pull request, please add your name to [AUTHORS.md](https://github.com/easypairings/api-replay/blob/master/AUTHORS.md).
