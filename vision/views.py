from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import LaptopPredictionForm
from .services import predict_price

@login_required
def predictor(request):
    result = None
    ppi = None
    form = LaptopPredictionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        result, ppi = predict_price(form.cleaned_data)
    return render(request, 'vision/predictor.html', {'form': form, 'result': result, 'ppi': ppi})
