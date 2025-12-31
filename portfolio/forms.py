from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(
    max_length=50,
    widget=forms.TextInput(attrs={
      'class': 'contact-input',
      'placeholder' : 'Your Name'
    })
      
  )
        
  email = forms.EmailField(
    max_length=50,
    widget=forms.EmailInput(attrs={
      'class' : 'contact-input',
      'placeholder' : 'Your Email'
    })
      
  )
    
  message = forms.CharField(
    widget=forms.Textarea(attrs={
      'class' : 'contact-textarea',
      'placeholder' : 'Your Message',
      'rows' : 5
    })
    
    )
      

  