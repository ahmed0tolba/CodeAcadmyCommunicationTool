# task 1 is beginer python
# task 2 is advanced oracle
# task 3 is intermediate display

from dotenv import load_dotenv
from flask import Flask, make_response, url_for, redirect, request, render_template, current_app, g, send_file, send_from_directory
import requests
from werkzeug.utils import secure_filename
import os
import openai
from datetime import datetime
import urllib.parse
import xlsxwriter
from werkzeug.wrappers import response
from io import BytesIO
from zipfile import ZipFile
import zipfile
from glob import glob
import pandas as pd
from uuid import uuid4
import time
# from html.parser import HTMLParser


application = Flask(__name__)

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


@application.route('/', methods=['GET'])
def index():
    # print("home server side")
    
    return render_template('index.html')

excels_folder = "excels/"

live = False  # to save trials
live = True  # 

prompt = '''write code Using the HR scheme in oracle live sql to 
1. declare job_sal record type that has two fields, job_title of the same type as jobs.job_title and avg_sal of the same type as employees.salary
2. declare a nested table type job_sal_tbl_type where the elements are of the record type job_sal
3. declare a nested table job_sal_tbl of type job_sal_tbl_type
4. Write a sql query to retrieve the JOB TITLE and average SALARY from the tables JOBS and
EMPLOYEES by calculating the average salary of all employees under (grouped) one job
title.
5. Store the result in job_sal_tbl using the BULK COLLECT INTO
6. declare an associative array type job_sal_assoc where the key is job title and the value is
average salary
7. declare an associative array job_avg_sal of the type job_sal_assoc
8. loop through the nested table and store the elements in the associative array
9. loop through the associative array to print each job title with the average salary.
10. use RPAD function to make your output clean and tidy.'''



# \n what is wrong with it ? does it check if A >0 and if B>0? don't provide corrected code


def Evaluate_IP(id):
    if id == None:
        return "-2"
    if len(id) < 1:
        return "-1"
    return 0

