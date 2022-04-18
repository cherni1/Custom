from odoo import models, fields

class DiagnosisProcess(models.Model):
    _name = 'diagnosis.process'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'process record'
    _rec_name = 'theme'

    theme = fields.Char(string='Theme')
    project_name = fields.Char(string='Project Name')
    animator = fields.Char(string='Animator')
    participants = fields.Char(string='Participants')
    process_lines = fields.One2many('diagnosis.process.lines', 'process_id', string='Process Lines')

class DiagnosisProcess(models.Model):
    _name = 'diagnosis.process.lines'
    _description = 'Process Lines'

    axes = fields.Text(string='Axes')
    item_for_discussion = fields.Text(string='Item For Discussion')
    comment_and_observation = fields.Text(string='Comment And Observation')
    note = fields.Integer(string='Note')
    process_id = fields.Many2one('diagnosis.process', string='Process ID')












