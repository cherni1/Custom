# -*- coding: utf-8 -*-
from odoo import models, fields, api

class DiagnosisProject(models.Model):
    _name = 'diagnosis.project'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'project record'
    _rec_name = 'project_name'

    project_name = fields.Char(string='Project Name')
    client = fields.Text(string='Client')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    email_address = fields.Char(string='Email Address')
    address = fields.Char(string='Address')
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: 'New')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', 'New') == 'New':
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('diagnosis.project.sequence') or ('New')
        result = super(DiagnosisProject, self).create(vals)
        return result
