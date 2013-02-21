# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DinnerGroup'
        db.create_table(u'dinners_dinnergroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('reservations_open', self.gf('django.db.models.fields.DateTimeField')()),
            ('reservations_close', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'dinners', ['DinnerGroup'])

        # Adding model 'Dinner'
        db.create_table(u'dinners_dinner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('dinner_group', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'dinners', to=orm['dinners.DinnerGroup'])),
        ))
        db.send_create_signal(u'dinners', ['Dinner'])

        # Adding model 'Reservation'
        db.create_table(u'dinners_reservation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'reservations', to=orm['custom_auth.User'])),
            ('dinner_group', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'reservations', to=orm['dinners.DinnerGroup'])),
            ('party_size', self.gf('django.db.models.fields.IntegerField')()),
            ('other_names', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('manual_review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dietary_restrictions', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'dinners', ['Reservation'])

        # Adding unique constraint on 'Reservation', fields ['user', 'dinner_group']
        db.create_unique(u'dinners_reservation', ['user_id', 'dinner_group_id'])

        # Adding model 'ReservationDinner'
        db.create_table(u'dinners_reservationdinner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reservation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dinners.Reservation'])),
            ('dinner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dinners.Dinner'])),
            ('first_choice', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'dinners', ['ReservationDinner'])

        # Adding unique constraint on 'ReservationDinner', fields ['reservation', 'dinner']
        db.create_unique(u'dinners_reservationdinner', ['reservation_id', 'dinner_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ReservationDinner', fields ['reservation', 'dinner']
        db.delete_unique(u'dinners_reservationdinner', ['reservation_id', 'dinner_id'])

        # Removing unique constraint on 'Reservation', fields ['user', 'dinner_group']
        db.delete_unique(u'dinners_reservation', ['user_id', 'dinner_group_id'])

        # Deleting model 'DinnerGroup'
        db.delete_table(u'dinners_dinnergroup')

        # Deleting model 'Dinner'
        db.delete_table(u'dinners_dinner')

        # Deleting model 'Reservation'
        db.delete_table(u'dinners_reservation')

        # Deleting model 'ReservationDinner'
        db.delete_table(u'dinners_reservationdinner')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'custom_auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mailing_list': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'dinners.dinner': {
            'Meta': {'object_name': 'Dinner'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'dinner_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'dinners'", 'to': u"orm['dinners.DinnerGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dinners.dinnergroup': {
            'Meta': {'object_name': 'DinnerGroup'},
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reservations_close': ('django.db.models.fields.DateTimeField', [], {}),
            'reservations_open': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'dinners.reservation': {
            'Meta': {'unique_together': "((u'user', u'dinner_group'),)", 'object_name': 'Reservation'},
            'dietary_restrictions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dinner_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'reservations'", 'to': u"orm['dinners.DinnerGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manual_review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'other_names': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'party_size': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'reservations'", 'to': u"orm['custom_auth.User']"})
        },
        u'dinners.reservationdinner': {
            'Meta': {'unique_together': "((u'reservation', u'dinner'),)", 'object_name': 'ReservationDinner'},
            'dinner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dinners.Dinner']"}),
            'first_choice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reservation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dinners.Reservation']"})
        }
    }

    complete_apps = ['dinners']