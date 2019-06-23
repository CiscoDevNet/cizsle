"""Jinja2 MongoDB template loader."""


from typing import Callable, Tuple

import jinja2
import mongoengine

from cizsle.server.mongo.models.template import Template


class MongoLoader(jinja2.BaseLoader):
    """Load Jinja2 templates from a MongoDB database."""

    def get_source(self, environment: jinja2.Environment, template: str) \
            -> Tuple[str, None, Callable[[], bool]]:
        """Get the template source (text) and reload helper function.

        Retrieve the template source text from MongoDB (querying by template
        name) and create a reload helper function that determines if the
        template has changed in MongoDB.

        The Jinja2 auto-reload feature uses the reload helper function
        to determine when the template needs to be reloaded from source.

        Args:
            environment: The rendering environment.
            template: The name of the template to be loaded from MongoDB.
        """
        try:
            loaded_template = Template.objects.get(name=template)

        except mongoengine.DoesNotExist:
            raise jinja2.TemplateNotFound(template)

        except mongoengine.MultipleObjectsReturned:
            raise jinja2.TemplateRuntimeError(
                f"Multiple templates exist with the name '{template}'."
            )

        def reload_helper() -> bool:
            """Compare sha256 hashes to determine if the template has changed.

            This helper function captures (as a closure) the sha256 hash of the
            template when it is loaded. Then, to detect changes, the function
            requests the latest hash from MongoDB and compares the latest hash
            with the captured hash and returns the result.
            """
            loaded_template_hash = loaded_template.sha256
            latest_template_hash = Template.objects.only("sha256").get(
                name=template,
            ).sha256
            return loaded_template_hash == latest_template_hash

        return loaded_template.template, None, reload_helper


# Setup the Jinja2 rendering environment
env = jinja2.Environment(
    loader=MongoLoader(),
    auto_reload=True,
)


# Main function for requesting templates
get_template = env.get_template
