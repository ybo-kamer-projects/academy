# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class academy(models.Model):
#     _name = 'academy.academy'
#     _description = 'academy.academy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, api


class Utilisateurs(models.Model):
    _inherit = 'res.partner'

    description = fields.Char()
    district = fields.Char()
    mobile_one = fields.Char()
    email_one = fields.Char()





class Contacts(models.Model):
    _name = 'academy.contacts'



    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('academy.courses', 'contact_id', string="Courses")





class Courses(models.Model):
    _name = 'academy.courses'
    _inherit = ['mail.thread']

    name = fields.Char()
    contact_id = fields.Many2one('academy.contacts', string="Contact")