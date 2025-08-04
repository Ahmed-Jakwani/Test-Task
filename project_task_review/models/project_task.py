from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ProjectTask(models.Model):
    _inherit = 'project.task'

    review_ids = fields.One2many('project.task.review', 'task_id')
    reviews_count = fields.Integer(compute="compute_reviews_count")

    def compute_reviews_count(self):
        for record in self:
            record.reviews_count = len(record.review_ids)

    def action_open_task_reviews(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Task Reviews',
            'view_mode': 'tree,form',
            'res_model': 'project.task.review',
            'domain': [('task_id', '=', self.id)],
            'context': {
                'default_task_id': self.id
            },
            'target': 'current',
        }