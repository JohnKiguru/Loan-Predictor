from django.contrib import messages
from django.shortcuts import render, redirect
import numpy as np
import pickle
model = pickle.load(open('loan.pkl', 'rb'))
print(model)

def predict(request):
    """
    This function renders our html page to the browser.
    """
    return render(request, 'predict.html')
def predict_loan(request):
    """
    This function takes the results of filling out the form and use them to predict whether an applicant's loan
    request will be granted or not.
    """
    results = list(request.POST.values())
    print(results)
    newlist = results[1:]
    print(newlist)
    int_features = [int(x) for x in newlist]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    if output == 0:
        messages.error(request, "Sorry... your loan request is declined.")
    elif output == 1:
        messages.info(request, "Congrats!!! Loan approved...")
    return redirect('/')