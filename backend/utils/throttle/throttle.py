from rest_framework.throttling import SimpleRateThrottle


# normal user
class AnonymousThrottle(SimpleRateThrottle):
    scope = 'AnonymousUser'

    def get_cache_key(self, request, view):
        return self.get_ident(request)


# Super user
class SuperThrottle(SimpleRateThrottle):
    scope = 'super_user'

    def get_cache_key(self, request, view):
        return request.user.username
