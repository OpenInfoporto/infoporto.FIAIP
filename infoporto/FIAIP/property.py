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

    full_description = RichText(
            title=_(u"Descrizione estesa"),
            required=False,
    )

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

    regione = schema.TextLine(
            title=_(u"Regione"),
            required=False,
    )

    provincia = schema.TextLine(
            title=_(u"Provincia"),
            required=False,
    )

    comune = schema.TextLine(
            title=_(u"Comune"),
            required=False,
    )

    cod_istat = schema.TextLine(
            title=_(u"Cod. ISTAT"),
            required=False,
    )

    localita = schema.TextLine(
            title=_(u"Localita'"),
            required=False,
    )

    indirizzo = schema.TextLine(
            title=_(u"Indirizzo"),
            required=False,
    )

    civico = schema.TextLine(
            title=_(u"Num. civico"),
            required=False,
    )

    tipologia = schema.TextLine(
            title=_("Tipologia"),
            required=False,
    )

    categoria = schema.Choice(
            title=_("Categoria"),
            values=[_(u'Residenziale'), _(u'Commerciale'), _(u'Rustici e terreni'),
                    _(u'Uffici, fondi')],
            required=False
    )

    prezzo = schema.TextLine(
            title=_(u"Prezzo"),
            required=False,
    )

    superficie = schema.TextLine(
            title=_(u"Superficie"),
            required=False,
    )

    vani = schema.TextLine(
            title=_(u"Vani"),
            required=False,
    )

    camere = schema.TextLine(
            title=_(u"Camere"),
            required=False,
    )

    bagni = schema.TextLine(
            title=_(u"Bagni"),
            required=False,
    )

    riscaldamento = schema.Choice(
            title=_("Riscaldamento"),
            values=[_(u'Non definite'), _(u'Centralizzato'), _(u'Autonomo'),
                    _(u'Inesistente')],
            required=False
    )

    condizioni = schema.Choice(
            title=_("Condizioni"),
            values=[_(u'Non definite'),_(u' Nuova costruzione'),
                    _(u'Ristrutturato'),_(u'Da ristrutturare'),
                    _(u'Abitabile'),_(u'Ottime'),
                    _(u'Seminuovo'),],
            required=False,
    )

    ascensore = schema.Bool(
            title=_(u"Ascensore"),
            required=False,
    )

    arredato = schema.Bool(
            title=_(u"Arredato"),
            required=False,
    )

    garage = schema.Bool(
            title=_(u"Garage"),
            required=False,
    )

    giardino = schema.Bool(
            title=_(u"Giardino"),
            required=False,
    )

    piano = schema.TextLine(
            title=_(u"Piano"),
            required=False,
    )

    classe_energ = schema.TextLine(
            title=_(u"Classe energetica"),
            required=False,
    )

    epi = schema.TextLine(
            title=_(u"EPI"),
            required=False,
    )

    epi_um = schema.TextLine(
            title=_(u"EPI un. misura"),
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
