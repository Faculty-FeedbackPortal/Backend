from django.shortcuts import render,HttpResponse
from django.db import models as mod
from django.http import JsonResponse
from django.contrib.auth.models import User
from . serializer import pracquestmodelSerializers,TheorymodelSerializers,FacultyMapmodelSerializers,SubjectmodelSerializers,FacultymodelSerializers,UserRegisterSerializer, UserLoginSerializer,DepartmentmodelSerializers,DivisionmodelSerializers,ImportSerializer
from . serializer import pracquestmodelSerializers,TheorymodelSerializers,FacultyMapmodelSerializers,SubjectmodelSerializers,FacultymodelSerializers,UserRegisterSerializer, UserLoginSerializer,DepartmentmodelSerializers,DivisionmodelSerializers,FacultyMapmodelNewSerializers, AcadmodelSerializers
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from . import models
from rest_framework.response import Response
from rest_framework import status
from anony.models import Theory_feedback,Practical_feedback
import io
from rest_framework.parsers import JSONParser
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, login, logout
from .validations import custom_validation, validate_email, validate_password
from rest_framework import permissions
from django.conf import settings
User = settings.AUTH_USER_MODEL
from .filters import SubjectsFilter,FacultyFilter,MapfacultyFilter,TheoryQuestionFilter,PracticalQuestionFilter,DepartmentFilter,DivisionFilter
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.parsers import MultiPartParser,FormParser
import pandas as pd
# Create your views here.



# permission_classes([IsAuthenticatedOrReadOnly])
@api_view(["POST"])  
def staffSignup(request):
    if request.method=="POST":
        # Get the signup parameters2
         # ##start
        # json_data = requests.data
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser.parse(stream=stream)
        # serializer = pracquestmodelSerializers(python_data)
        # ##end
        print(request.data)
        username=request.data['username']
        email=request.data['email']
        fname=request.data['fname'] 
        lname=request.data['lname']
        pass1=request.data['pass1']

        # check for wrong input
         
        if User.objects.filter(username=username).exists():
           return JsonResponse({'handlelogin':"already exist user"})
        else:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name= fname
            myuser.last_name= lname
            myuser.save()
            return JsonResponse({'handlelogin':"done"})

    else:
        return JsonResponse({"user":"404 - Not found"})
    



# permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET',"POST"])    
def pracquestDetail(requests):
    #For posting the data
    if requests.method  == "POST":
        # ##start
        # json_data = requests.body
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser.parse(stream=stream)
        # serializer = pracquestmodelSerializers(data=python_data)
        # ##end
        
        serializer = pracquestmodelSerializers(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            res = {"status":"posted succesfully"}
            return Response(res,status=status.HTTP_201_CREATED)
        else:
            return Response({"status":"Unsuccesfull"},status=status.HTTP_400_BAD_REQUEST)
    #for retriving the data
    else:
        tasks = models.practical_questions.objects.all()
        filterset = PracticalQuestionFilter(requests.GET, queryset=tasks)
        if filterset.is_valid():
         queryset = filterset.qs
        serializer = pracquestmodelSerializers(queryset,many=True)

        return Response(serializer.data)


# @permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET',"POST"])    
def theoryquestDetail(requests):
    #For posting the data
    if requests.method  == "POST":
        # ##start
        # json_data = requests.data
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser.parse(stream=stream)
        # serializer = TheorymodelSerializers(python_data)
        # ##end
        serializer = TheorymodelSerializers(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            res = {"status":"posted succesfully"}
            return Response(res,status=status.HTTP_201_CREATED)
        else:
            return Response({"status":"Unsuccesfull"},status=status.HTTP_400_BAD_REQUEST)
    #for retriving the data
    else:
        tasks = models.theory_questions.objects.all()
        filterset = TheoryQuestionFilter(requests.GET, queryset=tasks)
        if filterset.is_valid():
         queryset = filterset.qs
        serializer = TheorymodelSerializers(queryset,many=True)
        
        return Response(serializer.data)


# @authentication_classes([SessionAuthentication,BasicAuthentication])
# @permission_classes([IsAuthenticated])
# @permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET',"POST"])    
def mapfacultyDetail(requests):
    #For posting the data
    
    if requests.method  == "POST":
        # ##start
        # json_data = requests.body
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser.parse(stream=stream)
        # serializer = FacultyMapmodelSerializers(data=python_data)
        # ##end

        serializer = FacultyMapmodelSerializers(data=requests.data)
        
        if serializer.is_valid():
            serializer.save()#owner = requests.user
            print(serializer.data, serializer.errors)
            res = {"status":"posted succesfully"}
            return Response(res,status=status.HTTP_201_CREATED)
        else:
            return Response({"status":"Unsuccesfull"},status=status.HTTP_400_BAD_REQUEST)
    #for retriving the data    
    else:
        tasks = models.Mapfaculty.objects.all()
        filterset = MapfacultyFilter(requests.GET, queryset=tasks)
        if filterset.is_valid():
         queryset = filterset.qs
        serializer = FacultyMapmodelNewSerializers(queryset,many=True)
        return Response(serializer.data)
    




# @permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET',"POST"])    
def SubjectDetail(requests):
    #For posting the data
     
    if requests.method  == "POST":
        # ##start
        # json_data = requests.data
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser.parse(stream=stream)
        # serializer = SubjectmodelSerializers(python_data)
        # ##end

        # serializer = SubjectmodelSerializers(data = requests.data)

        serializer = SubjectmodelSerializers(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            res = {"status":"posted succesfully"}
            return Response(res,status=status.HTTP_201_CREATED)
        else:
            return Response({"status":"Unsuccesfull"},status=status.HTTP_400_BAD_REQUEST)
    #for retriving the data
    else:
        queryset = {}
        tasks = models.Subjects.objects.all()
        filterset = SubjectsFilter(requests.GET, queryset=tasks)
        if filterset.is_valid():
         queryset = filterset.qs
        serializer = SubjectmodelSerializers(queryset,many=True)
        
        return Response(serializer.data)


@api_view(['GET',"POST"])    
# @permission_classes([IsAuthenticatedOrReadOnly])
def FacultyDetail(requests):
    #For posting the data
    
    if requests.method == 'POST':
         # ##start
        # json_data = requests.data
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser.parse(stream=stream)
        # serializer = FacultymodelSerializers(python_data)
        # ##end
        serializer = FacultymodelSerializers(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            Response({"status":"Unsuccesfull"},status=status.HTTP_400_BAD_REQUEST)
    #for retriving the data
    else:
        queryset = {}
        tasks = models.Faculty.objects.all()
        filterset = FacultyFilter(requests.GET, queryset=tasks)
        if filterset.is_valid():
         queryset = filterset.qs
        serializer = FacultymodelSerializers(queryset,many=True)
        
        return Response(serializer.data)


# @permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET',"POST"])    
def DepartmentDetail(requests):
    #For posting the data
    
    if requests.method == 'POST':
         # ##start
        # json_data = requests.data
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser.parse(stream=stream)
        # serializer = FacultymodelSerializers(python_data)
        # ##end
        serializer = DepartmentmodelSerializers(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            newdata = serializer.data.copy()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            Response({"status":"Unsuccesfull"},status=status.HTTP_400_BAD_REQUEST)
    #for retriving the data
    else:
        queryset = {}
        tasks = models.Department.objects.all()
        filterset = DepartmentFilter(requests.GET, queryset=tasks)
        if filterset.is_valid():
         queryset = filterset.qs
        serializer = DepartmentmodelSerializers(queryset,many=True)
        
        return Response(serializer.data)
    
# @permission_classes([IsAuthenticatedOrReadOnly])
@api_view(["GET","POST"])
def Calculateavg(requests):
    try:
        faculty = "Yash"
        year = '20/11/2023'
        sem = 1
        subject1 = 'DSA'
        # faculty = requests.POST['faculty']
        # year = requests.POST['year']
        # sem = requests.POST['sem']
        cal = {}
        above = {}
        below = {}
        practical_feedback = {}
        theory_feedback = {}
        abov1 = []
        bel1 = []
        abov12 = []
        bel12 = []
        hight = 0
        lowt = 0
        totalt = 0
        highp = 0
        low = 0
        totalp = 0
        
        if models.Faculty.objects.filter(faculty_name=faculty).exists():
            id = models.Faculty.objects.get(faculty_name=faculty).id
            print(id)
        if models.Subjects.objects.filter(subject=subject1).exists():
            subid = models.Subjects.objects.get(subject=subject1).id
        if models.Mapfaculty.objects.filter(faculty=id,subject=subid).exists():
            subject = models.Mapfaculty.objects.get(faculty=id,subject=subid).subject.subject
            department = models.Mapfaculty.objects.get(faculty=id,subject=subid).department.name
            division = models.Mapfaculty.objects.get(faculty=id,subject=subid).division.name
            batch = models.Mapfaculty.objects.get(faculty=id,subject=subid).practical_batch
            cal['faculty'] = faculty
            cal['subject'] = subject
            cal['department'] = department
            cal['division'] = division
            cal['batch'] = batch
            cal['batch'] = batch
            cal['semester'] = sem
            cal['f_date'] = year
            hight = Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'high').count()
            lowt = Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'low').count()
            totalt = Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year).count()
            highp = Practical_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'high').count()
            lowp = Practical_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'low').count()
            totalp = Practical_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year).count()
            for i in range(12):
                # theory_feedback_quest_abov[f"Q{i+1}"] = Theory_feedback.objects.filter(faculty=id,semester = sem,f_date=year, attendence = 'above')[f'Q{i+1}__avg']
                if Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'high').exists():
                    
                    above['theory'] = float(Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'high').aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg'])
                    abov1.append(float(Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'high').aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg']))
                    # abov1[f"Q{i+1}"] = float(Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendence = 'above').aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg'])
                if Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'low').exists():
                    below['theory'] = float(Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'low').aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg'])
                    bel1.append(float(Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'low').aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg']))
                    # bel1[f"Q{i+1}"] = float(Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendence = 'low').aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg'])
                theory_feedback[f"Q{i+1}"] = Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year).aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg']
            for i in range(8):
                if Practical_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'high').exists():
                    above['practical'] = float(Practical_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'high').aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg'])
                    abov12.append(float(Practical_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'high').aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg']))
                    # abov12[f"Q{i+1}"] = float(Practical_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'high').aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg'])
                if Practical_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'low').exists():
                    below['practical'] = float(Practical_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'low').aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg'])
                    bel12.append(float(Practical_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'low').aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg']))
                    # bel12[f"Q{i+1}"] = float(Practical_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'low').aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg'])
                practical_feedback[f"Q{i+1}"] = Practical_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year).aggregate(mod.Avg(f"Q{i+1}"))[f'Q{i+1}__avg']
            above["hight"] = hight
            above["highp"] = highp
            below["lowt"] = lowt
            below["lowp"] = lowp
            cal["practical_feedback"] = practical_feedback
            cal["theory_feedback"] = theory_feedback
            cal["totalt"] = totalt
            cal["totalp"] = totalp
            above['theory_q'] = abov1
            above["practical_q"] = abov12
            below['theory_q'] = bel1
            below["practical_q"] = bel12
            cal["above"] = above
            cal["below"] = below

            return Response(cal,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({ 'error': 'Atleast One response should be there in both Practical and Theory Feedback' })
    

@api_view(['GET',"POST"])  
def DivisionDetail(requests):
    #For posting the data
    
    if requests.method == 'POST':
         # ##start
        # json_data = requests.data
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser.parse(stream=stream)
        # serializer = FacultymodelSerializers(python_data)
        # ##end6
        serializer = DivisionmodelSerializers(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            Response({"status":"Unsuccesfull"},status=status.HTTP_400_BAD_REQUEST)
    #for retriving the data
    else:
        queryset = {}
        tasks = models.Division.objects.all()
        filterset = DivisionFilter(requests.GET, queryset=tasks)
        if filterset.is_valid():
         queryset = filterset.qs
        serializer = DivisionmodelSerializers(queryset,many=True)
        return Response(serializer.data)

#Authentication

# For registration

class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user
        # print(user.is_authenticated)
        # if(user){

        # }
        
        try:
            if(user.is_authenticated):
                return Response({'isAuthenticated': True})
            else:
                return Response({ 'isAuthenticated': False })
        except:
            return Response({ 'error': 'Something went wrong when checking authentication status' })

@method_decorator(csrf_exempt, name='dispatch')       
class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        
        # print(serializer.initial_data)
        try:
            if serializer.is_valid(raise_exception=True):
                # user = serializer.save()
                print(serializer.data)
                user = serializer.create(clean_data)
                
                if user:
                    return Response({ 'Register': 'Success' }, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

#for LOGIN THE USER
# @method_decorator(csrf_exempt, name='dispatch')
class UserLogin(APIView):   
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    ##
    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                user = serializer.check_user(data)
                if user is not None:
                    login(request, user)
                    return Response({ 'success': 'User authenticated' }, status=status.HTTP_200_OK)
                else:
                    return Response({ 'success': 'User authenticated' }, status=status.HTTP_200_OK)
                # return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({ 'error': 'Something went wrong when logging in' },status=status.HTTP_404_NOT_FOUND)

          
# for logging out
class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"status":"posted succesfully"}, status=status.HTTP_200_OK)  
		# logout(request)
       


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({ 'success': 'CSRF cookie set' })
#authentication ends

# all bulk creation of rows and upladed files views are here

#for bulk import  for department
class ImportDepartmentDetail(APIView):
    serializer = ImportSerializer
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request):
        # print(request.FILES)
        # print(request.data)
        try:
            data = request.FILES
            serializer = self.serializer(data = data)
            if serializer.is_valid():
                excel_file = data.get('file')
                # print(excel_file)
                df = pd.read_excel(excel_file,sheet_name=0)
                alldep = []
                for index,row in df.iterrows():
                    name = row['name']
                    department = models.Department.objects.filter(name=name).exists()
                    if department:
                        continue
                    else:
                        dep = models.Department(name=name)
                        alldep.append(dep)
                models.Department.objects.bulk_create(alldep)
                res = {"status":"posted succesfully"}
                return Response(res,status=status.HTTP_201_CREATED)
            # else:
            #     return Response({"status":"Unsuccesfull"},status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as err:
            print(err)
            return Response({"status":"Unsuccesfull"},status=status.HTTP_406_NOT_ACCEPTABLE)


