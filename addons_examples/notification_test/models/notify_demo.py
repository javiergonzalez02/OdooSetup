from odoo import models, fields, api

class NotifyDemoWizard(models.Model):
    _name = 'notification_test.notify_demo'
    _description = 'Notificación demo'

    def notify_user(self):
        self.env.user.notify_success(message='¡Notificación de éxito desde el módulo!')
