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

    def properties(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        if not "vani" in self.request.form:
            query = {'portal_type': 'infoporto.FIAIP.property', "review_state" : "published"}
            if self.comune:
                query["comune"] = self.comune

            if self.category:
                query["categoria"] = self.category

            if self.contratto:
                query["contratto"] = self.contratto

            if self.minprice:
                query["price"] = {'query': self.request.form["minprice"], 'range': 'min'}

            if self.maxprice:
                query["price"] = {'query': self.request.form["maxprice"], 'range': 'max'}
           
            items = catalog.searchResults(query) 
        else:
            items = catalog.searchResults({'portal_type': 'infoporto.FIAIP.property', 'vani': self.request.form["vani"]})


        return [x.getObject() for x in items]
