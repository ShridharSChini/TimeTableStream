import streamlit as st
from datetime import datetime
import json
import re
from pathlib import Path

st.set_page_config(page_icon=":bell:", page_title="KLEIT- TimeTable",layout='wide')

# from PIL import Image
# image = Image.open('C:\\Users\\shrid\\OneDrive\\Documents\\Projects\\download.png')
# st.image(image)

st.markdown("""
<style>
.dept {
    font-size:25px !important;
    color: #474342;
    style="white-space: pre-line"
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.sub {
    font-size:25px !important;
    color: #cf320a;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.faculty {
    font-size:25px !important;
    color: #524aed;
    style="white-space: pre-line"
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.by {
    font-size:15px !important;
    color: black;
    style="white-space: pre-line"
}
</style>
""", unsafe_allow_html=True)


now = datetime.now()
current_time = str(now.strftime("%H:%M") )

days = ['Today','MON','TUE','WED','THU','FRI','SAT','SUN']
day = days[datetime.today().weekday() + 1]

Departments =["All_DEPT", "First_year", "CSE","ECE","EEE", "MCA", "CIV","MEC"]
# sem = ['ALL_SEM','3','5','7','C_Cycle','P_Cycle']
sem = ['ALL_SEM','4','6','8','C_Cycle','P_Cycle']
divisions = ['ALL_DIV','A','B','C','D','E','F']

slots = ["On Going","08:30", "09:30","10:30","11:00","12:00","13:00","13:30","14:30","15:30","16:30","17:30" ]


time_slots = ["08:30", "09:30","10:30","11:00","12:00","13:00","13:30","14:30","15:30","16:30","17:30" ]
for i in range(len(time_slots) - 1):
    if (current_time > time_slots[i] and current_time < time_slots[i+1]):
        current_time = time_slots[i]
# st.write(current_time)
content = {}


file_path = Path(__file__).parent / "timeTable.json"
with file_path.open('r') as f:
        content = json.load(f)

def getDeptClasses(deptName = 'All_DEPT',d_sem = 'ALL_SEM',d_div = 'ALL_DIV', getTime = current_time,day_r = day):
    lucHall=''
    sub_code =''
    faculty = ''
    cl_now = ''
    count = 0

    if d_sem != 'ALL_SEM':
        d_sem = deptName+d_sem+'SEM'

    if d_div != 'ALL_DIV':
        d_div = d_sem+d_div

    # st.subheader(deptName)
    if getTime < "08:30" or getTime > "17:30":
        st.header("Please come back in college hours ")
        return
    for title,depts in content.items():
        for dept_names,dept_classes in depts.items():
            if dept_names == deptName or deptName == 'All_DEPT':
                for sem,sem_class in dept_classes.items():
                    if ((sem == d_sem) or (d_sem == 'ALL_SEM') or (deptName == 'All_DEPT' and re.search(".*"+d_sem[8:],sem))):
                        for div,div_class in sem_class.items():
                            if div == d_div or d_div == 'ALL_DIV' or (re.search(".*"+d_div[4:],div) or (deptName == 'All_DEPT' and re.search(".*"+d_div[8:],div))):
                                if(deptName == 'All_DEPT' and d_sem == 'ALL_SEM' and d_div != 'ALL_DIV'):
                                    if re.search(".*"+d_div[4:],div):
                                        faculty = div_class['FACULTY']
                                        lh = div_class['LH']
                                        for d_day,day_map in div_class.items():
                                            if d_day == day_r:
                                                sub_code = day_map[getTime]
                                                cl_now = faculty[sub_code][0]
                                                faculty = faculty[sub_code][0]

                                                sem = sem.replace(dept_names,'')
                                                div = div.replace(dept_names+sem,'')
                                                display = dept_names+'/'+sem+'/'+div+'/'+lh
                                                st.markdown('<span class="dept">'+display+'</span>', unsafe_allow_html=True)
                                                st.markdown('<span class="sub">'+cl_now+'</span>'+'<span class="by">'+".........By:........"+'</span>'+'<span class="faculty">'+faculty+'</span>', unsafe_allow_html=True)
                                            
                                else:
                                    # st.write(div_class)
                                    faculty = div_class['FACULTY']
                                    lh = div_class['LH']
                                    for d_day,day_map in div_class.items():
                                        if d_day == day_r:
                                            sub_code = day_map[getTime]
                                            cl_now = faculty[sub_code][0]
                                            faculty = faculty[sub_code][0]

                                            sem = sem.replace(dept_names,'')
                                            div = div.replace(dept_names+sem,'')
                                            display = dept_names+'/'+sem+'/'+div+'/'+lh
                                            st.markdown('<span class="dept">'+display+'</span>', unsafe_allow_html=True)
                                            st.markdown('<span class="sub">'+cl_now+'</span>'+'<span class="by">'+".........By:........"+'</span>'+'<span class="faculty">'+faculty+'</span>', unsafe_allow_html=True)
                                            # st.markdown('<span class="faculty">'+faculty+'</span>', unsafe_allow_html=True)
                                            # st.write(cl_now)
    return cl_now

if day == 6 :
    st.header('Today is SUNDAY')
else:
    dept_c, sem_c, div_c, blank1, days_c, slot_c = st.columns(6)
    dept_s = dept_c.selectbox('Department',Departments)

    sem_s = sem_c.selectbox('Semister',sem)
    div_s = div_c.selectbox('Division',divisions)
    slot_s = slot_c.selectbox('Time slots',slots)
    days_s = days_c.selectbox('Day',days)
    if days_s == "Today":
        days_s = day
    # st.write(days_s,day)
    if slot_s == "On Going":
        slot_s = current_time
    getDeptClasses(dept_s,sem_s,div_s,slot_s,days_s)
