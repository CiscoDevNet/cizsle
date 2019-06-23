"""Template MongoDB data model."""


from datetime import datetime
from hashlib import sha256

from mongoengine import DateTimeField, DynamicDocument, signals, StringField


class Template(DynamicDocument):
    """Template document."""
    name = StringField(required=True, unique=True)
    template = StringField(required=True)
    sha256 = StringField()
    updated = DateTimeField()

    meta = {
        "collection": "templates",
        "indexes": [
            "name",
            "sha256",
        ]
    }

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        """Update the template attributes before saving the document."""
        assert isinstance(document, Template)
        document.updated = datetime.utcnow()
        document.sha256 = sha256(document.template.encode("utf-8")).hexdigest()


signals.pre_save.connect(
    Template.pre_save,
    sender=Template
)
