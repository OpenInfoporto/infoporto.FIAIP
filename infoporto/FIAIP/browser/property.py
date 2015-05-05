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

class IPropertyPortlet(IPortletDataProvider):

    target = schema.Choice(
        title=_(u"Browse for contents"),
        description=_(u"Choose contents to display."),
        required=True,
        source=SearchableTextSourceBinder(
            {'portal_type': ('Folder')},
            default_query='path:'))
    

class Assignment(base.Assignment):

    implements(IPropertyPortlet)

    def __init__(self, target=''):
        self.target = target
        
    @property
    def title(self):
        return 'Property'


class Renderer(base.Renderer):
    
    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    render = ViewPageTemplateFile('templates/property.pt')
    
    def properties(self):
        folder_path = self.data.target
        if not folder_path:
            return None
        
        portal = api.portal.get()
        folder = portal.restrictedTraverse(folder_path.strip('/'))
        items = folder.getFolderContents()
        return [x.getObject() for x in items[:20]]
       
         
class AddForm(base.AddForm):
    
    form_fields = form.Fields(IPropertyPortlet)
    form_fields['target'].custom_widget = UberSelectionWidget
    
    label = _(u"Add Property Portlet")
    description = _(u"Portlets content a Property.")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    
    form_fields = form.Fields(IPropertyPortlet) 
    form_fields['target'].custom_widget = UberSelectionWidget

    label = _(u"Edit Property Portlet")
    description = _(u"Portlets content a Property.")
