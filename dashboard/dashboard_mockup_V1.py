import streamlit as st
import pandas as pd
import random
import csv
import matplotlib.pyplot as plt

tab1,tab2,tab3=st.tabs(["Overview","Analytics","AI Insights"])

#fake sensor
for i in range(10):
    m=random.uniform(1,3) #Current Sensors
    n=random.randint(220,230) #Voltage Sensors
    p=random.randint(30,80) #Temperature Sensors 
    s=random.uniform(0,1) #Vibration Sensors
    z=random.choice(["Healthy", "Warning", "Faulty"]) #Health Status

    if z == "Healthy":
        q = random.randint(90,100)
    elif z == "Warning":
        q = random.randint(65,85)
    else:
        q = random.randint(20,50)

    from datetime import datetime
    et = datetime.now().strftime("%H:%M:%S")
    
    l=[et,m,n,p,s,q,z]
    #writing the data into csv files
    with open("orders.csv",mode="a") as file:
        w=csv.writer(file)
        w.writerow(l)

df=pd.read_csv("orders.csv")

with tab1:
    st.title("THE ANALYTICS DASHBOARD")
    st.header("Overview:")
    with st.container(border=True):
        if df.iloc[:,3].mean()<40 and df.iloc[:,4].mean()<0.3:
            st.write("Health Score:95/100")
            st.write("Healthy")
        elif df.iloc[:,3].mean()>40 and df.iloc[:,3].mean()<50:
            st.write("Health Score:75/100")
            st.write("Warning")
        else:
            st.write("Health Score:40/100")
            st.write("Faulty")
        st.write("Current:",round(df.iloc[:,1].mean()),"A")
        st.write("Voltage:",round(df.iloc[:,2].mean()),"V")
        st.write("Temperature:",round(df.iloc[:,3].mean()),"(C)")
        st.write("Vibration:",df.iloc[:,4].mean(),"g")

with tab2:
    st.title("THE ANALYTICS DASHBOARD")
    st.header("Analytics:")
    col1,col2=st.columns(2)
    
    with col1:
        fig,ax=plt.subplots()
        recent = df.tail(20)
        ax.set_xlabel("Time")
        ax.set_ylabel("Temperature")
        ax.plot(recent["Time"], recent["Temperature(C)"])
        st.pyplot(fig)

        fig2,axx=plt.subplots()
        recent = df.tail(20)
        axx.set_xlabel("Time")
        axx.set_ylabel("Vibration")
        axx.plot(recent["Time"], recent["Vibration(g)"])
        st.pyplot(fig2)

    with col2:
        fig3,ay=plt.subplots()
        ay.set_xlabel("Time")
        ay.set_ylabel("Current")
        ay.plot(recent["Time"], recent["Current(A)"])
        st.pyplot(fig3)

        fig4,ayy=plt.subplots()
        ayy.set_xlabel("Time")
        ayy.set_ylabel("Voltage")
        ayy.plot(recent["Time"], recent["Voltage(V)"])
        st.pyplot(fig4)
with tab3:
    st.title("THE ANALYTICS DASHBOARD")
    with st.expander("Predictions"):
        st.write("Motor Health: Warning")
    with st.expander("Confidence"):
        st.write("92.4%")
    with st.expander("Fault Records"):
        st.write("Total Faults : 3,Last Fault :18 Jul 2026")
    with st.expander("Recommendation"):
        st.write("• Inspect motor bearings.")
        st.write("• Check shaft alignment.")
        st.write("• Monitor vibration over the next 24 hours.")