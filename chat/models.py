from django.db import models

class Report(models.Model):   
   ticker_db              = models.CharField(max_length=50)
   report_content         = models.CharField(max_length=80)
   latest_pickle_of_the_report = models.CharField(max_length = 80)
   report_generated_time  = models.DateTimeField(auto_now_add=True)
   phonenumber            = models.PositiveIntegerField()

class Predictions(models.Model):   
   ticker_db              = models.CharField(max_length=50)
   model_name             = models.CharField(max_length=80)
   latest_pickle_of_model = models.CharField(max_length = 80)
   latest_update_time     = models.DateTimeField(auto_now_add=True)
   standardized_conviction_score = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

class Tickers(models.Model):
   ticker_db    = models.CharField(max_length=80)
   isin         = models.CharField(max_length=80)
   exchange     = models.CharField(max_length=80)
   bloomberg_id = models.CharField(max_length=80)
   reuters_id   = models.CharField(max_length=80)
   
class Models(models.Model):
   model_name   = models.CharField(max_length=80)

class Heat_map(models.Model):
   ticker_db           = models.CharField(max_length=80)
   LINEAR_REGRESSION   = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
   LOGISTIC_REGRESSION = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
   LSTM_1              = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
   LSTM_2              = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
   LDS_190101          = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
   REL_VAL_1           = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
   M2                  = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
   SUMMARY_SC_SCORE    = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