@application.route('/mark', methods=['GET'])
def mark():
    prof_id = request.args.get('prof_id')

    column_names = ["Student ID" , "Question 1 answer" , "Question 2 answer" , "Question 3 answer","ChatGPT questions", "ChatGPT questions count",
        "Question 1 period", "Question 2 period","Question 3 period",
        "Question 1 Mark Prof 1 Functional correctness","Question 1 Mark Prof 1 Efficiency","Question 1 Mark Prof 1 Readability","Question 1 Mark Prof 1 Maintainability",
        "Question 2 Mark Prof 1 Functional correctness","Question 2 Mark Prof 1 Efficiency","Question 2 Mark Prof 1 Readability","Question 2 Mark Prof 1 Maintainability",
        "Question 3 Mark Prof 1 Functional correctness","Question 3 Mark Prof 1 Efficiency","Question 3 Mark Prof 1 Readability","Question 3 Mark Prof 1 Maintainability",
        "Question 1 Mark Prof 2 Functional correctness","Question 1 Mark Prof 2 Efficiency","Question 1 Mark Prof 2 Readability","Question 1 Mark Prof 2 Maintainability",
        "Question 2 Mark Prof 2 Functional correctness","Question 2 Mark Prof 2 Efficiency","Question 2 Mark Prof 2 Readability","Question 2 Mark Prof 2 Maintainability",
        "Question 3 Mark Prof 2 Functional correctness","Question 3 Mark Prof 2 Efficiency","Question 3 Mark Prof 2 Readability","Question 3 Mark Prof 2 Maintainability",
        "Question 1 Mark Prof 3 Functional correctness","Question 1 Mark Prof 3 Efficiency","Question 1 Mark Prof 3 Readability","Question 1 Mark Prof 3 Maintainability",
        "Question 2 Mark Prof 3 Functional correctness","Question 2 Mark Prof 3 Efficiency","Question 2 Mark Prof 3 Readability","Question 2 Mark Prof 3 Maintainability",
        "Question 3 Mark Prof 3 Functional correctness","Question 3 Mark Prof 3 Efficiency","Question 3 Mark Prof 3 Readability","Question 3 Mark Prof 3 Maintainability",
        "Prof 1 Comment","Prof 2 Comment","Prof 3 Comment"
        
    ]

    Total_excel_files_count = 0
    
    directory = 'static/excels'
                    
    df_results = pd.DataFrame(columns = column_names)
    df_summary_row_index=0
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        if filename[0] != "_":
            full_path = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(full_path):
                Total_excel_files_count += 1
                # print(full_path)
                df = pd.read_excel(full_path, index_col=0,sheet_name='1')  
                Student_ID = ""
                Question_1_answer = ""
                Question_2_answer = ""
                Question_3_answer = ""
                ChatGPT_questions_count = 0
                Question_1_period = ""
                Question_2_period = ""
                Question_3_period = ""
                ChatGPT_questions=""
                Question_1_Mark_Prof_1_F=0
                Question_1_Mark_Prof_1_E=0
                Question_1_Mark_Prof_1_R=0
                Question_1_Mark_Prof_1_M=0
                Question_2_Mark_Prof_1_F=0
                Question_2_Mark_Prof_1_E=0
                Question_2_Mark_Prof_1_R=0
                Question_2_Mark_Prof_1_M=0
                Question_3_Mark_Prof_1_F=0
                Question_3_Mark_Prof_1_E=0
                Question_3_Mark_Prof_1_R=0
                Question_3_Mark_Prof_1_M=0
                Question_1_Mark_Prof_2_F=0
                Question_1_Mark_Prof_2_E=0
                Question_1_Mark_Prof_2_R=0
                Question_1_Mark_Prof_2_M=0
                Question_2_Mark_Prof_2_F=0
                Question_2_Mark_Prof_2_E=0
                Question_2_Mark_Prof_2_R=0
                Question_2_Mark_Prof_2_M=0
                Question_3_Mark_Prof_2_F=0
                Question_3_Mark_Prof_2_E=0
                Question_3_Mark_Prof_2_R=0
                Question_3_Mark_Prof_2_M=0
                Question_1_Mark_Prof_3_F=0
                Question_1_Mark_Prof_3_E=0
                Question_1_Mark_Prof_3_R=0
                Question_1_Mark_Prof_3_M=0
                Question_2_Mark_Prof_3_F=0
                Question_2_Mark_Prof_3_E=0
                Question_2_Mark_Prof_3_R=0
                Question_2_Mark_Prof_3_M=0
                Question_3_Mark_Prof_3_F=0
                Question_3_Mark_Prof_3_E=0
                Question_3_Mark_Prof_3_R=0
                Question_3_Mark_Prof_3_M=0
                Prof_1_Comment = ""
                Prof_2_Comment = ""
                Prof_3_Comment = ""
                
                for  row,index in df.iterrows():
                    if row == "Student ID" or row == "Student ID: ":
                        Student_ID = index[0]
                    if row == "answer 1":                        
                        Question_1_answer = index[0]
                    if row == "answer 2":                        
                        Question_2_answer = index[0]
                    if row == "answer 3":                        
                        Question_3_answer = index[0]
                    if row == "duration 1":                        
                        Question_1_period = round(index[0],2)
                    if row == "duration 2":                        
                        Question_2_period = index[0]
                    if row == "duration 3":                        
                        Question_3_period = index[0]                       
                    
                    if row == "request":
                        ChatGPT_questions_count += 1

                    if row == "request" or row == "respond":
                        ChatGPT_questions = ChatGPT_questions + str(index[0]) + "<br>" + "<br>"
                    if row == "respond":
                        ChatGPT_questions = ChatGPT_questions + "<br>"
                    if row == "Question 1 Mark Prof 1 Functional correctness":                        
                        Question_1_Mark_Prof_1_F = index[0]
                    if row == "Question 1 Mark Prof 1 Efficiency":                        
                        Question_1_Mark_Prof_1_E = index[0]
                    if row == "Question 1 Mark Prof 1 Readability":                        
                        Question_1_Mark_Prof_1_R = index[0]
                    if row == "Question 1 Mark Prof 1 Maintainability":                        
                        Question_1_Mark_Prof_1_M = index[0]
                        
                    if row == "Question 2 Mark Prof 1 Functional correctness":                        
                        Question_2_Mark_Prof_1_F = index[0]
                    if row == "Question 2 Mark Prof 1 Efficiency":                        
                        Question_2_Mark_Prof_1_E = index[0]
                    if row == "Question 2 Mark Prof 1 Readability":                        
                        Question_2_Mark_Prof_1_R = index[0]
                    if row == "Question 2 Mark Prof 1 Maintainability":                        
                        Question_2_Mark_Prof_1_M = index[0]

                    if row == "Question 3 Mark Prof 1 Functional correctness":                        
                        Question_3_Mark_Prof_1_F = index[0]
                    if row == "Question 3 Mark Prof 1 Efficiency":                        
                        Question_3_Mark_Prof_1_E = index[0]
                    if row == "Question 3 Mark Prof 1 Readability":                        
                        Question_3_Mark_Prof_1_R = index[0]
                    if row == "Question 3 Mark Prof 1 Maintainability":                        
                        Question_3_Mark_Prof_1_M = index[0]

                    if row == "Question 1 Mark Prof 2 Functional correctness":                        
                        Question_1_Mark_Prof_2_F = index[0]
                    if row == "Question 1 Mark Prof 2 Efficiency":                        
                        Question_1_Mark_Prof_2_E = index[0]
                    if row == "Question 1 Mark Prof 2 Readability":                        
                        Question_1_Mark_Prof_2_R = index[0]
                    if row == "Question 1 Mark Prof 2 Maintainability":                        
                        Question_1_Mark_Prof_2_M = index[0]
                        
                    if row == "Question 2 Mark Prof 2 Functional correctness":                        
                        Question_2_Mark_Prof_2_F = index[0]
                    if row == "Question 2 Mark Prof 2 Efficiency":                        
                        Question_2_Mark_Prof_2_E = index[0]
                    if row == "Question 2 Mark Prof 2 Readability":                        
                        Question_2_Mark_Prof_2_R = index[0]
                    if row == "Question 2 Mark Prof 2 Maintainability":                        
                        Question_2_Mark_Prof_2_M = index[0]

                    if row == "Question 3 Mark Prof 2 Functional correctness":                        
                        Question_3_Mark_Prof_2_F = index[0]
                    if row == "Question 3 Mark Prof 2 Efficiency":                        
                        Question_3_Mark_Prof_2_E = index[0]
                    if row == "Question 3 Mark Prof 2 Readability":                        
                        Question_3_Mark_Prof_2_R = index[0]
                    if row == "Question 3 Mark Prof 2 Maintainability":                        
                        Question_3_Mark_Prof_2_M = index[0]

                    if row == "Question 1 Mark Prof 3 Functional correctness":                        
                        Question_1_Mark_Prof_3_F = index[0]
                    if row == "Question 1 Mark Prof 3 Efficiency":                        
                        Question_1_Mark_Prof_3_E = index[0]
                    if row == "Question 1 Mark Prof 3 Readability":                        
                        Question_1_Mark_Prof_3_R = index[0]
                    if row == "Question 1 Mark Prof 3 Maintainability":                        
                        Question_1_Mark_Prof_3_M = index[0]
                        
                    if row == "Question 2 Mark Prof 3 Functional correctness":                        
                        Question_2_Mark_Prof_3_F = index[0]
                    if row == "Question 2 Mark Prof 3 Efficiency":                        
                        Question_2_Mark_Prof_3_E = index[0]
                    if row == "Question 2 Mark Prof 3 Readability":                        
                        Question_2_Mark_Prof_3_R = index[0]
                    if row == "Question 2 Mark Prof 3 Maintainability":                        
                        Question_2_Mark_Prof_3_M = index[0]

                    if row == "Question 3 Mark Prof 3 Functional correctness":                        
                        Question_3_Mark_Prof_3_F = index[0]
                    if row == "Question 3 Mark Prof 3 Efficiency":                        
                        Question_3_Mark_Prof_3_E = index[0]
                    if row == "Question 3 Mark Prof 3 Readability":                        
                        Question_3_Mark_Prof_3_R = index[0]
                    if row == "Question 3 Mark Prof 3 Maintainability":                        
                        Question_3_Mark_Prof_3_M = index[0]

                    if row == "Prof 1 Comment":                        
                        Prof_1_Comment = index[0]
                    if row == "Prof 2 Comment":                        
                        Prof_2_Comment = index[0]
                    if row == "Prof 3 Comment":                        
                        Prof_3_Comment = index[0]
                
                if Question_1_answer != "" and Question_2_answer != "" and Question_3_answer != "":
                    df_results.loc[df_summary_row_index] = [Student_ID,Question_1_answer,Question_2_answer,Question_3_answer,ChatGPT_questions,ChatGPT_questions_count,
                                                            Question_1_period,Question_2_period,Question_3_period,
                                                            Question_1_Mark_Prof_1_F, Question_1_Mark_Prof_1_E,Question_1_Mark_Prof_1_R,Question_1_Mark_Prof_1_M,
                                                            Question_2_Mark_Prof_1_F, Question_2_Mark_Prof_1_E,Question_2_Mark_Prof_1_R,Question_2_Mark_Prof_1_M,
                                                            Question_3_Mark_Prof_1_F, Question_3_Mark_Prof_1_E,Question_3_Mark_Prof_1_R,Question_3_Mark_Prof_1_M,
                                                            Question_1_Mark_Prof_2_F, Question_1_Mark_Prof_2_E,Question_1_Mark_Prof_2_R,Question_1_Mark_Prof_2_M,
                                                            Question_2_Mark_Prof_2_F, Question_2_Mark_Prof_2_E,Question_2_Mark_Prof_2_R,Question_2_Mark_Prof_2_M,
                                                            Question_3_Mark_Prof_2_F, Question_3_Mark_Prof_2_E,Question_3_Mark_Prof_2_R,Question_3_Mark_Prof_2_M,
                                                            Question_1_Mark_Prof_3_F, Question_1_Mark_Prof_3_E,Question_1_Mark_Prof_3_R,Question_1_Mark_Prof_3_M,
                                                            Question_2_Mark_Prof_3_F, Question_2_Mark_Prof_3_E,Question_2_Mark_Prof_3_R,Question_2_Mark_Prof_3_M,
                                                            Question_3_Mark_Prof_3_F, Question_3_Mark_Prof_3_E,Question_3_Mark_Prof_3_R,Question_3_Mark_Prof_3_M,
                                                            Prof_1_Comment,Prof_2_Comment,Prof_3_Comment                                                                                                
                                                            ]
                    df_summary_row_index += 1
                    # print(Question_1_answer)

    # print(df_results)
    return render_template('mark.html',df_results = df_results.to_numpy(),prof_id=prof_id)

