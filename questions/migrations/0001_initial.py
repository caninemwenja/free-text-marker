# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'questions_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('answer_keywords', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'questions', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'questions_question')


    models = {
        u'questions.question': {
            'Meta': {'object_name': 'Question'},
            'answer_keywords': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['questions']