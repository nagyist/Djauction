# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Purchase.item'
        db.alter_column('auction_purchase', 'item_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auction.AuctionItem'], null=True))


    def backwards(self, orm):
        
        # Changing field 'Purchase.item'
        db.alter_column('auction_purchase', 'item_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auction.AuctionItem']))


    models = {
        'auction.auctionitem': {
            'Meta': {'ordering': "['number']", 'object_name': 'AuctionItem'},
            'fair_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        'auction.person': {
            'Meta': {'ordering': "['bid_number']", 'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bid_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'table': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auction.Table']"})
        },
        'auction.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'by_whom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auction.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auction.AuctionItem']", 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Silent'", 'max_length': '10'})
        },
        'auction.table': {
            'Meta': {'ordering': "['number']", 'object_name': 'Table'},
            'captain': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'captain_of'", 'null': 'True', 'to': "orm['auction.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['auction']
