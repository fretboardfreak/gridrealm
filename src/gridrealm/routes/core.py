"""Gridrealm Static Routes Core Library."""

from flask.views import MethodView


class GRView(MethodView):
    """Base MethodView class for the Gridrealm game."""

    route = None
    endpoint = None

    @classmethod
    def register(cls, app):
        """Register the view on the given flask app."""
        if cls.route is None or cls.endpoint is None:
            raise NotImplementedError(
                'GRView classes must define a route and an endpoint value.')
        if isinstance(cls.route, str):
            app.add_url_rule(cls.route, view_func=cls.as_view(cls.endpoint))
        elif isinstance(cls.route, list):
            view_func = cls.as_view(cls.endpoint)
            for route in cls.route:
                app.add_url_rule(route, view_func=view_func)


def register_views(app, views):
    """Register the static views with the flask app."""
    for view in views:
        view.value.register(app)
