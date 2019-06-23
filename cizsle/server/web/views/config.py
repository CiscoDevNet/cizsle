"""Templated Configurations View."""

import logging

import jinja2
import mongoengine
from fastapi import HTTPException
from starlette.status import (
    HTTP_200_OK, HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from cizsle.server.mongo.models.device_data import DeviceData
from cizsle.server.mongo.template_loader import get_template
from cizsle.server.web import api


logger = logging.getLogger(__name__)


@api.get(
    "/config/{serial_number}",
    status_code=HTTP_200_OK,
    response_model=str,
    tags=["Device Configurations"],
)
def get_config(serial_number: str):
    """Get a rendered device configuration."""
    serial_number = serial_number.upper()

    try:
        device_data_object = DeviceData.objects.get(
            serial_number=serial_number
        )
        template = get_template(device_data_object.template_name)

    except mongoengine.DoesNotExist:
        error_message = (
            f"Serial number '{serial_number}' is invalid or the device "
            f"configuration for this serial number does not exist."
        )
        logger.error(error_message)
        raise HTTPException(HTTP_404_NOT_FOUND, detail=error_message)

    except jinja2.TemplateNotFound:
        error_message = (
            f"The template referenced in the device configuration for "
            f"serial number '{serial_number}' does not exist.  "
            f"Template Name: {device_data_object.template_name}"
        )
        logger.error(error_message)
        raise HTTPException(
            HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error_message,
        )

    except mongoengine.MultipleObjectsReturned as error:
        logger.error(error)
        raise HTTPException(
            HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error,
        )

    else:
        return template.render(**device_data_object.config_data)
