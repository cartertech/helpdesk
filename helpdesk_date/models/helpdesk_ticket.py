# Copyright (c) 2019 Carter Tech Pty Ltd
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
	
    date_logged = fields.Datetime(string='Date logged')