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
from odoo.exceptions import UserError


class InsuranceDetails(models.Model):
    _name = 'insurance.details'

    name = fields.Char(string='Name', required=False, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    partner_id = fields.Many2one('res.partner', string='Customer', required=False)
    date_start = fields.Date(string='Date Started', default=fields.Date.today(), required=False)
    close_date = fields.Date(string='Date Closed')
    invoice_ids = fields.One2many('account.move', 'insurance_id', string='Invoices', readonly=True)
    employee_id = fields.Many2one('employee.details', string='Agent', required=False)
    x_employee_id = fields.One2many('employee.details','x_insurance_id', string='Bénéficiaires', required=True)
    commission_rate = fields.Float(string='Commission Percentage')
    policy_id = fields.Many2one('policy.details', string='Policy', required=False)
    x_amount = fields.Float(related='policy_id.amount', string='Amount', default= 1.0)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('closed', 'Closed')],
                             required=False, default='draft')
    hide_inv_button = fields.Boolean(copy=False)
    note_field = fields.Html(string='Comment')
    x_num_mutuelle = fields.Integer(string='N° Mutuelle')
    x_nss = fields.Integer(string='Numéro Sécurité Sociale')
    x_sexe = fields.Selection([('masculin', 'Masculin'), ('feminin', 'Feminin')],
                             required=False, default='masculin')
    x_nom = fields.Char(string='Nom', required=False)
    x_prenom = fields.Char(string='Prénom', required=False)
    x_situation = fields.Selection([('celibataire', 'Celibataire'), ('marie', 'Marié'),('divorce', 'Divorcé')],
                             required=False, default='celibataire')
    x_nmc = fields.Integer(string='N° Mutuelle Conjoint')
    x_statut = fields.Selection([('salarie', 'Salarié'), ('non_salarie', 'Non Salarié')],
                             required=False, default='salarie')
    x_date_n = fields.Date(string='Date de naissance')
    x_tel = fields.Integer(string='Tel.')
    x_adresse = fields.Char(string='Adresse', required=False)
    x_num_compte = fields.Integer(string='Numéro de compte')
    x_agence = fields.Char(string='Agence Bancaire', required=False)


    def x_confirm_insurance(self):
        self.state = 'confirmed'
        self.hide_inv_button = True
    
    def confirm_insurance(self):
        self.state = 'confirmed'
        self.hide_inv_button = True


    def x_close_insurance(self):
        for records in self.invoice_ids:
            if records.state == 'paid':
                raise UserError(_("All invoices must be Paid"))
        self.state = 'closed'
        self.hide_inv_button = False
    
    def close_insurance(self):
        for records in self.invoice_ids:
            if records.state == 'paid':
                raise UserError(_("All invoices must be Paid"))
        self.state = 'closed'
        self.hide_inv_button = False

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('insurance.details') or 'New'
        return super(InsuranceDetails, self).create(vals)


class AccountInvoiceRelate(models.Model):
    _inherit = 'account.move'

    insurance_id = fields.Many2one('insurance.details', string='Insurance')
    claim_id = fields.Many2one('claim.details', string='Insurance')
