from odoo import models, api, _
from odoo.exceptions import AccessError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def write(self, vals):
        # Verificar si el partner está vinculado a una compañía
        company = self.env['res.company'].search([('partner_id', 'in', self.ids)], limit=1)
        
        if company:
            # Verificar si el usuario actual tiene el permiso de Administración/Configuración
            if not self.env.user.has_group('base.group_system'):
                raise AccessError(_(
                    'You do not have permission to modify the contact associated with the company. '
                    'Only users with Administration/Settings permissions can perform this action.'
                ))
        
        return super(ResPartner, self).write(vals)