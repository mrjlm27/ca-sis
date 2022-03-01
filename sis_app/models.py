from email.policy import default
from time import timezone
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.

# class Student(models.Model):

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)  

class Account(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)#passwords should be stored hashed 
    class Meta:
        abstract=True # Don't use this line if you want Contact to have its own table

class Student(Account):
    student_firstname = models.CharField(max_length=128, default=None)#
    student_lastname = models.CharField(max_length=128, default=None)#
    student_middlename = models.CharField(max_length=128, default=None)
    student_nickname = models.CharField(max_length=128, default=None)
    student_birthday = models.DateField(default=datetime.date.today())

    grade_levels = [
        ('Nursery','Nursery'),
        ('Kinder 1','Kinder 1'),
        ('Kinder 2 Junior', 'Kinder 2 Junior'),
        ('Kinder 2 Senior', 'Kinder 2 Senior'),
    ]
    student_grade_level = models.CharField(max_length=128, choices=grade_levels, default='Nursery')#
    status =[
    ('Not Enrolled','Not Enrolled'),
    ('Enrolled', 'Enrolled'),
    ]#
    enrollment_status = models.CharField(max_length=20, choices=status,default='Not Enrolled')#
    #student_schoolyear_start=models.IntegerField(('year'), validators=[MinValueValidator(2000), max_value_current_year], default=None)#
    student_schoolyear_start=models.IntegerField(('year'), validators=[MinValueValidator(2000)], default=None)#
    student_address = models.CharField(max_length=300, default=None)
    student_religion = models.CharField(max_length=128, default=None)
    student_nationality = models.CharField(max_length=128, default=None)
    student_hobbies = models.TextField(max_length=500, default=None)
    student_likes = models.TextField(max_length=500, default=None)
    student_dislikes = models.TextField(max_length=500, default=None)
    student_shm = models.TextField(max_length=500, default=None)
    student_allergies = models.TextField(max_length=500, default=None)
    student_sd = models.TextField(max_length=500, default=None)
    student_oconsiderations = models.TextField(max_length=500, default=None)
    student_guardianemail = models.EmailField(max_length = 254, default=None)
    student_f_firstname = models.CharField(max_length=128, default=None)
    student_f_lastname = models.CharField(max_length=128, default=None)
    student_f_middlename = models.CharField(max_length=128, default=None)
    student_f_telno = models.CharField(max_length=128, default=None)
    student_f_address = models.CharField(max_length=300, default=None)
    student_f_occupation = models.CharField(max_length=128, default=None)
    student_f_employer = models.CharField(max_length=128, default=None)
    student_f_oaddress = models.CharField(max_length=300, default=None)
    student_f_otelno = models.CharField(max_length=128, default=None)
    student_f_natureofbusiness = models.CharField(max_length=128, default=None)
    student_m_firstname = models.CharField(max_length=128, default=None)
    student_m_lastname = models.CharField(max_length=128, default=None)
    student_m_middlename = models.CharField(max_length=128, default=None)
    student_m_telno = models.CharField(max_length=128, default=None)
    student_m_address = models.CharField(max_length=300, default=None)
    student_m_occupation = models.CharField(max_length=128, default=None)
    student_m_employer = models.CharField(max_length=128, default=None)
    student_m_oaddress = models.CharField(max_length=300, default=None)
    student_m_otelno = models.CharField(max_length=128, default=None)
    student_m_natureofbusiness = models.CharField(max_length=128, default=None)
    student_sibling_name = models.CharField(max_length=300, default=None)
    student_sibling_gender = models.CharField(max_length=128, default=None)
    student_sibling_age = models.IntegerField(default=None)
    student_sibling_school=models.CharField(max_length=300, default=None)
    student_medexp = models.BooleanField(default = False)
    student_rules = models.BooleanField(default = False)
    student_accuracy = models.BooleanField(default = False)
    student_signedname = models.CharField(max_length=300, default=None)
    student_signdate = models.DateField(default=datetime.date.today())
    enrollment_plan_choices =[
    ('Annually','Annually'),
    ('Bi-Annually', 'Bi-Annually'),
    ('Quarterly', 'Quarterly'),
    ]
    student_enrollment_plan = models.CharField(max_length=20, choices=enrollment_plan_choices,default='Annually')
    


def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

class Teacher(Account):
    t_name = models.CharField(max_length=128)

