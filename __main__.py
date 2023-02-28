from faulthandler import disable
import json
from time import time
import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
from github import Github


st.set_page_config(layout="wide")

st.markdown(""" <style> div.stButton > button:first-child {background-color: #7aa19a;margin-left:40%;color:white;font-size:30px;height:3em;width:25%;border-radius:10px 10px10px 10px;}""", unsafe_allow_html=True)
st.markdown("""<style> .big-font { font-size:18px !important; color: red} </style>""", unsafe_allow_html=True)

subjectCode = ['No_Class','BREAK','LUNCH',]
subjectName= ['No_Class','BREAK','LUNCH',]
facultyName = ['No_Class','BREAK','LUNCH',]
days = []
monday = {}
tuesday = {}
wednesday = {}
thursday = {}
friday = {}
saturday = {}
hod_name  = ''

subject_faculty_map = {"lunch":"lunch"}

def subMapping(sec,subjectCode = subjectCode ,subjectName = subjectName,facultyName = facultyName):
  with st.form("subMapping",clear_on_submit= True):
    st.subheader(sec + " Subject Mapping")
    n_rows = 16
    n_cols = 4

    columns = [st.columns(n_cols) for n_row in range(n_rows)]

    columns[0][0].text('Subject Initial')
    columns[0][1].text('Subjecct Name')
    columns[0][2].text('Faculty Name')

    subjectCode.append(columns[1][0].text_input('sub1'))
    subjectCode.append(columns[2][0].text_input('sub2'))
    subjectCode.append(columns[3][0].text_input('sub3'))
    subjectCode.append(columns[4][0].text_input('sub4'))
    subjectCode.append(columns[5][0].text_input('sub5'))
    subjectCode.append(columns[6][0].text_input('sub6'))
    subjectCode.append(columns[7][0].text_input('sub7'))
    subjectCode.append(columns[8][0].text_input('sub8'))
    subjectCode.append(columns[9][0].text_input('sub9'))
    subjectCode.append(columns[10][0].text_input('sub10'))
    subjectCode.append(columns[11][0].text_input('sub11'))
    subjectCode.append(columns[12][0].text_input('sub12'))
    subjectCode.append(columns[13][0].text_input('sub13'))
    subjectCode.append(columns[14][0].text_input('sub14'))
    subjectCode.append(columns[15][0].text_input('sub15'))


    subjectName.append(columns[1][1].text_input('name_sub1'))
    subjectName.append(columns[2][1].text_input('name_sub2'))
    subjectName.append(columns[3][1].text_input('name_sub3'))
    subjectName.append(columns[4][1].text_input('name_sub4'))
    subjectName.append(columns[5][1].text_input('name_sub5'))
    subjectName.append(columns[6][1].text_input('name_sub6'))
    subjectName.append(columns[7][1].text_input('name_sub7'))
    subjectName.append(columns[8][1].text_input('name_sub8'))
    subjectName.append(columns[9][1].text_input('name_sub9'))
    subjectName.append(columns[10][1].text_input('name_sub10'))
    subjectName.append(columns[11][1].text_input('name_sub11'))
    subjectName.append(columns[12][1].text_input('name_sub12'))
    subjectName.append(columns[13][1].text_input('name_sub13'))
    subjectName.append(columns[14][1].text_input('name_sub14'))
    subjectName.append(columns[15][1].text_input('name_sub15'))


    facultyName.append(columns[1][2].text_input('faculty_1'))
    facultyName.append(columns[2][2].text_input('faculty_2'))
    facultyName.append(columns[3][2].text_input('faculty_3'))
    facultyName.append(columns[4][2].text_input('faculty_4'))
    facultyName.append(columns[5][2].text_input('faculty_5'))
    facultyName.append(columns[6][2].text_input('faculty_6'))
    facultyName.append(columns[7][2].text_input('faculty_7'))
    facultyName.append(columns[8][2].text_input('faculty_8'))
    facultyName.append(columns[9][2].text_input('faculty_9'))
    facultyName.append(columns[10][2].text_input('faculty_10'))
    facultyName.append(columns[11][2].text_input('faculty_11'))
    facultyName.append(columns[12][2].text_input('faculty_12'))
    facultyName.append(columns[13][2].text_input('faculty_13'))
    facultyName.append(columns[14][2].text_input('faculty_14'))
    facultyName.append(columns[15][2].text_input('faculty_15'))

    subjectCode = [i for i in subjectCode if i]
    subjectName = [i for i in subjectName if i]
    facultyName = [i for i in facultyName if i]

    global subject_faculty_map
    subject_faculty_map = {subjectCode[i]: [subjectName[i], facultyName[i]] for i in range(len(subjectCode))}
    subject_faculty_map = {"FACULTY": subject_faculty_map}
    
    st.error("!!! Must save before entering time table")
    map_submitted = st.form_submit_button("SAVE")
    if map_submitted:
      st.success('NOW you can enter the time table below:point_down::point_down::point_down:')

