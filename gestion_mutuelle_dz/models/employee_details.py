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


class EmployeeDetails(models.Model):
    _name = 'employee.details'

    name = fields.Char(string='Name', required=False)
    related_partner = fields.Many2one('res.users', string='Related User', copy=False)
    sex = fields.Selection([('male', 'Male'), ('female', 'Female')])
    phone = fields.Float(string='Phone Number', size=15, digits=(15, 0))
    salary_type = fields.Selection([('fixed', 'Fixed'), ('commission', 'Commission'), ('both', 'Both')],
                                   default='commission', required=False)
    base_salary = fields.Integer(string='Base Salary')
    last_salary = fields.Date(string='Last Payment On', copy=False)
    insurance_ids = fields.One2many('insurance.details', 'employee_id', string='Last Payment On', readonly=True)
    note_field = fields.Html(string='Comment')
    x_insurance_id = fields.Many2one('x_insurance.details', string='Assuré', copy=False)
    x_claim_id =fields.Many2one('claim.details', string='Contrat capital décès', copy=False)
    invoice_id = fields.Many2one('account.move', string='Last payment', copy=False, readonly=True)
    x_nom = fields.Char(string='Nom', required=False)
    x_prenom = fields.Char(string='Prénom', required=False)
    x_date_n = fields.Date(string='Date de naissance')
    x_sexe = fields.Selection([('masculin', 'Masculin'), ('feminin', 'Feminin')],
                             required=False, default='masculin')
    x_position = fields.Selection([('conjoint', 'Conjoint'), ('enfant_leg', 'Enfant Légitime'), ('enfant_rec_n', 'Enfant Recueilli Neuveu ou nièce'), ('enfant_rec_fs', 'Enfant Recueilli Frère ou Soeur'),('enfant_rec_a', 'Enfant Recueilli Autre'), ('enfant_a_ns', 'Enfant Assisté Neuveu ou nièce'),('enfant_a_fs', 'Enfant Assisté Frère ou Soeur'), ('enfant_a_a', 'Enfant Assisté Autre')],
                             required=False, default='conjoint')
