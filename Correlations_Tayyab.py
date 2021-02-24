import matplotlib.pyplot as plt
import pandas as pd

import operator

df = pd.read_excel(r'C:\Personal Data\Data Science\StudentCareerPortal-main\survey.xlsx')

df_abi = df[df['Status'] == 'Abitur']

df_bachelor = df[df['Status'] == 'Bachelor Studium']
df_master = df[df['Status'] == 'Master Studium']

# Participants=P
P1 = "Number of Highschool students: " + str(df_abi.shape[0])
P2 = "Number of Bachelor students: " + str(df_bachelor.shape[0])
P3 = "Number of Master students: " + str(df_master.shape[0])

print(P1 + " \n" + P2 + " \n" + P3)

# combining two study program columns

df_bachelor.loc[df_bachelor['bachelor_study'] == 'Studium nicht aufgelistet', 'bachelor_study'] = df_bachelor[
    'bachelor_study2']
df_master.loc[df_master['master_study'] == 'Studium nicht aufgelistet', 'master_study'] = df_master['master_study2']

# print combined columns
print(df_bachelor['bachelor_study'])
print(df_master['master_study'])


#print(df_bachelor.columns)
df_bachelor.drop(['Ausbildung', 'Ausbildung_year', 'Ausbildung_future' ], axis= 1)


print('--------------------------------------------------------')

def corBachelorFLK(x):
    a = df_bachelor['bachelor_study'] == x
    df_bachelor_tmp = df_bachelor[a]
    baselist = df_bachelor_tmp['bachelor_abitur_flk'].tolist()
    words = frozenset(baselist)
    counted_words = []
    cw= []
    cn= []
    for word in words:
        counted_words.append((word, baselist.count(word)))
        cw.append(word)
        cn.append(baselist.count(word))
        counted_words.sort(key = operator.itemgetter(1))


    plt.bar(cw, cn)
    plt.title('Correlation between ' + x + ' and First LK')
    plt.ylabel('Investigated students')
    plt.xlabel('Subjects')
    plt.show()

#for item in counted_words:
 #   print ("%-10s %i" % item)

corBachelorFLK('Wirtschaftsinformatik')

#gender comparsion

def geschlecht(x):
    a = df_bachelor['Geschlecht'] == x
    df_bachelor_tmp = df_bachelor[a]
    baselist = df_bachelor_tmp['bachelor_study'].tolist()
    words = frozenset(baselist)
    print (words)
    counted_words = []
    cw= []
    cn= []
    for word in words:
        counted_words.append((word, baselist.count(word)))
        cw.append(word)
        cn.append(baselist.count(word))
        counted_words.sort(key = operator.itemgetter(1))

    print (counted_words)
    print (cw)
    print (cn)
    plt.pie(cn, labels = cw, autopct='%1.1f%%', startangle=90)
    plt.title ('Study Programs ' + x)
    plt.show()


geschlecht('Männlich')
geschlecht('Weiblich')

# future_bachelor
def future_bachelor():
    baselist = df_bachelor['bachelor_future'].tolist()
    words = frozenset(baselist)
    print (words)
    counted_words = []
    cw= []
    cn= []
    for word in words:
        counted_words.append((word, baselist.count(word)))
        cw.append(word)
        cn.append(baselist.count(word))
        counted_words.sort(key = operator.itemgetter(1))

    print (counted_words)
    print (cw)
    print (cn)
    explode =(0.1, 0.1, 0.1, 0.1)
    plt.pie(cn, labels = cw, explode = explode, autopct='%1.1f%%', shadow= True, startangle=90)
    plt.title ('Future Preferences of Bachelor Students')
    plt.show()
future_bachelor()


def future_industry(x):
    a = df_bachelor['Geschlecht'] == x
    df_bachelor_tmp = df_bachelor[a]
    baselist = df_bachelor_tmp['future_work_field'].tolist()
    words = frozenset(baselist)
    print (words)
    counted_words = []
    cw= []
    cn= []
    for word in words:
        counted_words.append((word, baselist.count(word)))
        cw.append(word)
        cn.append(baselist.count(word))
        counted_words.sort(key = operator.itemgetter(1))

    print (counted_words)
    print (cw)
    print (cn)
    plt.pie(cn, labels = cw, autopct='%1.1f%%', startangle=90)
    plt.title ('Industry Fields ' + x)
    plt.show()
future_industry('Männlich')
