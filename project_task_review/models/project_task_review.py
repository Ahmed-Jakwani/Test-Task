from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class ProjectTaskReview(models.Model):
    _name = 'project.task.review'
    _rec_name = 'reviewer_id'
    
    date = fields.Date(default=datetime.now())
    reviewer_id = fields.Many2one('res.users', string="Reviewed By", default=lambda self: self.env.user, required=True)
    review = fields.Text()
    score = fields.Selection([
        ('1', "Bad"),
        ('2', "Below Average"),
        ('3', "Average"),
        ('4', "Above Average"),
        ('5', "Excellent")
    ])
    task_id = fields.Many2one('project.task', required="True")