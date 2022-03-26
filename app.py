#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


app =Flask(__name__)


# In[3]:


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST": #this happens after pressing button submit
        purchases = request.form.get("purchases") #add after testing
        suppcard = request.form.get("suppcard") #add after testing
        purchases = float(purchases) #add after testing
        suppcard = float(suppcard) #add after testing
        print(purchases, suppcard) #add after testing
        model1=joblib("CART") #add after testing
        pred1 = model1.predict([[purchases, suppcard]]) #add after testing
        model2=joblib("RF") #add after testing
        pred2 = model2.predict([[purchases, suppcard]]) #add after testing
        model3=joblib("GB") #add after testing
        pred3 = model3.predict([[purchases, suppcard]]) #add after testing
        return(render_template("index.html", result1=pred1, result2=pred2, result3=pred3)) #change from "1" to pred1, pred2, pred3
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2")) #this happens before pressing button submit


# In[ ]:


if __name__=="__main__":
  app.run()


# In[ ]:




