import dm.xmlsec.binding
dm.xmlsec.binding.initialize()


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    from Products.PluggableAuthService.PluggableAuthService import registerMultiPlugin
    from AccessControl.Permissions import manage_users
    from ftw.oidcauth import plugin

    registerMultiPlugin(plugin.OIDCPlugin.meta_type)
    context.registerClass(
        plugin.OIDCPlugin,
        permission=manage_users,
        constructors=(plugin.manage_addOIDCPlugin,
                      plugin.addOIDCPlugin),
        visibility=None)
