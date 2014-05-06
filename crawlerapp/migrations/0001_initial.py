# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'crawlerapp_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('income', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'crawlerapp', ['Company'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'crawlerapp_company')


    models = {
        u'crawlerapp.company': {
            'Meta': {'object_name': 'Company'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['crawlerapp']