@application.route('/download_marks', methods=['GET'])
def download_marks():

    column_names = ["Student ID" ,"Question Number",        
        "Prof 1 Functional correctness","Prof 1 Efficiency","Prof 1 Readability","Prof 1 Maintainability",
        "Prof 2 Functional correctness","Prof 2 Efficiency","Prof 2 Readability","Prof 2 Maintainability",
        "Prof 3 Functional correctness","Prof 3 Efficiency","Prof 3 Readability","Prof 3 Maintainability",
        "period",
        "ChatGPT questions count"        
    ]

    Total_excel_files_count = 0
    
    directory = 'static/excels'
                    
    df_results = pd.DataFrame(columns = column_names)
    df_summary_row_index=0
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        if filename[0] != "_":
            full_path = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(full_path):
                Total_excel_files_count += 1
                # print(full_path)
                df = pd.read_excel(full_path, index_col=0,sheet_name='1')  
                Student_ID = ""
                Question_1_answer = ""
                Question_2_answer = ""
                Question_3_answer = ""
                ChatGPT_questions_count = 0
                Question_1_period = ""
                Question_2_period = ""
                Question_3_period = ""
                ChatGPT_questions=""
                Question_1_Mark_Prof_1_F=0
                Question_1_Mark_Prof_1_E=0
                Question_1_Mark_Prof_1_R=0
                Question_1_Mark_Prof_1_M=0
                Question_2_Mark_Prof_1_F=0
                Question_2_Mark_Prof_1_E=0
                Question_2_Mark_Prof_1_R=0
                Question_2_Mark_Prof_1_M=0
                Question_3_Mark_Prof_1_F=0
                Question_3_Mark_Prof_1_E=0
                Question_3_Mark_Prof_1_R=0
                Question_3_Mark_Prof_1_M=0
                Question_1_Mark_Prof_2_F=0
                Question_1_Mark_Prof_2_E=0
                Question_1_Mark_Prof_2_R=0
                Question_1_Mark_Prof_2_M=0
                Question_2_Mark_Prof_2_F=0
                Question_2_Mark_Prof_2_E=0
                Question_2_Mark_Prof_2_R=0
                Question_2_Mark_Prof_2_M=0
                Question_3_Mark_Prof_2_F=0
                Question_3_Mark_Prof_2_E=0
                Question_3_Mark_Prof_2_R=0
                Question_3_Mark_Prof_2_M=0
                Question_1_Mark_Prof_3_F=0
                Question_1_Mark_Prof_3_E=0
                Question_1_Mark_Prof_3_R=0
                Question_1_Mark_Prof_3_M=0
                Question_2_Mark_Prof_3_F=0
                Question_2_Mark_Prof_3_E=0
                Question_2_Mark_Prof_3_R=0
                Question_2_Mark_Prof_3_M=0
                Question_3_Mark_Prof_3_F=0
                Question_3_Mark_Prof_3_E=0
                Question_3_Mark_Prof_3_R=0
                Question_3_Mark_Prof_3_M=0
                Prof_1_Comment = ""
                Prof_2_Comment = ""
                Prof_3_Comment = ""
                
                for  row,index in df.iterrows():
                    if row == "Student ID" or row == "Student ID: ":
                        Student_ID = index[0]
                    if row == "answer 1":                        
                        Question_1_answer = index[0]
                    if row == "answer 2":                        
                        Question_2_answer = index[0]
                    if row == "answer 3":                        
                        Question_3_answer = index[0]
                    if row == "duration 1":                        
                        Question_1_period = round(index[0],2)
                    if row == "duration 2":                        
                        Question_2_period = index[0]
                    if row == "duration 3":                        
                        Question_3_period = index[0]                       
                    
                    if row == "request":
                        ChatGPT_questions_count += 1

                    if row == "request" or row == "respond":
                        ChatGPT_questions = ChatGPT_questions + str(index[0]) + "<br>" + "<br>"
                    if row == "respond":
                        ChatGPT_questions = ChatGPT_questions + "<br>"
                    if row == "Question 1 Mark Prof 1 Functional correctness":                        
                        Question_1_Mark_Prof_1_F = index[0]
                    if row == "Question 1 Mark Prof 1 Efficiency":                        
                        Question_1_Mark_Prof_1_E = index[0]
                    if row == "Question 1 Mark Prof 1 Readability":                        
                        Question_1_Mark_Prof_1_R = index[0]
                    if row == "Question 1 Mark Prof 1 Maintainability":                        
                        Question_1_Mark_Prof_1_M = index[0]
                        
                    if row == "Question 2 Mark Prof 1 Functional correctness":                        
                        Question_2_Mark_Prof_1_F = index[0]
                    if row == "Question 2 Mark Prof 1 Efficiency":                        
                        Question_2_Mark_Prof_1_E = index[0]
                    if row == "Question 2 Mark Prof 1 Readability":                        
                        Question_2_Mark_Prof_1_R = index[0]
                    if row == "Question 2 Mark Prof 1 Maintainability":                        
                        Question_2_Mark_Prof_1_M = index[0]

                    if row == "Question 3 Mark Prof 1 Functional correctness":                        
                        Question_3_Mark_Prof_1_F = index[0]
                    if row == "Question 3 Mark Prof 1 Efficiency":                        
                        Question_3_Mark_Prof_1_E = index[0]
                    if row == "Question 3 Mark Prof 1 Readability":                        
                        Question_3_Mark_Prof_1_R = index[0]
                    if row == "Question 3 Mark Prof 1 Maintainability":                        
                        Question_3_Mark_Prof_1_M = index[0]

                    if row == "Question 1 Mark Prof 2 Functional correctness":                        
                        Question_1_Mark_Prof_2_F = index[0]
                    if row == "Question 1 Mark Prof 2 Efficiency":                        
                        Question_1_Mark_Prof_2_E = index[0]
                    if row == "Question 1 Mark Prof 2 Readability":                        
                        Question_1_Mark_Prof_2_R = index[0]
                    if row == "Question 1 Mark Prof 2 Maintainability":                        
                        Question_1_Mark_Prof_2_M = index[0]
                        
                    if row == "Question 2 Mark Prof 2 Functional correctness":                        
                        Question_2_Mark_Prof_2_F = index[0]
                    if row == "Question 2 Mark Prof 2 Efficiency":                        
                        Question_2_Mark_Prof_2_E = index[0]
                    if row == "Question 2 Mark Prof 2 Readability":                        
                        Question_2_Mark_Prof_2_R = index[0]
                    if row == "Question 2 Mark Prof 2 Maintainability":                        
                        Question_2_Mark_Prof_2_M = index[0]

                    if row == "Question 3 Mark Prof 2 Functional correctness":                        
                        Question_3_Mark_Prof_2_F = index[0]
                    if row == "Question 3 Mark Prof 2 Efficiency":                        
                        Question_3_Mark_Prof_2_E = index[0]
                    if row == "Question 3 Mark Prof 2 Readability":                        
                        Question_3_Mark_Prof_2_R = index[0]
                    if row == "Question 3 Mark Prof 2 Maintainability":                        
                        Question_3_Mark_Prof_2_M = index[0]

                    if row == "Question 1 Mark Prof 3 Functional correctness":                        
                        Question_1_Mark_Prof_3_F = index[0]
                    if row == "Question 1 Mark Prof 3 Efficiency":                        
                        Question_1_Mark_Prof_3_E = index[0]
                    if row == "Question 1 Mark Prof 3 Readability":                        
                        Question_1_Mark_Prof_3_R = index[0]
                    if row == "Question 1 Mark Prof 3 Maintainability":                        
                        Question_1_Mark_Prof_3_M = index[0]
                        
                    if row == "Question 2 Mark Prof 3 Functional correctness":                        
                        Question_2_Mark_Prof_3_F = index[0]
                    if row == "Question 2 Mark Prof 3 Efficiency":                        
                        Question_2_Mark_Prof_3_E = index[0]
                    if row == "Question 2 Mark Prof 3 Readability":                        
                        Question_2_Mark_Prof_3_R = index[0]
                    if row == "Question 2 Mark Prof 3 Maintainability":                        
                        Question_2_Mark_Prof_3_M = index[0]

                    if row == "Question 3 Mark Prof 3 Functional correctness":                        
                        Question_3_Mark_Prof_3_F = index[0]
                    if row == "Question 3 Mark Prof 3 Efficiency":                        
                        Question_3_Mark_Prof_3_E = index[0]
                    if row == "Question 3 Mark Prof 3 Readability":                        
                        Question_3_Mark_Prof_3_R = index[0]
                    if row == "Question 3 Mark Prof 3 Maintainability":                        
                        Question_3_Mark_Prof_3_M = index[0]

                

            #         column_names = ["Student ID" ,"Question Number"        
            # "Prof 1 Functional correctness","Prof 1 Efficiency","Prof 1 Readability","Prof 1 Maintainability",
            # "Prof 2 Functional correctness","Prof 2 Efficiency","Prof 2 Readability","Prof 2 Maintainability",
            # "Prof 3 Functional correctness","Prof 3 Efficiency","Prof 3 Readability","Prof 3 Maintainability",
            # "period",
            # "ChatGPT questions count"        
            #   ]   

                if Question_1_answer != "" and Question_2_answer != "" and Question_3_answer != "":
                    df_results.loc[df_summary_row_index] = [Student_ID,"1",                                                            
                                                            Question_1_Mark_Prof_1_F, Question_1_Mark_Prof_1_E,Question_1_Mark_Prof_1_R,Question_1_Mark_Prof_1_M,
                                                            Question_1_Mark_Prof_2_F, Question_1_Mark_Prof_2_E,Question_1_Mark_Prof_2_R,Question_1_Mark_Prof_2_M,
                                                            Question_1_Mark_Prof_3_F, Question_1_Mark_Prof_3_E,Question_1_Mark_Prof_3_R,Question_1_Mark_Prof_3_M,
                                                            Question_1_period,
                                                            0
                                                            ]
                    df_summary_row_index += 1
                    df_results.loc[df_summary_row_index] = [Student_ID,"2",                                                            
                                                            Question_2_Mark_Prof_1_F, Question_2_Mark_Prof_1_E,Question_2_Mark_Prof_1_R,Question_2_Mark_Prof_1_M,
                                                            Question_2_Mark_Prof_2_F, Question_2_Mark_Prof_2_E,Question_2_Mark_Prof_2_R,Question_2_Mark_Prof_2_M,
                                                            Question_2_Mark_Prof_3_F, Question_2_Mark_Prof_3_E,Question_2_Mark_Prof_3_R,Question_2_Mark_Prof_3_M,
                                                            Question_2_period,
                                                            0
                                                            ]
                    df_summary_row_index += 1
                    df_results.loc[df_summary_row_index] = [Student_ID,"3",                                                            
                                                            Question_3_Mark_Prof_1_F, Question_3_Mark_Prof_1_E,Question_3_Mark_Prof_1_R,Question_3_Mark_Prof_1_M,
                                                            Question_3_Mark_Prof_2_F, Question_3_Mark_Prof_2_E,Question_3_Mark_Prof_2_R,Question_3_Mark_Prof_2_M,
                                                            Question_3_Mark_Prof_3_F, Question_3_Mark_Prof_3_E,Question_3_Mark_Prof_3_R,Question_3_Mark_Prof_3_M,
                                                            Question_3_period,
                                                            ChatGPT_questions_count
                                                            ]
                    df_summary_row_index += 1
    
    df_results.to_csv('static/excels/_marks.csv',index=False)

    return send_from_directory('static/excels/', "_marks.csv")

