from odoo import models, fields


class MiModelo(models.Model):
    _name = "mi.primer.modelo"
    _description = "Mi Primer Modelo de Ejemplo"

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripcion")
