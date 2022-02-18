# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
from odoo import http
from odoo.http import request
from datetime import datetime
import calendar, math, re, io, base64, os, json, werkzeug

import logging
_logger = logging.getLogger(__name__)


class MyModelName(models.Model):
    _name = "my.model.name"
    _description = "My Model Names"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", readonly=True)
    photo = fields.Binary(string='Photo', attachment=True, store=True)
    company_id = fields.Many2one(comodel_name="res.company", string="Company", default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency", related="company_id.currency_id", stored=True)
    active = fields.Boolean(string="Active", default=True)
    amount = fields.Float(string="Amount", default=0)
    year = fields.Selection(lambda self: self._get_years(), string="Year", stored=True)
    is_blood_donar = fields.Boolean(string="Blood Bonar")
    blood_group = fields.Selection(
        [
            ('A+', 'A+ve'),
            ('B+', 'B+ve'),
            ('O+', 'O+ve'),
            ('AB+', 'AB+ve'),
            ('A-', 'A-ve'),
            ('B-', 'B-ve'),
            ('O-', 'O-ve'),
            ('AB-', 'AB-ve')
        ],
        string="Blood Group"
    )
    birthday = fields.Datetime(string="Birthday")
    note = fields.Text(string="Note")
    description = fields.Html(string="Description")
    my_model_name_line_ids = fields.One2many(comodel_name="my.model.name.line", inverse_name="my_model_name_id", string="My Model Lines")

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Name already exists!'),
        ('code_unique', 'unique(code)', 'Code already exists!'),
    ]


    def _get_years(self):
        year_list = []
        
        # Static Year Range
        current_year = int(datetime.now().year)
        for i in range(current_year - 10, current_year + 11):
            year_list.append((str(i), str(i)))
        
        return year_list


    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('my.model.name')
        res = super(MyModelName, self).create(vals)
        return res
    

    def action_update_data_wizard(self):
        self.ensure_one()
        
        company_id = self.company_id.id if self.company_id else None
        blood_group = self.blood_group

        view = self.env.ref('app_name.my_model_name_wizard_form_view')
        if view:
            return {
                'name': _('My Model Name Wizard'),
                'res_model': 'my.model.name.wizard',
                'type': 'ir.actions.act_window',
                'view_id': view.id,
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_id': False,
                'context': {
                    'self_id': self.id,
                    'default_company_id': company_id,
                    'default_blood_group': blood_group,
                },
            }



class MyModelNameLine(models.Model):
    _name = "my.model.name.line"
    _description = "My Model Name Lines"

    name = fields.Char(string="Name", required=True)
    amount = fields.Float(string="Amount", default=0)
    company_id = fields.Many2one(comodel_name="res.company", string="Company")
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency", related="company_id.currency_id", stored=True)
    my_model_name_id = fields.Many2one(comodel_name="my.model.name", string="My Model Name")



class MyModelNameWizard(models.Model):
    _name = "my.model.name.wizard"
    _description = "My Model Name Wizard"

    company_id = fields.Many2one(comodel_name="res.company", string="Company")
    blood_group = fields.Selection(
        [
            ('A+', 'A+ve'),
            ('B+', 'B+ve'),
            ('O+', 'O+ve'),
            ('AB+', 'AB+ve'),
            ('A-', 'A-ve'),
            ('B-', 'B-ve'),
            ('O-', 'O-ve'),
            ('AB-', 'AB-ve')
        ],
        string="Blood Group"
    )


    def set_data(self):
        self.ensure_one()
        
        ## Get Context
        self_id = self.env.context.get('self_id')
        company_id = self.env.context.get('company_id')
        blood_group = self.env.context.get('blood_group')

        
        ## Get Data using Model ID
        my_model_name = False
        if self_id:
            my_model_name = self.env['my.model.name'].browse(self_id)

        company = False
        if company_id:
            company = self.env['res.company'].browse(company_id)

        
        ## Get Fields Data
        company_id = self.company_id.id
        blood_group = self.blood_group

        
        ## Process & Update Data
        if my_model_name:
            my_model_name.write({
                'company_id': company_id,
                'blood_group': blood_group,
            })

            return {
                'type': 'ir.actions.client',
                'tag': 'reload',
            }