@application.route('/update_score', methods=['POST'])
def update_score():
    prof_id =  request.args.get('prof_id')
    student_id = request.args.get('student_id')
    task_number = request.args.get('task_number')
    FERM = request.args.get('FERM')

    score = request.args.get('score')

    # print(prof_id,student_id,task_number,score)

    filename = student_id + ".xlsx"
    if FERM == "F":
        FERM_name = "Functional correctness"
    if FERM == "E":
        FERM_name = "Efficiency"
    if FERM == "R":
        FERM_name = "Readability"
    if FERM == "M":
        FERM_name = "Maintainability"
    row_name = "Question " + task_number + " Mark Prof " + prof_id + " " + FERM_name
    
    update = False
    full_path = excels_folder+filename
    if not os.path.isfile("static/"+full_path):    
        df = pd.DataFrame()
    else:
        df = pd.read_excel("static/"+full_path, index_col=0,sheet_name='1')  
        for  row,index in df.iterrows():
            if row == row_name:
                update = True
                df.at[row_name,0]=score
                # print(df)
                # return "1" # update value
        
        if not update:
            df = pd.concat([df, pd.DataFrame([[score]], index=[row_name])])    

        # print(df)
        writer = pd.ExcelWriter("static/"+full_path, engine='xlsxwriter')
        df.to_excel(writer, sheet_name="1")
        workbook = writer.book
        worksheet = writer.sheets['1']
        format = workbook.add_format({'text_wrap': True})
        worksheet.set_column('B:B', 50, format)
        writer.close()



    return "0"