def timeTable(page_title,dd):
  # with st.form("Time Table"):
    dd = [i for i in dd if i]
    st.header(page_title + 'Time Table')
    n_rows = 10
    n_cols = 11

    dept_sem_div = str(page_title).split('/')
    columns = [st.columns(n_cols) for n_row in range(n_rows)]

    saturday.update({"08:30":(columns[6][1].selectbox('S1',dd))}) 
    saturday.update({"09:30":(columns[6][2].selectbox('S2',dd))})
    saturday.update({"10:30":(columns[6][3].selectbox('SBREAK',dd))})
    saturday.update({"11:00":(columns[6][4].selectbox('S4',dd))})
    saturday.update({"12:00":(columns[6][5].selectbox('S5',dd))})
    saturday.update({"13:00":(columns[6][6].selectbox('SLUNCH',dd))})
    saturday.update({"13:30":(columns[6][7].selectbox('S7',dd))})
    saturday.update({"14:30":(columns[6][8].selectbox('S8',dd))})
    saturday.update({"15:30":(columns[6][9].selectbox('S9',dd))})
    saturday.update({"16:30":(columns[6][10].selectbox('S10',dd))})

    friday.update({"08:30":(columns[5][1].selectbox('F1',dd))})
    friday.update({"09:30":(columns[5][2].selectbox('F2',dd))})
    friday.update({"10:30":(columns[5][3].selectbox('FBREAK',dd))})
    friday.update({"11:00":(columns[5][4].selectbox('F4',dd))})
    friday.update({"12:00":(columns[5][5].selectbox('F5',dd))})
    friday.update({"13:00":(columns[5][6].selectbox('FLUNCH',dd))})
    friday.update({"13:30":(columns[5][7].selectbox('F7',dd))})
    friday.update({"14:30":(columns[5][8].selectbox('F8',dd))})
    friday.update({"15:30":(columns[5][9].selectbox('F9',dd))})
    friday.update({"16:30":(columns[5][10].selectbox('F10',dd))})

    thursday.update({"08:30":(columns[4][1].selectbox('U1',dd))})
    thursday.update({"09:30":(columns[4][2].selectbox('U2',dd))})
    thursday.update({"10:30":(columns[4][3].selectbox('UBREAK',dd))})
    thursday.update({"11:00":(columns[4][4].selectbox('U4',dd))})
    thursday.update({"12:00":(columns[4][5].selectbox('U5',dd))})
    thursday.update({"13:00":(columns[4][6].selectbox('ULUNCH',dd))})
    thursday.update({"13:30":(columns[4][7].selectbox('U7',dd))})
    thursday.update({"14:30":(columns[4][8].selectbox('U8',dd))})
    thursday.update({"15:30":(columns[4][9].selectbox('U9',dd))})
    thursday.update({"16:30":(columns[4][10].selectbox('U10',dd))})

    wednesday.update({"08:30":(columns[3][1].selectbox('W1',dd))})
    wednesday.update({"09:30":(columns[3][2].selectbox('W2',dd))})
    wednesday.update({"10:30":(columns[3][3].selectbox('WBREAK',dd))})
    wednesday.update({"11:00":(columns[3][4].selectbox('W4',dd))})
    wednesday.update({"12:00":(columns[3][5].selectbox('W5',dd))})
    wednesday.update({"13:00":(columns[3][6].selectbox('WLUNCH',dd))})
    wednesday.update({"13:30":(columns[3][7].selectbox('W7',dd))})
    wednesday.update({"14:30":(columns[3][8].selectbox('W8',dd))})
    wednesday.update({"15:30":(columns[3][9].selectbox('W9',dd))})
    wednesday.update({"16:30":(columns[3][10].selectbox('W10',dd))})

    tuesday.update({"08:30":(columns[2][1].selectbox('T1',dd))})
    tuesday.update({"09:30":(columns[2][2].selectbox('T2',dd))})
    tuesday.update({"10:30":(columns[2][3].selectbox('TBREAK',dd))})
    tuesday.update({"11:00":(columns[2][4].selectbox('T4',dd))})
    tuesday.update({"12:00":(columns[2][5].selectbox('T5',dd))})
    tuesday.update({"13:00":(columns[2][6].selectbox('TLUNCH',dd))})
    tuesday.update({"13:30":(columns[2][7].selectbox('T7',dd))})
    tuesday.update({"14:30":(columns[2][8].selectbox('T8',dd))})
    tuesday.update({"15:30":(columns[2][9].selectbox('T9',dd))})
    tuesday.update({"16:30":(columns[2][10].selectbox('T10',dd))})

    monday.update({"08:30":(columns[1][1].selectbox('M1',dd))})
    monday.update({"09:30":(columns[1][2].selectbox('M2',dd))})
    monday.update({"10:30":(columns[1][3].selectbox('MBREAK',dd))})
    monday.update({"11:00":(columns[1][4].selectbox('M4',dd))})
    monday.update({"12:00":(columns[1][5].selectbox('M5',dd))})
    monday.update({"13:00":(columns[1][6].selectbox('MLUNCH',dd))})
    monday.update({"13:30":(columns[1][7].selectbox('M7',dd))})
    monday.update({"14:30":(columns[1][8].selectbox('M8',dd))})
    monday.update({"15:30":(columns[1][9].selectbox('M9',dd))})
    monday.update({"16:30":(columns[1][10].selectbox('M10',dd))})

    # st.warning("Please fill out so required field")
    columns[0][1].text('8:30-9:30')
    columns[0][2].text('9:30-10:30')
    columns[0][3].text('10:30-11:00')
    columns[0][4].text('11:00-12:00')
    columns[0][5].text('12:00-1:00')
    columns[0][6].text('1:00-1:30')
    columns[0][7].text('1:30-2:30')
    columns[0][8].text('2:30-3:30')
    columns[0][9].text('3:30-4:30')
    columns[0][10].text('4:30-5:30')

    days.append(columns[1][0].text('MON'))
    days.append(columns[2][0].text('TUE'))
    days.append(columns[3][0].text('WED'))
    days.append(columns[4][0].text('THU'))
    days.append(columns[5][0].text('FRI'))
    days.append(columns[6][0].text('SAT'))

    columns[7][0].markdown('<p class="big-font">L.H No.</p>', unsafe_allow_html=True)
    lh = columns[7][1].text_input('LH No.')
    day_map = {"LH":lh,"MON": monday,"TUE": tuesday,"WED": wednesday,"THU": thursday,"FRI": friday,"SAT": saturday,}
    day_map.update(subject_faculty_map)
    # timeTableJson = {dept_sem_div[0] : {dept_sem_div[0] + dept_sem_div[1]+"SEM":{dept_sem_div[0] + dept_sem_div[1]+"SEM"+dept_sem_div[2]:day_map}}}

    st.warning("NOTE: If Subjected is not mapped then it wont be displayed in dropdown")
    # tt_submitted = st.form_submit_button("SUBMIT",disable=False)
    placeholder = st.empty()
    tt_submitted = placeholder.button('SUBMIT',disabled=False,key=1)
    if tt_submitted:
      placeholder.button('SUBMIT',disabled=True,key=2)
      clearAllVariables()
      updateJson(dept_sem_div,day_map)
      uploadTogitHub(dept_sem_div)

