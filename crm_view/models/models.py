# -*- coding: utf-8 -*-

from odoo import models, fields, api

class equipo(models.Model):
    _name = 'crm.equipo'

    name = fields.Char(string='Nombre')
    leads = fields.One2many('crm.lead','equipos', string='Leads')

class marca(models.Model):
    _name = 'crm.marca'

    name = fields.Char(string='Nombre')
    leads = fields.One2many('crm.lead','marcas', string='Leads')

class modelo (models.Model):
    _name = 'crm.modelo'

    name = fields.Char(string='Nombre')
    leads = fields.One2many('crm.lead','modelos', string='Leads')

class marca(models.Model):
    _name = 'crm.servicio'

    name = fields.Char(string='Nombre')
    leads = fields.One2many('crm.lead','servicios', string='Leads')



class crm_lead(models.Model):
    _name = 'crm.lead'
    _inherit = 'crm.lead'

    client_name = fields.Char(string="Nombre")
    client_surname = fields.Char(string="Apellido")
    
    dni = fields.Char(string="DNI")
    equipos = fields.Many2one('crm.equipo', string='Equipos')
    marcas = fields.Many2one('crm.marca', string='Marcas')
    modelos = fields.Many2one('crm.modelo', string='Modelos')
    servicios = fields.Many2one('crm.servicio', string='Servicios')
    triplets = fields.One2many('crm.triplet', 'lead', string="Empleados")

class crm_employee(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    triplets = fields.One2many('crm.triplet','empleado_id', string='Leads')

class triplet(models.Model):
    _name = 'crm.triplet'
    
    empleado_id = fields.Many2one('hr.employee',string="Empleado")
    fecha = fields.Date(string="Fecha")
    descripcion = fields.Char(string="Descripción")
    lead = fields.Many2one('crm.lead',string="Lead")

# tengo que crear un modelo que tenga empleado, fecha y descripcion, y quitar la relacion con empleado sustituyendola por esto.