@application.route('/update_comment', methods=['POST'])
def update_comment():
    prof_id = request.args.get('prof_id')
    student_id = request.args.get('student_id')
    comment = get_char_from_ascii(request.args.get('comment').split(" "))

    filename = student_id + ".xlsx"

    row_name = "Prof " + prof_id + " Comment"
    
    update = False
    full_path = excels_folder+filename
    if not os.path.isfile("static/"+full_path):    
        df = pd.DataFrame()
    else:
        df = pd.read_excel("static/"+full_path, index_col=0,sheet_name='1')  
        for  row,index in df.iterrows():
            if row == row_name:
                update = True
                df.at[row_name,0]=comment
                # print(df)
                # return "1" # update value
        
        if not update:
            df = pd.concat([df, pd.DataFrame([[comment]], index=[row_name])])    

        # print(df)
        writer = pd.ExcelWriter("static/"+full_path, engine='xlsxwriter')
        df.to_excel(writer, sheet_name="1")
        workbook = writer.book
        worksheet = writer.sheets['1']
        format = workbook.add_format({'text_wrap': True})
        worksheet.set_column('B:B', 50, format)
        writer.close()

    # print(prof_id,student_id,comment)
    return "0"

@application.route('/store_start_time', methods=['POST'])
def store_start_time():
    id = request.args.get('id')
    if Evaluate_IP(id) != 0:
        return Evaluate_IP(id)
    task_number = request.args.get('task_number')
    filename = id + ".xlsx"
    full_path = excels_folder+filename
    if not os.path.isfile("static/"+full_path):    
        df = pd.DataFrame()
    else:
        df = pd.read_excel("static/"+full_path, index_col=0,sheet_name='1')  
        for  row,index in df.iterrows():
            if row == "start date " + task_number:
                return "already stored" 

    df = pd.concat([df, pd.DataFrame([[datetime.now()]], index=['start date ' + task_number])])

    # print(df)
    writer = pd.ExcelWriter("static/"+full_path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name="1")
    workbook = writer.book
    worksheet = writer.sheets['1']
    format = workbook.add_format({'text_wrap': True})
    worksheet.set_column('B:B', 50, format)
    writer.close()

    return "0"

def get_char_from_ascii(ascii_str):
    string_of_char=""
    for ascii_value in ascii_str:
        if ascii_value.isdigit():
            string_of_char += chr(int(ascii_value))
    return string_of_char


@application.route('/store_task', methods=['POST'])
def store_task():
    code_beginner_task = get_char_from_ascii(request.args.get('code_beginner_task').split(" "))
   
    task_number = request.args.get('task_number')
    subject = request.args.get('subject')
    id = request.args.get('id')
    if Evaluate_IP(id) != 0:
        return Evaluate_IP(id)
    if len(code_beginner_task) == 0:
        return "-1"
   
    filename = id + ".xlsx"

    answered = []
    datetime_str = ""
    start_time_found = False
    full_path = excels_folder+filename
    if not os.path.isfile("static/"+full_path):    
        df = pd.DataFrame()
    else:
        df = pd.read_excel("static/"+full_path, index_col=0,sheet_name='1')  
        count = 0
        for  row,index in df.iterrows():
            if row == "Task number":
                if index[0]== task_number:        
                    return "-1"
            if row == "start date " + task_number:
                datetime_str = index[0]
                start_time_found = True

    # store_date = secure_filename(str(datetime.now()))
    duration = 0
    if start_time_found:
        datetime_object = datetime_str
        # print("datetime_object" , datetime_object)
        # print("datetime.now" , datetime.now())
        duration = (datetime.now() - datetime_object).total_seconds() / 60
    if task_number == "1":      
        description = "Python tan"
        level = "Beginner"
    if task_number == "2":  
        description = "oracle live"
        level = "Advanced"
    if task_number == "3":  
        description = "display"
        level = "Intermediate"

    # for i, pl in enumerate(p_left_task1_array):
    df = pd.concat([df, pd.DataFrame([[str(id)],[subject],[level], [task_number], [description],[duration],[code_beginner_task.replace("<br>", "\n")]], index=["Student ID: ","subject",'Level', 'Task number', 'Task description','duration '+task_number, 'answer '+task_number])])
    # print(df)
    writer = pd.ExcelWriter("static/"+full_path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name="1")
    workbook = writer.book
    worksheet = writer.sheets['1']
    format = workbook.add_format({'text_wrap': True})
    worksheet.set_column('B:B', 50, format)
    writer.close()
    return "0"


@application.route('/download', methods=['GET'])
def download():
    full_path = "static/" + request.args.get('full_path')
    return send_file(full_path, as_attachment=True)


from dateutil import parser

