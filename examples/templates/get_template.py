from sparkpost import SparkPost

sp = SparkPost('YOUR API KEY')
template = sp.templates.get('template_id')
print template