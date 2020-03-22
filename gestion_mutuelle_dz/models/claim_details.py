# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Techno Solutions(odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from odoo import models, fields, api, _


class ClaimDetails(models.Model):
    _name = 'claim.details'

    name = fields.Char(string='Name', required=False, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    name_2 = fields.Char(string='Name 2', required=False, copy=False, readonly=True, index=True,
                         default=lambda self: _('New'))
    insurance_id = fields.Many2one('insurance.details', required=False)
    partner_id = fields.Many2one(related='insurance_id.partner_id', string='Customer', readonly=True)
    policy_id = fields.Many2one(related='insurance_id.policy_id', string='Policy', readonly=True)
    employee_id = fields.Many2one(related='insurance_id.employee_id', string='Agent', readonly=True)
    x_employee_id = fields.One2many('employee.details', 'x_claim_id', related='x_insurance_id.x_employee_id', string='Liste des bénéficiaires', readonly=True)
    x_insurance_id = fields.Many2one('x_insurance.details',string='Assuré', required=False)
    x_amount = fields.Float(related='insurance_id.amount', string='Amount')
    date_claimed = fields.Date(string='Date Applied', default=fields.Date.today())
    invoice_id = fields.Many2one('account.move', string='Invoiced', readonly=True, copy=False)
    note_field = fields.Html(string='Comment')
    x_date_dcsn = fields.Date(string='Date Décision')
    x_date_dec = fields.Date(string='Date Décès')
    x_etat = fields.Selection([('actif', 'Actif'), ('non_actif', 'Non Actif')],
                             required=False, default='actif')
    x_montant = fields.Float(string='Montant de capital')
    active = fields.Boolean('Active',default=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('claim.details') or 'New'
        return super(ClaimDetails, self).create(vals)