@application.route('/feedback_to_excels', methods=['GET'])
def feedback_to_excels():
    df = pd.read_csv('Evaluating Human vs AI .csv')
    df['Duration'] = ""
    df['P1 Grade-Functional Correctness'] = ""
    df['P1 Grade-Efficiency'] = ""
    df['P1 Grade-Readability'] = ""
    df['P1 Grade-Maintainability'] = ""
    df['P1 Grade-Average'] = ""
    df['P2 Grade-Functional Correctness'] = ""
    df['P2 Grade-Efficiency'] = ""
    df['P2 Grade-Readability'] = ""
    df['P2 Grade-Maintainability'] = ""
    df['P2 Grade-Average'] = ""
    df['P3 Grade-Functional Correctness'] = ""
    df['P3 Grade-Efficiency'] = ""
    df['P3 Grade-Readability'] = ""
    df['P3 Grade-Maintainability'] = ""
    df['P3 Grade-Average'] = ""
    for index1,row1 in df.iterrows():
        id = row1["KAU ID"]
        question = row1["Question"]
        full_path = "static/"+excels_folder+str(id)+".xlsx"
        # print(full_path)
        # print(id,question)
        # print(os.path)
        if os.path.isfile(full_path):
            df_student = pd.read_excel(full_path, index_col=0,sheet_name='1')  
            if question == 1:
                duration = 0
                Question_1_Mark_Prof_1_F=0
                Question_1_Mark_Prof_1_E=0
                Question_1_Mark_Prof_1_R=0
                Question_1_Mark_Prof_1_M=0
                Question_1_Mark_Prof_2_F=0
                Question_1_Mark_Prof_2_E=0
                Question_1_Mark_Prof_2_R=0
                Question_1_Mark_Prof_2_M=0
                Question_1_Mark_Prof_3_F=0
                Question_1_Mark_Prof_3_E=0
                Question_1_Mark_Prof_3_R=0
                Question_1_Mark_Prof_3_M=0
                for  index,row in df_student.iterrows():
                    if index == "duration 1" :                        
                        duration = int(row[0])
                    if index == "Question 1 Mark Prof 1 Functional correctness":                        
                        Question_1_Mark_Prof_1_F = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 1 Mark Prof 1 Efficiency":                        
                        Question_1_Mark_Prof_1_E = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 1 Mark Prof 1 Readability":                        
                        Question_1_Mark_Prof_1_R = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 1 Mark Prof 1 Maintainability":                        
                        Question_1_Mark_Prof_1_M = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 1 Mark Prof 2 Functional correctness":                        
                        Question_1_Mark_Prof_2_F = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 1 Mark Prof 2 Efficiency":                        
                        Question_1_Mark_Prof_2_E = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 1 Mark Prof 2 Readability":                        
                        Question_1_Mark_Prof_2_R = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 1 Mark Prof 2 Maintainability":                        
                        Question_1_Mark_Prof_2_M = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 1 Mark Prof 3 Functional correctness":                        
                        Question_1_Mark_Prof_3_F = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 1 Mark Prof 3 Efficiency":                        
                        Question_1_Mark_Prof_3_E = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 1 Mark Prof 3 Readability":                        
                        Question_1_Mark_Prof_3_R = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 1 Mark Prof 3 Maintainability":                        
                        Question_1_Mark_Prof_3_M = 0 if not str(row[0]).isnumeric() else int(row[0])
                
                df.at[index1,"Duration"]=duration
                df.at[index1,"P1 Grade-Functional Correctness"]=Question_1_Mark_Prof_1_F
                df.at[index1,"P1 Grade-Efficiency"]=Question_1_Mark_Prof_1_E
                df.at[index1,"P1 Grade-Readability"]=Question_1_Mark_Prof_1_R
                df.at[index1,"P1 Grade-Maintainability"]=Question_1_Mark_Prof_1_M
                df.at[index1,'P1 Grade-Average'] = (Question_1_Mark_Prof_1_F + Question_1_Mark_Prof_1_E + Question_1_Mark_Prof_1_R + Question_1_Mark_Prof_1_M)/4
                df.at[index1,"P2 Grade-Functional Correctness"]=Question_1_Mark_Prof_2_F
                df.at[index1,"P2 Grade-Efficiency"]=Question_1_Mark_Prof_2_E
                df.at[index1,"P2 Grade-Readability"]=Question_1_Mark_Prof_2_R
                df.at[index1,"P2 Grade-Maintainability"]=Question_1_Mark_Prof_2_M
                df.at[index1,'P2 Grade-Average'] = (Question_1_Mark_Prof_2_F + Question_1_Mark_Prof_2_E + Question_1_Mark_Prof_2_R + Question_1_Mark_Prof_2_M)/4
                df.at[index1,"P3 Grade-Functional Correctness"]=Question_1_Mark_Prof_3_F
                df.at[index1,"P3 Grade-Efficiency"]=Question_1_Mark_Prof_3_E
                df.at[index1,"P3 Grade-Readability"]=Question_1_Mark_Prof_3_R
                df.at[index1,"P3 Grade-Maintainability"]=Question_1_Mark_Prof_3_M
                df.at[index1,'P3 Grade-Average'] = (Question_1_Mark_Prof_3_F + Question_1_Mark_Prof_3_E + Question_1_Mark_Prof_3_R + Question_1_Mark_Prof_3_M)/4

            if question == 2:
                duration = 0
                Question_2_Mark_Prof_1_F=0
                Question_2_Mark_Prof_1_E=0
                Question_2_Mark_Prof_1_R=0
                Question_2_Mark_Prof_1_M=0
                Question_2_Mark_Prof_2_F=0
                Question_2_Mark_Prof_2_E=0
                Question_2_Mark_Prof_2_R=0
                Question_2_Mark_Prof_2_M=0
                Question_2_Mark_Prof_3_F=0
                Question_2_Mark_Prof_3_E=0
                Question_2_Mark_Prof_3_R=0
                Question_2_Mark_Prof_3_M=0
                for  index,row in df_student.iterrows():
                    if index == "duration 2" :                        
                        duration = int(row[0])
                    if index == "Question 2 Mark Prof 1 Functional correctness":                        
                        Question_2_Mark_Prof_1_F = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 2 Mark Prof 1 Efficiency":                        
                        Question_2_Mark_Prof_1_E = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 2 Mark Prof 1 Readability":                        
                        Question_2_Mark_Prof_1_R = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 2 Mark Prof 1 Maintainability":                        
                        Question_2_Mark_Prof_1_M = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 2 Mark Prof 2 Functional correctness":                        
                        Question_2_Mark_Prof_2_F = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 2 Mark Prof 2 Efficiency":                        
                        Question_2_Mark_Prof_2_E = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 2 Mark Prof 2 Readability":                        
                        Question_2_Mark_Prof_2_R = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 2 Mark Prof 2 Maintainability":                        
                        Question_2_Mark_Prof_2_M = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 2 Mark Prof 3 Functional correctness":                        
                        Question_2_Mark_Prof_3_F = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 2 Mark Prof 3 Efficiency":                        
                        Question_2_Mark_Prof_3_E = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 2 Mark Prof 3 Readability":                        
                        Question_2_Mark_Prof_3_R = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == "Question 2 Mark Prof 3 Maintainability":                        
                        Question_2_Mark_Prof_3_M = 0 if not str(row[0]).isnumeric() else int(row[0])
                
                df.at[index1,"Duration"]=duration
                df.at[index1,"P1 Grade-Functional Correctness"]=Question_2_Mark_Prof_1_F
                df.at[index1,"P1 Grade-Efficiency"]=Question_2_Mark_Prof_1_E
                df.at[index1,"P1 Grade-Readability"]=Question_2_Mark_Prof_1_R
                df.at[index1,"P1 Grade-Maintainability"]=Question_2_Mark_Prof_1_M
                df.at[index1,'P1 Grade-Average'] = (Question_2_Mark_Prof_1_F + Question_2_Mark_Prof_1_E + Question_2_Mark_Prof_1_R + Question_2_Mark_Prof_1_M)/4
                df.at[index1,"P2 Grade-Functional Correctness"]=Question_2_Mark_Prof_2_F
                df.at[index1,"P2 Grade-Efficiency"]=Question_2_Mark_Prof_2_E
                df.at[index1,"P2 Grade-Readability"]=Question_2_Mark_Prof_2_R
                df.at[index1,"P2 Grade-Maintainability"]=Question_2_Mark_Prof_2_M
                df.at[index1,'P2 Grade-Average'] = (Question_2_Mark_Prof_2_F + Question_2_Mark_Prof_2_E + Question_2_Mark_Prof_2_R + Question_2_Mark_Prof_2_M)/4
                df.at[index1,"P3 Grade-Functional Correctness"]=Question_2_Mark_Prof_3_F
                df.at[index1,"P3 Grade-Efficiency"]=Question_2_Mark_Prof_3_E
                df.at[index1,"P3 Grade-Readability"]=Question_2_Mark_Prof_3_R
                df.at[index1,"P3 Grade-Maintainability"]=Question_2_Mark_Prof_3_M
                df.at[index1,'P3 Grade-Average'] = (Question_2_Mark_Prof_3_F + Question_2_Mark_Prof_3_E + Question_2_Mark_Prof_3_R + Question_2_Mark_Prof_3_M)/4

            if question == 3:
                duration = 0
                Question_3_Mark_Prof_1_F=0
                Question_3_Mark_Prof_1_E=0
                Question_3_Mark_Prof_1_R=0
                Question_3_Mark_Prof_1_M=0
                Question_3_Mark_Prof_2_F=0
                Question_3_Mark_Prof_2_E=0
                Question_3_Mark_Prof_2_R=0
                Question_3_Mark_Prof_2_M=0
                Question_3_Mark_Prof_3_F=0
                Question_3_Mark_Prof_3_E=0
                Question_3_Mark_Prof_3_R=0
                Question_3_Mark_Prof_3_M=0
                for  index,row in df_student.iterrows():
                    if index == "duration 3" :                        
                        duration = int(row[0])
                    if index == " Question 3 Mark Prof 1 Functional correctness":                        
                        Question_3_Mark_Prof_1_F = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == " Question 3 Mark Prof 1 Efficiency":                        
                        Question_3_Mark_Prof_1_E = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == " Question 3 Mark Prof 1 Readability":                        
                        Question_3_Mark_Prof_1_R = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == " Question 3 Mark Prof 1 Maintainability":                        
                        Question_3_Mark_Prof_1_M = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == " Question 3 Mark Prof 2 Functional correctness":                        
                        Question_3_Mark_Prof_2_F = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == " Question 3 Mark Prof 2 Efficiency":                        
                        Question_3_Mark_Prof_2_E = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == " Question 3 Mark Prof 2 Readability":                        
                        Question_3_Mark_Prof_2_R = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == " Question 3 Mark Prof 2 Maintainability":                        
                        Question_3_Mark_Prof_2_M = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == " Question 3 Mark Prof 3 Functional correctness":                        
                        Question_3_Mark_Prof_3_F = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == " Question 3 Mark Prof 3 Efficiency":                        
                        Question_3_Mark_Prof_3_E = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == " Question 3 Mark Prof 3 Readability":                        
                        Question_3_Mark_Prof_3_R = 0 if not str(row[0]).isnumeric() else int(row[0])
                    if index == " Question 3 Mark Prof 3 Maintainability":                        
                        Question_3_Mark_Prof_3_M = 0 if not str(row[0]).isnumeric() else int(row[0])
                
                df.at[index1,"Duration"]=duration
                df.at[index1,"P1 Grade-Functional Correctness"]=Question_3_Mark_Prof_1_F
                df.at[index1,"P1 Grade-Efficiency"]=Question_3_Mark_Prof_1_E
                df.at[index1,"P1 Grade-Readability"]=Question_3_Mark_Prof_1_R
                df.at[index1,"P1 Grade-Maintainability"]=Question_3_Mark_Prof_1_M
                df.at[index1,'P1 Grade-Average'] = (Question_3_Mark_Prof_1_F + Question_3_Mark_Prof_1_E + Question_3_Mark_Prof_1_R + Question_3_Mark_Prof_1_M)/4
                df.at[index1,"P2 Grade-Functional Correctness"]=Question_3_Mark_Prof_2_F
                df.at[index1,"P2 Grade-Efficiency"]=Question_3_Mark_Prof_2_E
                df.at[index1,"P2 Grade-Readability"]=Question_3_Mark_Prof_2_R
                df.at[index1,"P2 Grade-Maintainability"]=Question_3_Mark_Prof_2_M
                df.at[index1,'P2 Grade-Average'] = (Question_3_Mark_Prof_2_F + Question_3_Mark_Prof_2_E + Question_3_Mark_Prof_2_R + Question_3_Mark_Prof_2_M)/4
                df.at[index1,"P3 Grade-Functional Correctness"]=Question_3_Mark_Prof_3_F
                df.at[index1,"P3 Grade-Efficiency"]=Question_3_Mark_Prof_3_E
                df.at[index1,"P3 Grade-Readability"]=Question_3_Mark_Prof_3_R
                df.at[index1,"P3 Grade-Maintainability"]=Question_3_Mark_Prof_3_M
                df.at[index1,'P3 Grade-Average'] = (Question_3_Mark_Prof_3_F + Question_3_Mark_Prof_3_E + Question_3_Mark_Prof_3_R + Question_3_Mark_Prof_3_M)/4
    

    df.to_csv('static/excels/_feedback.csv',index=False)
    
    return send_from_directory('static/excels/', "_feedback.csv")

