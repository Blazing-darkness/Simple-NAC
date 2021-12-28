from django import forms
from .models import Nas, Radacct, Radcheck, Radgroupcheck, Radgroupreply, Radpostauth, Radreply, Radusergroup
from unittest.util import _MAX_LENGTH

#------------------------------------------------------------------

class NasForm(forms.ModelForm):
    class Meta:
        model = Nas
        fields = '__all__'
        widgets = {'secret' : forms.PasswordInput(),}
        
class NasFormL(forms.Form):
    id = forms.IntegerField()

#------------------------------------------------------------------
          
class RadacctForm(forms.ModelForm):
    class Meta:
        model = Radacct
        fields = '__all__'
        
class RadacctFormL(forms.Form):
    id = forms.IntegerField()

#-------------------------------------------------------------------
            
class RadcheckForm(forms.ModelForm):
    class Meta:
        model = Radcheck
        fields = '__all__'       
        widgets = {'value' : forms.PasswordInput(),}
        
class RadcheckFormL(forms.Form):
    id = forms.IntegerField()
    
#-------------------------------------------------------------------    
        
class RadgroupcheckForm(forms.ModelForm):
    class Meta:
        model = Radgroupcheck
        fields = '__all__'
            
class RadgroupcheckFormL(forms.Form):
    id = forms.IntegerField()            
    
#-------------------------------------------------------------------
    
class RadgroupreplyForm(forms.ModelForm):
    class Meta:
        model = Radgroupreply
        fields = '__all__'

class RadgroupreplyFormL(forms.Form):
    id = forms.IntegerField()

#-------------------------------------------------------------------
        
class RadpostauthForm(forms.ModelForm):
    class Meta:
        model = Radpostauth
        fields = '__all__'
        
class RadpostauthFormL(forms.Form):
    id = forms.IntegerField()
    
#--------------------------------------------------------------------
        
class RadreplyForm(forms.ModelForm):
    class Meta:
        model = Radreply
        fields = '__all__'
        
class RadreplyFormL(forms.Form):
    id = forms.IntegerField()
    
#-------------------------------------------------------------------        
        
class RadusergroupForm(forms.ModelForm):
    class Meta:
        model = Radusergroup
        fields = '__all__'
        
class RadusergroupFormL(forms.Form):
    id = forms.IntegerField()
