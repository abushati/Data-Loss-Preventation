from django.db import models
from django.contrib import admin
import re

class regexCombs(models.Model):
    regexName = models.CharField(max_length=50)
    regexPattern = models.CharField(max_length=50)
    
    # Runs what the admin wants to save the regex pattern 
    def save(self, *args, **kwargs):
        validPattern = self.validRegex()
        patternExist = self.regexExist()
        if not validPattern or patternExist:            
            return
        else:
            super().save(*args, **kwargs)

    # Check if the admin regex pattern is a valid pattern
    def validRegex(self):
        try:
            re.compile(self.regexPattern)
            return True
        except re.error:
            return False
    # Check if the admin regex pattern is already in the database
    def regexExist(self):
        try:
            regexCombs.objects.get(regexPattern = self.regexPattern)
            return True
        except:
            return False


class incidentLog(models.Model):
    pattern_name = models.CharField(max_length=100)
    pattern_string = models.CharField(max_length=100)
    words_caught = models.CharField(max_length=100)
    message_sent = models.TextField()