@application.route('/download_all_files')
def zipped_data():
    # download link http://127.0.0.1:11000/download_all_files
    # creating summarizing file
    Total_excel_files_count = 0
    Question_1_Total = 0
    Question_2_Total = 0
    Question_3_Total = 0
    
    directory = 'static/excels'
    column_names = ["Student ID" , "Question 1" , "Question 2" , "Question 3", "ChatGPT questions count", "Question 1 period", "Question 2 period","Question 3 period"
                    ]
    df_summary = pd.DataFrame(columns = column_names)
    df_summary_row_index=0
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        if filename[0] != "_":
            full_path = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(full_path):
                Total_excel_files_count += 1
                # print(full_path)
                df = pd.read_excel(full_path, index_col=0,sheet_name='1')  
                Student_ID = ""
                Question_1 = ""
                Question_2 = ""
                Question_3 = ""
                ChatGPT_questions_count = 0
                Question_1_period = ""
                Question_2_period = ""
                Question_3_period = ""

                for  row,index in df.iterrows():
                    if row == "Student ID" or row == "Student ID: ":
                        Student_ID = index[0]
                    if row == "Task number":
                        if index[0] == "1":
                            Question_1 = "answered"  
                            Question_1_Total += 1                  
                        if index[0] == "2":
                            Question_2 = "answered"      
                            Question_2_Total += 1                  
                        if index[0] == "3":
                            Question_3 = "answered"
                            Question_3_Total += 1                  

                    if row == "request":
                        ChatGPT_questions_count += 1
                
                df_summary.loc[df_summary_row_index] = [Student_ID,Question_1,Question_2,Question_3,ChatGPT_questions_count,Question_1_period,Question_2_period,Question_3_period]
                df_summary_row_index += 1
    df_summary.loc[df_summary_row_index] = ["Total",Question_1_Total,Question_2_Total,Question_3_Total,"","","",""]
    df_summary_row_index += 1
    df_summary.loc[df_summary_row_index] = ["Average %",str(Question_1_Total /Total_excel_files_count),str(Question_2_Total/Total_excel_files_count),str(Question_3_Total/Total_excel_files_count),"","","",""]
    df_summary_row_index += 1
    df_summary.to_csv('static/excels/_all.csv',index=False)
                # for ind in df2.index:
                #     print(df2[ind][0])
            # if "Task number" in df.index:
            #     for item in df.index:
            #         if item == "Task number":
                

    timestr = time.strftime("%Y%m%d-%H%M%S")
    fileName = "Students_answers{}.zip".format(timestr)
    memory_file = BytesIO()
    file_path = 'static/excels/'
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
          for root, dirs, files in os.walk(file_path):
                    for file in files:
                              zipf.write(os.path.join(file_path, file))
    memory_file.seek(0)
    return send_file(memory_file,as_attachment=True, download_name =fileName)

