from turtle import title
import streamlit as st
from datetime import datetime
import json
import re

st.set_page_config(page_icon=":bell:", page_title="KLEIT- TimeTable")

st.markdown("""
<style>
.big-font {
    font-size:25px !important;
    color: blue;
}
</style>
""", unsafe_allow_html=True)

now = datetime.now()
current_time = str(now.strftime("%H:%M") )

days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
day = days[datetime.today().weekday()]

Departments =["All_DEPT", "First Year", "CSE","ECE","EEE", "MCA", "CIV","MEC"]
sem = ['ALL_SEM','3','5','7']
divisions = ['ALL_DIV','A','B']

slots = ["On Going","08:30", "09:30","10:30","11:00","12:00","13:00","13:30","14:30","15:30","16:30","17:30" ]


time_slots = ["08:30", "09:30","10:30","11:00","12:00","13:00","13:30","14:30","15:30","16:30","17:30" ]
for i in range(len(time_slots) - 1):
    if (current_time > time_slots[i] and current_time < time_slots[i+1]):
        current_time = time_slots[i]
# st.write(current_time)
content = {}
with open('C:\\Users\\shrid\\OneDrive\\Documents\\Projects\\TTP\\timeTable.json', 'r') as f:
        content = json.load(f)

def getDeptClasses(deptName = 'All_DEPT',d_sem = 'ALL_SEM',d_div = 'ALL_DIV', getTime = current_time):
    lucHall=''
    sub_code =''
    faculty = ''
    cl_now = ''
    count = 0

    if d_sem != 'ALL_SEM':
        d_sem = deptName+d_sem+'SEM'

    if d_div != 'ALL_DIV':
        d_div = d_sem+d_div

    st.subheader(deptName)
    if getTime < "08:30" or getTime > "17:30":
        st.header("Please come back in college hours ")
        return
    for title,depts in content.items():
        for dept_names,dept_classes in depts.items():
            if dept_names == deptName or deptName == 'All_DEPT':
                for sem,sem_class in dept_classes.items():
                    if ((sem == d_sem) or (d_sem == 'ALL_SEM') or (deptName == 'All_DEPT' and re.search(".*"+d_sem[8:],sem))):
                        # st.write(d_sem)
                        for div,div_class in sem_class.items():
                            if div == d_div or d_div == 'ALL_DIV' or (re.search(".*"+d_div[4:],div) or (deptName == 'All_DEPT' and re.search(".*"+d_div[8:],div))):
                                
                                if(deptName == 'All_DEPT' and d_sem == 'ALL_SEM' and d_div != 'ALL_DIV'):
                                    if re.search(".*"+d_div[4:],div):
                                        faculty = div_class['FACULTY']
                                        lh = div_class['LH']
                                        for d_day,day_map in div_class.items():
                                            # st.write(d_day,day)
                                            if d_day == day:
                                                sub_code = day_map[getTime]
                                                cl_now = faculty[sub_code][0]
                                                faculty = faculty[sub_code][0]
                                                st.write(cl_now)
                                else:
                                    # st.write(div,d_div)
                                    faculty = div_class['FACULTY']
                                    lh = div_class['LH']
                                    for d_day,day_map in div_class.items():
                                        # st.write(d_day,d_div)
                                        if d_day == day:
                                            sub_code = day_map[getTime]
                                            cl_now = faculty[sub_code][0]
                                            faculty = faculty[sub_code][0]
                                            st.write(cl_now)
    return cl_now

def display(msg):
    st.markdown('<p class="big-font">'+msg+'</p>', unsafe_allow_html=True)


def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    if day == 6 :
        st.header('Today is SUNDAY')
    else:
        dept_c, sem_c, div_c, blank1, blank2, slot_c = st.columns(6)
        dept_s = dept_c.selectbox('Department',Departments)
        sem_s = sem_c.selectbox('Semister',sem)
        div_s = div_c.selectbox('Division',divisions)
        slot_s = slot_c.selectbox('Time slots',slots)
        if slot_s == "On Going":
            slot_s = current_time
        # getDeptClasses(dept_s,sem_s,div_s,slot_s)
        # display("CSE/3SEM/A/ADSL1")
