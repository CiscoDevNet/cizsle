"""Cizsle server web service."""


import fastapi

import cizsle.config


api = fastapi.FastAPI(
    debug=cizsle.config.debug,
    title="cizsle",
    description="Cisco ZTP Server LE",
    version=cizsle.__version__,
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
)


# Views
import cizsle.server.web.views.config   # noqa
