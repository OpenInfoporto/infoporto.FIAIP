from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from infoporto.FIAIP import MessageFactory as _


# Interface class; used to define content-type schema.

class IProperty(form.Schema, IImageScaleTraversable):
    """
    Describe a place to live or work
    """

    id = schema.TextLine(
            title=_(u"Property ID"),
            required=False
        )

    id_agenzia = schema.TextLine(
            title=_(u"Agency ID"),
            required=False
        )

    email = schema.TextLine(
            title=_(u"E-mail"),
            required=False
        )

    rif = schema.TextLine(
            title=_(u"Property ref."),
            required=False
    )

    contratto = schema.Choice(
            title=_("Contract"),
            values=[_(u'V'), _(u'A'), _(u'S')],
            required=False
    )

    data = schema.Datetime(
            title=_(u"Data inserimento o modifica"),
            required=False,
    )

    
    


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Property(Container):
    grok.implements(IProperty)

    # Add your class methods and properties here
    pass


# View class
# The view will automatically use a similarly named template in
# property_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IProperty)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
