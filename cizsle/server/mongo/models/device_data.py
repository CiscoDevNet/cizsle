"""DeviceData MongoDB data model."""


from datetime import datetime

from mongoengine import (
    DateTimeField, DictField, DynamicDocument, StringField, signals,
)


class DeviceData(DynamicDocument):
    """Device data document."""
    serial_number = StringField(required=True, unique=True)
    template_name = StringField(required=True)
    config_data = DictField()
    updated = DateTimeField()

    meta = {
        "collection": "device_data",
        "indexes": [
            "serial_number",
        ]
    }

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        """Update the device data attributes before saving the document."""
        assert isinstance(document, DeviceData)
        document.updated = datetime.utcnow()


signals.pre_save.connect(
    DeviceData.pre_save,
    sender=DeviceData
)
