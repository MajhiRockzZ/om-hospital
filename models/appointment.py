# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from datetime import date


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "appointment_date desc"

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'hospital.appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result
    
    def _get_default_note(self):
        return "Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus."

    def _get_default_patient_id(self):
        return 2

    def _get_default_date(self):
        return date.today()

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    name = fields.Char(string='Appointment ID', required=True, copy=False,
                       readonly=True, index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one(
        'hospital.patient', string='Patient', required=True, default=_get_default_patient_id)
    patient_age = fields.Integer(string='Age', related='patient_id.patient_age')
    notes = fields.Text(string='Registration Note', default=_get_default_note)
    appointment_date = fields.Date(string='Date', required=True, default=_get_default_date)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], string='Status', readonly=True, default='draft')
