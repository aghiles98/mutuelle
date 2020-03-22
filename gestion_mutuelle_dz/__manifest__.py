# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Techno Solutions (odoo@cybrosys.com)
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

{
    'name': 'Gestion de la mutuelle',
    'version': '13.0.1.0.0',
    'summary': """Gestion et traitement de la mutuelle""",
    'description': """Gestion de la mutuelle""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'category': 'Industries',
    'depends': ['base', 'account'],
    'license': 'AGPL-3',
    'data': [
        'views/insurance_details.xml',
        'views/x_insurance_details.xml',
        'views/claim_details.xml',
        'views/employee_details.xml',
        'views/policy_management.xml',
        'views/insurance_sequence.xml',
        'views/x_organism_details.xml',
        'views/insurance_management.xml',
        'report/insurance_contract_report.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

