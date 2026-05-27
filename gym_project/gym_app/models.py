from django.db import models

# Trainer Model
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    contact = models.CharField(max_length=15)

    class Meta:
        db_table = 'gym_trainer'

# Member Model
class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    trainer_id = models.IntegerField()
    trainer_name = models.CharField(max_length=15)

    class Meta:
        db_table = 'gym_member'


# Membership Model
class Membership(models.Model):
    member_id = models.IntegerField()
    member_name = models.CharField(max_length=15)
    type = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    fee = models.FloatField()

    class Meta:
        db_table = 'gym_membership'


# Payment Model
class Payment(models.Model):
    member_id = models.IntegerField()
    member_name = models.CharField(max_length=100)
    amount = models.FloatField()
    payment_date = models.DateField()
    method = models.CharField(max_length=50)

    class Meta:
        db_table = 'gym_payment'


# Exercise Model
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=100)
    reps = models.IntegerField()
    sets = models.IntegerField()

    class Meta:
        db_table = 'gym_exercise'


# Workout Plan Model
class WorkoutPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    exercise_id = models.IntegerField()
    exercise_name = models.CharField(max_length=15)
    member_id = models.IntegerField()
    member_name = models.CharField(max_length=15)

    class Meta:
        db_table = 'gym_workplan'


# Equipment Model
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    maintenance_date = models.DateTimeField()
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'gym_equipment'

