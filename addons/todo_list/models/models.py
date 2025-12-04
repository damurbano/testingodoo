# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class TodoStage(models.Model):
    _name = 'todo_list.stage'
    _description = 'Etapa de Tarea'
    _order = 'sequence, id'

    name = fields.Char(string="Nombre", required=True)
    sequence = fields.Integer(string="Secuencia", default=10)
    fold = fields.Boolean(string="Plegado en Kanban")


class TodoTask(models.Model):
    _name = 'todo_list.task'
    _description = 'Tarea'
    _order = 'priority desc, date_deadline asc'

    name = fields.Char(string="Tarea", required=True)
    description = fields.Text(string="Descripción")
    stage_id = fields.Many2one('todo_list.stage', string="Etapa", 
        default=lambda self: self.env['todo_list.stage'].search([], limit=1),
        group_expand='_read_group_stage_ids')
    state = fields.Selection([
        ('todo', 'Por Hacer'),
        ('in_progress', 'En Progreso'),
        ('done', 'Completado'),
        ('cancelled', 'Cancelado')
    ], string="Estado", default='todo', tracking=True)
    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Normal'),
        ('2', 'Alta'),
        ('3', 'Urgente')
    ], string="Prioridad", default='1')
    date_deadline = fields.Date(string="Fecha límite")
    date_done = fields.Datetime(string="Fecha completado", readonly=True)
    user_id = fields.Many2one('res.users', string="Asignado a", default=lambda self: self.env.user)
    tag_ids = fields.Many2many('todo_list.tag', string="Etiquetas")
    is_late = fields.Boolean(compute="_compute_is_late", store=True, string="Atrasada")
    color = fields.Integer(string="Color")

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        """Mostrar todas las etapas en el Kanban, incluso las vacías"""
        return self.env['todo_list.stage'].search([])

    @api.depends('date_deadline', 'state')
    def _compute_is_late(self):
        today = date.today()
        for task in self:
            if task.date_deadline and task.state not in ('done', 'cancelled'):
                task.is_late = task.date_deadline < today
            else:
                task.is_late = False

    def action_start(self):
        self.write({'state': 'in_progress'})

    def action_done(self):
        for task in self:
            task.state = 'done'
            task.date_done = fields.Datetime.now()

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_restart(self):
        self.write({'state': 'todo', 'date_done': False})


class TodoTag(models.Model):
    _name = 'todo_list.tag'
    _description = 'Etiqueta'

    name = fields.Char(string="Nombre", required=True)
    color = fields.Integer(string="Color")

