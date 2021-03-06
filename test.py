import ResumeAnalyzer as ra

analyzer = ra.ResumeAnalyzer()

# define the ranking criteria that suits your requirement
# E.g. rank candidates based on Deep Learning, Machine Learning and Time Series skills
search_criteria = {
    
    "Deep Learning": 
  ["neural networks", "cnn", "rnn", "ann", "lstm", "bert", "transformers"],
  
    "Machine Learning": 
  ["regression", "classification", "clustering", "time series", "summarization", "nlp"],
  
    "Time Series":  
  ["arima","sarimax", "prophet", "holt winters"]
  
}

# render in jupyter notebook
analyzer.render(path="E:\\ProjectProd\\newenv\\Resume_Parser\\output", metadata=search_criteria, mode="notebook")

# render in browser
analyzer.render(path="E:\\ProjectProd\\newenv\\Resume_Parser\\output", metadata=search_criteria, mode="browser")