def uploadTogitHub(dept_name):
  folder_empl_in_git = 'timeTable.json'
  initial_file = Path(__file__).parent / "timeTable.json"
  git_branch = 'main'

  g = Github('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')
  repo = g.get_repo('ShridharSChini/TimeTableStream')
  all_files = []
  contents = repo.get_contents("")

  while contents:
      file_content = contents.pop(0)
      if file_content.type == "dir":
          contents.extend(repo.get_contents(file_content.path))
      else:
          file = file_content
          all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

  with open(initial_file, 'r') as file:
      content = file.read()

  if folder_empl_in_git in all_files:
      contents = repo.get_contents(folder_empl_in_git)
      repo.update_file(contents.path, "committing for " + dept_name, content, contents.sha, branch=git_branch)
      print(folder_empl_in_git + ' UPDATED FOR ' + dept_name[0]+' SEM '+dept_name[1]+' DIV '+dept_name[2])

def innerOptionMenu(sections):
  selected_tab = option_menu(
              menu_title=None,  # required
              options=sections,  # required
              icons=["house", "cpu", "motherboard","motherboard-fill","laptop","bricks",],  # optional
              menu_icon="cast",  # optional
              default_index=0, orientation="horizontal", # optional
              styles={
                  "container": {"padding": "0", "background-color": "#fafafa"},
                  "icon": {"color": "orange", "font-size": "10px"}, 
                  "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                  "nav-link-selected": {"background-color": "green"},
              }
          )
  return selected_tab

