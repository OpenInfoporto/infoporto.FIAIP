from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserView
from Products.CMFCore.utils import getToolByName

import zope.pagetemplate.pagetemplatefile

import json


class Result(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request

        self.comune = self.request.form["comune"]
        self.category = self.request.form["category"]
        self.contratto = self.request.form["contratto"]
        self.minprice = self.request.form["minprice"]
        self.maxprice = self.request.form["maxprice"]
        self.rif = self.request.form["riferimento"]

    def properties(self):
        catalog = getToolByName(self.context, 'portal_catalog')
            
        if "vani" in self.request.form:
            items = catalog.searchResults({'portal_type': 'infoporto.FIAIP.property', 'vani': self.request.form["vani"]})

        elif self.rif:
            items = catalog.searchResults({'portal_type': 'infoporto.FIAIP.property', 'rif': self.request.form["riferimento"]})

        else:
            query = {'portal_type': 'infoporto.FIAIP.property', "review_state" : "published"}
            if self.comune:
                query["comune"] = self.comune

            if self.category:
                categories = {'Residenziale': 'R',
                              'Commerciale': 'C',
                              'Rustici e terreni': 'T',
                              'Uffici, fondi': 'U'}
                query["cod_categoria"] = categories.get(self.category)

            if self.contratto:
                query["contratto"] = self.contratto[:1]

            if self.minprice:
                query["price"] = {'query': float(self.request.form["minprice"]), 'range': 'min'}

            if self.maxprice:
                query["price"] = {'query': float(self.request.form["maxprice"]), 'range': 'max'}

            items = catalog.searchResults(query)

        return [x.getObject() for x in items]
