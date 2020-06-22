class OIDCBaseError(Exception):
    """OIDC base error catched in the browser view.
    """
    message = 'Invalid Request'
    status_code = 400


class OIDCTokenError(OIDCBaseError):
    """Raised if the token request is invalid or unauthorized.

    More information:
    https://openid.net/specs/openid-connect-core-1_0.html#TokenErrorResponse
    """


class OIDCJwkEndpointError(OIDCBaseError):
    """Raised when an error occurs getting the jwks.
    """


class OIDCUserInfoError(OIDCBaseError):
    """Raised when an error condition occurs getting user information.
    """


class OIDCSubMismatchError(OIDCBaseError):
    """Error raised when the validated token sub doesn't match with the user
    information requests sub.

    For more info check out:
    https://rograce.github.io/openid-connect-documentation/explore_auth_code_flow#userinfo-successful-response
    """
    message = 'Subject mismatch'
    status_code = 400
