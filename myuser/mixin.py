"""API mixin classes."""


class UserMixin:
    """UserMixin class."""

    def initial(self, request, *args, **kwargs):
        """Write method to override initial."""
        super().initial(request, *args, **kwargs)
        self.user = self.request.user