def clearAllVariables():
  subjectCode = ['No_Class','BREAK','LUNCH',]
  subjectName= ['No_Class','BREAK','LUNCH',]
  facultyName = ['No_Class','BREAK','LUNCH',]
  days = []
  monday = {}
  tuesday = {}
  wednesday = {}
  thursday = {}
  friday = {}
  saturday = {}

def updateJson(dept_sem_div,day_map):
  updated = 0
  file_path = Path(__file__).parent / "timeTable.json"
  with file_path.open('r+') as f:
    content = json.load(f)
    for title,depts in content.items():
      if dept_sem_div[0] in depts:
        for dept_names,dept_classes in depts.items():
          if dept_sem_div[0] + dept_sem_div[1]+"SEM" in dept_classes:
            # st.write("inside sem" + dept_sem_div[0]+ dept_sem_div[1]+"SEM")
            prasent = []
            for sem,sem_class in dept_classes.items():
              ss = list(sem_class.keys())  
              prasent = prasent + ss
            if dept_sem_div[0] + dept_sem_div[1]+"SEM"+dept_sem_div[2] in prasent:
              # key = dept_sem_div[0] + dept_sem_div[1]+'SEM'+dept_sem_div[2]
              # # del dept_classes[dept_sem_div[0] + dept_sem_div[1]+"SEM"][key]
              # st.write('UPdating ',dept_classes[dept_sem_div[0] + dept_sem_div[1]+"SEM"][key],'with',day_map)
              # dept_classes[dept_sem_div[0] + dept_sem_div[1]+"SEM"][key] = day_map


              # f.seek(0)
              # json.dump(content,f,indent=4)
              # st.success('Submitted Successfully')
              # updated = 1
              st.error('Sorry you have already updated the this section for modification please contact admin')
              return
            elif updated == 0:
              # st.write('inner1 elif')
              timeTableJson ={dept_sem_div[0] + dept_sem_div[1]+"SEM"+dept_sem_div[2]:day_map}
              dept_classes[dept_sem_div[0] + dept_sem_div[1]+"SEM"].update(timeTableJson)
              f.seek(0)
              json.dump(content,f,indent=4)
              st.success('Submitted Successfully')
              updated = 1
              return
    
    if updated == 0:
      for title,depts in content.items():
        if dept_sem_div[0] in depts:
          # st.write("inside Dept2" + dept_sem_div[0])
          for dept_names,dept_classes in depts.items():
            if dept_sem_div[0] + dept_sem_div[1]+"SEM" in dept_classes:
              break
            elif updated == 0:
              timeTableJson = {dept_sem_div[0] + dept_sem_div[1]+"SEM":{dept_sem_div[0] + dept_sem_div[1]+"SEM"+dept_sem_div[2]:day_map}}
              depts[dept_sem_div[0]].update(timeTableJson)
              f.seek(0)
              json.dump(content,f,indent=4)
              st.success('Submitted Successfully')
              updated = 1
              return

    if updated == 0:
      for title,depts in content.items():
        if dept_sem_div[0] in depts:
          break
        elif updated == 0:
          timeTableJson = {dept_sem_div[0] : {dept_sem_div[0] + dept_sem_div[1]+"SEM":{dept_sem_div[0] + dept_sem_div[1]+"SEM"+dept_sem_div[2]:day_map}}}
          content['DEPT'].update(timeTableJson)
          f.seek(0)
          json.dump(content,f,indent=4)
          st.success('Submitted Successfully')
          updated = 1
          return

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
            st.session_state['user'] = st.session_state["username"]

            # del st.session_state["username"]
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
        # st.write(st.secrets["passwords"])
        return True

