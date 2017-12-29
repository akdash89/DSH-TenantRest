#https://python-jenkins.readthedocs.io/en/latest/examples.html#example-3-working-with-jenkins-jobs
import jenkins
from tkinter import *
from TenantRestConfig import *
from time import sleep

###############################
def pushit():
    global j, dMountedDisk, topic
    lb1.delete(0, 'end')
    lb1.insert(0, 'All')

    #Push from git url to mounted disk
    job1 = '{}-pushMountedDisk'.format(topic) 
    
    xmlPushMDisk = open(templatePushMDisk, 'r').read()  
    xmlPushMDisk = xmlPushMDisk.replace('GITURL', str(gitName.get())).replace('PASSWORD', str(pw.get())) \
                                .replace('USERNAME',str(uName.get())).replace('LOCATIONMOUNTEDDISK',str(dMountedDisk))
    try:
        j.create_job(job1, xmlPushMDisk)
    except:
        j.reconfig_job(job1, xmlPushMDisk)
    j.build_job(job1)
    
    try:
        last_build_number = j.get_job_info(job1)['lastCompletedBuild']['number']
    except:
        last_build_number = 0

    while True:

        try:
            lbn = j.get_job_info(job1)['lastCompletedBuild']['number']
        except:
            lbn = 0

        if last_build_number == lbn:
            sleep(1)
        else:
            break
    
    for test in os.listdir(os.path.join(dMountedDisk, 'Testcases')):
        lb1.insert(0, test)
    
    if var1.get()==1:
        print("A new job called {0}-AllTrigger will be made which will be automatically triggerd after execution of {1}".format(topic, job1))

def runit():
    global j, dMountedDisk, topic
    
    #Push from git url to mounted disk
    job2 = '{}-{}'.format(topic, lb1.get('active')) 
    
    xmlRun = open(templateExecKafkaRunCommand, 'r').read()  
    xmlRun = xmlRun.replace('TRIGGER', str(lb2.get('active'))).replace('PASSWORD', str(pw.get())) \
                                .replace('USERNAME',str(uName.get())).replace('PATHTOkafkaProduceRunCommand',str(fKafkaRunCommand)) \
                                .replace('TOPIC', topic).replace('RUNCOMMAND', lb1.get('active'))
    try:
        j.create_job(job2, xmlRun)
    except:
        j.reconfig_job(job2, xmlRun)
    j.build_job(job2)

#################OPEN JENKINS########################

j = jenkins.Jenkins('http://localhost:8084', 'admin', 'rak24283')

#################USER PROMT####################
def quiting():
    global root
    root.destroy()

root = Tk()
root.title('Prompt for Tenant')
root.geometry("600x1000")

frame1 = Frame(root, bg='#ffffdd')

#logo = PhotoImage(file=pLogo)
#lblImg = Label(root, image=logo)
#lblImg.pack(side=TOP,padx=10,pady=10)

lbl1 = Label(root, text='Hello {}, complete the following prompts'.format(topic))
lbl1.pack(side=TOP,padx=10,pady=10)

lbl2 = Label(root, text='UserName')
lbl2.pack(side=TOP,padx=10,pady=10)

uName = Entry(root, width=20)
uName.pack(side=TOP,padx=10,pady=10)

lbl3 = Label(root, text='Password')
lbl3.pack(side=TOP,padx=10,pady=10)

password = StringVar() #Password variable
pw = Entry(root, textvariable=password, show='*', width=20)
pw.pack(side=TOP,padx=10,pady=10)

lbl4 = Label(root, text='GIT account')
lbl4.pack(side=TOP,padx=10,pady=10)

gitName = Entry(root, width=30)
gitName.pack(side=TOP,padx=10,pady=10)

var1 = IntVar()
chk1 = Checkbutton(root, state='active', text="Trigger from push", variable=var1)
chk1.pack(side=TOP,padx=10,pady=10)

btn1 = Button(root, text='Mount Tests', command=pushit).pack(side=TOP)

lbl5 = Label(root, text='Available tests')
lbl5.pack(side=TOP,padx=10,pady=10)

lb1 = Listbox(root, height=5)
lb1.pack(side=TOP,padx=10,pady=10)

lbl6 = Label(root, text='Trigger')
lbl6.pack(side=TOP,padx=10,pady=10)

lb2 = Listbox(root, height=2)
lb2.pack(side=TOP,padx=10,pady=10)
lb2.insert(0, 'H 13 * * *')

btn2 = Button(root, text='Run Test(s)', command=runit).pack(side=TOP)
btn3 = Button(root, text='Close', command=quiting).pack(side= TOP)

root.mainloop()