from zope import schema
from zope.interface import Interface


class IFIAIP(Interface):
    pass

class IFIAIPSettings(Interface):

    sync_url  = schema.URI(title=u"URL",
                    description=u"http://localhost/filname.xml",
                    required=False
                    )
