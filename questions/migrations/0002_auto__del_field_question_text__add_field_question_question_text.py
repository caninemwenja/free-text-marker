# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Question.text'
        db.delete_column(u'questions_question', 'text')

        # Adding field 'Question.question_text'
        db.add_column(u'questions_question', 'question_text',
                      self.gf('django.db.models.fields.CharField')(default='question text', max_length=200),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Question.text'
        raise RuntimeError("Cannot reverse this migration. 'Question.text' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Question.text'
        db.add_column(u'questions_question', 'text',
                      self.gf('django.db.models.fields.CharField')(max_length=200),
                      keep_default=False)

        # Deleting field 'Question.question_text'
        db.delete_column(u'questions_question', 'question_text')


    models = {
        u'questions.question': {
            'Meta': {'object_name': 'Question'},
            'answer_keywords': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['questions']