if check_password():

  st.write("Welcome ",st.session_state["user"])

  dept = st.session_state["user"]
  dept = dept[-3:]
  dept = dept.upper()
  # st.write(dept.upper())
  selectedDept = dept
  # selectedDept = option_menu(
  #               menu_title=None,  # required
  #               options=["CSE", "First_year", "ECE","EEE", "MCA", "CIV","MEC"],  # required
  #               icons=["cpu", "house", "motherboard","motherboard-fill","laptop","bricks","airplane-fill"],  # optional
  #               menu_icon="cast",  # optional
  #               default_index=0,  # optional
  #               orientation="horizontal",
  #           )
  if (selectedDept == "CSE") | (selectedDept == "ECE") | (selectedDept == "MEC"):
    sections=[selectedDept+"/3/A", selectedDept+"/3/B", selectedDept+"/3/LE", selectedDept+"/5/A",selectedDept+"/5/B", selectedDept+"/7/A", selectedDept+"/7/B",]
    # sections=[selectedDept+"/4/A", selectedDept+"/4/B", selectedDept+"/6/A",selectedDept+"/6/B", selectedDept+"/8/A", selectedDept+"/8/B",]
  elif(selectedDept == "EEE") | (selectedDept == "MCA") | (selectedDept == "CIV"):
    sections=[selectedDept+"/3/A", selectedDept+"/3/LE",selectedDept+"/5/A",selectedDept+"/7/A",]
    # sections=[selectedDept+"/4/A",selectedDept+"/6/A",selectedDept+"/8/A",]

  elif (selectedDept == "First_year"):
    sections=["First_year/C_Cycle/A","First_year/C_Cycle/B","First_year/C_Cycle/C","First_year/P_Cycle/D","First_year/P_Cycle/E","First_year/P_Cycle/F",]

  selected_section = innerOptionMenu(sections)
  subMapping(selected_section +' DIV')
  timeTable(selected_section, subjectCode)
