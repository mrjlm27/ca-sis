from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import *


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('header','announcement')
        labels = {
            'header':'Header',
            'announcement':'Announcement Caption/Spiel'
        }
        widgets = {
            'header':forms.TextInput(attrs={'class': 'form-control'}),
            'announcement':forms.Textarea(attrs={'name':'body', 'rows':'10', 'cols':'45'})
        }
class StudentForm(forms.ModelForm):
    student_schoolyear_start:forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
    class Meta:
        model=Student
        fields = ('student_schoolyear_start', 'student_grade_level', 'student_birthday', 
        'student_lastname', 'student_firstname',
        'student_middlename', 'student_nickname',
        'student_address','student_religion', 
        'student_nationality','student_hobbies','student_likes',
        'student_dislikes', 'student_shm','student_allergies',
        'student_sd','student_oconsiderations','student_guardianemail',
        'student_f_firstname','student_f_lastname','student_f_middlename',
        'student_f_telno','student_f_address',
        'student_f_occupation','student_f_employer','student_f_oaddress',
        'student_f_otelno','student_f_natureofbusiness',
        'student_m_firstname','student_m_lastname','student_m_middlename',
        'student_m_telno','student_m_address','student_m_occupation',
        'student_m_occupation','student_m_employer','student_m_oaddress',
        'student_m_otelno','student_m_natureofbusiness',
        'student_sibling_name','student_sibling_gender','student_sibling_age','student_sibling_school',
        'student_medexp','student_rules','student_accuracy',
        'student_signedname','student_signdate', 'student_enrollment_plan'
        )
        labels = {
            'student_firstname': 'First Name',
            'student_lastname': 'Last Name',
            'student_middlename':'Middle Name',
            'student_nickname':'Nickname',
            'student_schoolyear_start':'School Year',
            'student_grade_level':'Grade Level',
            'student_birthday':'Birthday',
            'student_address':'Home Address',
            'student_religion':'Religion',
            'student_nationality':'Nationality',
            'student_hobbies':'Hobbies',
            'student_likes': 'Likes',
            'student_dislikes':'Dislikes',
            'student_shm': 'Special Health Medication',
            'student_allergies':'Allergies',
            'student_sd':'Special Diet',
            'student_oconsiderations':'Anything else that the school should know',
            'student_guardianemail':'''Guardian's Email Address''',
            'student_f_firstname': ''' Father's First Name''',
            'student_f_lastname': '''Father's Last Name''',
            'student_f_middlename':'''Father's Middle Name''',
            'student_f_telno':'''Father's Telephone Number''',
            'student_f_address':'''Father's Home Address''',
            'student_f_occupation':'''Father's Occupation''',
            'student_f_employer':'''Father's Employer''',
            'student_f_oaddress':'''Father's Office Address''',
            'student_f_otelno':'''Father's Office Telephone Number''',
            'student_f_natureofbusiness':'''Father's Nature of Business''',
            'student_m_firstname': ''' Mother's First Name''',
            'student_m_lastname': '''Mother's Last Name''',
            'student_m_middlename':'''Mother's Middle Name''',
            'student_m_telno':'''Mother's Telephone Number''',
            'student_m_address':'''Mother's Home Address''',
            'student_m_occupation':'''Mother's Occupation''',
            'student_m_employer':'''Mother's Employer''',
            'student_m_oaddress':'''Mother's Office Address''',
            'student_m_otelno':'''Mother's Office Telephone Number''',
            'student_m_natureofbusiness':'''Mother's Nature of Business''',
            'student_sibling_name': '''Sibling's Full Name''',
            'student_sibling_gender':'''Sibling's Gender''',
            'student_sibling_age':'''Sibling's Age''',
            'student_sibling_school':'''Sibling's School''',
            'student_medexp':'I hereby authorize Camelean Academy to obtain emergency medical/dental care or emergency evluation for my child at my expense',
            'student_rules':'I hereby been informed of the rules and regulations of Camelean Academy policies as well as it’s primary functions and obligations and I hereby agree to abide by them.The school reserves the right to terminate any enrollee due to bad behavior as well as parents who do not meet school requirements and have unharmonious relationship with school employees',
            'student_accuracy':'I hereby declare that all the information stated above are accurate and complete',
            'student_signedname':'Name',
            'student_signdate':'Date Today',
            'student_enrollment_plan':'Enrollment Plan'
        }

        required = {
            'student_likes': False,
            'student_sibling_age': False,
            'student_sibling_name': False,
            'student_sibling_gender': False,
            'student_sibling_school': False,
            'student_religion': False,
            'student_oconsiderations': False,
            'student_f_natureofbusiness': False,
            'student_m_natureofbusiness': False,
            'student_m_otelno': False,
            'student_f_otelno': False, 
        }

        widgets = {
            'student_schoolyear_start': forms.Select(attrs={'class': 'form-control', 'background-color': 'red'}),
            'student_grade_level': forms.Select(attrs={'class': 'form-control'}),
            'student_birthday': forms.SelectDateWidget(attrs={'class': 'form-control'}),

            'student_firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_lastname': forms.TextInput( attrs={'class': 'form-control'}),

            'student_middlename': forms.TextInput(attrs={'class': 'form-control'}),
            'student_nickname': forms.TextInput( attrs={'class': 'form-control'}),

            'student_address': forms.TextInput(attrs={'class': 'form-control'}),

            'student_religion': forms.TextInput(attrs={'class': 'form-control'}),
            'student_nationality': forms.TextInput( attrs={'class': 'form-control'}),

            'student_hobbies': forms.TextInput(attrs={'class': 'form-control'}),

            'student_likes': forms.TextInput(attrs={'class': 'form-control','required':False}),
            'student_dislikes': forms.TextInput( attrs={'class': 'form-control'}),

            'student_shm': forms.TextInput(attrs={'class': 'form-control'}),
            'student_allergies': forms.TextInput(attrs={'class': 'form-control'}),
            'student_sd': forms.TextInput(attrs={'class': 'form-control'}),
            'student_oconsiderations': forms.TextInput(attrs={'class': 'form-control'}),
            'student_hobbies': forms.TextInput(attrs={'class': 'form-control'}),
            'student_guardianemail': forms.TextInput(attrs={'class': 'form-control'}),

            'student_f_firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_middlename': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_telno': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_address': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_employer': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_oaddress': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_otelno': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_natureofbusiness': forms.TextInput(attrs={'class': 'form-control'}),

            'student_m_firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_middlename': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_telno': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_address': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_employer': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_oaddress': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_otelno': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_natureofbusiness': forms.TextInput(attrs={'class': 'form-control'}),

            'student_sibling_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_sibling_gender': forms.TextInput(attrs={'class': 'form-control'}),
            'student_sibling_age': forms.TextInput(attrs={'class': 'form-control'}),
            'student_sibling_school': forms.TextInput(attrs={'class': 'form-control'}),

            'student_medexp': forms.CheckboxInput,
            'student_rules': forms.CheckboxInput,
            'student_accuracy': forms.CheckboxInput,

            'student_signedname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_signdate': forms.DateInput(attrs={'class': 'form-control'}),
            'student_enrollment_plan': forms.Select(attrs={'class': 'form-control'}),
            

            # 'student_grade_level': forms.TextInput(attrs={'class': 'form-control'}),
            # 'special_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        def __init__(self,*args,**kwargs):
            super(StudentForm,self).__init__(*args, **kwargs)
            self.fields['student_religion'].required=False
            self.fields['student_middlename'].required=False
            self.fields['student_likes'].required=False
            self.fields['student_shm'].required=False
            self.fields['student_dislikes'].required=False
            self.fields['student_allergies'].required=False
            self.fields['student_sd'].required=False
            self.fields['student_oconsiderations'].required=False
            self.fields['student_f_middlename'].required=False
            self.fields['student_f_otelno'].required=False
            self.fields['student_m_middlename'].required=False
            self.fields['student_m_otelno'].required=False
            self.fields['student_m_otelno'].required=False
            self.fields['student_sibling_name'].required=False
            self.fields['student_sibling_gender'].required=False
            self.fields['student_sibling_age'].required=False
            self.fields['student_sibling_school'].required=False

class StudentFormDisabled(forms.ModelForm):
    student_schoolyear_start:forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
    class Meta:
        model=Student
        fields = ('student_birthday', 
        'student_address','student_religion', 
        'student_nationality','student_hobbies','student_likes',
        'student_dislikes', 'student_shm','student_allergies',
        'student_sd','student_oconsiderations','student_guardianemail',
        'student_f_firstname','student_f_lastname','student_f_middlename',
        'student_f_telno','student_f_address',
        'student_f_occupation','student_f_employer','student_f_oaddress',
        'student_f_otelno','student_f_natureofbusiness',
        'student_m_firstname','student_m_lastname','student_m_middlename',
        'student_m_telno','student_m_address','student_m_occupation',
        'student_m_occupation','student_m_employer','student_m_oaddress',
        'student_m_otelno','student_m_natureofbusiness',
        'student_sibling_name','student_sibling_gender','student_sibling_age','student_sibling_school',
        'student_medexp','student_rules','student_accuracy',
        'student_signedname','student_signdate', 'student_enrollment_plan'
        )
        labels = {
            'student_birthday':'Birthday',
            'student_address':'Home Address',
            'student_religion':'Religion',
            'student_nationality':'Nationality',
            'student_hobbies':'Hobbies',
            'student_likes': 'Likes',
            'student_dislikes':'Dislikes',
            'student_shm': 'Special Health Medication',
            'student_allergies':'Allergies',
            'student_sd':'Special Diet',
            'student_oconsiderations':'Anything else that the school should know',
            'student_guardianemail':'''Guardian's Email Address''',
            'student_f_firstname': ''' Father's First Name''',
            'student_f_lastname': '''Father's Last Name''',
            'student_f_middlename':'''Father's Middle Name''',
            'student_f_telno':'''Father's Telephone Number''',
            'student_f_address':'''Father's Home Address''',
            'student_f_occupation':'''Father's Occupation''',
            'student_f_employer':'''Father's Employer''',
            'student_f_oaddress':'''Father's Office Address''',
            'student_f_otelno':'''Father's Office Telephone Number''',
            'student_f_natureofbusiness':'''Father's Nature of Business''',
            'student_m_firstname': ''' Mother's First Name''',
            'student_m_lastname': '''Mother's Last Name''',
            'student_m_middlename':'''Mother's Middle Name''',
            'student_m_telno':'''Mother's Telephone Number''',
            'student_m_address':'''Mother's Home Address''',
            'student_m_occupation':'''Mother's Occupation''',
            'student_m_employer':'''Mother's Employer''',
            'student_m_oaddress':'''Mother's Office Address''',
            'student_m_otelno':'''Mother's Office Telephone Number''',
            'student_m_natureofbusiness':'''Mother's Nature of Business''',
            'student_sibling_name': '''Sibling's Full Name''',
            'student_sibling_gender':'''Sibling's Gender''',
            'student_sibling_age':'''Sibling's Age''',
            'student_sibling_school':'''Sibling's School''',
            'student_medexp':'I hereby authorize Camelean Academy to obtain emergency medical/dental care or emergency evluation for my child at my expense',
            'student_rules':'I hereby been informed of the rules and regulations of Camelean Academy policies as well as it’s primary functions and obligations and I hereby agree to abide by them.The school reserves the right to terminate any enrollee due to bad behavior as well as parents who do not meet school requirements and have unharmonious relationship with school employees',
            'student_accuracy':'I hereby declare that all the information stated above are accurate and complete',
            'student_signedname':'Name',
            'student_signdate':'Date Today',
            'student_enrollment_plan':'Enrollment Plan'
        }

        required = {
            'student_likes': False,
            'student_sibling_age': False,
            'student_sibling_name': False,
            'student_sibling_gender': False,
            'student_sibling_school': False,
            'student_religion': False,
            'student_oconsiderations': False,
            'student_f_natureofbusiness': False,
            'student_m_natureofbusiness': False,
            'student_m_otelno': False,
            'student_f_otelno': False, 
        }

        widgets = {
            'student_birthday': forms.SelectDateWidget(attrs={'class': 'form-control'}),

            'student_address': forms.TextInput(attrs={'class': 'form-control'}),

            'student_religion': forms.TextInput(attrs={'class': 'form-control'}),
            'student_nationality': forms.TextInput( attrs={'class': 'form-control'}),

            'student_hobbies': forms.TextInput(attrs={'class': 'form-control'}),

            'student_likes': forms.TextInput(attrs={'class': 'form-control','required':False}),
            'student_dislikes': forms.TextInput( attrs={'class': 'form-control'}),

            'student_shm': forms.TextInput(attrs={'class': 'form-control'}),
            'student_allergies': forms.TextInput(attrs={'class': 'form-control'}),
            'student_sd': forms.TextInput(attrs={'class': 'form-control'}),
            'student_oconsiderations': forms.TextInput(attrs={'class': 'form-control'}),
            'student_hobbies': forms.TextInput(attrs={'class': 'form-control'}),
            'student_guardianemail': forms.TextInput(attrs={'class': 'form-control'}),

            'student_f_firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_middlename': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_telno': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_address': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_employer': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_oaddress': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_otelno': forms.TextInput(attrs={'class': 'form-control'}),
            'student_f_natureofbusiness': forms.TextInput(attrs={'class': 'form-control'}),

            'student_m_firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_middlename': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_telno': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_address': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_employer': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_oaddress': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_otelno': forms.TextInput(attrs={'class': 'form-control'}),
            'student_m_natureofbusiness': forms.TextInput(attrs={'class': 'form-control'}),

            'student_sibling_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_sibling_gender': forms.TextInput(attrs={'class': 'form-control'}),
            'student_sibling_age': forms.TextInput(attrs={'class': 'form-control'}),
            'student_sibling_school': forms.TextInput(attrs={'class': 'form-control'}),

            'student_medexp': forms.CheckboxInput,
            'student_rules': forms.CheckboxInput,
            'student_accuracy': forms.CheckboxInput,

            'student_signedname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_signdate': forms.DateInput(attrs={'class': 'form-control'}),
            'student_enrollment_plan': forms.Select(attrs={'class': 'form-control'}),
            

            # 'student_grade_level': forms.TextInput(attrs={'class': 'form-control'}),
            # 'special_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        def __init__(self,*args,**kwargs):
            super(StudentFormDisabled,self).__init__(*args, **kwargs)
            # self.fields['student_schoolyear_start'].disabled = True
            # self.fields['student_grade_level'].disabled = True
            self.fields['student_religion'].required=False
            self.fields['student_middlename'].required=False
            self.fields['student_likes'].required=False
            self.fields['student_shm'].required=False
            self.fields['student_dislikes'].required=False
            self.fields['student_allergies'].required=False
            self.fields['student_sd'].required=False
            self.fields['student_oconsiderations'].required=False
            self.fields['student_f_middlename'].required=False
            self.fields['student_f_otelno'].required=False
            self.fields['student_m_middlename'].required=False
            self.fields['student_m_otelno'].required=False
            self.fields['student_m_otelno'].required=False
            self.fields['student_sibling_name'].required=False
            self.fields['student_sibling_gender'].required=False
            self.fields['student_sibling_age'].required=False
            self.fields['student_sibling_school'].required=False

 

class LogInForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username','password')
        labels = {
            'username': 'Username',
            'password': 'Password',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }

# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model=Payment
#         fields = ('payment_s_account_id','paymentdate_date','payment_amount')
#         labels = {
#             'payment_s_account_id': 'Select Student',
#             'paymentdate_date': 'Date of Payment',
#             'payment_amount': 'Amount of Payment',
#         }

#         widgets = {
#             'paymentdate_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
#             'payment_amount': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

YEAR_CHOICES= [tuple([x,x]) for x in range(2022,2035)]
gradelevel_choices = [
        ('Nursery','Nursery'),
        ('Kinder 1', 'Kinder 1'),
        ('Kinder 2 Junior', 'Kinder 2 Junior'), 
        ('Kinder 2 Senior', 'Kinder 2 Senior'),
    ]

class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields = ('paymentdate_date','payment_amount',)
        labels = {
            # 'payment_s_account_id': 'Input Student ID',
            'paymentdate_date': 'Date of Payment',
            'payment_amount': 'Amount of Payment',
            # 'school_year_end': 'End of School Year',
        }
        widgets = {
            # 'payment_s_account_id': forms.Select(attrs={'class': 'form-control'}),
            'paymentdate_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'payment_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'school_year_end': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        # error_messages = {
        #     'payment_amount': {
        #         'invalid': _("Student ID does not exist"),
        #     },
        # }
    # def __init__(self, *args, **kwargs):
    #     super(PaymentForm, self).__init__(*args, **kwargs)
    #     self.fields['payment_s_account_id'].widget = forms.TextInput()

class GradeReportForm(forms.ModelForm):
    class Meta:
        model=GradeReport
        fields = ('school_year','grading_period','readingreadiness1', 'readingreadiness2', 'readingreadiness3', 'readingreadiness4', 'readingreadiness5', 'readingreadiness6', 'readingreadiness7',
        'readingreadiness8', 'readingreadiness9', 'readingreadiness10', 'readingreadiness11', 'readingreadiness12', 'readingreadiness13',
        'science1','science2','science3' ,'science4','science5','science6', 'language1', 'language2', 'language3', 'language4', 'language5', 'language6',
        'language7', 'language8', 'language9', 'language10', 'math1', 'math2', 'math3', 'math4', 'math5', 'math6', 'math7', 'math8', 'math9', 'math10', 'math11',
        'penmanship1', 'penmanship2', 'penmanship3', 'penmanship4', 'filipino1', 'filipino2', 'filipino3', 'filipino4', 'school_days', 'absences')
        labels = {
            'school_year':'School Year',
            'grading_period':'Grading Period',
            'readingreadiness1': 'Identifies basic colors and shapes',
            'readingreadiness2': 'Identifies his/her name in a list',
            'readingreadiness3': 'Identifies and names letters of the alphabet',
            'readingreadiness4': 'Identifies and reproduces letter sounds',
            'readingreadiness5': 'Reads with correct pronounciation of sight words',
            'readingreadiness6': 'Reads phrases and sentences using familiar words',
            'readingreadiness7': 'Reads short stories',
            'readingreadiness8': 'Follows one-step direction and instruction',
            'readingreadiness9': 'Relates and remembers details of pictures, events, or stories',
            'readingreadiness10': 'Arranges 2 to 4 pictures of related events in correct sequence',
            'readingreadiness11': 'Completes a logic sequence',
            'readingreadiness12': 'Draws conclusion and predicts outcome',
            'readingreadiness13': 'Grasps the main idea of a picture or of a selection',
            'science1': "Knows how to take care of one's body",
            'science2': "Knows how to take care of one's environment",
            'science3': 'Classifies animals according to their habitat (Land, water, at home, and on leaves)',
            'science4': 'Classifies animals according to their body covering, color, size, number of legs, and movements',
            'science5': 'Classifies objects according to their color, size, shape (solid, liquid, gas) and texture',
            'science6': 'Identifies different weather conditions',
            'language1': 'Has an adequate English speaking vocabulary at his/her level',
            'language2': 'Pronounces CVC words and sight words correctly and clearly',
            'language3': 'Speaks in complete thought patterns',
            'language4': 'Communicates ideas orally',
            'language5': 'Observes correct phrasing and intonation patterns',
            'language6': 'Uses appropriate English expressions and correct grammar in familiar situations',
            'language7': 'Writes CVC words and sight words',
            'language8': 'Converses with ease on particular topics',
            'language9': 'Recites days of the week',
            'language10': 'Recites months of the year in order',
            'math1': 'Knows the concept of sequencing numbers (before, between, after) 0-20, 21-50, 51-100',
            'math2': 'Compares and orders objects according to size, height, length, quantity, etc.',
            'math3': 'Identifies/draws set of familiar objects',
            'math4': 'Identifies/recognizes/writes numeral consisting 0-50 elements/51-100 elements',
            'math5': 'Identifies the ordinal position of objects from first to fifth/sixth to tenth',
            'math6': 'Solves addition wtih 1-digit equations (ex. 9+3 = 12)',
            'math7': 'Solves subtraction with 1-digit equations',
            'math8': 'Solves 2-digit equations',
            'math9': 'Chooses the correct equation (+ or -) for a given situation',
            'math10': 'Writes the correct equation (+ or -) for a given situation',
            'math11': 'Solves simple word problems (+ or -)',
            'penmanship1': 'Follows direciton paths (tracing down broken lines with proper strokes)',
            'penmanship2': "Traces one's name",
            'penmanship3': "Writes one's name",
            'penmanship4': 'Writes words (1st)/ phrases(2nd)/ sentences(3rd) properly',
            'filipino1': 'Pagkilala/Pagsulat ng malaki/maliit na letra ng alpabeto',
            'filipino2': 'Nakakabasa ng salita at maikling kwento',
            'filipino3': 'Pagbuo/Pagsulat ng pantig at salita',
            'filipino4': 'Magkasingkahulugan at Magkasalungat',
            'school_days': 'Number of School Days',
            'absences': 'Number of Absences',
        }

        widgets = {
            'school_year':forms.Select(attrs={'class': 'form-control'}),
            'readingreadiness1': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness2': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness3': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness4': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness5': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness6': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness7': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness8': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness9': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness10': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness11': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness12': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness13': forms.NumberInput(attrs={'class': 'form-control'}),
            'science1': forms.NumberInput(attrs={'class': 'form-control'}),
            'science2': forms.NumberInput(attrs={'class': 'form-control'}),
            'science3': forms.NumberInput(attrs={'class': 'form-control'}),
            'science4': forms.NumberInput(attrs={'class': 'form-control'}),
            'science5': forms.NumberInput(attrs={'class': 'form-control'}),
            'science6': forms.NumberInput(attrs={'class': 'form-control'}),
            'language1': forms.NumberInput(attrs={'class': 'form-control'}),
            'language2': forms.NumberInput(attrs={'class': 'form-control'}),
            'language3': forms.NumberInput(attrs={'class': 'form-control'}),
            'language4': forms.NumberInput(attrs={'class': 'form-control'}),
            'language5': forms.NumberInput(attrs={'class': 'form-control'}),
            'language6': forms.NumberInput(attrs={'class': 'form-control'}),
            'language7': forms.NumberInput(attrs={'class': 'form-control'}),
            'language8': forms.NumberInput(attrs={'class': 'form-control'}),
            'language9': forms.NumberInput(attrs={'class': 'form-control'}),
            'language10': forms.NumberInput(attrs={'class': 'form-control'}),
            'math1': forms.NumberInput(attrs={'class': 'form-control'}),
            'math2': forms.NumberInput(attrs={'class': 'form-control'}),
            'math3': forms.NumberInput(attrs={'class': 'form-control'}),
            'math4': forms.NumberInput(attrs={'class': 'form-control'}),
            'math5': forms.NumberInput(attrs={'class': 'form-control'}),
            'math6': forms.NumberInput(attrs={'class': 'form-control'}),
            'math7': forms.NumberInput(attrs={'class': 'form-control'}),
            'math8': forms.NumberInput(attrs={'class': 'form-control'}),
            'math9': forms.NumberInput(attrs={'class': 'form-control'}),
            'math10': forms.NumberInput(attrs={'class': 'form-control'}),
            'math11': forms.NumberInput(attrs={'class': 'form-control'}),
            'penmanship1': forms.NumberInput(attrs={'class': 'form-control'}),
            'penmanship2': forms.NumberInput(attrs={'class': 'form-control'}),
            'penmanship3': forms.NumberInput(attrs={'class': 'form-control'}),
            'penmanship4': forms.NumberInput(attrs={'class': 'form-control'}),
            'filipino1': forms.NumberInput(attrs={'class': 'form-control'}),
            'filipino2': forms.NumberInput(attrs={'class': 'form-control'}),
            'filipino3': forms.NumberInput(attrs={'class': 'form-control'}),
            'filipino4': forms.NumberInput(attrs={'class': 'form-control'}),
            'school_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'absences': forms.NumberInput(attrs={'class': 'form-control'}),
            'gr_acknowledgement': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
        }

class GradeReportFormK2SR(forms.ModelForm):
    class Meta:
        model=GradeReport
        fields = ('school_year','grading_period','readingreadiness1', 'readingreadiness2', 'readingreadiness3', 'readingreadiness4', 'readingreadiness5', 'readingreadiness6', 'readingreadiness7',
        'readingreadiness8', 'readingreadiness9', 'readingreadiness10', 'readingreadiness11', 'readingreadiness12', 'readingreadiness13',
        'science1','science2','science3' ,'science4','science5','science6', 'language1', 'language2', 'language3', 'language4', 'language5', 'language6',
        'language7', 'language8', 'language9', 'language10', 'math1', 'math2', 'math3', 'math4', 'math5', 'math6', 'math7', 'math8', 'math9', 'math10', 'math11',
        'penmanship1', 'penmanship2', 'penmanship3', 'penmanship4', 'filipino1', 'filipino2', 'filipino3', 'filipino4', 'school_days', 'absences')
        labels = {
            'school_year':'School Year',
            'grading_period':'Grading Period',
            # 'gradelevel':'Grade Level',
            'readingreadiness1': 'Identifies basic colors and shapes',
            'readingreadiness2': 'Identifies his/her name in a list',
            'readingreadiness3': 'Identifies and names letters of the alphabet',
            'readingreadiness4': 'Identifies and reproduces letter sounds',
            'readingreadiness5': 'Reads with correct pronounciation of sight words',
            'readingreadiness6': 'Reads phrases and sentences using familiar words',
            'readingreadiness7': 'Reads short stories',
            'readingreadiness8': 'Follows one-step direction and instruction',
            'readingreadiness9': 'Relates and remembers details of pictures, events, or stories',
            'readingreadiness10': 'Arranges 2 to 4 pictures of related events in correct sequence',
            'readingreadiness11': 'Completes a logic sequence',
            'readingreadiness12': 'Draws conclusion and predicts outcome',
            'readingreadiness13': 'Grasps the main idea of a picture or of a selection',
            'science1': "Knows how to take care of one's body",
            'science2': "Knows how to take care of one's environment",
            'science3': 'Classifies animals according to their habitat (Land, water, at home, and on leaves)',
            'science4': 'Classifies animals according to their body covering, color, size, number of legs, and movements',
            'science5': 'Classifies objects according to their color, size, shape (solid, liquid, gas) and texture',
            'science6': 'Identifies different weather conditions',
            'language1': 'Has an adequate English speaking vocabulary at his/her level',
            'language2': 'Pronounces CVC words and sight words correctly and clearly',
            'language3': 'Speaks in complete thought patterns',
            'language4': 'Communicates ideas orally',
            'language5': 'Observes correct phrasing and intonation patterns',
            'language6': 'Uses appropriate English expressions and correct grammar in familiar situations',
            'language7': 'Writes CVC words and sight words',
            'language8': 'Converses with ease on particular topics',
            'language9': 'Recites days of the week',
            'language10': 'Recites months of the year in order',
            'math1': 'Knows the concept of sequencing numbers (before, between, after) 0-20, 21-50, 51-100',
            'math2': 'Compares and orders objects according to size, height, length, quantity, etc.',
            'math3': 'Identifies/draws set of familiar objects',
            'math4': 'Identifies/recognizes/writes numeral consisting 0-50 elements/51-100 elements',
            'math5': 'Identifies the ordinal position of objects from first to fifth/sixth to tenth',
            'math6': 'Solves addition wtih 1-digit equations (ex. 9+3 = 12)',
            'math7': 'Solves subtraction with 1-digit equations',
            'math8': 'Solves 2-digit equations',
            'math9': 'Chooses the correct equation (+ or -) for a given situation',
            'math10': 'Writes the correct equation (+ or -) for a given situation',
            'math11': 'Solves simple word problems (+ or -)',
            'penmanship1': 'Follows direciton paths (tracing down broken lines with proper strokes)',
            'penmanship2': "Traces one's name",
            'penmanship3': "Writes one's name",
            'penmanship4': 'Writes words (1st)/ phrases(2nd)/ sentences(3rd) properly',
            'filipino1': 'Pagkilala/Pagsulat ng malaki/maliit na letra ng alpabeto',
            'filipino2': 'Nakakabasa ng salita at maikling kwento',
            'filipino3': 'Pagbuo/Pagsulat ng pantig at salita',
            'filipino4': 'Magkasingkahulugan at Magkasalungat',
            'school_days': 'Number of School Days',
            'absences': 'Number of Absences',
        }

        widgets = {
            'school_year':forms.Select(attrs={'class': 'form-control'}),
            'readingreadiness1': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness2': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness3': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness4': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness5': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness6': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness7': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness8': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness9': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness10': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness11': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness12': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness13': forms.NumberInput(attrs={'class': 'form-control'}),
            'science1': forms.NumberInput(attrs={'class': 'form-control'}),
            'science2': forms.NumberInput(attrs={'class': 'form-control'}),
            'science3': forms.NumberInput(attrs={'class': 'form-control'}),
            'science4': forms.NumberInput(attrs={'class': 'form-control'}),
            'science5': forms.NumberInput(attrs={'class': 'form-control'}),
            'science6': forms.NumberInput(attrs={'class': 'form-control'}),
            'language1': forms.NumberInput(attrs={'class': 'form-control'}),
            'language2': forms.NumberInput(attrs={'class': 'form-control'}),
            'language3': forms.NumberInput(attrs={'class': 'form-control'}),
            'language4': forms.NumberInput(attrs={'class': 'form-control'}),
            'language5': forms.NumberInput(attrs={'class': 'form-control'}),
            'language6': forms.NumberInput(attrs={'class': 'form-control'}),
            'language7': forms.NumberInput(attrs={'class': 'form-control'}),
            'language8': forms.NumberInput(attrs={'class': 'form-control'}),
            'language9': forms.NumberInput(attrs={'class': 'form-control'}),
            'language10': forms.NumberInput(attrs={'class': 'form-control'}),
            'math1': forms.NumberInput(attrs={'class': 'form-control'}),
            'math2': forms.NumberInput(attrs={'class': 'form-control'}),
            'math3': forms.NumberInput(attrs={'class': 'form-control'}),
            'math4': forms.NumberInput(attrs={'class': 'form-control'}),
            'math5': forms.NumberInput(attrs={'class': 'form-control'}),
            'math6': forms.NumberInput(attrs={'class': 'form-control'}),
            'math7': forms.NumberInput(attrs={'class': 'form-control'}),
            'math8': forms.NumberInput(attrs={'class': 'form-control'}),
            'math9': forms.NumberInput(attrs={'class': 'form-control'}),
            'math10': forms.NumberInput(attrs={'class': 'form-control'}),
            'math11': forms.NumberInput(attrs={'class': 'form-control'}),
            'penmanship1': forms.NumberInput(attrs={'class': 'form-control'}),
            'penmanship2': forms.NumberInput(attrs={'class': 'form-control'}),
            'penmanship3': forms.NumberInput(attrs={'class': 'form-control'}),
            'penmanship4': forms.NumberInput(attrs={'class': 'form-control'}),
            'filipino1': forms.NumberInput(attrs={'class': 'form-control'}),
            'filipino2': forms.NumberInput(attrs={'class': 'form-control'}),
            'filipino3': forms.NumberInput(attrs={'class': 'form-control'}),
            'filipino4': forms.NumberInput(attrs={'class': 'form-control'}),
            'school_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'absences': forms.NumberInput(attrs={'class': 'form-control'}),
            'grading_period': forms.Select(attrs={'class': 'form-control'}),
        }

class GradeReportFormK1K2JR(forms.ModelForm):
    class Meta:
        model=GradeReport
        fields = ('school_year','grading_period', 'readingreadiness1', 'readingreadiness2', 'readingreadiness3', 'readingreadiness4', 'readingreadiness5', 'readingreadiness6', 'readingreadiness7',
        'readingreadiness8', 'readingreadiness9', 'readingreadiness10', 'readingreadiness11', 'readingreadiness12', 'readingreadiness13',
        'science1','science2','science3' ,'science4','science5','science6', 'language1', 'language2', 'language3', 'language4', 'language5', 'language6',
        'language7', 'language8', 'language9', 'language10', 'math1', 'math2', 'math3', 'math4', 'math5', 'math6', 'math7', 'math8', 'math9', 'math10', 'math11',
        'penmanship1', 'penmanship2', 'penmanship3', 'penmanship4', 'school_days', 'absences')
        labels = {
            'school_year':'School Year',
            'grading_period':'Grading Period',
            # 'gradelevel':'Grade Level',
            'readingreadiness1': 'Identifies basic colors and shapes',
            'readingreadiness2': 'Identifies his/her name in a list',
            'readingreadiness3': 'Identifies and names letters of the alphabet',
            'readingreadiness4': 'Identifies and reproduces letter sounds',
            'readingreadiness5': 'Reads with correct pronounciation of sight words',
            'readingreadiness6': 'Reads phrases and sentences using familiar words',
            'readingreadiness7': 'Reads short stories',
            'readingreadiness8': 'Follows one-step direction and instruction',
            'readingreadiness9': 'Relates and remembers details of pictures, events, or stories',
            'readingreadiness10': 'Arranges 2 to 4 pictures of related events in correct sequence',
            'readingreadiness11': 'Completes a logic sequence',
            'readingreadiness12': 'Draws conclusion and predicts outcome',
            'readingreadiness13': 'Grasps the main idea of a picture or of a selection',
            'science1': "Knows how to take care of one's body",
            'science2': "Knows how to take care of one's environment",
            'science3': 'Classifies animals according to their habitat (Land, water, at home, and on leaves)',
            'science4': 'Classifies animals according to their body covering, color, size, number of legs, and movements',
            'science5': 'Classifies objects according to their color, size, shape (solid, liquid, gas) and texture',
            'science6': 'Identifies different weather conditions',
            'language1': 'Has an adequate English speaking vocabulary at his/her level',
            'language2': 'Pronounces CVC words and sight words correctly and clearly',
            'language3': 'Speaks in complete thought patterns',
            'language4': 'Communicates ideas orally',
            'language5': 'Observes correct phrasing and intonation patterns',
            'language6': 'Uses appropriate English expressions and correct grammar in familiar situations',
            'language7': 'Writes CVC words and sight words',
            'language8': 'Converses with ease on particular topics',
            'language9': 'Recites days of the week',
            'language10': 'Recites months of the year in order',
            'math1': 'Knows the concept of sequencing numbers (before, between, after) 0-20, 21-50, 51-100',
            'math2': 'Compares and orders objects according to size, height, length, quantity, etc.',
            'math3': 'Identifies/draws set of familiar objects',
            'math4': 'Identifies/recognizes/writes numeral consisting 0-50 elements/51-100 elements',
            'math5': 'Identifies the ordinal position of objects from first to fifth/sixth to tenth',
            'math6': 'Solves addition wtih 1-digit equations (ex. 9+3 = 12)',
            'math7': 'Solves subtraction with 1-digit equations',
            'math8': 'Solves 2-digit equations',
            'math9': 'Chooses the correct equation (+ or -) for a given situation',
            'math10': 'Writes the correct equation (+ or -) for a given situation',
            'math11': 'Solves simple word problems (+ or -)',
            'penmanship1': 'Follows direciton paths (tracing down broken lines with proper strokes)',
            'penmanship2': "Traces one's name",
            'penmanship3': "Writes one's name",
            'penmanship4': 'Writes words (1st)/ phrases(2nd)/ sentences(3rd) properly',
            'school_days': 'Number of School Days',
            'absences': 'Number of Absences',
        }

        widgets = {
            'school_year':forms.Select(attrs={'class': 'form-control'}),
            'readingreadiness1': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness2': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness3': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness4': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness5': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness6': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness7': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness8': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness9': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness10': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness11': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness12': forms.NumberInput(attrs={'class': 'form-control'}),
            'readingreadiness13': forms.NumberInput(attrs={'class': 'form-control'}),
            'science1': forms.NumberInput(attrs={'class': 'form-control'}),
            'science2': forms.NumberInput(attrs={'class': 'form-control'}),
            'science3': forms.NumberInput(attrs={'class': 'form-control'}),
            'science4': forms.NumberInput(attrs={'class': 'form-control'}),
            'science5': forms.NumberInput(attrs={'class': 'form-control'}),
            'science6': forms.NumberInput(attrs={'class': 'form-control'}),
            'language1': forms.NumberInput(attrs={'class': 'form-control'}),
            'language2': forms.NumberInput(attrs={'class': 'form-control'}),
            'language3': forms.NumberInput(attrs={'class': 'form-control'}),
            'language4': forms.NumberInput(attrs={'class': 'form-control'}),
            'language5': forms.NumberInput(attrs={'class': 'form-control'}),
            'language6': forms.NumberInput(attrs={'class': 'form-control'}),
            'language7': forms.NumberInput(attrs={'class': 'form-control'}),
            'language8': forms.NumberInput(attrs={'class': 'form-control'}),
            'language9': forms.NumberInput(attrs={'class': 'form-control'}),
            'language10': forms.NumberInput(attrs={'class': 'form-control'}),
            'math1': forms.NumberInput(attrs={'class': 'form-control'}),
            'math2': forms.NumberInput(attrs={'class': 'form-control'}),
            'math3': forms.NumberInput(attrs={'class': 'form-control'}),
            'math4': forms.NumberInput(attrs={'class': 'form-control'}),
            'math5': forms.NumberInput(attrs={'class': 'form-control'}),
            'math6': forms.NumberInput(attrs={'class': 'form-control'}),
            'math7': forms.NumberInput(attrs={'class': 'form-control'}),
            'math8': forms.NumberInput(attrs={'class': 'form-control'}),
            'math9': forms.NumberInput(attrs={'class': 'form-control'}),
            'math10': forms.NumberInput(attrs={'class': 'form-control'}),
            'math11': forms.NumberInput(attrs={'class': 'form-control'}),
            'penmanship1': forms.NumberInput(attrs={'class': 'form-control'}),
            'penmanship2': forms.NumberInput(attrs={'class': 'form-control'}),
            'penmanship3': forms.NumberInput(attrs={'class': 'form-control'}),
            'penmanship4': forms.NumberInput(attrs={'class': 'form-control'}),
            'school_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'absences': forms.NumberInput(attrs={'class': 'form-control'}),
            'grading_period': forms.Select(attrs={'class': 'form-control'}),
        }

class GradeReportFormN(forms.ModelForm):
    class Meta:
        model=GradeReport
        fields = ('school_year','grading_period', 'Nlanguage1', 'Nlanguage2', 'Nlanguage3', 'Nlanguage4', 'Nlanguage5', 'Nlanguage6', 'Nlanguage7', 'Nlanguage8', 
        'Nlanguage9', 'Nlanguage10', 'N_reading_readiness1', 'N_reading_readiness2', 'N_reading_readiness3', 'N_reading_readiness4', 'N_reading_readiness5', 
        'N_reading_readiness6', 'N_reading_readiness7', 'N_reading_readiness8', 'N_reading_readiness9', 'N_reading_readiness10', 'N_reading_readiness11', 
        'N_reading_readiness12', 'N_reading_readiness13', 'N_number_readiness1', 'N_number_readiness2', 'N_number_readiness3', 'N_number_readiness4', 
        'N_number_readiness5', 'N_number_readiness6', 'N_number_readiness7', 'N_number_readiness8', 'N_science1', 'N_science2', 'N_science3', 
        'N_science4', 'N_science5', 'N_science6', 'N_interpersonal_skills1', 'N_interpersonal_skills2', 'N_interpersonal_skills3', 'N_interpersonal_skills4', 
        'N_interpersonal_skills5', 'N_interpersonal_skills6', 'N_interpersonal_skills7', 'N_interpersonal_skills8', 'N_interpersonal_skills9', 'N_interpersonal_skills10',
        'N_interpersonal_skills11', 'N_interpersonal_skills12', 'N_interpersonal_skills13', 'N_motor_skills1', 'N_motor_skills2', 'N_motor_skills3', 'N_motor_skills4', 
        'N_motor_skills5', 'N_motor_skills6', 'N_motor_skills7', 'N_motor_skills8', 'N_motor_skills9', 'N_motor_skills10', 'N_motor_skills11', 'N_motor_skills12', 
        'N_motor_skills13', 'N_creative_domain1', 'N_creative_domain2', 'N_creative_domain3', 'N_creative_domain4', 'N_creative_domain5', 'N_good_moral_valueformation1', 
        'N_good_moral_valueformation2', 'N_good_moral_valueformation3', 'N_good_moral_valueformation4', 'N_good_moral_valueformation5', 'N_good_moral_valueformation6', 
        'N_good_moral_valueformation7', 'N_good_moral_valueformation8', 'N_good_moral_valueformation9', 'school_days', 'absences')
        
        labels = {
            'school_year':'School Year',
            'grading_period':'Grading Period',
            # 'gradelevel': 'Grade Level',
            'Nlanguage1': 'CAN GIVE FIRST/LAST NAME',
            'Nlanguage2': 'HAS CLEAR PRONOUNCIATION',
            'Nlanguage3': 'SPEAKS IN SENTENCES',
            'Nlanguage4': 'EXPRESSES IDEAS VERBALLY',
            'Nlanguage5': 'RECITES (confident in front of a group)',
            'Nlanguage6': 'REPEATS PARTS OF SONGS, RHYMES AND FINGER PLAYS',
            'Nlanguage7': 'FOLLOWS SIMPLE DIRECTIONS',
            'Nlanguage8': 'NAMES CONCRETE OBJECTS IN ENVIRONMENT AND ON PICTURES',
            'Nlanguage9': 'CAN IDENTIFY CORRECT USAGE OF PRONOUNS (HE, SHE, IT, THEY AND WE)',
            'Nlanguage10': 'FOLLOWS SIMPLE RULES IN A GAME',
            'N_reading_readiness1': 'CAN IDENTIFY PICTURES',
            'N_reading_readiness2': 'SHOWS INTEREST IN STORIES',
            'N_reading_readiness3': 'CAN RECOGNIZE / NAME LETTERS',
            'N_reading_readiness4': 'DISTINGUISHES SOUNDS OF LETTERS',
            'N_reading_readiness5': 'TELLS A STORY ABOUT SIMPLE PICTURES',
            'N_reading_readiness6': 'HAS SUFFICIENT VOCABULARY WORDS',
            'N_reading_readiness7': 'CAN WRITE LETTERS',
            'N_reading_readiness8': 'CAN BLEND CV, VC, CVC',
            'N_reading_readiness9': 'CAN FOLLOW INSTRUCTION',
            'N_reading_readiness10': 'CAN READ A PHRASE',
            'N_reading_readiness11': 'CAN READ SIMPLE SENTENCES',
            'N_reading_readiness12': 'DISTINGUISHES INITIAL AND FINAL SOUND OF LETTER',
            'N_reading_readiness13': 'CAN IDENTIFY 5 VOWELS (long and short)',
            'N_number_readiness1': 'CAN RECOGNIZE / NAME BASIC SHAPES',
            'N_number_readiness2': 'CAN RECOGNIZE AND NAME BASIC COLORS',
            'N_number_readiness3': 'SORT OBJECTS INTO 2 TO 3 GIVEN CATEGORIES (color, shape, size)',
            'N_number_readiness4': 'UNDERSTANDS big/small; tall/short; long/short, etc.',
            'N_number_readiness5': 'ROTECOUNTS',
            'N_number_readiness6': 'CAN COUNT ACTUAL OBJECTS',
            'N_number_readiness7': 'CAN RECOGNIZE NUMBERS',
            'N_number_readiness8': 'CAN WRITE NUMBERS 1-10/11-20/20-50/50-100',
            'N_science1': 'CAN NAME BODY PARTS',
            'N_science2': 'CAN IDENTIFY THE 5 SENSES',
            'N_science3': 'CAN IDENTIFY DIFFERENT ANIMALS (farm, zoo and domestic)',
            'N_science4': 'CAN DIFFERENTIATE LIVING FROM NON-LIVING THINGS',
            'N_science5': "KNOWS HOW TO TAKE CARE OF ONE'S BODY",
            'N_science6': 'CAN IDENTIFY DIFFERENT WEATHER CONDITIONS',
            'N_interpersonal_skills1': 'IS CONSCIENTIOUS AND INDUSTRIOUS',
            'N_interpersonal_skills2': 'IS ATTENTIVE',
            'N_interpersonal_skills3': 'IS NEAT AND CLEAN',
            'N_interpersonal_skills4': 'FINISHES ASSIGNED WORK',
            'N_interpersonal_skills5': 'TAKES CARE OF MATERIALS AFTER USE',
            'N_interpersonal_skills6': 'TAKES CARE OF BELONGINGS AND THOSE OF OTHERS',
            'N_interpersonal_skills7': 'SELF RELIANT IN TOILETING AND WASHING',
            'N_interpersonal_skills8': 'FOLLOWS SIMPLE DIRECTIONS',
            'N_interpersonal_skills9': 'SHARES AND WAITS FOR HIS/HER TURN',
            'N_interpersonal_skills10': 'PLAYS COOPERATIVELY',
            'N_interpersonal_skills11': 'WORKS INDEPENDENTLY',
            'N_interpersonal_skills12': 'ASSERTS SELF',
            'N_interpersonal_skills13': 'IS FRIENDLY',
            'N_motor_skills1': 'CAN CATCH AND ROLL THE BALL',
            'N_motor_skills2': 'CAN JUMP',
            'N_motor_skills3': 'CAN CLIMB THE SLIDE',
            'N_motor_skills4': 'CAN DO BUNNY HOP',
            'N_motor_skills5': 'CAN RUN',
            'N_motor_skills6': 'CAN DO LOG ROLL',
            'N_motor_skills7': 'CAN MANIPULATE THE CLAY',
            'N_motor_skills8': 'CAN HANDLE WRITING/DRAWING MATERIALS PROPERLY',
            'N_motor_skills9': 'CAN COLOR PICTURES WITHIN THE LINE',
            'N_motor_skills10': 'CAN TRACE LINES/PICTURES',
            'N_motor_skills11': 'CAN STRING BEADS',
            'N_motor_skills12': 'CAN APPLY GLUE ON PAPER',
            'N_motor_skills13': 'HANDLES SCISSORS CORRECTLY',
            'N_creative_domain1': 'SINGS WITH THE GROUP',
            'N_creative_domain2': 'RESPONDS TO RHYTHM',
            'N_creative_domain3': 'ENJOYS LISTENING TO VARIOUS FORMS OF MUSIC',
            'N_creative_domain4': 'SHOWS INTEREST IN IMAGINATIVE PLAY / DRAMATIZATION',
            'N_creative_domain5': 'EXPRESSES IDEAS THROUGH THE USE OF ART IN DIFFERENT MEDIA',
            'N_good_moral_valueformation1': 'RESPECTS RIGHTS AND FEELINGS OF OTHERS',
            'N_good_moral_valueformation2': 'KIND AND HELPFUL',
            'N_good_moral_valueformation3': 'SHARES WITH OTHERS',
            'N_good_moral_valueformation4': 'ACCEPTS CORRECTION IN GOOD SPIRIT',
            'N_good_moral_valueformation5': 'SHOWS EMOTIONAL CONTROL',
            'N_good_moral_valueformation6': 'EXHIBITS COURTEOUS HABITS',
            'N_good_moral_valueformation7': 'BEHAVES PROPERLY DURING PRAYER TIME',
            'N_good_moral_valueformation8': 'BEGINS TO UNDERSTAND ABOUT GOD',
            'N_good_moral_valueformation9': 'IS POLITE',
            'school_days': 'Number of School Days',
            'absences': 'Number of Absences',
        }

        widgets = {
            'school_year':forms.Select(attrs={'class': 'form-control'}),
            'Nlanguage1': forms.Select(attrs={'class': 'form-control'}),
            'Nlanguage2': forms.Select(attrs={'class': 'form-control'}),
            'Nlanguage3': forms.Select(attrs={'class': 'form-control'}),
            'Nlanguage4': forms.Select(attrs={'class': 'form-control'}),
            'Nlanguage5': forms.Select(attrs={'class': 'form-control'}),
            'Nlanguage6': forms.Select(attrs={'class': 'form-control'}),
            'Nlanguage7': forms.Select(attrs={'class': 'form-control'}),
            'Nlanguage8': forms.Select(attrs={'class': 'form-control'}),
            'Nlanguage9': forms.Select(attrs={'class': 'form-control'}),
            'Nlanguage10': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness1': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness2': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness3': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness4': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness5': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness6': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness7': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness8': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness9': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness10': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness11': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness12': forms.Select(attrs={'class': 'form-control'}),
            'N_reading_readiness13': forms.Select(attrs={'class': 'form-control'}),
            'N_number_readiness1': forms.Select(attrs={'class': 'form-control'}),
            'N_number_readiness2': forms.Select(attrs={'class': 'form-control'}),
            'N_number_readiness3': forms.Select(attrs={'class': 'form-control'}),
            'N_number_readiness4': forms.Select(attrs={'class': 'form-control'}),
            'N_number_readiness5': forms.Select(attrs={'class': 'form-control'}),
            'N_number_readiness6': forms.Select(attrs={'class': 'form-control'}),
            'N_number_readiness7': forms.Select(attrs={'class': 'form-control'}),
            'N_number_readiness8': forms.Select(attrs={'class': 'form-control'}),
            'N_science1': forms.Select(attrs={'class': 'form-control'}),
            'N_science2': forms.Select(attrs={'class': 'form-control'}),
            'N_science3': forms.Select(attrs={'class': 'form-control'}),
            'N_science4': forms.Select(attrs={'class': 'form-control'}),
            'N_science5': forms.Select(attrs={'class': 'form-control'}),
            'N_science6': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills1': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills2': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills3': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills4': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills5': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills6': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills7': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills8': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills9': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills10': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills11': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills12': forms.Select(attrs={'class': 'form-control'}),
            'N_interpersonal_skills13': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills1': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills2': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills3': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills4': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills5': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills6': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills7': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills8': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills9': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills10': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills11': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills12': forms.Select(attrs={'class': 'form-control'}),
            'N_motor_skills13': forms.Select(attrs={'class': 'form-control'}),
            'N_creative_domain1': forms.Select(attrs={'class': 'form-control'}),
            'N_creative_domain2': forms.Select(attrs={'class': 'form-control'}),
            'N_creative_domain3': forms.Select(attrs={'class': 'form-control'}),
            'N_creative_domain4': forms.Select(attrs={'class': 'form-control'}),
            'N_creative_domain5': forms.Select(attrs={'class': 'form-control'}),
            'N_good_moral_valueformation1': forms.Select(attrs={'class': 'form-control'}),
            'N_good_moral_valueformation2': forms.Select(attrs={'class': 'form-control'}),
            'N_good_moral_valueformation3': forms.Select(attrs={'class': 'form-control'}),
            'N_good_moral_valueformation4': forms.Select(attrs={'class': 'form-control'}),
            'N_good_moral_valueformation5': forms.Select(attrs={'class': 'form-control'}),
            'N_good_moral_valueformation6': forms.Select(attrs={'class': 'form-control'}),
            'N_good_moral_valueformation7': forms.Select(attrs={'class': 'form-control'}),
            'N_good_moral_valueformation8': forms.Select(attrs={'class': 'form-control'}),
            'N_good_moral_valueformation9': forms.Select(attrs={'class': 'form-control'}),
            'school_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'absences': forms.NumberInput(attrs={'class': 'form-control'}),
            'grading_period': forms.Select(attrs={'class': 'form-control'}),
        }


class AcknowledgementForm(forms.ModelForm):
    class Meta:
        model=GradeReport
        fields =  ('gr_acknowledgement',)

        widgets = {'gr_acknowledgement': forms.CheckboxInput(attrs={'class': 'form-control','required':True}),}

        labels = {'gr_acknowledgement': "Please click on the box to acknowledge that you have seen the student's report card",
        }

        def __init__(self,*args,**kwargs):
            super(AcknowledgementForm,self).__init__(*args, **kwargs)
            self.fields['gr_acknowledgement'].required=True