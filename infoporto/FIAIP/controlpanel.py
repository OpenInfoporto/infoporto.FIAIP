from plone.app.registry.browser import controlpanel
from infoporto.FIAIP.interfaces import IFIAIPSettings


class FIAIPSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IFIAIPSettings
    label = u"FIAIP settings"

    def __init__(self, a, b):
        super(FIAIPSettingsEditForm, self).__init__(a, b)

    def updateFields(self):
        super(FIAIPSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(FIAIPSettingsEditForm, self).updateWidgets()

    def applyChanges(self, data):
        return super(FIAIPSettingsEditForm, self).applyChanges(data)


class FIAIPSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = FIAIPSettingsEditForm
