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

from odoo import models, fields


class PolicyDetails(models.Model):
    _name = 'policy.details'

    name = fields.Char(string='Name', required=False)
    policy_type = fields.Many2one('policy.type', string='Policy Type', required=False)
    payment_type = fields.Selection([('fixed', 'Fixed'), ('installment', 'Installment')],
                                    required=False, default='fixed')
    x_amount = fields.Float(string='Amount', required=False, default= 1.0)
    policy_duration = fields.Integer(string='Duration in Days', required=False)
    note_field = fields.Html(string='Comment')
    x_mode_p = fields.Selection([('caisse', 'Caisse'), ('cheque', 'Chèque'), ('virement', 'Virement')],
                                    required=False, default='caisse')
    x_date_af = fields.Date(string='Date Affiliation')
    x_date_ef = fields.Date(string='Date Effet')
    x_montant = fields.Float(string='Montant Cotisation', required=False)
    x_adherent = fields.Many2one('x_insurance.details', related='x_num_mutuelle', string='Adhérent', required=False)
    x_organism = fields.Char(related='x_adherent.x_organism', string='Organisme')
    active = fields.Boolean('Active',default=True)


class PolicyType(models.Model):
    _name = 'policy.type'

    name = fields.Char(string='Name')
