dataset = ['Braund, Mr. Owen Harris',
    'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
    'Heikkinen, Miss. Laina',
    'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
    'Allen, Mr. William Henry',
    'Moran, Mr. James',
    'McCarthy, Mr. Timothy J',
    'Palsson, Master. Gosta Leonard',
    'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
    'Nasser, Mrs. Nicholas (Adele Achem)',
    'Sandstrom, Miss. Marguerite Rut',
    'Bonnell, Miss. Elizabeth',
    'Saundercock, Mr. William Henry',
    'Andersson, Mr. Anders Johan',
    'Vestrom, Miss. Hulda Amanda Adolfina',
    'Hewlett, Mrs. (Mary D Kingcome) ',
    'Rice, Master. Eugene',
    'Williams, Mr. Charles Eugene',
    'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
    'Masselmani, Mrs. Fatima',
    'Fynney, Mr. Joseph J',
    'Beesley, Mr. Lawrence',
    'McGowan, Miss. Anna \"Annie\"',
    'Sloper, Mr. William Thompson',
    'Palsson, Miss. Torborg Danira',
    'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
    'Emir, Mr. Farred Chehab',
    'Fortune, Mr. Charles Alexander',
    'Dwyer, Miss. Ellen \"Nellie\"',
    'Todoroff, Mr. Lalio']

m_count =0
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'M':
            m_count +=1
print(m_count)
