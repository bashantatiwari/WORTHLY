from django import forms

COMPANIES = ['Acer','Apple','Asus','Chuwi','Dell','Fujitsu','Google','HP','Huawei','LG','Lenovo','MSI','Mediacom','Microsoft','Razer','Samsung','Toshiba','Vero','Xiaomi']
TYPES = ['2 in 1 Convertible','Gaming','Netbook','Notebook','Ultrabook','Workstation']
CPUS = ['AMD Processor','Intel Core i3','Intel Core i5','Intel Core i7','Other Intel Processor']
GPUS = ['AMD','Intel','Nvidia']
OS_OPTIONS = [('Windows','Windows'),('Mac','macOS / Mac'),('Others/No OS/Linux','Linux / No OS / Other')]

class LaptopPredictionForm(forms.Form):
    Company = forms.ChoiceField(choices=[(x,x) for x in COMPANIES], label='Brand')
    TypeName = forms.ChoiceField(choices=[(x,x) for x in TYPES], label='Laptop type')
    Ram = forms.TypedChoiceField(choices=[(x, f'{x} GB') for x in [2,4,6,8,12,16,24,32,64]], coerce=int, label='RAM')
    Weight = forms.FloatField(min_value=0.5, max_value=8, initial=1.8, label='Weight (kg)')
    screen_size = forms.FloatField(min_value=8, max_value=25, initial=15.6, label='Screen size (inches)')
    resolution_width = forms.IntegerField(min_value=800, max_value=7680, initial=1920, label='Resolution width')
    resolution_height = forms.IntegerField(min_value=600, max_value=4320, initial=1080, label='Resolution height')
    Touchscreen = forms.TypedChoiceField(choices=[(0,'No'),(1,'Yes')], coerce=int, label='Touchscreen')
    Ips = forms.TypedChoiceField(choices=[(0,'No'),(1,'Yes')], coerce=int, label='IPS display')
    HDD = forms.TypedChoiceField(choices=[(x, f'{x} GB') for x in [0,128,256,500,512,1000,2000]], coerce=int, label='HDD storage')
    SSD = forms.TypedChoiceField(choices=[(x, f'{x} GB') for x in [0,8,16,32,64,128,180,240,256,512,1000,2000]], coerce=int, label='SSD storage')
    cpu_brand = forms.ChoiceField(choices=[(x,x) for x in CPUS], label='Processor family')
    gpu_brand = forms.ChoiceField(choices=[(x,x) for x in GPUS], label='Graphics brand')
    os = forms.ChoiceField(choices=OS_OPTIONS, label='Operating system')
