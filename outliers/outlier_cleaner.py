#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    ### your code goes here
    test_list = list()
    for idx in list(range(len(predictions))):
        test_list.append((ages[idx], net_worths[idx], abs(predictions[idx] - net_worths[idx])))
    
    sorted_list = sorted(test_list, key=lambda x:x[2])

    selected_num = int(len(predictions) * 0.1)
    end_idx = len(predictions) - selected_num
    cleaned_data = sorted_list[0:end_idx]
    return cleaned_data

