from django.shortcuts import render
from django.http import HttpResponse
from email import header
import pandas as pd
import csv


# Create your views here.
a="hari"
b=[1,2,3,4,5,6,7,8,9,0]
file=open('D:\Projects\django\projects\\20210309_2020_1.csv')

csvreader=csv.reader(file)
header=next(csvreader)
header=[]
rows=[]
for row in csvreader:
    rows.append(row)


# print(header)
# print(rows)

def index(request):
    return render(request,'index.html',{'header_name':b})

def about(request):
    return HttpResponse("<h1>About</h1>")