class Payment(models.Model):
    payment_s_account_id = models.ForeignKey(Student, on_delete=models.CASCADE, null = False)
    paymentdate_date = models.DateField(null = False)
    payment_amount = models.IntegerField(null = False)
    outstandingbalance = models.IntegerField(default = 0)
    
    payment_sy_end = 0
    outstandingbalance = models.IntegerField(default = 1000000)
    school_year_end=models.IntegerField(('year'), validators=[MinValueValidator(2000)], default=None)#

    # tuitionfee = models.IntegerField(default = 50000)

    # @property
    # def getoutstandingbalance(self):
    #     annual = 37999
    #     biannual = 38998
    #     quarterly = 41663

    #     if self.payment_s_account_id.student_enrollment_plan == 'Annually': 
    #         return annual
    #     elif self.payment_s_account_id.student_enrollment_plan == 'Bi-Annually':
    #         return  biannual
    #     else:
    #         return  quarterly

    def getenrollmentplan(self):
        return self.payment_s_account_id.student_enrollment_plan

    def getstudentfirstname(self):
        return self.payment_s_account_id.student_firstname

    def getstudentlastname(self):
        return self.payment_s_account_id.student_lastname
    
    def getstudentenrollmentstatus(self):
        return self.payment_s_account_id.enrollment_status
    
    def getstudentid(self):
        return self.payment_s_account_id.id

    def get_sy_start(self):
        first_half = [6,7,8,9,10,11,12]
        payment_sy_start = 0
        if self.paymentdate_date.month in first_half:
            payment_sy_start = self.paymentdate_date.year
            return payment_sy_start
        else:
            payment_sy_start = self.paymentdate_date.year - 1
            return payment_sy_start
    def get_sy_end(self):
        first_half = [6,7,8,9,10,11,12]
        payment_sy_start = 0
        payment_sy_end = 0
        if self.paymentdate_date.month in first_half:
            payment_sy_start = self.paymentdate_date.year
            payment_sy_end = payment_sy_start + 1
            return payment_sy_end
        else:
            payment_sy_start = self.paymentdate_date.year - 1
            payment_sy_end = payment_sy_start + 1
            return payment_sy_end
    
class TranscriptOfRecord(models.Model):
    tor_id = models.IntegerField(default = 0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null = False, default=None)

