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


class XInsuranceDetails(models.Model):
    _name = 'x_insurance.details'

    x_name = fields.Char(string='N° Mutuelle', required=False, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    x_employee_id = fields.One2many('employee.details','x_insurance_id', string='Ayants droit', required=True)
    x_state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('closed', 'Closed')],
                             required=False, default='draft')
    x_hide_inv_button = fields.Boolean(copy=False)
    x_note_field = fields.Html(string='Comment')
    x_num_mutuelle = fields.Char(string='N° Mutuelle')
    x_nss = fields.Char(string='Numéro Sécurité Sociale')
    x_sexe = fields.Selection([('masculin', 'Masculin'), ('feminin', 'Feminin')],
                             required=False, default='masculin')
    x_nom = fields.Char(string='Nom', required=False)
    x_prenom = fields.Char(string='Prénom', required=False)
    x_situation = fields.Selection([('celibataire', 'Celibataire'), ('marie', 'Marié'),('divorce', 'Divorcé')],
                             required=False, default='celibataire')
    x_nmc = fields.Char(string='N° Mutuelle Conjoint')
    x_statut = fields.Selection([('salarie', 'Salarié'), ('non_salarie', 'Retraité')],
                             required=False, default='salarie')
    x_date_n = fields.Date(string='Date de naissance')
    x_tel = fields.Char(string='Tel.')
    x_adresse = fields.Char(string='Adresse', required=False)
    x_num_compte = fields.Char(string='Numéro de compte')
    x_agence = fields.Char(string='Agence Bancaire', required=False)
    x_organism = fields.Many2one('x_organism.details',string='Organisme', required=False)
    x_date_af = fields.Date(string='Date Affiliation')


    def x_confirm_insurance(self):
        self.x_state = 'confirmed'
        self.x_hide_inv_button = True

    def x_close_insurance(self):
        self.x_state = 'closed'
        self.x_hide_inv_button = False


    @api.model
    def create(self, vals):
        if vals.get('x_name', 'New') == 'New':
            vals['x_name'] = self.env['ir.sequence'].next_by_code('x_insurance.details') or 'New'
        return super(XInsuranceDetails, self).create(vals)
