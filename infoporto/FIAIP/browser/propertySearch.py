from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope import schema
from zope.formlib import form
from zope.interface import implements

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget


from infoporto.FIAIP import MessageFactory as _

from plone import api

class IPropertySearchPortlet(IPortletDataProvider):
    
    title = schema.TextLine(
        title=_(u"Title portlet"),
        required=False,
    ) 

class Assignment(base.Assignment):

    implements(IPropertySearchPortlet)
        
    @property
    def title(self):
        return 'Property Search'


class Renderer(base.Renderer):
    
    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    render = ViewPageTemplateFile('templates/propertySearch.pt')

    def getComuni(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        return set([el.comune for el in catalog(portal_type='infoporto.FIAIP.property')])

    def getCategoria(self):
        return [None,_(u'Residenziale'), _(u'Commerciale'), _(u'Rustici e terreni'),_(u'Uffici, fondi')]

    def getContratto(self):
        return [None, _(u'V'), _(u'A'), _(u'S')]

    def getPrezzoMinimo(self):
        return [None, 10, 200, 500]

    def getPrezzoMax(self):
        return [None, 600,200,900]

    
class AddForm(base.AddForm):
    
    form_fields = form.Fields(IPropertySearchPortlet)
    
    label = _(u"Add Property Search Portlet")
    description = _(u"Portlets content a Property Search.")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    
    form_fields = form.Fields(IPropertySearchPortlet) 

    label = _(u"Edit Property Search Portlet")
    description = _(u"Portlets content a Property Search.")
