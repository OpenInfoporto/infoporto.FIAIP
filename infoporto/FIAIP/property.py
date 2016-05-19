from five import grok

from zope import schema

from plone.dexterity.content import Container

from plone.directives import form
from plone.app.textfield import RichText
from plone.namedfile.interfaces import IImageScaleTraversable

from infoporto.FIAIP import MessageFactory as _
from fiaipsync import dataFetcher
from collective import dexteritytextindexer

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName

from plone import api
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import logging


logger = logging.getLogger('infoporto.FIAIP')


class IProperty(form.Schema, IImageScaleTraversable):
    """
    Describe a place to live or work
    """

    # Campo utilizzato nella scheda
    id_agenzia = schema.TextLine(
            title=_(u"Agency ID"),
            required=False
        )

    dexteritytextindexer.searchable('rif')
    rif = schema.TextLine(
            title=_(u"Property ref."),
            required=False
    )

    dexteritytextindexer.searchable('contratto')
    contratto = schema.Choice(
            title=_("Contract"),
            values=[_(u'V'), _(u'A'), _(u'S')],
            required=False
    )

    data = schema.TextLine(
            title=_(u"Data inserimento o modifica"),
            required=False,
    )

    cod_regione = schema.TextLine(
            title=_(u"Codice Regione"),
            required=False,
    )

    regione = schema.TextLine(
            title=_(u"Regione"),
            required=False,
    )

    cod_provincia = schema.TextLine(
            title=_(u"Codice provincia"),
            required=False,
    )

    provincia = schema.TextLine(
            title=_(u"Provincia"),
            required=False,
    )

    sigla_provincia = schema.TextLine(
            title=_(u"Sigla provincia"),
            required=False,
    )

    cod_comune = schema.TextLine(
            title=_(u"Codice comune"),
            required=False,
    )

    dexteritytextindexer.searchable('comune')
    comune = schema.TextLine(
            title=_(u"Comune"),
            required=False,
    )

    cod_istat = schema.TextLine(
            title=_(u"Cod. ISTAT"),
            required=False,
    )

    cod_zona_comune = schema.TextLine(
            title=_(u"Cod. Zona comune"),
            required=False,
    )

    localita = schema.TextLine(
            title=_(u"Localita'"),
            required=False,
    )

    ubicazione = schema.TextLine(
            title=_(u"Ubicazione'"),
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

    latitudine = schema.TextLine(
            title=_(u"latitudine"),
            required=False,
    )

    longitudine = schema.TextLine(
            title=_(u"longitudine"),
            required=False,
    )

    cod_tipologia = schema.TextLine(
            title=_("Codice tipologia"),
            required=False,
    )

    tipologia = schema.TextLine(
            title=_("Tipologia"),
            required=False,
    )

    dexteritytextindexer.searchable('categoria')
    categoria = schema.Choice(
            title=_("Categoria"),
            values=[_(u'Residenziale'), _(u'Commerciale'), _(u'Rustici e terreni'),
                    _(u'Uffici, fondi')],
            required=False
    )

    # testo
    testo = schema.Text(
            title=_(u"Descrizione"),
            required=False,
    )

    full_description = RichText(
            title=_(u"Descrizione estesa"),
            required=False,
    )

    dexteritytextindexer.searchable('prezzo')
    prezzo = schema.TextLine(
            title=_(u"Prezzo"),
            required=False,
    )

    dexteritytextindexer.searchable('price')
    price = schema.Float(
            title=_(u"Prezzo vero"),
            required=False,
    )

    dexteritytextindexer.searchable('mq')
    mq = schema.TextLine(
            title=_(u"Superficie"),
            required=False,
    )

    dexteritytextindexer.searchable('vani')
    vani = schema.TextLine(
            title=_(u"Vani"),
            required=False,
    )

    piano = schema.TextLine(
            title=_(u"Piano"),
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

    cod_condizioni = schema.TextLine(
            title=_(u"Codice condizioni"),
            required=False,
    )

    dexteritytextindexer.searchable('condizioni')
    condizioni = schema.Choice(
            title=_("Condizioni"),
            values=[_(u'Non definite'),_(u' Nuova costruzione'),
                    _(u'Ristrutturato'),_(u'Da ristrutturare'),
                    _(u'Abitabile'),_(u'Ottime'),
                    _(u'Seminuovo'),],
            required=False,
    )

    cod_riscaldamento = schema.TextLine(
            title=_(u"Codice riscaldamento"),
            required=False,
    )

    riscaldamento = schema.Choice(
            title=_("Riscaldamento"),
            values=[_(u'Non definite'), _(u'Centralizzato'), _(u'Autonomo'),
                    _(u'Inesistente')],
            required=False
    )

    classe_energetica = schema.TextLine(
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

    cod_cucina = schema.TextLine(
            title=_(u"Codice cucina"),
            required=False,
    )

    cucina = schema.TextLine(
            title=_(u"Cucina"),
            required=False,
    )

    garage = schema.Bool(
            title=_(u"Garage"),
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

    condizionatore = schema.Bool(
            title=_(u"Condizionatore"),
            required=False,
    )

    giardino = schema.Bool(
            title=_(u"Giardino"),
            required=False,
    )

    giardino_tipo = schema.TextLine(
            title=_(u"Tipo giardino"),
            required=False,
    )

    giardino_mq = schema.TextLine(
            title=_(u"Mq giardino"),
            required=False,
    )

    email = schema.TextLine(
            title=_(u"E-mail"),
            required=False,
    )

    # foto Element
    titolo1 = schema.TextLine(
            title=_(u"Foto"),
            required=False,
    )

    url1 = schema.TextLine(
            title=_(u"Url"),
            required=False,
    )

    # foto Element
    titolo2 = schema.TextLine(
            title=_(u"Foto"),
            required=False,
    )

    url2 = schema.TextLine(
            title=_(u"Url"),
            required=False,
    )

    # foto Element
    titolo3 = schema.TextLine(
            title=_(u"Foto"),
            required=False,
    )

    url3 = schema.TextLine(
            title=_(u"Url"),
            required=False,
    )

    # foto Element
    titolo4 = schema.TextLine(
            title=_(u"Foto"),
            required=False,
    )

    url4 = schema.TextLine(
            title=_(u"Url"),
            required=False,
    )

    # foto Element
    titolo5 = schema.TextLine(
            title=_(u"Foto"),
            required=False,
    )

    url5 = schema.TextLine(
            title=_(u"Url"),
            required=False,
    )

    # foto Element
    titolo6 = schema.TextLine(
            title=_(u"Foto"),
            required=False,
    )

    url6 = schema.TextLine(
            title=_(u"Url"),
            required=False,
    )

    # foto Element
    titolo7 = schema.TextLine(
            title=_(u"Foto"),
            required=False,
    )

    url7 = schema.TextLine(
            title=_(u"Url"),
            required=False,
    )

    # foto Element
    titolo8 = schema.TextLine(
            title=_(u"Foto"),
            required=False,
    )

    url8 = schema.TextLine(
            title=_(u"Url"),
            required=False,
    )

    # foto Element
    titolo9 = schema.TextLine(
            title=_(u"Foto"),
            required=False,
    )

    url9 = schema.TextLine(
            title=_(u"Url"),
            required=False,
    )

    # foto Element
    titolo10 = schema.TextLine(
            title=_(u"Foto"),
            required=False,
    )

    url10 = schema.TextLine(
            title=_(u"Url"),
            required=False,
    )

    # foto Element
    titolo11 = schema.TextLine(
            title=_(u"Foto"),
            required=False,
    )

    url11 = schema.TextLine(
            title=_(u"Url"),
            required=False,
    )

    # foto Element
    titolo12 = schema.TextLine(
            title=_(u"Foto"),
            required=False,
    )

    url12 = schema.TextLine(
            title=_(u"Url"),
            required=False,
    )

    trattativa_riservata = schema.TextLine(
            title=_(u"Trattativa riservata"),
            required=False,

    )

    skip_sync = schema.Bool(
            title=_("Skip sync"),
            required=False
    )


class Property(Container):
    grok.implements(IProperty)

    def getPriceString(self):
        if self.contratto == 'A':
            return "%s %s/mese" % (self.prezzo,u"\u20AC")

        if self.contratto == 'V':
            return "%s %s" % (self.prezzo,u"\u20AC")

    def getImage(self):
        for item in self.listFolderContents():
            return item

        return None

    def getPreview(self):
        print "getPreview"
        for item in self.listFolderContents():
            return item.absolute_url()

        return None


    # Add your class methods and properties here


class testImport(BrowserView):

    template = ViewPageTemplateFile('property_templates/testimport.pt')

    def __call__(self):

        df = dataFetcher(url="http://62.149.166.102/agenzia_xml/fc86110a489b4c71a73a6abfb2286556.xml")

        fetched = df.getElements(df.connectAndGet())

        logger.info("%s elements found" % len(fetched))

        ref_list = []

        for el in fetched:
            ref_list.append(el['rif'])

            print el['prezzo']

            try:
                el['price'] = float(el['prezzo'])
            except:
                logger.error('Error converting price for %s' % el['rif'])


            catalog = api.portal.get_tool(name='portal_catalog')
            existing = catalog(portal_type='infoporto.FIAIP.property',
                               rif=el['rif'])

            if existing:
                logger.info("Existing found for ref %s" % el['rif'])

                if existing[0].getObject().skip_sync:
                    logger.info("skip_sync flag found for %s" % el['rif'])

                else:
                    logger.info("No skip_sync flag found for %s" % el['rif'])
                    logger.info("Deleting existing %s..." % el['rif'])
                    api.content.delete(existing[0].getObject())

                    logger.info("Creating ref: %s..." % el['rif'])
                    title = "%s %s vani %s - %s" % (el['tipologia'], el['vani'], el['comune'], el['ubicazione'])
                    obj = api.content.create(type="infoporto.FIAIP.property",
                                             title=title,
                                             container=api.content.get(path='/immobili/'),
                                             **el)
                    api.content.transition(transition='publish', obj=obj)

            else:
                logger.info("No existing item found for ref %s" % el['rif'])

                logger.info("Creating ref: %s..." % el['rif'])
                title = "%s %s vani %s - %s" % (el['tipologia'], el['vani'], el['comune'], el['ubicazione'])
                obj = api.content.create(type="infoporto.FIAIP.property",
                                         title=title,
                                         container=api.content.get(path='/immobili/'),
                                         **el)
                api.content.transition(transition='publish', obj=obj)

        # clean up not existing
        logger.info("Checking for something to remove...")
        items = catalog(portal_type='infoporto.FIAIP.property')

        logger.info("%s elements on remote vs %s elements locally" % (len(fetched), len(items)))

        """
        tobe_removed = list(set(items)-set(fetched))
        for i in tobe_removed:
            el = catalog(portal_type='infoporto.FIAIP.property',rif=i)
            logger.info("Deleting unmatched item ref %s..." % i)
            api.content.delete(existing[0].getObject())

        """
        return self.template()

class View(grok.View):
    grok.context(IProperty)
    grok.require('zope2.View')

    # sorting

    # Add view methods here
    def getPhotos(self):
        context = aq_inner(self.context)
        pics = []

        if context.titolo1:
            pics.append(dict(url=context.url1, title=context.titolo1))

        if context.titolo2:
            pics.append(dict(url=context.url2, title=context.titolo2))

        if context.titolo3:
            pics.append(dict(url=context.url3, title=context.titolo3))

        if context.titolo4:
            pics.append(dict(url=context.url4, title=context.titolo4))

        if context.titolo5:
            pics.append(dict(url=context.url5, title=context.titolo5))

        if context.titolo6:
            pics.append(dict(url=context.url6, title=context.titolo6))

        if context.titolo7:
            pics.append(dict(url=context.url7, title=context.titolo7))

        if context.titolo8:
            pics.append(dict(url=context.url8, title=context.titolo8))

        if context.titolo9:
            pics.append(dict(url=context.url9, title=context.titolo9))

        if context.titolo10:
            pics.append(dict(url=context.url10, title=context.titolo10))

        if context.titolo11:
            pics.append(dict(url=context.url11, title=context.titolo11))

        if context.titolo12:
            pics.append(dict(url=context.url12, title=context.titolo12))


        catalog = getToolByName(context, 'portal_catalog')

        limit = 1
        local_pics =  catalog(portal_type="Image", path='/'.join(context.getPhysicalPath()))

        for lp in local_pics:
            lp = lp.getObject()
            pics.append(dict(url=lp.absolute_url(), title=lp.title))

        return pics