class GradeReport(models.Model):
    #General Fields For All Students
    tor_id = models.ForeignKey(TranscriptOfRecord, on_delete=models.CASCADE, null=True, blank = True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank = True)
    school_year = models.IntegerField(('year'), validators=[MinValueValidator(2000), max_value_current_year], default=None)
    period =[
    ('1','1'),
    ('2', '2'),
    ('3', '3'),
    ]
    gradelevel_choices = [
        ('Nursery','Nursery'),
        ('Kinder 1', 'Kinder 1'),
        ('Kinder 2 Junior', 'Kinder 2 Junior'), 
        ('Kinder 2 Senior', 'Kinder 2 Senior'),
    ]
    gradelevel = models.CharField(default='Nursery', max_length=30, choices=gradelevel_choices)
    grading_period = models.CharField(default='1', max_length=10, choices=period)
    sem_average = models.FloatField(null=True, blank=True, default= None)
    year_average = models.FloatField(null=True, blank=True, default= None)
    
    
    #For K1 to K2 SR Grade Reports
    reading_grade = models.FloatField(null=True, blank = True)
    mathematics_grade = models.FloatField(null=True, blank = True)
    language_grade = models.FloatField(null=True, blank = True)
    science_grade = models.FloatField(null=True, blank = True)
    penmanship_grade = models.FloatField(null=True, blank = True)
    filipino_grade = models.FloatField(null=True, blank = True)
    final_reading = models.FloatField(null=True, blank=True, default= None)
    final_mathematics = models.FloatField(null=True, blank=True, default= None)
    final_language = models.FloatField(null=True, blank=True, default= None)
    final_science = models.FloatField(null=True, blank=True, default= None)
    final_penmanship = models.FloatField(null=True, blank=True, default= None)
    final_filipino = models.FloatField(null=True, blank=True, default= None)
    readingreadiness1 = models.IntegerField(null=True, blank=True, default= None)
    readingreadiness2 = models.IntegerField(null=True, blank=True, default= None)
    readingreadiness3 = models.IntegerField(null=True, blank=True, default= None)
    readingreadiness4 = models.IntegerField(null=True, blank=True, default= None)
    readingreadiness5 = models.IntegerField(null=True, blank=True, default= None)
    readingreadiness6 = models.IntegerField(null=True, blank=True, default= None)
    readingreadiness7 = models.IntegerField(null=True, blank=True, default= None)
    readingreadiness8 = models.IntegerField(null=True, blank=True, default= None)
    readingreadiness9 = models.IntegerField(null=True, blank=True, default= None)
    readingreadiness10 = models.IntegerField(null=True, blank=True, default= None)
    readingreadiness11 = models.IntegerField(null=True, blank=True, default= None)
    readingreadiness12 = models.IntegerField(null=True, blank=True, default= None)
    readingreadiness13 = models.IntegerField(null=True, blank=True, default= None)
    science1 = models.IntegerField(null=True, blank=True, default= None)
    science2 = models.IntegerField(null=True, blank=True, default= None)
    science3 = models.IntegerField(null=True, blank=True, default= None)
    science4 = models.IntegerField(null=True, blank=True, default= None)
    science5 = models.IntegerField(null=True, blank=True, default= None)
    science6 = models.IntegerField(null=True, blank=True, default= None)
    language1 = models.IntegerField(null=True, blank=True, default= None)
    language2 = models.IntegerField(null=True, blank=True, default= None)
    language3 = models.IntegerField(null=True, blank=True, default= None)
    language4 = models.IntegerField(null=True, blank=True, default= None)
    language5 = models.IntegerField(null=True, blank=True, default= None)
    language6 = models.IntegerField(null=True, blank=True, default= None)
    language7 = models.IntegerField(null=True, blank=True, default= None)
    language8 = models.IntegerField(null=True, blank=True, default= None)
    language9 = models.IntegerField(null=True, blank=True, default= None)
    language10 = models.IntegerField(null=True, blank=True, default= None)
    math1 = models.IntegerField(null=True, blank=True, default= None)
    math2 = models.IntegerField(null=True, blank=True, default= None)
    math3 = models.IntegerField(null=True, blank=True, default= None)
    math4 = models.IntegerField(null=True, blank=True, default= None)
    math5 = models.IntegerField(null=True, blank=True, default= None)
    math6 = models.IntegerField(null=True, blank=True, default= None)
    math7 = models.IntegerField(null=True, blank=True, default= None)
    math8 = models.IntegerField(null=True, blank=True, default= None)
    math9 = models.IntegerField(null=True, blank=True, default= None)
    math10 = models.IntegerField(null=True, blank=True, default= None)
    math11 = models.IntegerField(null=True, blank=True, default= None)
    penmanship1 = models.IntegerField(null=True, blank=True, default= None)
    penmanship2 = models.IntegerField(null=True, blank=True, default= None)
    penmanship3 = models.IntegerField(null=True, blank=True, default= None)
    penmanship4 = models.IntegerField(null=True, blank=True, default= None)
    filipino1 = models.IntegerField(null=True, blank=True, default= None)
    filipino2 = models.IntegerField(null=True, blank=True, default= None)
    filipino3 = models.IntegerField(null=True, blank=True, default= None)
    filipino4 = models.IntegerField(null=True, blank=True, default= None)
    school_days = models.IntegerField(null=True, blank=True, default= None)
    absences = models.IntegerField(null=True, blank=True, default= None)
    gr_acknowledgement = models.BooleanField(default = False)
    
    #For Nursery Grade Reports
    nursery_evaluation_choices =[
    ('O','O'),
    ('VG', 'VG'),
    ('G', 'G'),
    ('F', 'F'),
    ('N/A', 'N/A'),
    ]
    N_language = models.FloatField(null=True, blank=True, default= None)
    N_reading_readiness = models.FloatField(null=True, blank=True, default= None)
    N_number_readiness = models.FloatField(null=True, blank=True, default= None)
    N_science = models.FloatField(null=True, blank=True, default= None)
    N_interpersonal_skills = models.FloatField(null=True, blank=True, default= None)
    N_motor_skills = models.FloatField(null=True, blank=True, default= None)
    N_creative_domain = models.FloatField(null=True, blank=True, default= None)
    N_good_moral_valueformation = models.FloatField(null=True, blank=True, default= None)
    N_final_language = models.CharField(null=True, max_length=20, blank=True, default= None)
    N_final_reading_readiness = models.CharField(null=True, max_length=20, blank=True, default= None)
    N_final_number_readiness = models.CharField(null=True, max_length=20, blank=True, default= None)
    N_final_science = models.CharField(null=True, max_length=20, blank=True, default= None)
    N_final_interpersonal_skills = models.CharField(null=True, max_length=20, blank=True, default= None)
    N_final_motor_skills = models.CharField(null=True, max_length=20, blank=True, default= None)
    N_final_creative_domain = models.CharField(null=True, max_length=20, blank=True, default= None)
    N_year_average = models.CharField(null=True, max_length=20, blank=True, default= None)
    N_final_good_moral_valueformation = models.CharField(null=True, max_length=20, blank=True, default= None)
    Nlanguage1 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    Nlanguage2 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    Nlanguage3 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    Nlanguage4 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    Nlanguage5 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    Nlanguage6 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    Nlanguage7 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    Nlanguage8 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    Nlanguage9 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    Nlanguage10 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness1 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness2 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness3 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness4 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness5 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness6 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness7 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness8 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness9 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness10 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness11 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness12 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_reading_readiness13 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_number_readiness1 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_number_readiness2 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_number_readiness3 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_number_readiness4 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_number_readiness5 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_number_readiness6 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_number_readiness7 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_number_readiness8 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_science1 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_science2 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_science3 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_science4 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_science5 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_science6 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills1 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills2 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills3 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills4 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills5 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills6 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills7 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills8 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills9 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills10 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills11 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills12 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_interpersonal_skills13 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills1 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills2 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills3 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills4 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills5 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills6 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills7 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills8 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills9 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills10 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills11 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills12 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_motor_skills13 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_creative_domain1 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_creative_domain2 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_creative_domain3 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_creative_domain4 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_creative_domain5 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_good_moral_valueformation1 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_good_moral_valueformation2 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_good_moral_valueformation3 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_good_moral_valueformation4 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_good_moral_valueformation5 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_good_moral_valueformation6 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_good_moral_valueformation7 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_good_moral_valueformation8 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)
    N_good_moral_valueformation9 = models.CharField(null=True, max_length=20, choices=nursery_evaluation_choices, default=None)