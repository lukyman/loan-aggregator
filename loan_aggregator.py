def aggregate_by_column(data, column_keys):
    # first item in the list as the column names
    """
    :return list: [[column_key], [aggregate_key, Total, Count]]
    """
    sorted_list = [column_keys]
    for key,group in data.items():
        month = key
        count = len(group)
        total = 0
        for item in group:
            total+=float(item['Amount'])
        row = [month, eval(str(total)), count]
        sorted_list.append(row)
    return sorted_list

def groupby_column(data, column_name, column_filter_method=None):
    """
    :param column_filter_method: a method that you wish to apply to group key i.e :column_name
    :return dict: loan data are grouped and converted to dict with key as :column_name 
    """
    grouped_dict = {}
    for value in data:
        key = None
        if column_filter_method is not None:
            key = column_filter_method(value[column_name])
        else:
             key = value[column_name]
        # add to grouped_dict
        if grouped_dict.get(key) is not None:
            grouped_dict[key].append(value)
        else:
            grouped_dict[key] = [value]
    return grouped_dict