#for bulk import  for division
class ImportDivisionDetail(APIView):
    serializer = ImportSerializer
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request):
        try:
            data =  request.FILES
            serializer = self.serializer(data = data)
            if serializer.is_valid():
                excel_file = data.get('file')
                df = pd.read_excel(excel_file,sheet_name=0)
                alldiv = []
                for index,row in df.iterrows():
                    department = row['department']
                    num_tutorial_batch = row['num_tutorial_batch']
                    num_pract_batch = row['num_pract_batch']
                    name = row['name']
                    division = models.Division.objects.filter(name=name).exists()
                    if division:
                        continue
                    else:
                        div = models.Department(name=name,num_tutorial_batch=num_tutorial_batch,num_pract_batch=num_pract_batch,department=department)
                        alldiv.append(div)
                models.Division.objects.bulk_create(alldiv)
                res = {"status":"posted succesfully"}
                return Response(res,status=status.HTTP_201_CREATED)
        except:
            return Response({"status":"Unsuccesfull"},status=status.HTTP_406_NOT_ACCEPTABLE)


#for bulk import  for faculty
class ImportFacultyDetail(APIView):
    serializer = ImportSerializer
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request):
        try:
            data =  request.FILES
            serializer = self.serializer(data = data)
            if serializer.is_valid():
                excel_file = data.get('file')
                df = pd.read_excel(excel_file,sheet_name=0)
                allfac = []
                for index,row in df.iterrows():
                    faculty_name = row['faculty_name']
                    department = row['department']
                    department_instance, created = models.Department.objects.get_or_create(id=department)
                    faculty = models.Faculty.objects.filter(faculty_name=faculty_name).exists()
                    if faculty:
                        continue
                    else:
                        dep = models.Faculty(faculty_name=faculty_name,department=department_instance)
                        allfac.append(dep)
                models.Faculty.objects.bulk_create(allfac)
                res = {"status":"posted succesfully"}
                return Response(res,status=status.HTTP_201_CREATED)
        except:
            return Response({"status":"Unsuccesfull"},status=status.HTTP_406_NOT_ACCEPTABLE)

