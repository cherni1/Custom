from odoo import models, fields

class DiagnosisPlanning(models.Model):
    _name = 'diagnosis.planning'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'planning record'
    _rec_name = 'company_name'


    company_name = fields.Char(string='company name')
    project = fields.Text(string='project')
    author = fields.Text(string='author')
    planning_lines = fields.One2many('diagnosis.planning.lines', 'planning_id', string='Planning Lines')

class DiagnosisPlanning(models.Model):
    _name = 'diagnosis.planning.lines'
    _description = 'Planning Lines'

    theme = fields.Char(string='Theme')
    interlocutors = fields.Char(string='Interlocutors')
    contact = fields.Char(string='Contact/Mail')
    intervener = fields.Char(string='Zenith Intervener')
    week = fields.Text(string='week')
    date = fields.Date(string='Date')
    hour = fields.Text(string='Time Of The Interview')
    time = fields.Text(string='Duration')
    status = fields.Text(string='Status')
    planning_id = fields.Many2one('diagnosis.planning', string='Planning ID')