@application.route('/chatgpt', methods=['GET'])
def chatgpt():
    
    return render_template('chatgpt.html')


@application.route('/ask_chatgpt', methods=['POST'])
def ask_chatgpt():
    id = request.args.get('id')
    if Evaluate_IP(id) != 0:
        return Evaluate_IP(id)

    filename = id + ".xlsx"
    full_path = excels_folder+filename
    if not os.path.isfile("static/"+full_path):        
        df = pd.DataFrame()
    else:
        df = pd.read_excel("static/"+full_path, index_col=0,sheet_name='1')  
        count = 0
        for  row,index in df.iterrows():
            if row == "Task number":
                count += 1        
                if (count>2):
                    return "-3"
            
    if request.args.get('last_respond') == "":
        textarea_ask_chatgpt_send = get_char_from_ascii(request.args.get('text').split(" ")) + " \n AI: "
    else:
        textarea_ask_chatgpt_send = get_char_from_ascii(request.args.get('last_respond').split(" ")) + " \n Human: " + get_char_from_ascii(request.args.get('text').split(" ")) + " \n AI: "
    print("textarea_ask_chatgpt_send",textarea_ask_chatgpt_send)
    if request.args.get('conversation_id'):
        conversation_id = request.args.get('conversation_id')
    else:
        conversation_id = str(uuid4())


    # if live:
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman:" + textarea_ask_chatgpt_send,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
        # if last_respond == "":
        #     completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
        #                                             messages=[{"role": "user",  # user , assistant (chat) , system
        #                                                         "content": textarea_ask_chatgpt_send 
        #                                                         }]
        #                                             )
        #     response = str(completion["choices"][0]["message"]["content"])
        # else:
        #     completion = openai.Edit.create(model="text-davinci-edit-001", input = last_respond, instruction = textarea_ask_chatgpt_send)
        #     response = str(completion["choices"][0]["text"])

    # if not live:
        # if last_respond == "":
        #     completion = {
        #         "choices": [
        #             {
        #                 "finish_reason": "stop",
        #                 "index": 0,
        #                 "message": {
        #                     "content": "1231231341231243",
        #                     "role": "assistant"
        #                 }
        #             }
        #         ],
        #         "created": 1681222484,
        #         "id": "chatcmpl-7493cuNlfD4lFnYIVM2jPbQgObxq5",
        #         "model": "gpt-3.5-turbo-0301",
        #         "object": "chat.completion",
        #         "usage": {
        #             "completion_tokens": 259,
        #             "prompt_tokens": 56,
        #             "total_tokens": 315
        #         }
        #     }
        #     response = str(completion["choices"][0]["message"]["content"])
        # else:
        #     completion = {
        #         "object": "edit",
        #         "created": 1589478378,
        #         "choices": [
        #             {
        #             "text": "What day of the week is it?",
        #             "index": 0,
        #             }
        #         ],
        #         "usage": {
        #             "prompt_tokens": 25,
        #             "completion_tokens": 32,
        #             "total_tokens": 57
        #         }
        #     }
    response = str(completion["choices"][0]["text"])



    print(completion)
    

    df = pd.concat([df, pd.DataFrame([[str(id)],[datetime.now()],[get_char_from_ascii(request.args.get('text').split(" ")).replace("<br>", "\n")],[response.replace("<br>", "\n")]], index=['Student ID','Ask time', 'request', 'respond'])])
    # print(df)
    writer = pd.ExcelWriter("static/"+full_path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name="1")
    workbook = writer.book
    worksheet = writer.sheets['1']
    format = workbook.add_format({'text_wrap': True})
    worksheet.set_column('B:B', 50, format)
    writer.close()

    return response


if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0", use_reloader=False, port=11000)