#for bulk import  for SUBJECTS
class ImportSubjectDetail(APIView):
    serializer = ImportSerializer
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request):
        try:
            data =  request.FILES
            serializer = self.serializer(data = data)
            if serializer.is_valid():
                excel_file = data.get('file')
                df = pd.read_excel(excel_file,sheet_name=0)
                allsub = []
                for index,row in df.iterrows():
                    subject = row['subject']
                    semester = row['semester']
                    department = row['department']
                    subject_ = models.Subjects.objects.filter(subject=subject).exists()
                    department_instance, created = models.Department.objects.get_or_create(id=department)
                    # print(department)
                    if subject_:
                        continue
                    else:
                        dep = models.Subjects(subject=subject,semester=semester,department=department_instance)
                        allsub.append(dep)
                print(allsub)
                models.Subjects.objects.bulk_create(allsub)
                res = {"status":"posted succesfully"}
                return Response(res,status=status.HTTP_201_CREATED)
        except Exception as err:
            print(err)
            return Response({"status":"Unsuccesfull"},status=status.HTTP_406_NOT_ACCEPTABLE)


#for bulk import  for Mapfaculty
class ImportMapDetail(APIView):
    serializer = ImportSerializer
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request):
        try:
            data =  request.FILES
            serializer = self.serializer(data = data)
            if serializer.is_valid():
                excel_file = data.get('file')
                df = pd.read_excel(excel_file,sheet_name=0)
                allsub = []
                for index,row in df.iterrows():
                    sem = row["sem"]
                    faculty = row["faculty"]
                    department = row["department"]
                    subject = row["subject"]
                    division = row["division"]
                    theory = row["theory"]
                    practical = row["practical"]
                    tutorial = row["tutorial"]
                    practical_batch = row["practical_batch"]
                    tutorial_batch = row["tutorial_batch"]
                    year = row["year"]
                    
                    dep = models.Mapfaculty(sem=sem,faculty=faculty,department = department,subject=subject,division=division,theory=theory,practical=practical,tutorial=tutorial,practical_batch=practical_batch,tutorial_batch=tutorial_batch,year=year)
                    allsub.append(dep)
                models.Mapfaculty.objects.bulk_create(allsub)
                res = {"status":"posted succesfully"}
                return Response(res,status=status.HTTP_201_CREATED)
        except:
            return Response({"status":"Unsuccesfull"},status=status.HTTP_406_NOT_ACCEPTABLE)

def print_all(requests):
    faculty = "Mrunali"
    year = 2023
    sem = 5
    if models.Faculty.objects.filter(faculty_name=faculty).exists():
        id = models.Faculty.objects.get(faculty_name=faculty).id
    print(Theory_feedback.objects.filter(faculty=faculty,semester = sem,f_date=year, attendance = 'high')[f'Q1__avg'])
    return requests.data

class AcademicYView(APIView):   
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    ##
    def post(self, request):
        data = request.data
        serializer = AcadmodelSerializers(data=data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({ 'error': 'Something went wrong' },status=status.HTTP_404_NOT_FOUND)
    def get(self, request):
        data = models.Academic_year.objects.all();
        serializer = AcadmodelSerializers(data=data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # try:
        #     # if serializer.is_valid():
        #     #     serializer.save()
        #         return Response(serializer.data, status=status.HTTP_200_OK)
        # except:
        #     return Response({ 'error': 'Something went wrong' },status=status.HTTP_404_NOT_FOUND)
