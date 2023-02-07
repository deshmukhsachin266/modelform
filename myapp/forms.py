from django import forms

from .models import TrainerModel

class TrainerForm(forms.ModelForm):
    class Meta:
        model=TrainerModel
        # fields=['empid','name','experience','date_of_join','salary','subject'] 
            # ANOTHER METHOD TO DISPLAY ALL FILEDS
        fields='__all__'
        #exclude=['subject','name']
        widgets={
            'empid':forms.TextInput(attrs={'placeholder':'employee id'}),
            'name':forms.TextInput(attrs={'placeholder':'Trainer name'}),
            'date_of_join':forms.DateInput(attrs={'type':'date'})
        }
    def clean_name(self):
        name=self.cleaned_data['name']
        if not(4<=len(name)<=12):
            raise forms.ValidationError('name should have min 4 and max 12')
        return name